import streamlit as st
import pandas as pd
import plotly.express as px
import json

# -------------------------------
# PAGE CONFIGURATION
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
# HEADER
# -------------------------------
st.title("🌾 Tacke Hidden Hunger in Rwanda")
st.markdown("### 🎯 A Data Science Tool for Nutrition Policy & Action")
st.success("""
This dashboard visualizes **stunting risk**, **geographic disparities**, and **root causes** 
to inform evidence-based interventions in Rwanda. Powered by machine learning and national survey data.
""")

# -------------------------------
# LOAD DATA FUNCTION
# -------------------------------
@st.cache_data
def load_data():
    data_path = "Data/"  # Relative path
    district_df = pd.read_csv(data_path + "district_geospatial_summary.csv")
    xgb_imp = pd.read_csv(data_path + "xgb_feature_importances.csv")
    lgbm_imp = pd.read_csv(data_path + "lgbm_smote_classweight_feature_importance.csv")
    logreg_imp = pd.read_csv(data_path + "logreg_feature_importance.csv")
    catboost_imp = pd.read_csv(data_path + "cat_feature_importances.csv")
    model_perf = pd.read_csv(data_path + "model_comparison_results.csv")

    with open(data_path + "rwanda_districts.geojson", "r", encoding="utf-8") as f:
        geo_district = json.load(f)
    with open(data_path + "rwanda_province.json", "r", encoding="utf-8") as f:
        geo_province = json.load(f)

    return district_df, xgb_imp, lgbm_imp, logreg_imp, catboost_imp, model_perf, geo_district, geo_province

# Load all data
district_df, xgb_imp, lgbm_imp, logreg_imp, catboost_imp, model_perf, geo_district, geo_province = load_data()

# -------------------------------
# TABS SETUP
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
    st.markdown("Analyze **stunting**, **wasting**, and **underweight** rates across Rwanda.")

    col1, col2, col3 = st.columns(3)
    with col1:
        region_level = st.selectbox("🗺️ Region Level", ["District", "Province"])
    with col2:
        mal_type = st.selectbox("📊 Malnutrition Indicator", [
            "Stunting Rate (%)", "Wasting Rate (%)", "Underweight Rate (%)"
        ])
    with col3:
        color_scale = st.selectbox("🎨 Color Scale", ["YlOrRd", "Viridis", "Reds", "Blues", "YlGnBu"])

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

    df[mal_type] = pd.to_numeric(df[mal_type], errors="coerce").fillna(0)

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
        st.error("⚠️ Map failed to render. Check data format or GeoJSON.")

    if region_level == "District":
        st.markdown("### 🏅 Top & Bottom Districts by Stunting Rate")
        high_risk = district_df.sort_values(by="Stunting Rate (%)", ascending=False).head(5)
        low_risk = district_df.sort_values(by="Stunting Rate (%)", ascending=True).head(5)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🔴 High Risk Districts")
            st.dataframe(high_risk[["District", "Stunting Rate (%)"]])
        with col2:
            st.markdown("#### 🟢 Low Risk Districts")
            st.dataframe(low_risk[["District", "Stunting Rate (%)"]])

    st.markdown("### 📊 Summary Statistics")
    st.dataframe(df[[location_col, mal_type]].describe().T)

# ============================================================
# TAB 2: FEATURE IMPORTANCE
# ============================================================
with tab2:
    st.subheader("📈 Key Predictors of Stunting (ML Models)")

    model_choice = st.selectbox("Select Model", [
        "XGBoost", "LightGBM", "Logistic Regression", "CatBoost"
    ])

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
        df_imp, x="Score", y="Feature",
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

    # Model Performance Table
    st.markdown("### 🧪 Model Performance Comparison")
    model_perf.rename(columns={"AUC Score": "AUC-ROC", "F1-Score": "F1-score"}, inplace=True)
    for col in ['Accuracy', 'Precision', 'Recall', 'F1-score', 'AUC-ROC']:
        model_perf[col] = pd.to_numeric(model_perf[col], errors='coerce')

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
# TAB 3: STUNTING RISK SIMULATION
# ============================================================
with tab3:
    st.subheader("🧠 Predict Stunting Risk (Simulation)")
    st.markdown("Estimate risk using key household and child features.")

    with st.expander("ℹ️ How this works"):
        st.info("""
        This tool simulates stunting risk based on real-world predictors.
        It uses simple scoring logic to highlight high-risk profiles — not clinical diagnostics.
        """)

    with st.form("risk_form"):
        st.markdown("#### 👶 Household & Child Profile")
        col1, col2 = st.columns(2)

        with col1:
            muac = st.number_input("Child MUAC (mm)", 80, 200, 125)
            child_age = st.number_input("Child Age (months)", 0, 59, 24)
            fortified_porridge = st.selectbox("Drank fortified porridge?", ["Yes", "No"])
            vitamin_a = st.selectbox("Received Vitamin A?", ["Yes", "No"])
            water_source = st.selectbox("Water source", ["Piped", "Protected", "Unprotected", "Far"])
            maternal_education = st.selectbox("Mother completed primary school?", ["Yes", "No"])

        with col2:
            mouth_illness = st.selectbox("Recent mouth illness?", ["No", "Yes"])
            solid_food = st.slider("Solid meals/day", 0, 5, 2)
            handwash = st.selectbox("Handwashing before meals?", ["Yes", "No"])
            wealth = st.slider("Wealth Index", 1.0, 5.0, 3.0)
            disability = st.selectbox("Disability in household?", ["No", "Yes"])
            household_size = st.slider("Household size (people)", 1, 20, 6)

        submitted = st.form_submit_button("🔍 Predict")

    if submitted:
        # Basic risk score
        risk = 0.1

        # Risk logic
        if muac < 125: risk += 0.25
        if fortified_porridge == "No": risk += 0.15
        if vitamin_a == "No": risk += 0.10
        if water_source in ["Unprotected", "Far"]: risk += 0.10
        if mouth_illness == "Yes": risk += 0.10
        if solid_food < 2: risk += 0.10
        if handwash == "No": risk += 0.05
        if wealth <= 2: risk += 0.15
        if disability == "Yes": risk += 0.05
        if child_age < 12: risk += 0.05
        if maternal_education == "No": risk += 0.10
        if household_size >= 8: risk += 0.05

        risk_percent = min(risk * 100, 100)

        st.metric("Estimated Stunting Risk", f"{risk_percent:.1f} %")

        # Interpretation
        if risk_percent > 50:
            st.warning("🔴 High Risk of Stunting — Consider urgent action.")
        elif risk_percent > 30:
            st.info("🟠 Moderate Risk — Needs support.")
        else:
            st.success("🟢 Low Risk — Normal growth expected.")

# ============================================================
# TAB 4: ROOT CAUSES & POLICY RECOMMENDATIONS
# ============================================================
with tab4:
    st.subheader("🧩 Root Causes & Policy Recommendations")

    st.markdown("### 🔍 Data-Informed Root Causes")
    st.markdown("""
    - 🍼 Low dietary diversity and poor feeding practices  
    - 🚱 Unsafe water and poor hygiene  
    - 💰 Household poverty and food insecurity  
    - 👩‍🏫 Low maternal education  
    - 🏥 Incomplete antenatal/postnatal care  
    - 👨‍👩‍👧 Large households / care strain  
    - ♿ Disability limiting caregiving capacity  
    """)

    st.info("### 🛠️ Short-Term Actions (0–1 Year)")
    st.markdown("""
    - Community-based IYCF counseling  
    - Distribute fortified porridge & micronutrients  
    - WASH interventions in critical zones  
    - Improve Vitamin A & deworming coverage  
    - Track & support high-risk children using risk prediction tool  
    """)

    st.success("### 📈 Medium-Term Strategies (1–3 Years)")
    st.markdown("""
    - Promote nutrition-sensitive agriculture  
    - Integrate nutrition in welfare schemes   
    - Strengthen antenatal & early childhood services  
    - Nutrition education via ECD and school systems  
    """)

    st.warning("### 🌱 Long-Term Vision (3+ Years)")
    st.markdown("""
    - Embed nutrition in schools & national development plans  
    - Deploy real-time malnutrition surveillance  
    - Prioritize rural and vulnerable communities  
    - Empower women in agri-nutrition value chains  
    """)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("Built using Streamlit | Hackathon 2025 | Data Sources: CFSVA 2024, DHS, National Nutrition Surveys")
