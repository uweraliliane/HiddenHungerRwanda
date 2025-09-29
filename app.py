import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

# --- Page Setup ---
st.set_page_config(page_title="🇷🇼 Rwanda Malnutrition Dashboard", layout="wide")
st.title("Rwanda Malnutrition Dashboard")
st.markdown("""
    A data-driven look at malnutrition indicators and risk factors in Rwanda.
    interact with the map to explore stunting, wasting, and underweight rates in different provinces and districts.
""")

# --- File Paths ---
DISTRICT_DATA_PATH = "district_malnutrition_rates.csv"
PROVINCE_DATA_PATH = "province_malnutrition_rates.csv"
DISTRICT_GEOJSON_PATH = "rwanda_districts.geojson"
PROVINCE_GEOJSON_PATH = "rwanda_province.json"

# --- Error Checks ---
missing_files = []
for path in [DISTRICT_DATA_PATH, PROVINCE_DATA_PATH, DISTRICT_GEOJSON_PATH, PROVINCE_GEOJSON_PATH]:
    if not os.path.exists(path):
        missing_files.append(path)

if missing_files:
    st.error(f"❌ Missing required files:\n{', '.join(missing_files)}")
    st.stop()

# --- Load Data ---
@st.cache_data
def load_csv(path):
    return pd.read_csv(path)

@st.cache_data
def load_geojson(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

df_district = load_csv(DISTRICT_DATA_PATH)
df_province = load_csv(PROVINCE_DATA_PATH)
geo_district = load_geojson(DISTRICT_GEOJSON_PATH)
geo_province = load_geojson(PROVINCE_GEOJSON_PATH)

# --- Sidebar: Region and Malnutrition Type Selection ---
with st.sidebar.expander("🌍 Region Selection", expanded=True):
    region_level = st.selectbox("🗺️ Select Level", ["District", "Province"])
    mal_type = st.radio(
        "📊 Select Malnutrition Type",
        ["Stunting Rate (%)", "Underweight Rate (%)", "Wasting Rate (%)"]
    )

# --- Map Visualization ---
if region_level == "District":
    st.subheader(f"{mal_type} by District")

    # Ensure malnutrition data is numeric and fill missing with 0
    df_district[mal_type] = pd.to_numeric(df_district[mal_type], errors='coerce').fillna(0)

    # Map visualization for District
    featureid_key = "properties.District"  # Adjust based on your GeoJSON

    fig = px.choropleth(
        df_district,
        geojson=geo_district,
        locations="District",
        color=mal_type,
        featureidkey=featureid_key,
        color_continuous_scale="Reds",
        title=f"{mal_type} by District",
        labels={mal_type: mal_type}
    )

elif region_level == "Province":
    st.subheader(f"{mal_type} by Province")

    # Ensure malnutrition data is numeric and fill missing with 0
    df_province[mal_type] = pd.to_numeric(df_province[mal_type], errors='coerce').fillna(0)

    # Check that the province names match between the CSV and GeoJSON
    featureid_key = "properties.name"  # Adjust this based on your GeoJSON field for province name

    # Map visualization for Province
    fig = px.choropleth(
        df_province,
        geojson=geo_province,
        locations="Province",
        color=mal_type,
        featureidkey=featureid_key,
        color_continuous_scale="Blues",
        title=f"{mal_type} by Province",
        labels={mal_type: mal_type}
    )

# Update geo settings and display map
fig.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig, use_container_width=True)

# --- Additional Data Table ---
st.sidebar.subheader("Malnutrition Data")
if region_level == "District":
    st.sidebar.dataframe(df_district)
else:
    st.sidebar.dataframe(df_province)

