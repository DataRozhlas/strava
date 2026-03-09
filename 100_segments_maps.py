# /// script
# dependencies = [
#     "geopandas==1.1.2",
#     "marimo",
#     "matplotlib==3.10.8",
#     "osmnx==2.1.0",
#     "pandas==3.0.1",
#     "pyarrow==23.0.1",
# ]
# requires-python = ">=3.12"
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import os
    import json
    import ast
    import pandas as pd
    import geopandas as gpd
    import osmnx as ox
    import matplotlib.pyplot as plt

    return gpd, ox, pd, plt


@app.cell
def _(pd):
    df = pd.read_parquet('data/segments.parquet')
    df = df[df['country'].str.contains('Cz',na=True)]
    return (df,)


@app.cell
def _(df):
    df['lat'] = df['start_latlng'].apply(lambda x: x[0])
    df['lon'] = df['start_latlng'].apply(lambda x: x[1])
    return


@app.cell
def _(ox):
    admin_country = ox.geocode_to_gdf('Czech Republic')
    return (admin_country,)


@app.cell
def _(df, gpd):
    points_gdf = gpd.GeoDataFrame(
        df, 
        geometry=gpd.points_from_xy(df['lon'], df['lat']),
        crs="EPSG:4326"
    )
    return (points_gdf,)


@app.cell
def _(points_gdf):
    run_points = points_gdf[points_gdf['activity_type'] == 'Run']
    run_track_points = points_gdf[(points_gdf['activity_type'] == 'Run') & (points_gdf['start_to_finish_distance'] < 0.03)]
    ride_points = points_gdf[points_gdf['activity_type'] == 'Ride']
    hike_points = points_gdf[points_gdf['activity_type'] == 'Hike']
    return hike_points, ride_points, run_points, run_track_points


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Run segments
    """)
    return


@app.cell
def _(admin_country, plt, run_points):
    fig, ax = plt.subplots(figsize=(15, 10))
    admin_country.plot(ax=ax, alpha=0.5, color='lightgray')
    run_points.plot(ax=ax, color='red', marker='o', label='Run', markersize=100)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Tracks
    """)
    return


@app.cell
def _(admin_country, plt, run_track_points):
    fig_track, ax_track = plt.subplots(figsize=(15, 10))
    admin_country.plot(ax=ax_track, alpha=0.5, color='lightgray')
    run_track_points.plot(ax=ax_track, color='green', marker='o', label='Run', markersize=100)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ride Segments
    """)
    return


@app.cell
def _(admin_country, plt, ride_points):
    fig_ride, ax_ride = plt.subplots(figsize=(15, 10))
    admin_country.plot(ax=ax_ride, alpha=0.5, color='lightgray')
    ride_points.plot(ax=ax_ride, color='blue', marker='o', label='Ride', markersize=100)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hike segments
    """)
    return


@app.cell
def _(admin_country, hike_points, plt):
    fig_hike, ax_hike = plt.subplots(figsize=(15, 10))
    admin_country.plot(ax=ax_hike, alpha=0.5, color='lightgray')
    hike_points.plot(ax=ax_hike, color='green', marker='o', label='Hike', markersize=100)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Top / representative segments
    """)
    return


@app.cell
def _():
    import yaml

    return (yaml,)


@app.cell
def _(yaml):
    with open("data_raw/behani_top_20.yaml", "r", encoding="utf-8") as f:
        behani20 = yaml.safe_load(f.read())

    with open("data_raw/kolo_top_20.yaml", "r", encoding="utf-8") as f:
        kolo20 = yaml.safe_load(f.read())
    return behani20, kolo20


@app.cell
def _(behani20, kolo20, points_gdf):
    behani_top_20 = points_gdf[points_gdf['name'].isin(behani20)]
    kolo_top_20 = points_gdf[points_gdf['name'].isin(kolo20)]
    return behani_top_20, kolo_top_20


@app.cell
def _(behani_top_20):
    behani_top_20.sort_values(by="lon",ascending=False)
    return


@app.cell
def _(admin_country, behani_top_20, plt):
    fig_run20, ax_run20 = plt.subplots(figsize=(15, 10))
    admin_country.plot(ax=ax_run20, alpha=0.5, color='lightgray')
    behani_top_20.plot(ax=ax_run20, color='green', marker='o', label='Hike', markersize=100)
    return


@app.cell
def _(admin_country, kolo_top_20, plt):
    fig_kolo20, ax_kolo20 = plt.subplots(figsize=(15, 10))
    admin_country.plot(ax=ax_kolo20, alpha=0.5, color='lightgray')
    kolo_top_20.plot(ax=ax_kolo20, color='blue', marker='o', label='Hike', markersize=100)
    return


if __name__ == "__main__":
    app.run()
