import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


HOST = "https://api-ssl.bitly.com"


def shorten_link(link, headers):
    """Функция сокращает ссылку"""
    url = f"{HOST}/v4/shorten"
    content = {"long_url": link}
    response = requests.post(url, headers=headers, json=content)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(link, headers):
    """Функция считает клики"""
    parse = urlparse(link)
    netloc = parse.netloc
    path = parse.path
    url = f"{HOST}/v4/bitlinks/{netloc}/{path}/clicks/summary"
    params = {"unit": "day", "units": -1}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(link, headers):
    """Функция проверяет является ли ссылка битлинком"""
    parse = urlparse(link)
    netloc = parse.netloc
    path = parse.path
    url = f"{HOST}/v4/bitlinks/{netloc}/{path}"
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    """Основная функция"""
    load_dotenv()
    token = os.environ["BITLY_TOKEN"]
    headers = {"Authorization": f"Bearer {token}"}
    user_url = input("Введите ссылку: ")
    if is_bitlink(user_url, headers):
        try:
            count = count_clicks(user_url, headers)
        except requests.exceptions.HTTPError:
            print("Что-то пошло не так")
        else:
            print(f"По вашей ссылке прошли {count} раз(а)")
    else:
        try:
            bitlink = shorten_link(user_url, headers)
        except requests.exceptions.HTTPError:
            print("Вы ввели не верную ссылку")
        else:
            print(f"Битлинк: {bitlink}")


if __name__ == "__main__":
    main()
