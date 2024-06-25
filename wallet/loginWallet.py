from selenium.webdriver.common.by import By
import time

from wallet.WebDriverHelper import WebDriverHelper


def login_with_sy(driver, sY, pwd):
    try:
        # 打开 Chrome 扩展页面
        driver.open_url('chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/home.html')
        # 等待页面加载
        driver.wait_for_page_load()
        # 选择转跳的浏览器窗口
        driver.switch_to_window(window_index=0)
        #开始输入私钥操作
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div/div[2]/button')
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div/div[1]')
        driver.click_element(By.XPATH, '/ html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]')
        #输入私钥
        driver.send_keys_to_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div/textarea', sY)
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div[4]/div/button')
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div')
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/button')
        #输入钱包密码
        driver.send_keys_to_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/div[1]/div[2]/div/div/div/div/input', pwd)
        driver.send_keys_to_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/div[3]/div[2]/div/div/div/div/input', pwd)
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/div[5]/div/div/div/div/div/button')
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div/button')
        #登陆成功
        time.sleep(100)
    except Exception as e:
        print(f"An error occurred: {e}")


# 示例使用
if __name__ == "__main__":
    #需要用到的插件文件路径
    EXTENSION_PATH = 'C:/Users/y/Desktop/PythonStudy/web3Util/crx/okxWallet.crx'
    #使用封装的工具类helper
    helper = WebDriverHelper(driver_path='chromedriver', browser='chrome', extension_path=EXTENSION_PATH)
    pwd = 'asdfzxcv1234'
    #测试
    login_with_sy(helper,'96a003794d4148858f7442763bded70c14578b8edbee17645ae602bf9814f82e', pwd)
    print("abc")
    helper.quit()
