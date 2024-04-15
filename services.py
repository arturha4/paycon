import time
import urllib.request
from conf import *
import ssl, json
import csv
import os

def get_api_data_names(url: str = paycon_url):
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        json_bin = urllib.request.urlopen(paycon_url)
        data = json.load(json_bin)
        return [f'{item["name"]} {item["price"]}' for item in data]
    except ConnectionError:
        return


def get_csv_data_names(filename=csv_name):
    data = []
    file = open(os.path.abspath(filename),encoding='utf-8')
    reader = csv.DictReader(file)
    for row in reader:
        data.append(f"{row['Title']} {row['Price']}")
    return data