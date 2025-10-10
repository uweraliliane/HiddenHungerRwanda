# 🌍 Ending Hidden Hunger in Rwanda  
### 📊 NISR Big Data Hackathon 2025 — Track 2  
**Team:** UWERA Liliane  
**Language:** Python  
**Platform:** Streamlit  

---

## 📌 Introduction

Despite commendable progress in food security, over **33% of Rwandan children under five** still suffer from **stunting** due to chronic undernutrition and hidden hunger (micronutrient deficiencies).

This project uses **machine learning and geospatial analysis** to identify at-risk populations and inform targeted interventions. A user-friendly dashboard empowers policymakers, NGOs, and public health professionals to make data-driven decisions.

---

## 🎯 Objectives

This project was developed for **Hackathon Track 2: Ending Hidden Hunger**, with the following key goals:

- 🗺️ **Map** stunting, wasting, and underweight across Rwanda  
- 🤖 **Model** household-level malnutrition risk using ML (XGBoost, LightGBM, Logistic Regression)  
- 📉 **Identify** top predictive risk factors  
- 🧮 **Simulate** household stunting probabilities  
- 🛠️ **Recommend** actionable policy & program interventions  
- 📊 **Visualize** findings through an interactive Streamlit dashboard  

---

## 📊 Data Sources

- 🗃️ **CFSVA 2024 – Comprehensive Food Security and Vulnerability Analysis**  
  🔗 [CFSVA 2024](https://statistics.gov.rw/data-sources/surveys/CFSVA/comprehensive-food-security-vulnerability-analysis-cfsva-2024)

- 🌍 **Rwanda Geospatial Boundaries**  
  🔗 [SimpleMaps Rwanda GIS](https://simplemaps.com/gis/country/rw)

- ➕ **Supplemental data**: DHS, WASH, health indicators

---

## 🧠 Key Findings

### 🔺 Top 5 High-Stunting Districts

1. Nyabihu  
2. Rubavu  
3. Rutsiro  
4. Burera  
5. Gakenke  

### 💡 Top Predictive Risk Factors

- Low MUAC (Mid-Upper Arm Circumference)  
- Lack of Vitamin A intake  
- Poor wealth index  
- Low dietary diversity (women)  
- Unsafe water source  
- Illness history (diarrhea, fever)  

---

## 🧩 Root Cause Analysis & Interventions

| **Feature**            | **Root Cause**            | **Suggested Intervention**                         |
|------------------------|---------------------------|----------------------------------------------------|
| Low MUAC               | Undernutrition            | Growth monitoring, feeding support                 |
| No Vitamin A Intake    | Micronutrient deficiency  | Supplementation campaigns                          |
| Low Wealth Index       | Poverty                   | Cash transfers, income-generation programs         |
| Unsafe Water Source    | WASH infrastructure gaps  | Water access projects, hygiene promotion           |
| Rare Handwashing       | Hygiene knowledge gap     | Community education, WASH campaigns                |
| Low Dietary Diversity  | Food insecurity           | Kitchen gardens, school feeding, home farming      |

---

## 💻 Dashboard Features

An interactive **Streamlit dashboard** includes:

- 🗺️ Geospatial Choropleths – District-level stunting & wasting rates  
- 📊 Feature Importance Viewers – Compare risk factors across models  
- 🧮 Stunting Risk Simulator – Predict household risk interactively  
- 📝 Policy Brief Generator – Auto-generate PDF recommendations  
- 📦 Data Download – Export processed summaries  

---

## 🧠 Machine Learning Pipeline

- 🔍 Data preprocessing: missing values, encoding, normalization  
- 🧪 Feature engineering: nutrition, health, WASH, socioeconomics  
- ⚖️ Class balancing: SMOTE & `class_weight`  
- 🧠 Models used:
  - Logistic Regression  
  - XGBoost  
  - LightGBM  
  - CatBoost (for comparison)  
- 🧮 Evaluation metrics: Accuracy, F1, ROC AUC, Precision, Recall  
- 💾 Model serialization: `joblib`  

---

## 🗂️ Directory Structure

```bash
├── app.py                         # Main Streamlit entry point
├── Models/                        # Serialized ML models
│   ├── stunting_model.pkl
│   └── feature_pipeline.pkl
├── Data/                          # Raw and processed data
│   ├── district_geospatial_summary.csv
│   ├── rwanda_districts.geojson
│   ├── Microdata.zip
│   ├── ... (other feature importance CSVs)
├── demo/
│   └── demo.webm                  # Screen recording of app demo
├── 🇷🇼 Tackling Hidden Hunger.docx
├── To whom Uwera Liliane final.pdf
├── LICENSE
└── README.md
