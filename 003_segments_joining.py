import os
import json
import math
import polars as pl

## FOLDERS & CONFIG DIVISION

source_folders = os.listdir("/mnt/usbdrive/strava/downloads/segments")
data_raw = "/mnt/usbdrive/strava/data_raw/segments"
data_folder = "/mnt/usbdrive/strava/data/"
os.makedirs(data_raw, exist_ok=True)
os.makedirs(data_folder, exist_ok=True)

done = [x.replace(".parquet", "") for x in os.listdir(data_raw)]

## DAILY PARQUET DIVISION

## DAILY PARQUET DIVISION

for s in source_folders:
    source_path = os.path.join("/mnt/usbdrive/strava/downloads/segments", s)
    parquet_path = os.path.join(data_raw, f"{s}.parquet")
    
    # Determine if we need to process this folder
    should_process = False
    
    if not os.path.exists(parquet_path):
        # Case 1: Parquet file doesn't exist yet
        should_process = True
    else:
        # Case 2: Compare modification times (mtime)
        # If the source folder was modified AFTER the parquet file was written, update it.
        src_mtime = os.path.getmtime(source_path)
        dst_mtime = os.path.getmtime(parquet_path)
        if src_mtime > dst_mtime:
            should_process = True

    if should_process:
        print(f"Processing: {s}")
        day = []
        # Note: Added error handling for empty folders or non-files
        try:
            files = os.listdir(source_path)
        except NotADirectoryError:
            continue

        for f in files:
            # Basic validation to ensure we only look at files with underscores (as per your split logic)
            if "_" not in f: continue
            
            try:
                time = f.split("_")[1].split(".")[0]
                full_path = os.path.join(source_path, f)
                
                with open(full_path, "r", encoding="utf-8") as file:
                    segment = json.loads(file.read())
                    segment["date"] = time
                    day.append(segment)
            except Exception as e:
                print(f"Error reading {f}: {e}")
                continue
        
        if day:
            df = pl.DataFrame(day)
            df.write_parquet(parquet_path)
        else:
            print(f"No valid data found in {s}")
    else:
        # Optional: Print skipped folders to know the logic is working
        # print(f"Skipping {s} (Up to date)")
        pass

## FINAL JOIN DIVISION // HAIL CLAUDE

df = pl.read_parquet("/mnt/usbdrive/strava/data_raw/segments/*.parquet")
print(f"{len(df)} rows loaded.")

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
df = df.with_columns(
    pl.col("country").str.replace_many(replacements)
    ).with_columns(
    pl.col("city").str.replace_many(replacements)
    ).with_columns(
    pl.col("name").str.strip_chars()
    )

df.write_parquet(os.path.join(data_folder, "segments.parquet"))

## OVERVIEW DIVISION

overview = (
    df.with_columns(pl.col("name").str.slice(0, 32))
    .with_columns(pl.col("distance").cast(int))
    .with_columns(pl.col("total_elevation_gain").cast(int).alias("elevation_gain"))
    .with_columns(pl.col("effort_count").alias("efforts"))
    .with_columns(pl.col("activity_type").alias("type"))
    .group_by(
        ["name", "type", "country", "city", "distance", "elevation_gain"]
    )
    .agg(pl.col("efforts").max())
    .sort("efforts", descending=True)
)
last_date = df.select(pl.col("date")).max().item()
last_date = last_date.strftime("%Y-%m-%d")

print(df.sort(by="date").group_by_dynamic(index_column="date",every='1d').agg(pl.col("name").unique().len()).sort(by="date").tail(10))

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
