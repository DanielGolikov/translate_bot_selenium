import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")stop
#chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver', 0, chrome_options)


def translate(text, target):

    driver.get(f"https://translate.google.com/?sl=auto&tl={target}&text={text}&op=translate")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".JLqJ4b.ChMk0b")))
    time.sleep(1)
    content = driver.find_elements_by_class_name("JLqJ4b.ChMk0b")
    content2 = driver.find_element_by_css_selector(".aCQag")
    return content[0].text, content2.text.split(" - ")[0]
