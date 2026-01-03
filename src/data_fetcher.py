"""
data_fetcher.py
----------------
Downloads satellite images for properties using latitude & longitude
via Sentinel Hub API.

Images are saved as:
images/{property_id}/{image_hash}.jpg

NOTE:
- Requires valid Sentinel Hub credentials
- Image downloading is disabled by default to avoid re-running
"""

import os
import pandas as pd
from sentinelhub import (
    SHConfig,
    BBox,
    CRS,
    SentinelHubRequest,
    DataCollection,
    MimeType,
    bbox_to_dimensions
)

# =========================
# CONFIGURATION
# =========================

DOWNLOAD_IMAGES = False  # Set to True ONLY if credentials are active

DATA_PATH = "data/train.csv"
OUTPUT_DIR = "images"

# Sentinel Hub credentials
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

# =========================
# SETUP
# =========================

config = SHConfig()
config.sh_client_id = CLIENT_ID
config.sh_client_secret = CLIENT_SECRET

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)
df["id"] = df["id"].astype(str)

print(f"Loaded {len(df)} rows from {DATA_PATH}")

# =========================
# DOWNLOAD FUNCTION
# =========================

def download_image(prop_id, lat, lon):
    bbox = BBox(
        bbox=[lon - 0.002, lat - 0.002, lon + 0.002, lat + 0.002],
        crs=CRS.WGS84
    )

    size = bbox_to_dimensions(bbox, resolution=10)

    request = SentinelHubRequest(
        data_folder=os.path.join(OUTPUT_DIR, prop_id),
        evalscript="""
        //VERSION=3
        function setup() {
            return {
                input: ["B04", "B03", "B02"],
                output: { bands: 3 }
            };
        }
        function evaluatePixel(sample) {
            return [sample.B04, sample.B03, sample.B02];
        }
        """,
        input_data=[
            SentinelHubRequest.input_data(
                data_collection=DataCollection.SENTINEL2_L1C,
                time_interval=("2020-01-01", "2020-12-31")
            )
        ],
        responses=[
            SentinelHubRequest.output_response("default", MimeType.JPEG)
        ],
        bbox=bbox,
        size=size,
        config=config
    )

    request.get_data(save_data=True)

# =========================
# MAIN LOOP
# =========================

if not DOWNLOAD_IMAGES:
    print("DOWNLOAD_IMAGES=False -> Skipping download (safe mode)")
    print("Enable it only if Sentinel Hub credits are available.")
else:
    for idx, row in df.iterrows():
        try:
            download_image(row["id"], row["lat"], row["long"])
            if idx % 200 == 0:
                print(f"Downloaded {idx}/{len(df)}")
        except Exception as e:
            print(f"Failed for ID {row['id']} | {e}")

    print("DONE: Image download complete.")