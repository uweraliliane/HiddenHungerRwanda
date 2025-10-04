Ending Hidden Hunger in Rwanda

Track 2 — Big Data Hackathon 2025
Team: [Your Name / Team Name]
Theme: Predictive Analytics for Child Malnutrition and Policy Targeting
Focus: Childhood Stunting using 2024 CFSVA Microdata
Submission Type: Full Stack Dashboard + Policy Brief + Predictive Models

🌍 Problem Background

Despite national progress, an estimated 33% of children under five in Rwanda remain stunted — a condition that causes irreversible cognitive, physical, and economic disadvantages. Hidden hunger, driven by micronutrient deficiencies and chronic undernutrition, threatens Rwanda’s long-term human capital development.

This project leverages 2024 CFSVA data and machine learning to:

🔍 Identify hotspots of stunting and related malnutrition indicators

🧠 Model key predictive factors and root causes

🧩 Recommend evidence-based multisector interventions

💻 Deploy an interactive dashboard for policy design and targeting

🎯 Objectives

📍 Map district-level stunting, wasting, and underweight using 2024 CFSVA data

📊 Model the drivers of stunting via XGBoost, LightGBM, and Logistic Regression

🧠 Predict stunting risk using household-level input simulation

📈 Visualize feature importance and geographic disparities

🧩 Recommend root cause-based policies and sectoral interventions

🧠 Key Insights

High-stunting districts include: Nyabihu, Burera, Rubavu, Rutsiro, Gakenke

Top predictive features across all models:

MUAC (Mid-Upper Arm Circumference)

Vitamin A supplementation status

Household Wealth Index

Dietary diversity (especially women’s MDD-W)

WASH factors (water source, handwashing practices)

Health shocks like diarrhea, fever, and mouth illness remain key risk amplifiers

🔍 Root Causes & Interventions
🔎 Feature	📉 Root Cause	🎯 Example Intervention
MUAC (Low)	Inadequate feeding	Growth monitoring & feeding support
No Vitamin A	Micronutrient deficiency	Supplementation programs
Low Wealth Index	Chronic poverty	Cash transfers & livelihood programs
Unsafe Water	Infrastructure gap	Safe water access, boreholes
Poor Hygiene	Behavior/awareness	Hygiene promotion, handwashing stations
Low Dietary Diversity	Food insecurity, access	Nutrition-sensitive agriculture, women-led farming
Low Maternal Education	Knowledge gap	Parenting education & adult literacy
💻 Dashboard Features

Built with Streamlit and Plotly, the dashboard has four core tabs:

🗺️ Geographic Insights
Choropleth maps of malnutrition indicators across districts and provinces

📈 Feature Importance
Visualization of top features from XGBoost, LightGBM, and Logistic Regression

🧠 Predict Risk (Simulator)
Heuristic stunting risk calculator based on key household inputs

🧩 Root Cause Analysis & Policies
Data-informed policy mapping for each top feature and geographic priority

📦 Repository Structure
HiddenHungerRwanda/
│
├── app.py                          # Streamlit dashboard
├── data/                           # CSV and GeoJSON data files
│   ├── district_geospatial_summary.csv
│   ├── xgb_feature_importances.csv
│   ├── LightGBM_feature_importance.csv
│   ├── logreg_feature_importance.csv
│   ├── rwanda_districts.geojson
│   └── rwanda_province.json
├── outputs/                        # Maps, charts, feature graphs
├── notebooks/                      # EDA, modeling, PCA, MI, etc.
├── scripts/                        # Model training, preprocessing
├── docs/                           # Policy brief, write-ups
├── requirements.txt                # Python dependencies
└── README.md                       # This file

📈 Data Sources

Survey: 2024 Comprehensive Food Security and Vulnerability Assessment (CFSVA)

Publisher: National Institute of Statistics of Rwanda (NISR)

Coverage: Nationally representative household, women, and child data

Geography: Province and District level

Domain	Indicator Examples	Dataset
Nutrition	MUAC, MDD-W, Birth Weight	df_children, df_women
Food Security	Food shortages, spending patterns	df_household
Health Access	ANC visits, vitamin A intake	df_women
WASH	Water source, handwashing, toilets	df_household
Agriculture	Garden, livestock, biofortified crops	df_household
🧪 Methodology Overview

Data Wrangling: Standardized variables, missing value imputation

Exploratory Analysis: Distribution of indicators by geography & wealth quintiles

Modeling: XGBoost, LightGBM, Logistic Regression for feature selection

Visualization: Choropleth maps, bar plots, summary stats

Risk Simulation: Heuristic model using key predictors

Root Cause Analysis: Link features → root causes → recommended policies

📊 Outputs

✅ ML-based feature importance rankings

✅ Interactive stunting risk simulator

✅ Choropleth maps for stunting, wasting, underweight

✅ Root-cause linked policy recommendations

✅ Executive Summary / Policy Brief (2 pages)
