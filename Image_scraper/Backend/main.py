import requests
from bs4 import BeautifulSoup
import os

def create_image_folder(folder_path='Images/'):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def get_image_urls(query):
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    image_tags = soup.find_all('img')[1:]
    return [img['src'] for img in image_tags if 'src' in img.attrs]

def save_images_from_google(query):
    folder = create_image_folder()
    image_urls = get_image_urls(query)

    for i, image_url in enumerate(image_urls):
        image_data = requests.get(image_url).content
        with open(os.path.join(folder, f"{i}.jpeg"), "wb") as file:
            file.write(image_data)
    return len(image_urls)