from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import urlparse
from urllib.parse import parse_qs
import pandas as pd
#import datetime


def get_url_parameter(url, param):
    parsed_url = urlparse(url)
    captured_value = parse_qs(parsed_url.query)[param][0]
    print(captured_value)
    return captured_value

# Inisialisasi variable
search_key = 'Samsung s21'
total_page = 3
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