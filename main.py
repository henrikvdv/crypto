# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import urllib.request
import pandas as pd

def get_crypto(name):
    # Use a breakpoint in the code line below to debug your script.
    key = "uBzKP8jdbvhqgxTQUlLMyoJGyOBu1QIhJekChUlr"
    format = "csv"
    url = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1&api_key={}&format={}".format(key, format)
    data = urllib.request.urlopen(url).read()# Press ⌘F8 to toggle the breakpoint.
    df = pd.read_table(data.decode())





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_crypto('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
