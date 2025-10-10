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
- **Other:** DHS, WASH indicators (if applicable)  

---

## 📈 Key Findings

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

## 📂 Directory Structure
 <pre> RwandaHiddenHungerRwanda/
│
├── app.py # Streamlit entrypoint
├── 🇷🇼 Tackling Hidden Hunger.docx # Final write-up
├── To whom Uwera Liliane final.pdf 
├── LICENSE
├── README.md 
│
├── Data/
│ ├── Microdata.zip
│ ├── gadm41_RWA_shp.zip
│ ├── rwanda_districts.geojson
│ ├── feature_importance CSVs
│ └── model_comparison_results.csv
│
├── Models/
│ └── Trained ML models (.pkl)
│
├── demo/
│ └── demo.webm # Video demo
</pre>

---

## ▶️ Running the App

Ensure **Python 3.9+** is installed and required packages are available.

### Step 1: Install dependencies

```bash
pip install -r requirements.txt


