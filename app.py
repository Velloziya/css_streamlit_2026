import streamlit as st
import pandas as pd

# PAGE CONFIG
st.set_page_config(
    page_title="Researcher Profile and STEM Data Explorer",
    layout="wide"
)

# FUNCTION FOR STYLED HEADINGS
def styled_header(text):
    st.markdown(
        f"<h2 style='background-color:#ADD8E6; color:black; padding:10px; border-radius:10px;'>{text}</h2>",
        unsafe_allow_html=True
    )

# SIDEBAR MENU
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Go to:",
    ["Academic Profile",
     "Air Quality & Environmental Data Explorer",
     "Contact Details"]
)

# DATASETS 

meteorological_data = pd.DataFrame({
    "Temperature (C)": [18,23,18,24,25,19.45,22.6,23.8,25,25.6,25,25,26.7,23,23,24.5,27,27.8,25,23],
    "Rainfall (mm)": [4.2, 1.5, 2.9, 3.4, 7.1,0.5,1.09,2.4,2.6,3.4,3.6,3.4,5.6,7.9,7.9,6.7,5,6,4,2.4],
    "Relative Humidity (%)":[84.13,80.44,78.73,72.34,71.22,56.78,69.56,57.8,78.9,34.56,67.8,32.4,56.7,78.9,54.3,32.1,34.5,67.8,65.4,56.8],
    "Date": pd.date_range(start="2025-10-01", periods=20),
})

pollution_data = pd.DataFrame({
    "NO2 (ppb)": [13.29,1.3,0.09,12.52,5.64,3.34,7.86,2.34,6.78,9.87,6.54,8.59,3.54,6.87,9.87,3.54,5.34,4.56,6.76,5.7],
    "SO2 (ppb)": [11.21,13,23.4,15.3,16.5,21.2,16,23.2,24.5,22,24,23,24,25,26,23.4,26.7,25.6,23,24],
    "PM2.5 (µg/m3)":[18.89,6.7,4.3,12.34,12.12,13.4,21.1,2.34,4.56,4.56,4.56,3.23,4.54,7.78,7.67,8.95,5.64,6.78,5.4,6.78],
    "PM10 (µg/m3)":[12.34,12.12,13.4,21.1,2.34,4.56,4.56,4.56,3.23,4.54,8,8,8,8,5,4,3,6.78,5.4,6.78],
    "Observation Date": pd.date_range(start="2025-10-01", periods=20),
})

aerobiology_data = pd.DataFrame({
    "Weekday": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "Grass pollen (Poacea)": [625,410,565,315,230,320,324],
    "Tree pollen": [165,270,155,280,350,412,214],
    "Weed pollen":[123, 453, 234, 212, 345, 567,432],
    "Recorded Date": pd.date_range(start="2025-10-01", periods=7),
})

# MENU SECTIONS

if menu == "Academic Profile":

    styled_header("Academic Profile")

    name = "Yolanda C. Makgale"
    field = "Aerobiology | Environmental Sciences | GIS | Remote Sensing"
    institution = "Walter Sisulu University | University of Fort Hare | North-West University"

    st.write(f"**Name:** {name}")
    st.write(f"**Fields of Specialisation:** {field}")
    st.write(f"**Institutions:** {institution}")

    styled_header("Upload a Pollen Image (Only One Allowed)")

    uploaded_file = st.file_uploader(
        "Choose a pollen image",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False
    )

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Pollen Image", use_column_width=True)
    else:
        st.info("Please upload one pollen image to display here.")

    st.image(
        "https://www.mdpi.com/applsci/applsci-12-07126/article_deploy/html/images/applsci-12-07126-g003-550.jpg",
        caption="Different types of pollen grains (Chen and Ju, 2022)"
    )


elif menu == "Air Quality & Environmental Data Explorer":

    styled_header("Air Quality & Environmental Dataset Visualiser")

    st.sidebar.header("Select Dataset")

    data_option = st.sidebar.selectbox(
        "Select a dataset to explore",
        ["Meteorological Data", "Pollution Data", "Aerobiology Data"]
    )

    if data_option == "Meteorological Data":

        styled_header("Meteorological Data")

        temp_filter = st.slider(
            "Filter by Temperature (°C)",
            float(meteorological_data["Temperature (C)"].min()),
            float(meteorological_data["Temperature (C)"].max()),
            (20.0, 26.0)
        )

        filtered = meteorological_data[
            meteorological_data["Temperature (C)"].between(temp_filter[0], temp_filter[1])
        ]

        st.dataframe(filtered)


    elif data_option == "Pollution Data":

        styled_header("Pollution Data")

        pm_filter = st.slider(
            "Filter by PM2.5 (µg/m3)",
            float(pollution_data["PM2.5 (µg/m3)"].min()),
            float(pollution_data["PM2.5 (µg/m3)"].max()),
            (5.0, 15.0)
        )

        filtered = pollution_data[
            pollution_data["PM2.5 (µg/m3)"].between(pm_filter[0], pm_filter[1])
        ]

        st.dataframe(filtered)


    elif data_option == "Aerobiology Data":

        styled_header("Aerobiology Data")

        weekday_selection = st.multiselect(
            "Select weekdays to display",
            aerobiology_data["Weekday"].unique(),
            default=aerobiology_data["Weekday"].unique()
        )

        filtered = aerobiology_data[
            aerobiology_data["Weekday"].isin(weekday_selection)
        ]

        st.dataframe(filtered)


elif menu == "Contact Details":

    styled_header("Contact Details")

    st.write("📧 Email: makgalec@gmail.com")
    st.write("📞 Cellphone: +27 83 913 3030")
    st.write("🔗 LinkedIn: https://www.linkedin.com/in/makgalec")
