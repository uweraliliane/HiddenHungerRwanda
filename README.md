# 🌍 Ending Hidden Hunger in Rwanda  
### 📊 NISR Big Data Hackathon 2025 — Track 2  
**Team:** UWERA Liliane  
**Language:** Python  
**Platform:** Streamlit  

---

## 📌 Introduction

Despite progress in recent years, over **33% of Rwandan children under five** remain stunted due to **micronutrient deficiencies and chronic undernutrition**.  

This project leverages **CFSVA 2024 data** and machine learning to:  
- Identify geographic **malnutrition hotspots**  
- Model **key risk factors** contributing to undernutrition  
- Simulate **household-level stunting risk**  
- Recommend **evidence-based interventions**  
- Deliver a **decision-support dashboard** for policymakers and NGOs  

---

## 🎯 Objectives

This solution addresses the **Hackathon Track 2: Ending Hidden Hunger**, by:

1. **Mapping** stunting, wasting, and underweight prevalence across Rwanda  
2. **Modeling** malnutrition risk using ML (XGBoost, LightGBM, Logistic Regression)  
3. **Identifying** high-impact predictors and risk factors  
4. **Simulating** household-level stunting probabilities  
5. **Recommending** policy and program interventions  
6. **Visualizing** insights via an interactive Streamlit dashboard  

---

## 📊 Data Sources

- **Primary Dataset:** [CFSVA 2024 – Comprehensive Food Security and Vulnerability Analysis](https://statistics.gov.rw/data-sources/surveys/CFSVA/comprehensive-food-security-vulnerability-analysis-cfsva-2024)  
- **Provider:** National Institute of Statistics of Rwanda (NISR)  
- Additional sources: DHS, WASH datasets (if applicable)

---

## 🧠 Key Findings

### 🔺 Top 5 High-Stunting Districts
1. Nyabihu  
2. Rubavu  
3. Rutsiro  
4. Burera  
5. Gakenke  

### 💡 Top Predictive Risk Factors
- Mid-Upper Arm Circumference (MUAC)  
- Vitamin A intake  
- Wealth Index  
- Dietary Diversity (Women)  
- Unsafe Water Source  
- Illness History (Diarrhea, Fever)  

---

## 🧩 Root Cause Analysis & Interventions

| **Feature**               | **Root Cause**            | **Suggested Intervention**                         |
|---------------------------|---------------------------|----------------------------------------------------|
| Low MUAC                  | Undernutrition            | Growth monitoring, feeding support                 |
| No Vitamin A Intake       | Micronutrient deficiency  | Supplementation campaigns                          |
| Low Wealth Index          | Poverty                   | Cash transfers, income-generation programs         |
| Unsafe Water Source       | WASH infrastructure gaps  | Water access projects, hygiene promotion           |
| Rare Handwashing          | Hygiene knowledge gap     | Community education, WASH campaigns                |
| Low Dietary Diversity     | Food insecurity           | Kitchen gardens, school feeding, home farming      |

---

## 💻 Dashboard Features

An interactive **Streamlit dashboard** was developed with the following key components:

- 🗺️ **Geographic Insights** – Choropleth maps of malnutrition rates  
- 📊 **Feature Importance** – Visual analysis of top risk factors  
- 🧮 **Stunting Risk Simulator** – Household-level predictions  
- 🧠 **Root Cause & Policy Mapping** – Interventions by predictor  
- 📝 **Policy Brief Generator** – Auto-generate local policy briefs  

---

## 📈 Machine Learning Pipeline

- Data cleaning & preprocessing (missing values, encoding)
- Feature engineering (nutritional, socioeconomic, WASH indicators)
- Class balancing (SMOTE, class weights)
- Model training:
  - Logistic Regression
  - XGBoost
  - LightGBM
- Evaluation metrics: Accuracy, Precision, Recall, F1, ROC AUC, Log Loss
- Model serialization via `joblib`  

---

## 🛠 Tech Stack

- **Frontend:** Streamlit  
- **Visualization:** Plotly, Seaborn, Matplotlib, Folium  
- **ML & Data:** Pandas, NumPy, Scikit-learn, XGBoost, LightGBM, Imbalanced-learn  
- **Utilities:** Joblib, Statsmodels, Collections, OS, Regex  

---
<pre> ## 📂 Repository Structure

├── app/
│ ├── dashboard.py # Streamlit frontend
│ ├── simulator.py # Risk prediction interface
│ ├── visualizations.py # Mapping and plotting functions
│ └── utils.py # Helper functions
├── models/
│ ├── stunting_model.pkl # Trained ML model
│ └── feature_pipeline.pkl # Feature engineering pipeline
├── data/
│ ├── raw/ # Raw CFSVA data
│ └── processed/ # Cleaned datasets
├── reports/
│ └── policy_brief.pdf # Intervention recommendations
├── README.md
└── requirements.txt
  </pre>

---

## 📢 Hackathon Fit & Innovation

✔ Aligned with **Track 2: Ending Hidden Hunger**  
✔ Uses **national survey data (CFSVA)**  
✔ Delivers **predictive insights & interventions**  
✔ Builds a **user-friendly decision support tool**  
✔ Bridges **data science with public policy**

---

## 🔮 Future Work

- Integrate **real-time data** from mobile surveys or health systems  
- Expand simulator to include **nutrition-sensitive agriculture inputs**  
- Deploy dashboard as a **web app for policymakers**  
- Collaborate with **local NGOs and government** for piloting  

---

## 🙌 Acknowledgments

Special thanks to:
- National Institute of Statistics of Rwanda (NISR)  
- Organizers of the Big Data Hackathon 2025  
- CFSVA data collection team  


