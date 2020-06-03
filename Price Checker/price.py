import time
from time import sleep
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def get_price(url,appid):

	steamdb = "https://steamdb.info/app/"
 
	appid_str = str(appid)
 
	url = steamdb + appid_str + "/"
 
	print(url)

	# url is the STeam URL that will be printed for the user
	# internally we will just use steamdb

	# to make it more simple, selenium is set to not show screen
	option = Options()
	option.headless = True
	driver = webdriver.Firefox()
	driver.get(url)
 
	sleep(15)
 
	# element = driver.find_element_by_xpath("//div[@class='container']//div[@class='tabbable']//div[@class='tab-content']//div[@class='tab-pane selected']//div[@class='table-responsive']//table[@class='table table-fixed table-prices table-hover table-sortable']//tbody//tr[@class='table-prices-current']")
	
	element = driver.find_element_by_xpath("//div[@class='container']//div[@class='tabbable']//div[@class='tab-content']//div[@class='tab-pane selected']//div[@class='table-responsive']//table[@class='table table-fixed table-prices table-hover table-sortable']")
	html_content = element.get_attribute('outerHTML')

	#print(html_content)

	soup = BeautifulSoup(html_content, features="lxml")
	table = soup.find(name='table')

	df_full = pd.read_html(str(table))[0]
	df = df_full[['Currency', 'Current Price', 'Lowest Recorded Price.1']]
	df.columns = ['Currency', 'Price atm', 'Lowest Price Ever'] 


	info = {}
	info = df.to_dict()

	i = 0
 
	#print(tabela)
	#print(tabela['Currency'].get(i))
 
	driver.quit()
 	# page = requests.get(url)
	return(info)
