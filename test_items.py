from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_exist_basket(browser):
    browser.get(link)
    time.sleep(10)
    button=False
    try:
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-add-to-basket"))
        )
    finally:
        assert button