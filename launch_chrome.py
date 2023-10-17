from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-dev-shm-using")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
#
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=chrome_options)

url = 'https://www.google.com/'
driver.get(url)
driver.quit()
