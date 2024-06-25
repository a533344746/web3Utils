import time

from selenium.webdriver.common.by import By

from wallet.WebDriverHelper import WebDriverHelper

def tw_to_login(driver):
    driver.open_new_tab("https://twitter.com/login")
    driver.wait_for_page_load()


if __name__ == '__main__':
    driver = WebDriverHelper(driver_path='chromedriver', browser='chrome')
    tw_to_login(driver)
    time.sleep(10)
    driver.quit()