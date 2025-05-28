from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

def initialize_driver():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    return driver, wait

def scroll_and_collect_places(driver, wait, search_query):
    driver.get(f"https://www.google.com/maps/search/{search_query}")
    time.sleep(10)
    for _ in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(2)
    places = driver.find_elements(By.CSS_SELECTOR, ".hfpxzc")
    return places

def extract_place_data(driver, wait, places):
    data = []
    for place in places[:20]:
        try:
            driver.execute_script("arguments[0].scrollIntoView();", place)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".hfpxzc")))
            place.click()
            time.sleep(5)
            try:
                name_element = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "h1.DUwDvf, h1.fontHeadlineLarge")))
                name = name_element.text.strip()
            except:
                name = "Not Found"
            try:
                phone_element = driver.find_element(By.CSS_SELECTOR, 'button[data-tooltip*="phone"]')
                phone = phone_element.get_attribute('aria-label').replace('Copy phone number: ', '').replace('Phone: ', '')
            except:
                phone = "Not Found"
            try:
                location_element = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-item-id="address"], div[data-item-id="address"], div.rogA2c'))
                )
                location = location_element.text.strip().replace('\n', ' ')
            except:
                try:
                    location_element = driver.find_element(By.CSS_SELECTOR, 'div.rogA2c')
                    location = location_element.text.strip().replace('\n', ' ')
                except:
                    location = "Not Found"
            data.append({
                "Name": name,
                "Phone": phone,
                "Location": location
            })
            driver.find_element(By.CSS_SELECTOR, 'button[jsaction*="back"]').click()
            time.sleep(3)
        except:
            continue
    return data
def scrape(search_query):
    driver, wait = initialize_driver()
    try:
        places = scroll_and_collect_places(driver, wait, search_query)
        data = extract_place_data(driver, wait, places)
    finally:
        driver.quit()
    if data:
        df = pd.DataFrame(data)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        save_path = os.path.join(base_dir, "places.csv")
        df.to_csv(save_path, index=False)
        return save_path
    else:
        return None
