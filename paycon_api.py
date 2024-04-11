import requests

paycon_url = 'https://paycon.su/api1.php'


def get_api1_data_names(url: str = paycon_url):
    try:
        response = requests.get(url)
        data = response.json()
        return [f'{item["name"]} {item["price"]}' for item in data]
    except ConnectionError:
        return
