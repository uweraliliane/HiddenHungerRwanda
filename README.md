# 🧭 Hidden Hunger in Rwanda — Data-Driven Analysis (CFSVA 2024)

This repository contains a data science framework for identifying and addressing hidden hunger and micronutrient deficiencies in Rwanda using the **2024 Comprehensive Food Security and Vulnerability Assessment (CFSVA)** microdata. It was developed as part of **Track 2 – NISR Big Data Hackathon 2025**.

---

## 🎯 Objectives

- 📍 Map malnutrition and dietary inadequacy hotspots
- 🧠 Identify socio-economic and structural root causes
- 🧒🏽 Predict risk of malnutrition among children and women
- 🏥 Propose localized interventions across health, agriculture, and education

---

## 📦 Data Source

- **Survey**: CFSVA 2024 by the National Institute of Statistics of Rwanda (NISR)
- **Coverage**: Nationally representative household and individual-level data
- **Units of Analysis**: Children under 5, women of reproductive age, and households
- **Geography**: Province and district level

---

## 🔍 Key Indicators

| Domain        | Indicator                           | Source Dataset |
|---------------|--------------------------------------|----------------|
| Nutrition     | MUAC (Children & Women), MDD-W       | `df_children`, `df_women` |
| Food Security | Food shortage, food group spending   | `df_household` |
| Health Access | ANC visits, supplementation          | `df_women`     |
| WASH          | Water source, sanitation             | `df_household` |
| Agriculture   | Garden, livestock, biofortified crops| `df_household` |

---

## 🧪 Methodology

1. **Data Cleaning & Wrangling**: Standardize variables, handle missing data  
2. **Exploratory Analysis**: Malnutrition by geography, gender, income  
3. **Geospatial Mapping**: Hotspots, dietary gaps, clustering  
4. **Root Cause Analysis**: Multivariate modeling (e.g., logistic regression)  
5. **Predictive Modeling**: Risk prediction using Random Forest, XGBoost  

---

## 📈 Outputs

- ✅ Geospatial risk maps (folium, kepler.gl)
- ✅ Statistical models of key malnutrition drivers
- ✅ Prediction tool for identifying high-risk households
- ✅ Policy dashboard (optional)
- ✅ 1–2 page policy brief with actionable insights

---

## 📂 Repository Structure

```bash
HiddenHungerRwanda/
│
├── data/               # Cleaned & raw data (excluded from GitHub)
├── notebooks/          # Jupyter Notebooks (EDA, modeling, mapping)
├── scripts/            # Python scripts for preprocessing & modeling
├── outputs/            # Figures, maps, and charts
├── docs/               # Policy brief and supplementary documentation
├── requirements.txt    # Python dependencies
└── README.md           # This file
