from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://web.chal.csaw.io:5010/")

def scrape_links():
    try:
        href = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//a[@href]")))
        print('links found')
    except TimeoutException:
        print('links not found')

    link = href.get_attribute("href")
    driver.get(link)

while True:
    try:
        scrape_links()
    except:
        print(driver.page_source)
        break