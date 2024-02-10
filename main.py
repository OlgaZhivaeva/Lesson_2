import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


HOST = "https://api-ssl.bitly.com"


def shorten_link(token, link):
    """Функция сокращает ссылку"""
    url = f"{HOST}/v4/shorten"
    content = {"long_url": user_url}
    response = requests.post(url, headers=headers, json=content)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(token, link):
    """Функция считает клики"""
    bitlink = f"bit.ly{urlparse(link).path}"
    url = f"{HOST}/v4/bitlinks/{bitlink}/clicks/summary"
    params = {"unit": "day", "units": -1}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(link):
    """Функция проверяет является ли ссылка битлинком"""
    netloc = urlparse(link).netloc
    path = urlparse(link).path
    url = f"{HOST}/v4/bitlinks/{netloc}/{path}"
    response = requests.get(url, headers=headers)
    return response.ok


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["BITLY_TOKEN"]
    headers = {"Authorization": f"Bearer {token}"}
    user_url = input("Введите ссылку: ")
    if is_bitlink(user_url):
        try:
            count = count_clicks(token, user_url)
        except requests.exceptions.HTTPError:
            print("Что-то пошло не так")
        else:
            print(f"По вашей ссылке прошли {count} раз(а)")
    else:
        try:
            bitlink = shorten_link(token, user_url)
        except requests.exceptions.HTTPError:
            print("Вы ввели не верную ссылку")
        else:
            print(f"Битлинк: {bitlink}")
