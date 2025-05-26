import streamlit as st
import pandas as pd
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from main import scrape
st.title("Location Data Finder")
location = st.text_input("Enter a location")
find_data_clicked = st.button("Find Data")
if find_data_clicked:
    if location:
        st.info("Scraping... Please wait.")
        csv_path = scrape(location)
        if csv_path and os.path.exists(csv_path):
            data = pd.read_csv(csv_path)
            st.success("Data scraped successfully!")
            st.dataframe(data)
        else:
            st.error("No data was collected.")
    else:
        st.warning("Please enter a location.")