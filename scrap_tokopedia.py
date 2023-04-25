from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
#import datetime

# Inisialisasi variable
search_key = 'Samsung s21'
total_page = 3
check_available = False
# temp untuk menyimpan semua data
temp = []
# Set target website
website = 'http://www.tokopedia.com/'
# Set path untuk chrome driver
PATH = 'Scrapping/chromedriver'

# Create driver untuk ngebuka chrome
driver = webdriver.Chrome(PATH)

# Open Website
driver.get(website)

search = driver.find_elements(By.TAG_NAME, 'input')[0]
search.send_keys(search_key)
search.send_keys(Keys.RETURN)

for i in range(1, total_page+1):
    time.sleep(2)
    check_footer = False
    while True:
        try:
            driver.execute_script("window.scrollTo(200, 1000)") 
            time.sleep(0.8)
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
        list_item = body[ii].find_elements(By.CLASS_NAME, 'css-gwkf0u')
        
        for iii in range(0, len(list_item)):
            title = list_item[iii].find_element(By.CLASS_NAME, 'css-12fc2sy').text
            price = list_item[iii].find_element(By.CLASS_NAME, 'css-a94u6c').text
            if list_item[iii].find_elements(By.TAG_NAME, 'span')[0].text == 'Ad':
                location = list_item[iii].find_elements(By.TAG_NAME, 'span')[1].text
                toko = list_item[iii].find_elements(By.TAG_NAME, 'span')[2].text
            else:    
                location = list_item[iii].find_elements(By.TAG_NAME, 'span')[0].text
                toko = list_item[iii].find_elements(By.TAG_NAME, 'span')[1].text
            temp.append((title, price, location, toko, i))
            print(temp)
    print(temp)
    print(i)
    next_page = 'https://www.tokopedia.com/search?navsource=home&page=' + str(i) + '&q=' + search_key + '&st=product'
    driver.get(next_page)

driver.quit() 
if check_available == True:       
    df = pd.DataFrame(temp, columns=('Title', 'Price', 'Location', 'Toko', 'Page'))
    print(df)
    #df.to_excel('Hasil.xlsx', sheet_name='sheet1')
else:
    print('No data has found')



