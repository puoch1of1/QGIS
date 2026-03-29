# QGIS Workflow Guide

This guide outlines how to use QGIS for geospatial analysis and visualization in the Climate Against Conflict project.

---

## Getting Started with QGIS

### Project Setup

1. **Create a new QGIS project**
   - File → New → Default Project
   - Save in `qgis-projects/` with a descriptive name (e.g., `conflict_hotspots_2026.qgs`)

2. **Set Project CRS (Coordinate Reference System)**
   - Project → Properties → CRS
   - Select **EPSG:4326** (WGS 84) for global compatibility
   - Or **EPSG:32636** for South Sudan (UTM Zone 36N)

3. **Configure default styles**
   - Settings → Style Manager
   - Create and save custom color schemes for conflict intensity

---

## Data Integration

### Importing Tabular Data

1. **Import CSV/Excel data with coordinates**
   - Layer → Add Layer → Add Delimited Text Layer
   - Select processed CSV files from `/data/processed/`
   - Specify X field (longitude) and Y field (latitude)
   - Set CRS to EPSG:4326

2. **Expected data format for import:**
   ```
   location_name, latitude, longitude, fatalities, event_count, date
   Juba, 4.851, 31.587, 25, 5, 2026-03-01
   ```

---

## Visualization Techniques

### Heatmap Visualization

1. **Create conflict heatmaps**
   - Use Point Interpolation (Heatmap) renderer
   - Raster → Analysis Tools → Heatmap
   - Configure radius (in map units) based on conflict spread

2. **Color ramp selection**
   - Red (high intensity) → Orange → Yellow → Green (low intensity)

### Choropleth Mapping (Regional Data)

1. **Import South Sudan administrative boundaries**
   - download from: https://www.openstreetmap.org/
   - Layer → Add Layer → Add Vector Layer
   - Select boundary shapefile (.shp)

2. **Join data to boundaries**
   - Right-click layer → Properties → Joins
   - Join attribute table based on state/region name

3. **Apply symbology**
   - Layer → Properties → Symbology
   - Graduated symbols based on fatality counts

---

## Time Series & Temporal Analysis

### Creating animated maps (time series)

1. **Install Time Manager plugin** (if not pre-installed)
   - Plugins → Manage and Install Plugins
   - Search "Time Manager"
   - Install and enable

2. **Configure temporal data**
   - Ensure data includes date/time fields
   - Time Manager → Settings → Configure layers with temporal data

3. **Create animation**
   - Time Manager → Play animation
   - Export as video (File → Export → Video)

---

## Multi-Layer Analysis

### Overlay Analysis

1. **Layer order matters**
   - Place conflict data on top
   - Underlying layers: regional boundaries, environmental data

2. **Example workflow:**
   ```
   Bottom → Top:
   1. Base map (OpenStreetMap)
   2. South Sudan administrative boundaries
   3. Conflict events (points with heatmap)
   4. Displaced populations (if available)
   ```

### Identify Hotspots

1. **Vector → Analysis Tools → Spatial Index**
   - Create spatial index for faster queries

2. **Vector → Analysis Tools → Density**
   - Calculate kernel density estimation
   - Identify statistically significant conflict clusters

---

## Exporting Results

### Save QGIS Project
- File → Save As
- Name: descriptive (e.g., `political_violence_heatmap_jan2026`)
- Format: `.qgs` (QGIS project format)

### Export Visualizations

1. **Export as image**
   - Project → Import/Export → Export as Image
   - Formats: PNG, JPG, PDF (recommended for reports)
   - Resolution: 300 DPI for printed maps

2. **Export as vector (Shapefile/GeoJSON)**
   - Right-click layer → Export → Save Features As
   - Format: Shapefile or GeoJSON

3. **Web map export**
   - Project → Import/Export → Export to HTML
   - Creates interactive web-based map

---

## Project Organization

```
qgis-projects/
├── conflict_hotspots_2026.qgs
├── political_violence_analysis.qgs
├── displacement_patterns.qgs
└── regional_comparison.qgs
```

### Naming convention
- `[analysis_type]_[region]_[date].qgs`
- Example: `civilian_targeting_northern_states_mar2026.qgs`

---

## Recommended Analyses

### 1. Conflict Intensity by Region
- Import political violence dataset
- Create point layer with fatality counts
- Apply heatmap visualization
- Identify top 5 hotspots

### 2. Displacement-Conflict Correlation
- Overlay DTM mobility data with conflict events
- Analyze geographic proximity
- Document spatial correlation patterns

### 3. Temporal Trends
- Create separate layers for each month
- Use Time Manager for animation
- Observe seasonal patterns

### 4. Multi-hazard Risk Assessment
- Combine conflict data with environmental variables
- Create composite risk index
- Export risk maps for humanitarian planning

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Data not displaying | Check CRS compatibility; ensure coordinates are in valid range |
| Slow performance | Create spatial index; reduce layer complexity |
| Styling not updating | Right-click layer → Refresh |
| Export quality poor | Increase DPI; check output resolution |

---

## References

- QGIS Documentation: https://docs.qgis.org/
- South Sudan Geospatial Data: https://data.humdata.org/
- OpenStreetMap: https://www.openstreetmap.org/

---

## Contact & Support

For QGIS-specific questions or troubleshooting, refer to the community forum or the main project README.
