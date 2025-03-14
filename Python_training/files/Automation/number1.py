from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd
from datetime import datetime
import os
import sys


application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

website = 'https://www.thesun.co.uk/sport/football/'
path = "C:\Python 2.0/filemanipulating"


options = Options()
options.headless = True


service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="fteaser_copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text
    subtitle = container.find_element(by="xpath", value='./a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)



my_dict = {'titles':titles,
           'subtitle':subtitles,
           'link':links}

df_headlines = pd.DataFrame(my_dict)
file_name = f'headline-{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(final_path)

driver.quit()