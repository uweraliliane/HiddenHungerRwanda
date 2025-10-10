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

An interactive **Streamlit dashboard** includes:

- 🗺️ **Geospatial Choropleths** – District-level stunting & wasting rates  
- 📊 **Feature Importance Viewers** – Compare risk factors across models  
- 🧮 **Stunting Risk Simulator** – Predict household risk interactively  
- 📝 **Policy Brief Generator** – Auto-generate PDF recommendations  
- 📦 **Data Download** – Export processed summaries  

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

🛠️ Dependencies
📦 Required Libraries
bash
Install all dependencies using:
pip install -r requirements.txt

or install manually:
bash
pip install streamlit pandas numpy scikit-learn xgboost lightgbm catboost matplotlib seaborn plotly folium imbalanced-learn statsmodels joblib geopandas

📄 Sample requirements.txt
text

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

🚀 How to Run
Option 1: Local Machine
bash
streamlit run app.py
Option 2: GitHub + Streamlit Cloud

Push your project to GitHub

Deploy via Streamlit Cloud

Set app.py as the main entry point

🔒 License

This project is licensed under the terms of the MIT License.
See the LICENSE
 file for details.

📢 Hackathon Fit & Innovation

✅ Directly addresses Track 2: Ending Hidden Hunger
✅ Leverages national data (CFSVA 2024)
✅ Blends machine learning + geospatial + public health
✅ Offers actionable policy suggestions
✅ Provides an interactive & scalable tool

🔮 Future Roadmap

📲 Real-time data integration (mobile surveys, HMIS)

🧑‍🌾 Agriculture-nutrition modeling (e.g., kitchen gardens)

🌐 Full cloud deployment for ministries & NGOs

🤝 Government + NGO pilot collaboration

🙌 Acknowledgments

National Institute of Statistics of Rwanda (NISR)

Organizers of the NISR Big Data Hackathon 2025

CFSVA survey teams and all data contributors

🔗 GitHub Repository

github.com/uweraliliane/RwandaHiddenHungerRwanda

yaml

---

### ✅ What This Final Version Fixes:

- ✅ Proper Markdown formatting with headers, bullet points, and tables
- ✅ All code, shell commands, and configs inside triple backticks (for syntax highlighting)
- ✅ All URLs are clickable
- ✅ Everything will **render perfectly** on GitHub

---

Let me know if you’d also like a downloadable version (`README.md`) or if you need help deploying it to **Streamlit Cloud**.

