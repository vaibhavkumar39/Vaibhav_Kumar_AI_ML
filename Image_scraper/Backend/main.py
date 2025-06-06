import requests
from bs4 import BeautifulSoup
import os

def save_images_from_google(query):
    save_images = 'Images/'
    if not os.path.exists(save_images):
        os.makedirs(save_images)

    url = f"https://www.google.com/search?q={query}&tbm=isch"
    response = requests.get(url) 
    soup = BeautifulSoup(response.content, 'html.parser')
    image_tags = soup.find_all('img')[1:]

    i = 0
    for image in image_tags:
        image_url = image['src']
        image_data = requests.get(image_url).content
        with open(os.path.join(save_images, f"{i}.jpeg"), "wb") as file:
            file.write(image_data)
        i += 1
    return i