
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import datetime

# Inisialisasi variable
# set_index_body untuk menentukan tbody keberapa yang akan kita ambil
set_index_body = 9
# temp untuk menyimpan semua data
temp = []
# check_slash untuk memvalidasi apakah cell yang kita looping mempunyai '/'
# jika mempunyai '/' maka check_slash akan bertambah 1 karena untuk mengambil value setelah data date kita temukan
# jika cell setelah date (value) kita ambil, maka check_slash akan menjadi 0
check_slash = 0
value = ''
date = ''
# Set target website
website = 'https://www.knak.jp/japan/naphtha.htm'
# Set path untuk chrome driver
PATH = 'Scrapping/chromedriver'

# Create driver untuk ngebuka chrome
driver = webdriver.Chrome(PATH)

# Open Website
driver.get(website)

# Cari element dari table yang di tuju, 
# Disini kita mencari element berdasarkan tagname yang bernama tbody
body = driver.find_elements(By.TAG_NAME, 'tbody')

# Disini mencari tagname yang bernama tr
# dan melisting semua element yang ber tagname tr
list_row = body[set_index_body].find_elements(By.TAG_NAME, 'tr')
# Looping untuk setiap list row
for i in range(0, len(list_row)):
    # Cari element di dalam list_row berdasarkan td (ini untuk mencari setiap cell dalam 1 row)
    list_col = list_row[i].find_elements(By.TAG_NAME, 'td')
    # Looping untuk setiap cell
    for ii in range(0, len(list_col)):
        # Untuk memvalidasi apakah sebelumnya cell ini merupakan data date atau bukan
        if check_slash == 1:
            # mengurangi check_slash agar setelah cell ini tidak di ambil datanya
            check_slash -= 1
            # menghapus character ',' dan menyimpan kedalam value
            value = list_col[ii].text.replace(',', '')
            # check apakah valuenya kosong atau tidak
            if value != '':
                # merubah date menjadi monthkey
                monthkey = datetime.datetime.strptime(date, '%y/%m').strftime('%Y%m')
                # menambahkan date, value, dan currency kedalam temp
                temp.append((monthkey, value, 'yen / kl', 'Naphtha'))
            #print(list_col[ii].text)
        # validasi cell jika memiliki character '/'
        if '/' in list_col[ii].text:
            # menambahkan check_slash 1 agar next cell akan kita ambil
            check_slash += 1
            #print(list_col[ii].text)
            # menyimpan data date
            date = list_col[ii].text
            
#print(temp)

# menutup aplikasi
driver.quit()

# membuat data temp menjadi dataframe
df = pd.DataFrame(temp, columns=('MonthKey', 'Value', 'Currency', 'Material'))
df = df.sort_values(by = ['MonthKey'])
print(df)