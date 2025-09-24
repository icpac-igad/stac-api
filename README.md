# STAC API Implementation for E4DRR Impact-Based Forecasting

## Overview

This repository contains a STAC (Spatio Temporal Asset Catalog) API implementation for E4DRR Impact-Based Forecasting data. The catalog is designed to organize drought and flood forecasting data according to the STAC specification v1.1.0.

## Directory Structure

The main working catalog is in `ibf_catalog/` which contains:

```
ibf_catalog/
├── stac_server.py          # CORS-enabled HTTP server for serving STAC catalogs
├── drought/                # Drought-related catalog data
│   ├── dr_catalog.json     # Main drought catalog
│   └── collections/        # Drought data collections
├── flood/                  # Flood-related catalog data
│   ├── fl_catalog.json     # Main flood catalog
│   └── collections/        # Flood data collections
└── images/                 # Preview images and thumbnails
```

## STAC Catalog Structure

### Main Catalogs

**Drought Catalog** (`drought/dr_catalog.json`):
- Catalog ID: `drought-ibf-catalog`
- Contains 6 main collections:
  - Observations
  - Ensemble Predictions
  - Hazard Model
  - Impact Model
  - Forecast Verification
  - Risk Knowledge

**Flood Catalog** (`flood/fl_catalog.json`):
- Catalog ID: `flood-ibf-catalog`
- Contains the same 6 collection types as drought catalog

### Data Collections

Each collection contains subcollections and items organized hierarchically:
- **Collections**: High-level data groupings (e.g., ensemble-predictions, observations)
- **Subcollections**: Specific datasets within collections (e.g., seas5, cpt9)
- **Items**: Individual data assets with specific time periods and locations

## STAC Server

The `stac_server.py` provides a simple HTTP server with CORS headers enabled for serving the STAC catalogs:

### Features:
- CORS headers for cross-origin requests
- Configurable port (default: 8000)
- Serves static JSON files and images
- Compatible with STAC Browser applications

### Usage:
```bash
cd ibf_catalog
python stac_server.py [port]
```

### Access Points:
- Local server: `http://localhost:8000/drought/dr_catalog.json`
- Local server: `http://localhost:8000/flood/fl_catalog.json`

## STAC Browser Integration

The catalogs are designed to work with the STAC Browser at:
https://radiantearth.github.io/stac-browser/

### To use with STAC Browser:
1. Deploy the catalog to a publicly accessible location (e.g., GitHub raw content)
2. Use the URL pattern: `https://radiantearth.github.io/stac-browser/#/external/[YOUR_RAW_GITHUB_URL]/catalog_v5/drought/dr_catalog.json`

Example URL structure (like the reference provided):
```
https://radiantearth.github.io/stac-browser/#/external/raw.githubusercontent.com/[username]/[repo]/[branch]/catalog_v5/drought/dr_catalog.json?.language=en
```

## Data Coverage

### Spatial Extent:
- Bounding box: [32.0, -12.0, 51.0, 6.0] (East Africa region)

### Temporal Extent:
- Start: 2013-01-01T00:00:00Z
- End: 2025-05-06T10:53:26.869075Z

### Data Providers:
- **E4DRR**: Engineering for Disaster Risk Reduction (producer, licensor)
- **ICPAC**: IGAD Climate Prediction and Applications Centre (host, processor)

## Development History

The catalog went through multiple iterations (catalog/, catalog_v2/, catalog_v3/, catalog_v4/, catalog_v5/) with trial and error to achieve STAC browser compatibility. The `catalog_v5/` directory represents the final working version with:
- Proper STAC 1.1.0 specification compliance
- Correct link relationships between catalogs, collections, and items
- CORS-enabled server for web browser access
- Hierarchical organization suitable for large-scale geospatial data

## Images and Assets

### Image Usage Analysis

**Images used in catalogs:**
- `/images/dr_hazard.png` - Drought hazard model previews
- `/images/dr_obs.png` - Drought observations (most commonly used)
- `/images/fcst_verify.png` - Forecast verification previews
- `/images/fl_eps.png` - Flood ensemble predictions
- `/images/fl_haz.jpg` - Flood hazard previews (NOTE: uses .jpg extension)
- `/images/fl_obs.png` - Flood observations
- `/images/imp_model.png` - Impact model previews
- `/images/risk_know.png` - Risk knowledge previews

**Files to remove:** The root-level PNG/JPG files are duplicates of those in `catalog_v5/images/` and can be safely removed:
```bash
rm dr_hazard.png dr_obs.png fcst_verify.png fl_eps.png fl_haz.jpg fl_obs.png imp_model.png risk_know.png
```

**Note:** There are also duplicate `dr_obs.png` files in `catalog_v5/drought/images/` and `catalog_v5/flood/images/` that appear unused by the catalogs.

## External Data Integration

### GCS Bucket and COG Integration

To link your catalog items to actual data sources in Google Cloud Storage (GCS) buckets or Cloud Optimized GeoTIFFs (COGs), modify the `assets` section in each item JSON file:

```json
{
  "assets": {
    "data": {
      "href": "gs://your-bucket-name/path/to/file.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "title": "Cloud Optimized GeoTIFF",
      "roles": ["data"],
      "gsd": 30.0,
      "proj:epsg": 4326
    },
    "thumbnail": {
      "href": "/images/preview.png",
      "type": "image/png",
      "title": "Preview",
      "roles": ["thumbnail"]
    }
  }
}
```

### k/Zarr Integration
For Kerchunk reference files or virtual Zarr datasets:

```json
{
  "assets": {
    "kerchunk_reference": {
      "href": "gs://your-bucket/path/to/reference.json",
      "type": "application/json",
      "title": "Kerchunk Reference File",
      "roles": ["metadata"],
      "description": "Kerchunk reference for accessing NetCDF/HDF5 as Zarr"
    },
    "zarr": {
      "href": "gs://your-bucket/path/to/dataset.zarr",
      "type": "application/x-zarr",
      "title": "Zarr Dataset",
      "roles": ["data"],
      "description": "Cloud-native Zarr format dataset"
    }
  }
}
```

### Integration with External STAC Catalogs

#### Radiant Earth OpenStreetMap
```json
{
  "links": [
    {
      "rel": "derived_from",
      "href": "https://radiant-earth-stac.s3.amazonaws.com/osm/catalog.json",
      "type": "application/json",
      "title": "Radiant Earth OpenStreetMap STAC Catalog"
    }
  ]
}
```

#### Source Cooperative Overture Maps
```json
{
  "links": [
    {
      "rel": "related",
      "href": "s3://us-west-2.opendata.source.coop/youssef-harby/overture-maps-stac/catalog.json",
      "type": "application/json",
      "title": "Overture Maps STAC Catalog"
    }
  ]
}
```

### Implementation Strategy

1. **Data Source Mapping**: Create a mapping file that connects each catalog item to its actual data source
2. **Asset Generation Script**: Develop a script to automatically update asset links based on GCS bucket contents
3. **Validation**: Implement validation to ensure all asset URLs are accessible
4. **Metadata Extraction**: Use tools like `rio-stac` or `stac-geoparquet` to extract metadata from actual files

### Example Integration Script Structure

```python
import json
from pathlib import Path

def update_item_assets(item_path, gcs_base_path, data_mapping):
    """Update STAC item with real GCS asset links"""
    with open(item_path) as f:
        item = json.load(f)

    # Update assets based on mapping
    for asset_key, asset_info in data_mapping.items():
        item['assets'][asset_key] = {
            'href': f"{gcs_base_path}/{asset_info['path']}",
            'type': asset_info['media_type'],
            'roles': asset_info['roles']
        }

    # Save updated item
    with open(item_path, 'w') as f:
        json.dump(item, f, indent=2)
```

This approach ensures your STAC catalog becomes a true index of your actual geospatial data rather than just a structural template.
