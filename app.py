import streamlit as st
import pandas as pd
import plotly.express as px
import json

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="🇷🇼 Ending Hidden Hunger in Rwanda",
    page_icon="🌾",
    layout="wide"
)

# -------------------------------
# SIDEBAR NAVIGATION
# -------------------------------
with st.sidebar:
    st.title("📌 Navigation")
    st.markdown("""
    - 🗺️ Geographic Insights  
    - 📈 Feature Importance  
    - 🧠 Predict Stunting  
    - 🧩 Root Causes & Policies  
    """)
    st.markdown("---")
    st.markdown("👨‍💻 Built for **NISR Big Data Hackathon 2025**")

# -------------------------------
# PAGE HEADER
# -------------------------------
st.title("🌾 Ending Hidden Hunger in Rwanda")
st.markdown("### 🎯 A Data Science Tool for Nutrition Policy & Action")

st.success("""
This dashboard visualizes **stunting risk**, **geographic disparities**, and **root causes** 
to inform evidence-based interventions in Rwanda. Powered by machine learning and national survey data.
""")

# -------------------------------
# LOAD DATA
# -------------------------------
@st.cache_data
def load_data():
    data_path = "Data/"  # Relative path

    district_df = pd.read_csv(data_path + "district_geospatial_summary.csv")
    xgb_imp = pd.read_csv(data_path + "xgb_feature_importances.csv")
    lgbm_imp = pd.read_csv(data_path + "LightGBM_feature_importance.csv")
    logreg_imp = pd.read_csv(data_path + "logreg_feature_importance.csv")
    catboost_imp = pd.read_csv(data_path + "cat_feature_importances.csv")
    model_perf = pd.read_csv(data_path + "model_comparison_results.csv")

    #st.write("📋 Model Performance Columns:", model_perf.columns.tolist())

    with open(data_path + "rwanda_districts.geojson", "r", encoding="utf-8") as f:
        geo_district = json.load(f)
    with open(data_path + "rwanda_province.json", "r", encoding="utf-8") as f:
        geo_province = json.load(f)

    return district_df, xgb_imp, lgbm_imp, logreg_imp, catboost_imp, model_perf, geo_district, geo_province

district_df, xgb_imp, lgbm_imp, logreg_imp, catboost_imp, model_perf, geo_district, geo_province = load_data()

# -------------------------------
# RISK RANKING TABLES
# -------------------------------
sorted_df = district_df.sort_values(by="Stunting Rate (%)", ascending=False)
high_risk = sorted_df.head(5)[["District", "Stunting Rate (%)", "Household wealth index", "Minimum Dietary Diversity - Women"]].reset_index(drop=True)
low_risk = sorted_df.tail(5)[["District", "Stunting Rate (%)", "Household wealth index", "Minimum Dietary Diversity - Women"]].reset_index(drop=True)

# -------------------------------
# TABS
# -------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🗺️ Geographic Insights",
    "📈 Feature Importance",
    "🧠 Predict Stunting Risk",
    "🧩 Root Causes & Policies"
])

# ============================================================
# TAB 1: GEOGRAPHIC INSIGHTS
# ============================================================

with tab1:
    st.subheader("📍 Geographic Distribution of Malnutrition")
    st.markdown("Analyze key malnutrition indicators (stunting, wasting, underweight) across Rwanda by **district** or **province** level.")

    # ------------------------------
    # Filters
    # ------------------------------
    col1, col2, col3 = st.columns(3)
    with col1:
        region_level = st.selectbox("🗺️ Region Level", ["District", "Province"])
    with col2:
        mal_type = st.selectbox("📊 Malnutrition Indicator", [
            "Stunting Rate (%)", "Wasting Rate (%)", "Underweight Rate (%)"
        ])
    with col3:
        color_scale = st.selectbox("🎨 Color Scale", ["YlOrRd", "Viridis", "Reds", "Blues", "YlGnBu"])

    # ------------------------------
    # Data Aggregation
    # ------------------------------
    if region_level == "District":
        df = district_df.copy()
        geo = geo_district
        location_col = "District"
        featureidkey = "properties.District"
    else:
        df = district_df.groupby("Province", as_index=False).mean(numeric_only=True)
        geo = geo_province
        location_col = "Province"
        featureidkey = "properties.name"

    # Handle missing or non-numeric values
    df[mal_type] = pd.to_numeric(df[mal_type], errors="coerce").fillna(0)

    # ------------------------------
    # Choropleth Map
    # ------------------------------
    try:
        fig_map = px.choropleth(
            df,
            geojson=geo,
            locations=location_col,
            featureidkey=featureidkey,
            color=mal_type,
            hover_name=location_col,
            hover_data={
                "Household wealth index": True,
                "Household food security": True,
                "Minimum Dietary Diversity - Women": True
            },
            color_continuous_scale=color_scale,
            title=f"{mal_type} by {region_level}"
        )
        fig_map.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig_map, use_container_width=True)
    except Exception as e:
        st.error("⚠️ Map rendering failed. Showing raw data below.")
        st.dataframe(df.head())

    # ------------------------------
    # Ranked Table (District Only)
    # ------------------------------
    if region_level == "District":
        st.markdown("### 🏅 District Ranking by Stunting Rate")
        ranked_districts = district_df[["District", "Stunting Rate (%)"]].sort_values(
            by="Stunting Rate (%)", ascending=False
        ).reset_index(drop=True)

        with st.expander("📋 View Ranked Districts"):
            for i, row in ranked_districts.iterrows():
                st.write(f"{i+1}. **{row['District']}** — {row['Stunting Rate (%)']:.1f}%")

    # ------------------------------
    # Summary Statistics
    # ------------------------------
    st.markdown("### 📊 Summary Statistics")
    st.dataframe(df[[location_col, mal_type]].describe().T)

# ============================================================
# TAB 2: FEATURE IMPORTANCE + MODEL PERFORMANCE
# ============================================================
with tab2:
    st.subheader("📈 Key Predictors of Stunting (ML Models)")
    st.markdown("These charts show the most important predictors of stunting from different models:")

    model_choice = st.selectbox(
        "Select Model", ["XGBoost", "LightGBM", "Logistic Regression", "CatBoost"]
    )

    if model_choice == "XGBoost":
        df_imp = xgb_imp.rename(columns={"Importance": "Score"})
        color = "Purples"
    elif model_choice == "LightGBM":
        df_imp = lgbm_imp.rename(columns={"Importance": "Score"})
        color = "Greens"
    elif model_choice == "CatBoost":
        df_imp = catboost_imp.rename(columns={"Importance": "Score"})
        color = "Oranges"
    else:
        df_imp = logreg_imp.rename(columns={"Abs_Coefficient": "Score"})
        color = "Blues"

    df_imp = df_imp.sort_values("Score", ascending=True).tail(10)

    fig_imp = px.bar(
        df_imp,
        x="Score", y="Feature",
        orientation="h",
        color="Score",
        color_continuous_scale=color,
        title=f"Top 10 Features - {model_choice}"
    )
    fig_imp.update_layout(
        yaxis_title=None,
        xaxis_title="Importance / Coefficient",
        height=500
    )
    st.plotly_chart(fig_imp, use_container_width=True)

    st.markdown("### 📊 Model Performance Comparison")

        # Optional: Rename columns for consistency (or keep original names)
    model_perf.rename(columns={
        "AUC Score": "AUC-ROC",
        "F1-Score": "F1-score"  # For consistent formatting
    }, inplace=True)

    # Format numeric columns
    numeric_cols = ['Accuracy', 'Precision', 'Recall', 'F1-score', 'AUC-ROC']
    for col in numeric_cols:
        model_perf[col] = pd.to_numeric(model_perf[col], errors='coerce')

    # Display nicely formatted table
    st.markdown("### 📊 Model Performance Comparison")
    st.dataframe(
        model_perf.style.format({
            "Accuracy": "{:.3f}",
            "Precision": "{:.3f}",
            "Recall": "{:.3f}",
            "F1-score": "{:.3f}",
            "AUC-ROC": "{:.3f}"
        }),
        use_container_width=True
    )

# ============================================================
# TAB 3: STUNTING RISK SIMULATOR
# ============================================================
# ============================================================
# TAB 3: STUNTING RISK SIMULATOR (UPDATED)
# ============================================================
with tab3:
    st.subheader("🧠 Predict Stunting Risk (Simulation)")
    st.markdown("Estimate stunting risk based on key household and child characteristics.")

    with st.expander("ℹ️ How this works"):
        st.info("""
        This is a simplified scoring model based on health research and machine learning results.  
        It helps illustrate how different risk factors contribute to stunting in children.  
        **Note:** This is not a clinical tool, but a data-informed simulation.
        """)

    with st.form("predict_form"):
        st.markdown("#### 👶 Child & Household Characteristics")

        col1, col2 = st.columns(2)
        with col1:
            muac = st.number_input("Child MUAC (mm)", 80, 200, 125)
            child_age = st.number_input("Child Age (months)", 0, 59, 24)
            fortified_porridge = st.selectbox("Drank fortified porridge?", ["Yes", "No"])
            vitamin_a = st.selectbox("Received Vitamin A (last 6 months)?", ["Yes", "No"])
            water_source = st.selectbox("Main water source", ["Piped", "Protected", "Unprotected", "Far"])
        with col2:
            mouth_illness = st.selectbox("Recent mouth illness?", ["No", "Yes"])
            solid_food_freq = st.slider("Solid food meals per day", 0, 5, 2)
            handwash_before_meal = st.selectbox("Handwashing before meals?", ["Yes", "No"])
            wealth_index = st.slider("Household Wealth Index", 1.0, 5.0, 3.0)
            disability = st.selectbox("Any disability in household?", ["No", "Yes"])

        submitted = st.form_submit_button("🔍 Predict Risk")

    if submitted:
        # ---------------------------
        # Risk scoring logic
        # ---------------------------
        risk = 0.1  # base risk

        if muac < 125: risk += 0.25
        if fortified_porridge == "No": risk += 0.15
        if vitamin_a == "No": risk += 0.10
        if water_source in ["Unprotected", "Far"]: risk += 0.10
        if mouth_illness == "Yes": risk += 0.10
        if solid_food_freq < 2: risk += 0.10
        if handwash_before_meal == "No": risk += 0.05
        if wealth_index <= 2: risk += 0.15
        if disability == "Yes": risk += 0.05
        if child_age < 12: risk += 0.05  # higher risk in infants

        risk_percentage = min(risk * 100, 100)

        # ---------------------------
        # Display results
        # ---------------------------
        st.markdown("### 🧮 Prediction Result")
        st.metric("Estimated Stunting Risk", f"{risk_percentage:.1f} %")

        if risk_percentage > 50:
            st.warning("🔴 High Risk of Stunting — Consider urgent interventions.")
        elif risk_percentage > 30:
            st.info("🟠 Moderate Risk — Recommend monitoring and support.")
        else:
            st.success("🟢 Low Risk of Stunting")

        with st.expander("📌 Interpretation"):
            st.markdown("""
            - **MUAC < 125 mm:** Indicates possible malnutrition  
            - **Lack of fortified porridge or Vitamin A:** Nutrition gaps  
            - **Unsafe water & hygiene:** Increased infection risk  
            - **Low wealth index / disability:** Social vulnerability  
            - **Young age (<12 months):** Early stunting risk  
            """)
        st.markdown("### 🧭 Risk Categories")
        st.markdown("""
        - 🔴 **High Risk**: > 50% — Urgent attention  
        - 🟠 **Moderate Risk**: 31–50% — Monitor and support  
        - 🟢 **Low Risk**: ≤ 30% — Normal growth expected
        """)

# ============================================================
# TAB 4: ROOT CAUSES & POLICIES
# ============================================================
# ============================================================
# TAB 4: ROOT CAUSES & POLICY ACTIONS (REFINED)
# ============================================================
with tab4:
    st.subheader("🧩 Root Causes & Policy Actions")
    st.markdown("Based on data analysis, machine learning models, and public health research, these are the key drivers of stunting in Rwanda and recommended actions:")

    st.markdown("### 📌 Root Causes of Stunting (Data-Informed)")
    st.markdown("""
    - 🍼 **Low dietary diversity** and poor complementary feeding practices  
    - 🚱 **Unsafe water sources** and inadequate hand hygiene  
    - 💰 **Poverty** and low household wealth index  
    - 👩‍🏫 **Low maternal education** and limited nutrition knowledge  
    - 🏥 **Gaps in antenatal/postnatal care** and vitamin A supplementation  
    - 👨‍👩‍👧 **Large household size** and poor resource allocation  
    - ♿ **Disability within households** limiting food security or care capacity  
    """)

    st.markdown("### 🛠️ Policy Recommendations")

    st.info("🔹 Short-Term Actions (0–1 year):")
    st.markdown("""
    - Deploy **community IYCF counseling** and home visits for at-risk households  
    - Distribute **fortified porridge and micronutrient powders** to vulnerable children  
    - Increase **access to clean water** and promote **safe handwashing behaviors**  
    - Ensure **Vitamin A** and **deworming coverage** in child health campaigns  
    """)

    st.success("🟢 Medium-Term Strategies (1–3 years):")
    st.markdown("""
    - Support **biofortified crops** and **kitchen garden programs**  
    - Integrate **nutrition into social protection** and cash transfer schemes  
    - Improve **antenatal care (ANC)** access with embedded nutrition counseling  
    - Provide **parent-focused nutrition education** in community centers and ECDs  
    """)

    st.warning("🟠 Long-Term Vision (3+ years):")
    st.markdown("""
    - Institutionalize **nutrition in schools and early childhood development (ECD)**  
    - Develop **real-time monitoring systems** for malnutrition hotspots  
    - Invest in **equity-first policies** for remote, poor, or underserved districts  
    - Scale up **nutrition-sensitive agriculture** and women’s empowerment programs  
    """)

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.caption("Built using Streamlit | Hackathon 2025 | Data Sources: CFSVA, DHS, National Surveys")
