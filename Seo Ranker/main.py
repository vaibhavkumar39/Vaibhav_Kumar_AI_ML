from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd
import time

def SetupDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def FetchSearchResults(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    driver = SetupDriver()
    driver.get(url)
    time.sleep(2)
    pageSource = driver.page_source
    driver.quit()
    return pageSource

def ParseResults(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []

    for i, result in enumerate(soup.select("a.zReHs")[:10], start=1):
        try:
            titleTag = result.select_one("h3.LC20lb")
            link = result["href"]
            if titleTag and link:
                title = titleTag.get_text()
                domain = urlparse(link).netloc.replace("www.", "").split(".")[0]
                results.append({"rank": i, "site": domain, "title": title, "url": link})
        except Exception:
            continue
    return results

def SaveToCsv(results, query):
    filename = f"{query}.csv"
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Results saved to '{filename}'")

def Main():
    query = input("Enter keyword: ")
    html = FetchSearchResults(query)
    results = ParseResults(html)
    SaveToCsv(results, query)

if __name__ == "__main__":
    Main()