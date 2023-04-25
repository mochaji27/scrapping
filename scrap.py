import requests
from bs4 import BeautifulSoup

result_name = []

url = 'https://www.charitynavigator.org'

for i in range(1, 10):

    url_base = url + '/search?page=' + ("" if i == 1 else str(i))
  

    r = requests.get(url = url_base)
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.prettify())
    containers = soup.find("div", class_ = 'tw-mt-3 tablet:tw-mt-14 tablet:tw-px-12 tw-w-full tw-max-w-[1200px]')
    block = containers.find_all("a", class_ = 'SearchResult-module__SearchResult___Z0d4h')

    for detail in block:
        #result_name = result_name + [detail.find("h2", class_ = 'tw-font-sofia-pro tw-font-semibold tw-text-lg tablet:tw-text-xl tw-text-night-sky-800 tw-tracking-normal tablet:tw-tracking-[-0.2px] tw-mb-1').get_text()]
        href = detail.get('href')
        url_detail = url + href
        r_detail = requests.get(url = url_detail)
        soup_detail = BeautifulSoup(r_detail.content, 'html.parser')
        #print(soup_d)
        company_name = soup_detail.find('h1', class_ = 'cardrow__header-row--title').get_text()
        profile_bullet = soup_detail.find_all('span', class_ = 'icon-text-indent')
        print(len(profile_bullet))
        print(company_name)
        print(profile_bullet[len(profile_bullet)-2].get_text())
        print(profile_bullet[len(profile_bullet)-1].get_text())
        

#print(result_name)
