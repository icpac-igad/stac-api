# Flood STAC API - E4DRR Impact-Based Forecasting

## Overview

This repository contains a STAC (SpatioTemporal Asset Catalog) API implementation for Flood Impact-Based Forecasting data in the IGAD/ICPAC region. The catalog organizes flood-related geospatial data according to the STAC specification v1.1.0.

## Catalog Structure

```
ibf_catalog/
└── flood/
    ├── fl_catalog.json              # Main flood catalog
    └── collections/
        ├── admin-layers/             # Administrative boundaries
        ├── inundation/               # Flood inundation maps
        ├── hazards/                  # Flood hazard data and alerts
        ├── impact/                   # Flood impact assessments
        ├── deterministic-forecasts/  # Deterministic flood forecasts
        └── observations/             # Flood observations and monitoring
```

## Collections

### 1. Administrative Boundaries
- Administrative boundaries for the IGAD region
- Admin level 1 boundaries and features

### 2. Flood Inundation Maps
- Daily flood inundation maps
- Integrated with HMC (Hydrological Monitoring Center) data
- Shows quantitative flood levels

### 3. Flood Hazards
- Merged alerts from daily monitoring
- Hazard assessment data
- Risk levels and warnings

### 4. Flood Impact Layers
- Impact assessment on population and infrastructure
- Economic impact estimates
- Affected areas analysis

### 5. Deterministic Forecasts
- Time-series flood forecasts
- Model-based predictions
- Short to medium-range forecasts

### 6. Flood Observations
- Real-time flood monitoring points
- Historical flood records
- Ground truth data

## Deployment

### Automated GitHub Actions Validation

The repository includes automated STAC catalog validation via GitHub Actions when pushing to:
- `flood-main` - Primary flood catalog branch
- `flood-*` - Any branch starting with "flood-" (e.g., flood-dev, flood-staging)

The workflow validates all STAC collections and generates the correct STAC Browser URLs. No additional deployment is needed as the catalog is accessed directly from the GitHub repository via raw content URLs.

### Access URLs

The catalog is accessible via STAC Browser using GitHub raw content URLs:

```
https://radiantearth.github.io/stac-browser/#/external/https://raw.githubusercontent.com/[GITHUB_USERNAME]/stac-api/refs/heads/[BRANCH_NAME]/ibf_catalog/flood/fl_catalog.json?.language=en
```

Example for flood-main branch:
```
https://radiantearth.github.io/stac-browser/#/external/https://raw.githubusercontent.com/icpac-igad/stac-api/refs/heads/flood-main/ibf_catalog/flood/fl_catalog.json?.language=en
```

Direct catalog access:
```
https://raw.githubusercontent.com/icpac-igad/stac-api/refs/heads/flood-main/ibf_catalog/flood/fl_catalog.json
```

## Data Format

Each collection contains:
- **Collection JSON**: Metadata describing the collection
- **Item JSON files**: Individual data items with references to actual data files (GeoTIFFs, COGs)

Example item structure:
```json
{
  "type": "Feature",
  "assets": {
    "data": {
      "href": "./data/flood_inundation_20241017.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["data"]
    }
  }
}
```

## Local Development

### Running the STAC Server Locally

If you encounter CORS issues with the GitHub raw URLs, you can run a local server:

```bash
cd ibf_catalog
python stac_server.py 8000
```

Then access via:
- **Direct catalog**: `http://localhost:8000/flood/fl_catalog.json`
- **STAC Browser**: `https://radiantearth.github.io/stac-browser/#/external/http://localhost:8000/flood/fl_catalog.json`

The local server includes proper CORS headers to work with STAC Browser.

## License

Proprietary - IGAD Climate Prediction and Applications Centre (ICPAC)

## Contact

- **ICPAC**: https://www.icpac.net
- **E4DRR**: Engineering for Disaster Risk Reduction