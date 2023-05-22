
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

search_key = 'iphone 14 pro'

base_url = f'https://www.amazon.com/s?k={search_key}&page='


PATH = 'Scrapping/chromedriver'
# Create driver untuk ngebuka chrome
driver = webdriver.Chrome(PATH)

# Open Website
driver.get(f'{base_url}1')

list_item = driver.find_elements(By.XPATH, '//div[@class="sg-col-inner"]/div/div[0]/h2/a/span')
print(len(list_item))
for item in list_item:
    name = item.text
    #type = item.find_element(By.XPATH, './/span[@class="a-color-information a-text-bold"]').text
    #rating = item.find_element(By.XPATH, './/span[@class="a-icon-alt"]').text
    #review = item.find_element(By.XPATH, './/span[@class="a-size-base s-underline-text"]').text

    print(name)

driver.quit() 