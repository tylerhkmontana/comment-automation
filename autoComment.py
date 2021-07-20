
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


url = 'https://www.instagram.com' 
target_url = 'https://www.instagram.com/_jerishop.toy/'
curr_num_posts = 1317
comment = '저요!'
username = '' # username
password = '' # password

with webdriver.Firefox() as driver:
	driver.get(url)

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
	driver.find_element_by_name('username').send_keys(username)
	driver.find_element_by_name('password').send_keys(password)
	driver.find_element_by_xpath("//*[contains(@type,'sub')]").click()

	time.sleep(5)
	driver.get(target_url)
	soup = BeautifulSoup(driver.page_source)
	num_posts = int(soup.find('span', class_='g47SY').text.replace(',', ''))

	while num_posts <= curr_num_posts:
		driver.refresh()
		soup = BeautifulSoup(driver.page_source)
		num_posts = int(soup.find('span', class_='g47SY').text.replace(',', ''))		

	driver.find_element_by_class_name('v1Nh3').click()
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'Ypffh')))
	textarea = driver.find_element_by_xpath('//textarea')
	textarea.click()
	textarea2 = driver.find_element_by_tag_name('textarea')
	textarea2.send_keys(comment)
	driver.find_element_by_xpath("//*[contains(@type,'sub')]").click()


