import time
from time import sleep
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os


def get_price(url,appid):

	steamdb = "https://steamdb.info/app/"
	appid_str = str(appid)
	url = steamdb + appid_str + "/"
	print(url)

	# we use SteamDB to get all answers possible
	# but It is possible to make this much more simple, by getting only the country you care about

	# to make it more simple, selenium is set to not show screen
	option = Options()
	option.headless = True
	os.environ['MOZ_HEADLESS'] = '1'
	driver = webdriver.Firefox()
	driver.get(url)

	# we have to wait just a little for the firefox window to fully load
	sleep(15)
 
	# this gets the pure html of the part that is important
	element = driver.find_element_by_xpath("//div[@class='container']//div[@class='tabbable']//div[@class='tab-content']//div[@class='tab-pane selected']//div[@class='table-responsive']//table[@class='table table-fixed table-prices table-hover table-sortable']")
	html_content = element.get_attribute('outerHTML')

	# this makes the previous html mess more understandable
	soup = BeautifulSoup(html_content, features="lxml")
	table = soup.find(name='table')

	# It turns everything into a table with all info we need (we get only the important fields)
	df_full = pd.read_html(str(table))[0]
	df = df_full[['Currency', 'Current Price', 'Lowest Recorded Price.1']]
	df.columns = ['Currency', 'Price atm', 'Lowest Price Ever'] 

	# we turn the table into a Python structure
	info = {}
	info = df.to_dict()

	i = 0

	# cleses firefox
	driver.quit()
  
	return(info)
