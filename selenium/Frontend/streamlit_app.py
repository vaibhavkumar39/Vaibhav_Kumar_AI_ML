import streamlit as st
import pandas as pd
import requests
import os
st.title("Location Data Finder")
location = st.text_input("Enter a location")
find_data_clicked = st.button("Find Data")
if find_data_clicked:
    if location:
        st.info("Sending request to Flask API...")
        response = requests.post("http://127.0.0.1:5000/scrape", json={"location": location})
        if response.status_code == 200:
            result = response.json()
            if result.get("status") == "success":
                csv_path = result.get("csv_path")
                if os.path.exists(csv_path):
                    data = pd.read_csv(csv_path)
                    st.success("Data scraped successfully!")
                    st.dataframe(data)
                else:
                    st.error("CSV path not found.")
            else:
                st.warning(result.get("message", "No data returned"))
        else:
            st.error("API error occurred.")
    else:
        st.warning("Please enter a location.")