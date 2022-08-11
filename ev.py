from urllib.request import Request, urlopen

import pandas as pd

key = "uBzKP8jdbvhqgxTQUlLMyoJGyOBu1QIhJekChUlr"
format = "csv"
url = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1&api_key={}&format={}".format(key, format)
url_request = Request(url)
data = urlopen(url_request)
my_table = pd.read_table(data.read())
len(my_table)



import requests

resp = requests.get(url)
txt = resp.json()
pd.DataFrame(txt['metrics'])