import os, time
from selenium import webdriver
from urllib.request import urlretrieve

keyword = "KEYWORD"

print("Connecting...")
driver = webdriver.Chrome()
driver.implicitly_wait(30)

url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(keyword)
driver.get(url)

imgs = driver.find_elements_by_css_selector('img._img')
result = []
for img in imgs:
	if "http" in img.get_attribute("src"): result.append(img.get_attribute("src"))

driver.close()


if not os.path.isdir('./{}'.format(keyword)): os.mkdir('./{}'.format(keyword))

for idx, link in enumerate(result):
	start = link.rfind('.')
	end = link.rfind('&')
	filetype = link[start:end]

	urlretrieve(link, './{}/{}{}{}'.format(keyword, keyword, idx, filetype))

print("Collecting is finished!")
