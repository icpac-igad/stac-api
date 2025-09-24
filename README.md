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
https://radiantearth.github.io/stac-browser/#/external/https://raw.githubusercontent.com/icpac-igad/stac-api/refs/heads/main/ibf_catalog/drought/dr_catalog.json?.language=en

https://radiantearth.github.io/stac-browser/#/external/https://raw.githubusercontent.com/icpac-igad/stac-api/refs/heads/main/ibf_catalog/flood/fl_catalog.json?.language=en

```

## External Data Integration

### GCS Bucket and COG Integration

To link catalog items to actual data sources in Google Cloud Storage (GCS) buckets or Cloud Optimized GeoTIFFs (COGs), modify the `assets` section in each item JSON file:

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


