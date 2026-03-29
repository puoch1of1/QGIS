# 🌍 Climate Against Conflict

A data-driven project analyzing the relationship between climate change, environmental stress, and conflict in South Sudan and Sub-Saharan Africa.

This project leverages geospatial analysis, conflict datasets, and environmental indicators to uncover patterns, trends, and insights that can support peacebuilding and climate resilience efforts.

---

## 🎯 Objectives

- Analyze how climate factors influence conflict patterns
- Explore trends in political violence and civilian targeting
- Build geospatial visualizations using QGIS
- Support data-driven policy and humanitarian insights

---

## 📊 Datasets

This repository currently includes:

- Civilian targeting events and fatalities (monthly data)
- Political violence events and fatalities
- Mobility tracking baseline assessment (DTM dataset)

> 📌 Data sources include humanitarian and conflict monitoring organizations (HRP, IOM, etc.)

---

## 🛠️ Tools & Technologies

- **QGIS** – geospatial analysis and mapping
- **Excel / CSV** – data storage and preprocessing
- **Python** (Pandas, GeoPandas) for automation and analysis

---

## 🧠 Methodology

1. **Data Collection**
   - Gather conflict and mobility datasets from verified sources

2. **Data Cleaning**
   - Standardize formats (dates, regions, metrics)
   - Handle missing or inconsistent values

3. **Data Analysis**
   - Identify trends in fatalities and conflict events
   - Compare across time (monthly/yearly patterns)

4. **Geospatial Mapping (QGIS)**
   - Map conflict hotspots
   - Overlay environmental or regional data

5. **Insight Generation**
   - Highlight correlations between environmental stress and conflict
   - Support interpretation with visual outputs

---

## 🗺️ Planned Visualizations

- Conflict event heatmaps
- Fatality distribution maps
- Time-series dashboards
- Regional comparison maps

---

## 📁 Project Structure

```
climate-against-conflict/
├── README.md
├── data/
│   ├── raw/               # Original datasets
│   ├── processed/         # Cleaned data
│   └── metadata/          # Data dictionaries and documentation
├── notebooks/             # Jupyter notebooks for analysis
├── scripts/               # Python automation scripts
├── qgis-projects/         # QGIS project files (.qgs)
└── outputs/               # Visualizations, maps, and reports
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- QGIS (for mapping)
- pandas, geopandas, openpyxl (see `requirements.txt`)

### Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Explore the data
jupyter notebook notebooks/01_data_exploration.ipynb
```

---

## 🚀 Future Improvements

- Automate data pipelines (Python + APIs)
- Integrate climate datasets (rainfall, drought index, temperature)
- Build interactive dashboards (Power BI / Streamlit)
- Develop reproducible workflows for analysis

---

## 🤝 Contributing

Contributions, ideas, and feedback are welcome.

---

## 📜 License

See LICENSE file for details.

---

## 💡 Project Vision

Promoting sustainable peace through data, climate awareness, and geospatial intelligence.