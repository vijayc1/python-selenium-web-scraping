from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome(executable_path = 'add your chromedriver.exe path here')
driver.get('https://www.yelp.com/search?find_desc=Plumbers&find_loc=San+Francisco%2C+CA&ns=1')
driver.maximize_window()
time.sleep(1)

names = driver.find_elements_by_xpath('//h4[@class="css-p44n4y"]/span/a')
ratings = driver.find_elements_by_xpath('//span[@class=" display--inline__09f24__nqZ_W border-color--default__09f24__3Epto"]/div')
ratings_count = driver.find_elements_by_xpath('//div[@class=" attribute__09f24__1La1D display--inline-block__09f24__3SvIn border-color--default__09f24__3Epto"]/span')

names_list, ratings_list, ratings_count_list = [], [], []

for i in names:
    names_list.append(i.text)
for i in ratings:
    ratings_list.append(i.get_attribute('aria-label'))
for i in ratings_count:
    ratings_count_list.append(i.text)

print(names_list)
print(ratings_list)
print(ratings_count_list)