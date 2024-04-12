import urllib.request
from conf import paycon_url
import ssl, json

def get_api1_data_names(url: str = paycon_url):
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        json_bin = urllib.request.urlopen(paycon_url)
        data = json.load(json_bin)
        print(data)
    except ConnectionError:
        return
