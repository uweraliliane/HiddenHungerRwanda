# 🇷🇼 Ending Hidden Hunger in Rwanda

**Track 2 — Big Data Hackathon 2025**  
**Team:** [Your Name or Team Name]  
**Theme:** Predictive Analytics for Child Malnutrition  
**Focus Area:** Childhood Stunting using 2024 CFSVA Data

---

## 🌍 Project Overview

Despite progress in recent years, over **33% of Rwandan children under 5** remain stunted. This project uses national survey data and machine learning to:

- Identify **malnutrition hotspots**
- Model **key predictive factors**
- Simulate **stunting risk** based on household inputs
- Recommend **data-driven interventions**
- Provide a user-friendly **dashboard** for policy support

---

## 🎯 Objectives

- 🗺️ Map stunting, wasting, and underweight rates across districts and provinces
- 🤖 Train models (XGBoost, LightGBM, Logistic Regression) to identify key predictors
- 🧠 Simulate child stunting risk using household data
- 📍 Pinpoint root causes of malnutrition
- 📊 Provide a dashboard for policy planning and simulation

---

## 🧠 Key Findings

- **High-Stunting Districts:** Nyabihu, Rubavu, Rutsiro, Burera, Gakenke
- **Top Risk Factors:**
  - Child MUAC (Mid-Upper Arm Circumference)
  - Vitamin A intake
  - Household Wealth Index
  - Dietary Diversity (Women)
  - WASH variables (water source, handwashing practices)
  - Recent illnesses (diarrhea, fever)

---

## 🔍 Root Cause Summary

| Feature               | Root Cause               | Suggested Intervention           |
|----------------------|--------------------------|----------------------------------|
| Low MUAC             | Undernutrition           | Growth monitoring, feeding aid   |
| No Vitamin A         | Micronutrient deficiency | Supplementation campaigns        |
| Low Wealth Index     | Poverty                  | Cash transfers, job programs     |
| Unsafe Water Source  | Infrastructure gaps      | Safe water access, WASH support  |
| Rare Handwashing     | Behavior & education     | Hygiene campaigns                |
| Low Dietary Diversity| Food insecurity          | Home gardens, nutrition farming  |

---

## 💻 Dashboard Features

Interactive Streamlit app with the following tabs:

1. **🗺️ Geographic Insights** — Choropleth maps of malnutrition indicators  
2. **📈 Feature Importance** — Visualize top predictive features per model  
3. **🧠 Predict Risk** — Estimate child stunting risk via user inputs  
4. **🧩 Root Causes & Policies** — Feature-level RCA with intervention mapping

---

## 📂 Repository Structure

