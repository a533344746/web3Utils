from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


class WebDriverHelper:
    def __init__(self, driver_path='chromedriver', browser='chrome', extension_path=None):
        options = webdriver.ChromeOptions()
        if extension_path:
            options.add_extension(extension_path)
        if browser == 'chrome':
            self.driver = webdriver.Chrome(options=options)
        elif browser == 'firefox':
            self.driver = webdriver.Firefox(options=options)
        else:
            raise ValueError("Unsupported browser: choose 'chrome' or 'firefox'")

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element(self, by, value, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            print(f"Element with {by}='{value}' not found within {timeout} seconds.")
            return None

    def click_element(self, by, value, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            return True
        except TimeoutException:
            print(f"Element with {by}='{value}' not clickable within {timeout} seconds.")
            return False

    def send_keys_to_element(self, by, value, keys, timeout=30):
        try:
            element = self.wait_for_element(by, value, timeout)
            if element:
                element.send_keys(keys)
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred while sending keys to element: {e}")
            return False

    def quit(self):
        self.driver.quit()


    def switch_to_window(self, window_name=None, window_index=None):
        try:
            if window_name:
                self.driver.switch_to.window(window_name)
            elif window_index is not None:
                window_handles = self.driver.window_handles
                self.driver.switch_to.window(window_handles[window_index])
            else:
                raise ValueError("You must provide either a window_name or a window_index")
        except Exception as e:
            print(f"An error occurred while switching to window: {e}")

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_all_window_handles(self):
        return self.driver.window_handles

    # 等待页面加载完毕
    def wait_for_page_load(self, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
        except TimeoutException:
            print("Timed out waiting for page to load")