import quandl
import pandas as pd
quandl.ApiConfig.api_key = "_x7FtWP7yfH89vbXcoz4"
gun_data = quandl.get("WIKI/RGR", start_date="1982-01-01", end_date="2019-12-12")
print(gun_data.head())
gun_data.to_csv('data/rgr.csv')
