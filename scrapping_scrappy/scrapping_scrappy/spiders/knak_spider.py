import scrapy
from pathlib import Path
from datetime import datetime

class KnakSpider(scrapy.Spider):
    name = 'knak'

    start_urls  = [
            'https://www.knak.jp/japan/naphtha.htm'
        ]
        

    def parse(self, response):
        check_slash = 0
        value = ''
        date = ''
        table = response.css('table')[9]
        for list_tr in table.css('tr'):
            for list_td in list_tr.css('td').css('font::text, strong::text')[5:].getall():
                list_td = list_td.strip()
                if list_td == '':
                    continue
                if check_slash == 1:
                    # menghapus character ',' dan menyimpan kedalam value
                    value = list_td.replace(',', '').replace('\\', '')
                    # mengurangi check_slash agar setelah cell ini tidak di ambil datanya
                    check_slash = 0
                    # check apakah valuenya kosong atau tidak
                    if value != '':
                        # merubah date menjadi monthkey
                        print(date)
                        try:
                            monthkey = datetime.strptime(date, '%y/%m').strftime('%Y%m')
                        except:
                            date = '0' + date
                            monthkey = datetime.strptime(date, '%y/%m').strftime('%Y%m')
                    yield{
                        'date' : monthkey,
                        'value' : value
                    }
                if '/' in list_td and len(list_td) <= 5:
                    # menambahkan check_slash 1 agar next cell akan kita ambil
                    check_slash += 1
                    # menyimpan data date
                    date = list_td
                    



