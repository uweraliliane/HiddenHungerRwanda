🌍 Ending Hidden Hunger in Rwanda
Track 2 – Big Data Hackathon 2025

Team: UWERA Liliane
Language: Python
Deployment: Streamlit

📊 Project Overview

Despite progress in recent years, over 33% of Rwandan children under 5 remain stunted. This project leverages national data and machine learning to:

🗺️ Identify malnutrition hotspots

🧠 Model key predictive risk factors

🧮 Simulate household-level stunting risk

🧩 Recommend evidence-based policy interventions

💻 Provide a decision-support dashboard for government and NGO planning

🎯 Objectives

Map stunting, wasting, and underweight rates across Rwanda

Train models (XGBoost, LightGBM, Logistic Regression) on CFSVA 2024 data

Pinpoint top malnutrition predictors

Simulate stunting risk using household inputs

Recommend root-cause-based interventions

Build a decision-support dashboard

📊 Key Findings
Top 5 High-Stunting Districts:

Nyabihu

Rubavu

Rutsiro

Burera

Gakenke

Top Predictive Risk Factors:

Mid-Upper Arm Circumference (MUAC)

Vitamin A intake

Household Wealth Index

Dietary Diversity (Women)

WASH conditions (water source, handwashing)

Illness history (diarrhea, fever)

🧠 Root Cause Summary
Feature	Root Cause	Suggested Intervention
Low MUAC	Undernutrition	Growth monitoring, feeding support
No Vitamin A	Micronutrient deficiency	Supplementation campaigns
Low Wealth Index	Poverty	Cash transfers, job creation programs
Unsafe Water Source	Infrastructure gaps	Water access projects, WASH support
Rare Handwashing	Hygiene knowledge gap	Community hygiene education
Low Dietary Diversity	Food insecurity	Kitchen gardens, local nutrition farming
💻 Dashboard Features

The Streamlit dashboard includes the following interactive tabs:

🗺️ Geographic Insights – Choropleth maps by district & province

📈 Feature Importance – Model-driven risk factor analysis

🧠 Stunting Risk Simulator – Predict household stunting risk

🧩 Root Causes & Interventions – RCA and policy mapping

📂 Repository Structure
HiddenHungerRwanda/
├── app.py                               # Streamlit dashboard
├── README.md                            # Project documentation
├── To_whom_Uwera_Liliane_final.pdf      # Project report
├── demo/
│   └── demo.webm                        # Demo walkthrough
├── Data/
│   ├── district_geospatial_summary.csv
│   ├── gadm41_RWA_shp.zip               # Shapefiles
│   ├── rwanda_districts.geojson
│   ├── rwanda_province.json
│   ├── xgb_feature_importances.csv
│   ├── lgbm_smote_classweight_feature_importance.csv
│   ├── logreg_feature_importance.csv
│   ├── LightGBM_feature_importance.csv
│   └── Microdata.zip                    # Raw data

📦 Installation

To get started with the project, follow these steps:

git clone https://github.com/<yourusername>/HiddenHungerRwanda.git
cd HiddenHungerRwanda
pip install -r requirements.txt
streamlit run app.py

📈 Data Sources

This project uses the following publicly available dataset:

National Institute of Statistics of Rwanda (NISR)

Comprehensive Food Security and Vulnerability Analysis (CFSVA) 2024, Version 0.1 – Public Use Dataset

Kigali, Rwanda: NISR, 2024.

Available from: NISR Microdata Portal

License: Public Use Dataset — for research and policy analysis purposes.
Access: Free download from the NISR Microdata Portal.

🧩 Variables Used in Modeling
Categories:

Child Health: MUAC (Mid-Upper Arm Circumference), Illness history (fever, diarrhea)

Dietary Factors: Vitamin A intake, Dietary diversity (children & women)

Socioeconomic Status: Household wealth index, Education level of caregiver

WASH Indicators: Drinking water source, Handwashing availability

Household Demographics: Household size, Region (province/district)

⚠️ Note: Variables directly implying stunting (e.g., height-for-age Z-scores) were excluded to prevent data leakage.

⚙️ Data Preprocessing Steps

Removed incomplete or duplicate records

Replaced “Unknown” location values with randomly assigned valid cells/villages

Standardized categorical and numerical values

Applied normalization to scale features between 0–1

Balanced the dataset using SMOTE and class weighting

🗺️ Geospatial Data

Rwanda district and province boundaries from GADM v4.1 shapefiles

Converted to GeoJSON format for integration in Streamlit maps

🧾 Citation for Use

Data Citation:

“National Institute of Statistics of Rwanda (NISR). Comprehensive Food Security and Vulnerability Analysis (CFSVA) 2024, Version 0.1, Public Use Dataset.”

📝 License

This project is for educational and research purposes under the Big Data Hackathon 2025 – Ending Hidden Hunger in Rwanda (Track 2).
Data: © NISR (2024) — Public Use Dataset.
Dashboard and model code: © UWERA Liliane (2025).
