"""
2022 (c) Putivskaya
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_smoke(browser):
    """"
    WERT-1. Smoke Test
    """

    browser.get('https://testqastudio.me/')

    #driver.quit()

    assert True
