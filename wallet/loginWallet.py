from selenium.webdriver.common.by import By
import time

from wallet.WebDriverHelper import WebDriverHelper

# 使用私钥登陆钱包
def login_with_sy(driver, sy, password):
    try:
        # 打开 Chrome 扩展页面
        driver.open_url('chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/home.html')
        # 等待页面加载
        driver.wait_for_page_load()
        # 选择转跳的浏览器窗口
        driver.switch_to_window(window_index=0)

        # 开始输入私钥操作
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div/div[2]/button')
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div/div[1]')
        driver.click_element(By.XPATH, '/ html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]')

        # 输入私钥
        driver.send_keys_to_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div/textarea', sy)
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div[4]/div/button')
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div')
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/button')

        # 输入钱包密码
        driver.send_keys_to_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/div[1]/div[2]/div/div/div/div/input', password)
        driver.send_keys_to_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/div[3]/div[2]/div/div/div/div/input', password)
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/div[5]/div/div/div/div/div/button')
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div/button')
        # 登陆成功

    except Exception as e:
        print(f"使用私钥登陆钱包发生错误: {e}")
# 使用注记词登陆钱包(12位注记词)
def login_with_word(driver, word, password):
    try:
        # 打开 Chrome 扩展页面
        driver.open_url('chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/home.html')
        # 等待页面加载
        driver.wait_for_page_load()

        # 选择转跳的浏览器窗口
        driver.switch_to_window(window_index=0)
        driver.click_element(By.XPATH, '//*[@id="app"]/div/div/div/div[3]/div/div[2]/button/span')
        driver.click_element(By.XPATH, '//*[@id="app"]/div/div/div/div[3]/div/div[1]/div[2]/div/div')

        # 按空格分割注记词
        str1 = word.split()
        try:
            for i in range(1, 13):
                driver.send_keys_to_element(By.XPATH, f'/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div[{i}]/div[2]/input',str1[i-1])
                driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[2]/div')
        except Exception as e:
            print(f"注记词单词输入错误： {e}")
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div/button')
        driver.send_keys_to_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/div[1]/div[2]/div/div/div/div/input', pwd)
        driver.send_keys_to_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/div[3]/div[2]/div/div/div/div/input', pwd)
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/div[5]/div/div/div/div/div/button')
        driver.click_element(By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div/button')
    except Exception as e:
        print(f"使用注记词登陆钱包发生错误: {e}")

# 示例使用
if __name__ == "__main__":
    # 需要用到的插件文件路径
    EXTENSION_PATH = 'C:/Users/y/Desktop/PythonStudy/web3Util/crx/okxWallet.crx'

    # 使用封装的工具类helper
    helper = WebDriverHelper(driver_path='chromedriver', browser='chrome', extension_path=EXTENSION_PATH)
    pwd = 'asdfzxcv1234'

    # 测试
    # login_with_sy(helper,'96a003794d4148858f7442763bded70c14578b8edbee17645ae602bf9814f82e', pwd)
    login_with_word(helper,'document success better sketch leader secret library couple little turtle siege absent', pwd)
    time.sleep(100)
    helper.quit()
