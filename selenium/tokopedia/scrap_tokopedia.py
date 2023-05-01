

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from tokopedia_function import get_url_parameter
import pandas as pd
from datetime import datetime


now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime('%d-%m-%Y %H-%M-%S')


# Inisialisasi variable
search_key = 'iphone 14 pro'
total_page = 5
check_available = False
# temp untuk menyimpan semua data
temp = []
# Set target website
website = 'http://www.tokopedia.com/'
# Set path untuk chrome driver
PATH = 'chromedriver'

# Create driver untuk ngebuka chrome
driver = webdriver.Chrome(PATH)

# Open Website
driver.get(website)

search = driver.find_elements(By.TAG_NAME, 'input')[0]
search.send_keys(search_key)
search.send_keys(Keys.RETURN)

for i in range(1, total_page+1):
    #time.sleep(2)
    check_footer = False
    while True:
        try:
            driver.execute_script("window.scrollTo(200, 1000)") 
            #time.sleep(0.8)
            footer = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-gvoll6')))
            actions = ActionChains(driver)
            actions.move_to_element(footer).perform()
            print('Ketemu')
            check_available = True
            check_footer = True
            break
        except TimeoutException:
            print('gak ketemu')
            break
    if check_footer == False:
        break
    body = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-jza1fo')))
    for ii in range(0, len(body)):
        #body = driver.find_elements(By.CLASS_NAME, 'css-jza1fo')
        list_item = body[ii].find_elements(By.CSS_SELECTOR, 'a.css-gwkf0u')
        for iii in range(0, len(list_item)):
            url_product = list_item[iii].get_attribute('href')
            title = list_item[iii].find_element(By.CSS_SELECTOR, 'div.css-3um8ox').text
            price = list_item[iii].find_element(By.CSS_SELECTOR, 'div.css-1ksb19c').text
            location = list_item[iii].find_elements(By.TAG_NAME, 'span')[0].text
            toko = list_item[iii].find_elements(By.TAG_NAME, 'span')[1].text
            url_product = url_product if 'ta.tokopedia.com' not in url_product else get_url_parameter(url_product, param='r')
            temp.append((title, price, location, toko, url_product, i))
            
            #print(temp)
    #print(i)
    if total_page == 1:
        break
    next_page = 'https://www.tokopedia.com/search?navsource=home&page=' + str(i) + '&q=' + search_key + '&st=product'
    driver.get(next_page)

driver.quit() 
if check_available == True:       
    df = pd.DataFrame(temp, columns=('Title', 'Price', 'Location', 'Toko', 'URL', 'Page'))
    #df['Price_fix'] = df['Price'].str.replace('Rp','').str.replace('.', '')
    print(df.head())
    df.to_excel(f'selenium/tokopedia/result_{search_key}_{total_page} page_{dt_string}.xlsx', sheet_name='sheet1')
else:
    print('No data has found')

