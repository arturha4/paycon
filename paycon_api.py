import time
import urllib.request
from conf import paycon_url, paycon_url2
import ssl, json

def get_api_data_names(url: str = paycon_url):
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        json_bin = urllib.request.urlopen(paycon_url)
        data = json.load(json_bin)
        return data
    except ConnectionError:
        return