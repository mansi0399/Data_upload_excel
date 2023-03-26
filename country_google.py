import pandas as pd
import webbrowser
mansi = pd.read_excel('C:/Users/mansi/OneDrive/Desktop/Country.xlsx', usecols = ['Name'])
for country in mansi['Name']:
    url = "https://www.google.com/search?q=" + country
    webbrowser.open(url, new = 2)
