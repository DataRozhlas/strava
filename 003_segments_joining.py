import os
import json
import math
import polars as pl

## FOLDERS & CONFIG DIVISION

source_folders = os.listdir("downloads/segments")
data_raw = "data_raw/segments"
data_folder = "data/"
os.makedirs(data_raw, exist_ok=True)
os.makedirs(data_folder, exist_ok=True)
pl.Config(tbl_rows=300)
pl.Config.set_fmt_str_lengths(200)
pl.Config.set_tbl_width_chars(200)

done = [x.replace(".parquet", "") for x in os.listdir(data_raw)]

## DAILY PARQUET DIVISION

for s in source_folders:
    if s not in done:
        print(s)
        day = []
        for f in os.listdir(f"downloads/segments/{s}"):
            time = f.split("_")[1].split(".")[0]
            with open(
                os.path.join(f"downloads/segments/{s}", f), "r", encoding="utf-8"
            ) as file:
                segment = json.loads(file.read())
                segment["date"] = time
                day.append(segment)
        df = pl.DataFrame(day)
        df.write_parquet(os.path.join(data_raw, f"{s}.parquet"))

## FINAL JOIN DIVISION // HAIL CLAUDE

df = pl.read_parquet("data_raw/segments/*.parquet")


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on Earth.
    Returns distance in kilometers.
    """
    R = 6371  # Earth's radius in kilometers

    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.asin(math.sqrt(a))

    return R * c


df = df.with_columns(
    pl.struct(["start_latlng", "end_latlng"])
    .map_elements(
        lambda x: haversine_distance(
            x["start_latlng"][0],
            x["start_latlng"][1],
            x["end_latlng"][0],
            x["end_latlng"][1],
        ),
        return_dtype=float,
    )
    .alias("start_to_finish_distance")
)

df = (
    df.with_columns(
        (pl.col("date").cast(pl.Int64) * 1000000).cast(pl.Datetime(time_zone="CET"))
    )
    .filter(pl.col("date").dt.hour() > 22)
    .select(
        [
            "id",
            "name",
            "activity_type",
            "distance",
            "average_grade",
            "elevation_high",
            "elevation_low",
            "total_elevation_gain",
            "start_latlng",
            "end_latlng",
            "country",
            "state",
            "city",
            "effort_count",
            "athlete_count",
            "date",
            "start_to_finish_distance",
        ]
    )
)

replacements = {
    "Czech Republic": "Czechia",
    "United Kingdom": "UK",
    "Mole Valley District, Surrey, UK": "Mole Valley District",
}
df = df.with_columns(pl.col("country").str.replace_many(replacements)).with_columns(
    pl.col("city").str.replace_many(replacements)
)

df.write_parquet(os.path.join(data_folder, "segments.parquet"))

## OVERVIEW DIVISION

overview = (
    df.with_columns(pl.col("name").str.slice(0, 25))
    .with_columns(pl.col("distance").cast(int))
    .with_columns(pl.col("total_elevation_gain").cast(int).alias("elevation_gain"))
    .with_columns(pl.col("effort_count").alias("efforts"))
    .group_by(
        ["name", "activity_type", "country", "city", "distance", "elevation_gain"]
    )
    .agg(pl.col("efforts").max())
    .sort("efforts", descending=True)
)
last_date = df.select(pl.col("date")).max().item()
last_date = last_date.strftime("%Y-%m-%d")

with pl.Config() as cfg:
    cfg.set_tbl_formatting("ASCII_MARKDOWN")
    overview_markdown = repr(overview).splitlines()
    overview_markdown = '\n'.join(overview_markdown[1:3] + overview_markdown[5:])

with open("README.md", "r", encoding="utf8") as readme:
    content = readme.read()
    content = content.split("##")[0]
with open("README.md", "w+", encoding="utf8") as readme:
    readme.write(
        f"""{content}## Poslední aktualizace\n\n{last_date}\n\n## Sledované segmenty\n\n{overview_markdown}"""
    )
