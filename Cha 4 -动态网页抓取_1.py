from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()

chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/usr/bin/chromedriver")

driver.get("http://www.santostang.com/2018/07/04/hello-world/")
print(driver.page_source)
driver.close()