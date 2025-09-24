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

### Automated GitHub Actions Deployment

The repository includes automated deployment via GitHub Actions when pushing to:
- `flood-main` - Primary flood catalog deployment
- `flood-*` - Any branch starting with "flood-" (e.g., flood-dev, flood-staging)

### Access URLs

After deployment, the catalog is accessible via STAC Browser:

```
https://radiantearth.github.io/stac-browser/#/external/https://[GITHUB_USERNAME].github.io/stac-api/[BRANCH_NAME]/fl_catalog.json
```

Example for flood-main branch:
```
https://radiantearth.github.io/stac-browser/#/external/https://icpac-igad.github.io/stac-api/flood-main/fl_catalog.json
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

```bash
cd ibf_catalog
python stac_server.py 8000
```

Access at: `http://localhost:8000/flood/fl_catalog.json`

## License

Proprietary - IGAD Climate Prediction and Applications Centre (ICPAC)

## Contact

- **ICPAC**: https://www.icpac.net
- **E4DRR**: Engineering for Disaster Risk Reduction