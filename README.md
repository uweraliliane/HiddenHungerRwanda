# 🌍 Ending Hidden Hunger in Rwanda

📊 **NISR Big Data Hackathon 2025 — Track 2**  
**Team:** UWERA Liliane  
**Language:** Python  
**Platform:** Streamlit  

---

## 📌 Introduction

Despite notable progress, over **33% of Rwandan children under five** remain stunted, primarily due to **micronutrient deficiencies** and **chronic undernutrition**. This project leverages **CFSVA 2024 data** and advanced machine learning to:

- Identify geographic **malnutrition hotspots**  
- Model **key risk factors**  
- Simulate **household-level stunting risks**  
- Recommend **targeted interventions**  
- Provide an interactive **Streamlit dashboard** for decision-makers  

---
📅 **Submission Date:** 10 October 2025

## 🎯 Objectives

This project addresses **Track 2: Ending Hidden Hunger**, aiming to:

1. **Map** stunting, wasting, and underweight prevalence across Rwanda  
2. **Model** malnutrition risk with ML (XGBoost, LightGBM, Logistic Regression, CatBoost)  
3. **Identify** high-impact predictors of stunting  
4. **Simulate** stunting probability at household level  
5. **Recommend** data-driven policy & program interventions  
6. **Visualize** key findings in a user-friendly dashboard  

---

## 📊 Data Sources

- **Primary Dataset:** [CFSVA 2024 – Comprehensive Food Security and Vulnerability Analysis](https://statistics.gov.rw/data-sources/surveys/CFSVA/comprehensive-food-security-vulnerability-analysis-cfsva-2024)  
- **Geospatial Data:**  
  - [GADM Rwanda Shapefiles](https://gadm.org/)  
  - [SimpleMaps Rwanda GeoJSON](https://simplemaps.com/gis/country/rw)  
---

## 📈 Key Findings – Hotspots & Risk Factors


### 🔺 Top 5 High-Stunting Districts

1. Nyabihu  
2. Rubavu  
3. Rutsiro  
4. Burera  
5. Gakenke  

### 💡 Most Predictive Risk Factors

- **Mid-Upper Arm Circumference (MUAC)**  
- **Vitamin A intake**  
- **Wealth Index**  
- **Women's Dietary Diversity**  
- **Unsafe Water Source**  
- **Recent Illness (Diarrhea/Fever)**  

---

## 🧩 Root Cause Analysis & Interventions

| **Factor**            | **Root Cause**            | **Recommended Intervention**                          |
|-----------------------|---------------------------|------------------------------------------------------|
| Low MUAC              | Chronic undernutrition     | Community feeding & monitoring programs              |
| No Vitamin A Intake   | Micronutrient deficiency   | Supplementation campaigns, food fortification        |
| Low Wealth Index      | Poverty                   | Cash transfers, job training, income-generation activities |
| Unsafe Water Source   | WASH infrastructure gaps  | Safe water access projects, hygiene education        |
| Low Handwashing Rates | Knowledge / behavior gaps | WASH campaigns, school-based hygiene education       |
| Low Dietary Diversity | Food insecurity           | Kitchen gardens, school feeding programs             |

---

## 💻 Dashboard Features (Streamlit)

- 🗺️ **District-level Maps** – Stunting prevalence visualized via Folium & Plotly  
- 📊 **Risk Factor Importance** – ML-based ranking of features  
- 🧮 **Household Risk Simulator** – Predict stunting from custom inputs  
- 🧠 **Root Cause & Intervention Map** – Policy suggestions by driver  
- 📝 **Policy Brief Generator** – Auto-creates local policy recommendations (PDF)  

---

## 🛠️ Tech Stack

| Component    | Libraries & Tools                                  |
|--------------|--------------------------------------------------|
| **Frontend** | Streamlit, Streamlit-Folium, Plotly               |
| **Data**     | Pandas, NumPy, GeoPandas                          |
| **ML Models**| XGBoost, LightGBM, CatBoost, Logistic Regression |
| **ML Utils** | Scikit-learn, imbalanced-learn (SMOTE), joblib   |
| **Mapping**  | Folium, GeoJSON, SimpleMaps                       |
| **Viz**      | Matplotlib, Seaborn, Plotly                       |
| **Stats**    | Statsmodels                                       |
| **Others**   | Regex, Collections, OS                            |

---

## 🧠 Machine Learning Pipeline

1. **Preprocessing:**  
   - Handle missing data  
   - One-hot encoding, scaling, class balancing (SMOTE, class weights)  
2. **Feature Engineering:**  
   - Nutritional indicators (e.g., MUAC)  
   - Socioeconomic variables (wealth, income)  
   - WASH & health features (water source, recent illness)  
3. **Models Used:**  
   - Logistic Regression  
   - XGBoost  
   - LightGBM  
   - CatBoost  
4. **Evaluation Metrics:**  
   - Accuracy, Precision, Recall, F1, ROC-AUC, Log Loss  
5. **Serialization:**  
   - `joblib` used for model saving/loading  

---
▶️ Demo Video

## 📂 Directory Structure
```text
RwandaHiddenHungerRwanda/
├── app.py
├── Tackling_Hidden_Hunger.docx
├── To whom Uwera Liliane final.pdf
├── LICENSE
├── README.md
├── Data/
│   ├── Microdata.zip
│   ├── gadm41_RWA_shp.zip
│   ├── rwanda_districts.geojson
│   ├── feature_importance CSVs
│   └── model_comparison_results.csv
├── Models/
│   └── Trained ML models (.pkl)
├── demo/
│   └── demo.webm
```

---

## ▶️ Running the App

Ensure **Python 3.9+** is installed and required packages are available.

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```
### Step 2: Launch the Streamlit app
```bash
streamlit run app.py
```
📦 Dependencies (requirements.txt)
```txt
streamlit==1.32.0
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.4.2
xgboost==3.0.5
lightgbm==4.6.0
catboost==1.2.8
matplotlib==3.10.3
seaborn==0.13.2
plotly==5.22.0
folium==0.20.0
imbalanced-learn==0.12.3
joblib==1.4.2
statsmodels==0.14.2
geopandas==1.1.0
```
Generate this list with:
```bash
pip freeze > requirements.txt
```
📢 **Hackathon Relevance & Innovation**

- ✅ Built for Hackathon Track 2: Ending Hidden Hunger  
- ✅ Uses official CFSVA national survey data  
- ✅ Applies machine learning for public health  
- ✅ Interactive dashboard to aid decision-making  
- ✅ Produces localized intervention recommendations  

---

🔮 **Future Work**

- Incorporate real-time health reporting (e.g., mobile surveys)  
- Integrate nutrition-sensitive agriculture components  
- Pilot web-based deployment for government agencies  
- Partner with NGOs for community-level rollouts  

---

🙌 **Acknowledgments**

- National Institute of Statistics of Rwanda (NISR)  
- Organizers of the Big Data Hackathon 2025  
- CFSVA 2024 data collection teams  
- SimpleMaps & GADM for GIS data  

---

🔗 **Useful Links**

---

🔗 **Useful Links**

- 📊 [CFSVA 2024 Dataset](https://statistics.gov.rw/data-sources/surveys/CFSVA/comprehensive-food-security-vulnerability-analysis-cfsva-2024)  
- 🌍 [Rwanda GeoJSON Data – SimpleMaps](https://simplemaps.com/gis/country/rw)  
- 🧠 [GitHub Repository](https://github.com/uweraliliane/RwandaHiddenHungerRwanda)  
- 📽️ [Demo Video – Google Drive](https://drive.google.com/file/d/1u7Df-iwcgYH2t_qK8pennIRMtwxw5wVx/view?usp=drive_link)  

---

## 🧾 Declaration of Originality

I declare that this submission is my own original work, and all data sources, libraries, and references are fully acknowledged. Any assistance received has been appropriately disclosed.
