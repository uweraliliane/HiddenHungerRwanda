import streamlit as st
import folium
import geopandas as gpd
import pandas as pd
from folium.features import GeoJsonTooltip
from streamlit_folium import st_folium

# --- Load Data ---
# Load GeoJSON for provinces (use the correct path to your file)
province_geojson_path = r"D:\NISR\HiddenHungerRwanda\rwanda_province.json"
gdf_province = gpd.read_file(province_geojson_path)

# Load the malnutrition rates data for both province and district levels
malnutrition_province_data_path = "D:/NISR/HiddenHungerRwanda/province_malnutrition_rates.csv"
malnutrition_province_rates = pd.read_csv(malnutrition_province_data_path)

# Rename the 'Province' column to 'name' in malnutrition_province_rates
malnutrition_province_rates = malnutrition_province_rates.rename(columns={'Province': 'name'})

# Merge GeoDataFrame with malnutrition data for provinces
merged_province = gdf_province.merge(malnutrition_province_rates, on='name', how='left')

# Check the result
print(merged_province.head())

# --- Streamlit App Layout ---
st.title("Rwanda Malnutrition Dashboard")
st.markdown("""
    This dashboard visualizes malnutrition rates in Rwanda at both the province and district levels. 
    You can interact with the map to explore stunting, wasting, and underweight rates in different provinces and districts.
""")

# --- Add Filter Options ---
st.sidebar.header("Filter Options")
level = st.sidebar.radio("Choose map level", options=["Province", "District"])

selected_indicator = st.sidebar.selectbox(
    "Choose malnutrition indicator",
    options=['Stunting Rate (%)', 'Wasting Rate (%)', 'Underweight Rate (%)']
)

# --- Create Folium Map ---
m = folium.Map(location=[-1.95, 29.9], zoom_start=8, tiles='CartoDB positron')

# --- Province-level Choropleth ---
if level == "Province":
    # Add Choropleth Layer for Province level
    choropleth = folium.Choropleth(
        geo_data=merged_province,
        data=merged_province,
        columns=['name', selected_indicator],  # Changed 'Province' to 'name'
        key_on='feature.properties.name',  # This should match your GeoJSON property for the province name
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.3,
        nan_fill_color='lightgrey',
        legend_name=selected_indicator,
        highlight=True
    ).add_to(m)

    # Add Tooltip for Province-level Info
    tooltip = GeoJsonTooltip(
        fields=['name', 'Stunting Rate (%)', 'Wasting Rate (%)', 'Underweight Rate (%)'],  # Changed 'NAME_1' to 'name'
        aliases=['Province:', 'Stunting Rate (%):', 'Wasting Rate (%):', 'Underweight Rate (%):'],
        localize=True,
        sticky=True,
        labels=True,
        style="""background-color: #F0EFEF; border: 1px solid black; border-radius: 3px; box-shadow: 3px;""",
    )
    choropleth.geojson.add_child(tooltip)

# --- District-level Choropleth ---
else:
    # Load the district-level GeoJSON
    district_geojson_path = "D:/NISR/HiddenHungerRwanda/rwanda_districts.geojson"
    gdf_district = gpd.read_file(district_geojson_path)

    # Load the malnutrition district-level data
    district_malnutrition_data_path = "D:/NISR/HiddenHungerRwanda/district_malnutrition_rates.csv"
    district_malnutrition_rates = pd.read_csv(district_malnutrition_data_path)

    # Merge GeoDataFrame with district malnutrition data
    merged_district = gdf_district.merge(district_malnutrition_rates, on='District', how='left')

    # Convert CRS to match Folium map
    merged_district = merged_district.to_crs(epsg=4326)

    # Add Choropleth Layer for District level
    choropleth = folium.Choropleth(
        geo_data=merged_district,
        data=merged_district,
        columns=['District', selected_indicator],
        key_on='feature.properties.District',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.3,
        nan_fill_color='lightgrey',
        legend_name=selected_indicator,
        highlight=True
    ).add_to(m)

    # Add Tooltip for District-level Info
    tooltip = GeoJsonTooltip(
        fields=['District', 'Stunting Rate (%)', 'Wasting Rate (%)', 'Underweight Rate (%)'],
        aliases=['District:', 'Stunting Rate (%):', 'Wasting Rate (%):', 'Underweight Rate (%):'],
        localize=True,
        sticky=True,
        labels=True,
        style="""background-color: #F0EFEF; border: 1px solid black; border-radius: 3px; box-shadow: 3px;""",
    )
    choropleth.geojson.add_child(tooltip)

# --- Display Map ---
st_folium(m, width=700, height=500)

# --- Data Table ---
st.sidebar.subheader("Malnutrition Data")
if level == "Province":
    st.sidebar.dataframe(malnutrition_province_rates)
else:
    st.sidebar.dataframe(district_malnutrition_rates)

# --- Additional Analysis ---
st.header("Analysis and Insights")
st.markdown("""
    You can also analyze the overall rates of stunting, wasting, and underweight across the provinces and districts.
    Use the filters in the sidebar to toggle between different malnutrition indicators and levels.
""")

# Optional: Summary statistics or other insights (you can enhance as per your need)
if level == "Province":
    st.write("Total Provinces:", len(malnutrition_province_rates))
    st.write(f"Average Stunting Rate: {malnutrition_province_rates['Stunting Rate (%)'].mean():.2f}%")
    st.write(f"Average Wasting Rate: {malnutrition_province_rates['Wasting Rate (%)'].mean():.2f}%")
    st.write(f"Average Underweight Rate: {malnutrition_province_rates['Underweight Rate (%)'].mean():.2f}%")
else:
    st.write("Total Districts:", len(district_malnutrition_rates))
    st.write(f"Average Stunting Rate: {district_malnutrition_rates['Stunting Rate (%)'].mean():.2f}%")
    st.write(f"Average Wasting Rate: {district_malnutrition_rates['Wasting Rate (%)'].mean():.2f}%")
    st.write(f"Average Underweight Rate: {district_malnutrition_rates['Underweight Rate (%)'].mean():.2f}%")
