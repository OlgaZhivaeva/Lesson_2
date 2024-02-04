import os
import requests
from pprint import pprint
from urllib.parse import urlparse
from dotenv import load_dotenv
HOST = "https://api-ssl.bitly.com"

def shorten_link(token, link):
    """Функция сокращает ссылку"""
    url = f"{HOST}/v4/shorten"
    json = {"long_url": user_url}
    response = requests.post(url, headers=headers, json=json)
    response.raise_for_status()
    return response.json()["link"]

def count_clicks(token, link):
    """Функция считает клики"""
    bitlink = f"bit.ly{urlparse(link).path}"
    url = f"{HOST}/v4/bitlinks/{bitlink}/clicks/summary"
    params = {"unit": "day","units": -1}
    response = requests.get(url, params=params, headers=headers)
    # print(response.status_code)
    # print(response.json())
    response.raise_for_status()
    return response.json()["total_clicks"]

def is_bitlink(link):
    """Функция проверяет является ли ссылка битлинком """
    path = urlparse(link).path
    url = f"{HOST}/v4/bitlinks/bit.ly{path}"
    response = requests.get(url, headers=headers)
    return response.ok

def get_profile(token):
    """"Функция дает сведения об аккаунте"""
    url = f"{HOST}/v4/user"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    """Основная функция"""
    if is_bitlink(user_url):
        try:
            count = count_clicks(token, user_url)
        except requests.exceptions.HTTPError:
            print("Что-то пошло не так")
        else:
            print(f"Число кликов: {count}")
    else:
        try:
            bitlink = shorten_link(token, user_url)
        except requests.exceptions.HTTPError:
            print("Вы ввели не верную ссылку")
        else:
            print(f"Короткая ссылка: {bitlink}")

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("TOKEN")
    headers = {"Authorization": f"Bearer {token}"}
    # user_url = "https://devops.org.ru/docker-summary#d1"

    try:
        profile = get_profile(token)
    except requests.exceptions.HTTPError:
        print("Токен не работает")
    else:
        print(f"Ваш профиль:")
        pprint(profile)
        user_url = input("Введите ссылку: ")
        main()


