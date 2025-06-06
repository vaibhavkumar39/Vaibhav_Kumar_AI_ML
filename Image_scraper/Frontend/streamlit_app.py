import streamlit as st
import requests

st.title('Image Scraper Tool')

query = st.text_input("Enter image name you want to scrape:")

if st.button("Scrape and Save"):
    if query:
        try:
            response = requests.get("http://127.0.0.1:5000/scrape", params={"query": query})
            if response.status_code == 200:
                st.success(response.text)
            else:
                st.error(f"Failed: {response.text}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a search query.")