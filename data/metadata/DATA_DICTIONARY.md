# Data Dictionary

This document describes the structure and content of all datasets in the Climate Against Conflict project.

---

## 1. Civilian Targeting Events and Fatalities

**File:** `south-sudan_hrp_civilian_targeting_events_and_fatalities_by_month-year_as-of-26mar2026.xlsx`

**Description:** Monthly records of civilian targeting events and fatalities in South Sudan from humanitarian response data.

### Expected Columns
- **Date/Month/Year** – Time period for the record
- **State/Region** – Geographic location within South Sudan
- **Events** – Number of civilian targeting events
- **Fatalities** – Number of civilian deaths
- **Incidents** – Incident count or type classification

### Data Quality Notes
- Fill gaps in monthly data (if any) with interpolation or forward-fill methods
- Validate regional names against standardized administrative boundaries
- Check for outliers in fatality counts

### Use Cases
- Trend analysis of civilian casualties over time
- Regional comparison of targeting intensity
- Correlation with seasonal/climate patterns

---

## 2. Political Violence Events and Fatalities

**File:** `south-sudan_hrp_political_violence_events_and_fatalities_by_month-year_as-of-26mar2026.xlsx`

**Description:** Monthly records of political violence events and fatalities, including armed conflict incidents.

### Expected Columns
- **Date/Month/Year** – Time period for the record
- **State/Region** – Geographic location
- **Events** – Count of political violence events
- **Fatalities** – Number of deaths from political violence
- **Event Type** – Classification (e.g., armed conflict, protest violence)

### Data Quality Notes
- Cross-reference with international conflict datasets for validation
- Standardize event type classifications
- Investigate spikes in fatality data

### Use Cases
- Political violence trend analysis
- Comparison with civilian targeting patterns
- Regional conflict intensity mapping

---

## 3. Mobility Tracking Baseline Assessment (DTM Dataset)

**File:** `ssd-dtm-mobility-tracking-r16-baseline-assessment-dataset_updated_20250507.xlsx`

**Description:** Baseline assessment of population mobility from the IOM Displacement Tracking Matrix (DTM), Round 16.

### Expected Columns
- **County/Location** – Administrative area assessed
- **Population Count** – Number of individuals tracked
- **IDPs (Internally Displaced Persons)** – Count of displaced populations
- **Returnees** – Population returning home
- **Assessment Date** – When the assessment was conducted
- **Status/Conditions** – Living conditions, shelter status, etc.

### Data Quality Notes
- Verify geographic coordinates for all locations
- Check population consistency across rounds
- Note any methodological changes from previous assessments

### Use Cases
- Understanding population displacement patterns
- Correlating mobility with conflict events
- Humanitarian needs assessment

---

## Data Standards

### Field Naming Convention
- Column names use **snake_case** in processed data
- Maintain original names for raw data (preserve integrity)

### Date Format
- All dates in processed data: `YYYY-MM-DD`
- Standardize year-only data to `YYYY-01-01` or `YYYY-06-30` (depending on context)

### Geographic Data
- Use ISO 3166-2:SS codes for South Sudan states
- Include latitude/longitude for spatial analysis
- Validate against QGIS boundary files

### Fatality/Event Data
- Use integers (no decimals for counts)
- Document any estimated or missing values
- Maintain metadata on data reliability/source

---

## Processing Workflow

1. **Raw Data** → Stored in `/data/raw/`
2. **Cleaning** → Scripts in `/scripts/` handle standardization
3. **Processed Data** → Stored in `/data/processed/`
4. **Analysis** → Notebooks in `/notebooks/` use processed data

---

## Data Access & Credibility

- All data sourced from humanitarian and conflict monitoring organizations
- HRP (Humanitarian Response Plan)
- IOM (International Organization for Migration)
- Verify source URLs and access dates in project logs

---

## Contact & Questions

For data-related inquiries or clarifications, reference the methodology section in the main README.
