from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd
import time

query = input("Enter keyword: ")
url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get(url)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

results = []


for i, result in enumerate(soup.select("a.zReHs")[:10], start=1):
    try:
        title_tag = result.select_one("h3.LC20lb")
        link = result["href"]
        if title_tag and link:
            title = title_tag.get_text()
            domain = urlparse(link).netloc.replace("www.", "").split(".")[0]
            results.append({"rank": i, "site": domain, "title": title, "url": link})
    except Exception:
        continue

filename = f"{query}.csv"
df = pd.DataFrame(results)
df.to_csv(filename, index=False, encoding="utf-8")
print(f"Results saved to '{filename}'")
