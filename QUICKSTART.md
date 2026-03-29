# Quick Start Guide

Get up and running with the Climate Against Conflict project.

---

## 1. Initial Setup (5 minutes)

### Install Python Dependencies

```bash
# Navigate to project root
cd "c:\Users\lomas\QGIS\QGIS"

# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Verify Data Files

Check that the following datasets exist in the project root:
```
OK - south-sudan_hrp_civilian_targeting_events_and_fatalities_by_month-year_as-of-26mar2026.xlsx
OK - south-sudan_hrp_political_violence_events_and_fatalities_by_month-year_as-of-26mar2026.xlsx
OK - ssd-dtm-mobility-tracking-r16-baseline-assessment-dataset_updated_20250507.xlsx
```

---

## 2. Explore Data (10 minutes)

### Option A: Run Python Script

```bash
cd scripts
python explore_data.py
```

**Output:** Summary statistics and data quality report for all datasets.

### Option B: Interactive Jupyter Notebook

```bash
cd notebooks
jupyter notebook 01_data_exploration.ipynb
```

**Advantages:** 
- Interactive visualization
- Ability to run cells individually
- Easy to modify and experiment

---

## 3. Data Structure Overview

After exploration, familiarize yourself with:

- **Raw Data** → `/data/raw/` (original, unmodified files)
- **Processed Data** → `/data/processed/` (cleaned CSV files)
- **Metadata** → `/data/metadata/DATA_DICTIONARY.md` (data definitions)

---

## 4. Next Steps

### For Data Analysis
1. Review [DATA_DICTIONARY.md](data/metadata/DATA_DICTIONARY.md)
2. Run exploration script to understand data structure
3. Check `/notebooks/` for analysis examples
4. Create new scripts in `/scripts/` for specific analyses

### For Geospatial Mapping
1. Open QGIS
2. Follow [QGIS_WORKFLOW.md](QGIS_WORKFLOW.md)
3. Import processed CSV files as point layers
4. Create visualizations and save in `/qgis-projects/`

### For Documentation
1. Record findings in `/notebooks/` or `/outputs/`
2. Save visualizations from QGIS to `/outputs/`
3. Update methodology in project README

---

## Key Files

| File | Purpose |
|------|---------|
| [README.md](README.md) | Project overview |
| [DATA_DICTIONARY.md](data/metadata/DATA_DICTIONARY.md) | Data definitions |
| [QGIS_WORKFLOW.md](QGIS_WORKFLOW.md) | QGIS instructions |
| [requirements.txt](requirements.txt) | Python dependencies |
| [scripts/data_loader.py](scripts/data_loader.py) | Load datasets in Python |
| [scripts/explore_data.py](scripts/explore_data.py) | Basic data exploration |
| [notebooks/01_data_exploration.ipynb](notebooks/01_data_exploration.ipynb) | Interactive notebook |

---

## Common Commands

```bash
# Activate virtual environment
venv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Run Jupyter
jupyter notebook

# Run Python script
python scripts/explore_data.py

# Deactivate environment
deactivate
```

---

## Troubleshooting

**Q: Data files not found when running scripts?**
- Ensure you're in the project root directory (`c:\Users\lomas\QGIS\QGIS`)
- Check that data files are in `/data/raw/` (or project root)

**Q: QGIS won't open the data layer?**
- Ensure coordinates are in latitude/longitude format (EPSG:4326)
- Check that numeric columns don't have text or special characters

**Q: Python script returns "module not found"?**
- Activate virtual environment: `venv\Scripts\activate`
- Reinstall dependencies: `pip install -r requirements.txt`

---

## Support

For questions or issues:
1. Check [DATA_DICTIONARY.md](data/metadata/DATA_DICTIONARY.md) for data structure
2. Review [QGIS_WORKFLOW.md](QGIS_WORKFLOW.md) for mapping guidance
3. Refer to project README for methodology

---

## Checklist for First Session

- [ ] Python environment set up
- [ ] Dependencies installed
- [ ] Data exploration completed
- [ ] Data structure understood
- [ ] First QGIS map created
- [ ] Results saved to /outputs/

---

**Ready to analyze climate and conflict? Let's go!**
