from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login_with_token(driver, token):
    # 打开 Discord 的登录页面
    driver.get('https://discord.com/login')

    # 等待页面加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # 使用 JavaScript 设置 token
    script = """
    function login(token) {
        setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
            location.reload();
        }, 2500);
    }
    login(arguments[0]);
    """
    driver.execute_script(script, token)

    # 等待页面重新加载并完成登录
    WebDriverWait(driver, 10).until(EC.url_contains('/channels/@me'))


if __name__ == "__main__":
    # 设置 Chrome 浏览器选项
    options = webdriver.ChromeOptions()
    # 这里可以添加你需要的其他选项，比如无头模式
    # options.add_argument('--headless')

    # 初始化 Chrome 浏览器驱动
    service = ChromeService(executable_path='path/to/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # 替换为你的 Discord token
        discord_token = ''

        # 使用 token 登录 Discord
        login_with_token(driver, discord_token)

        # 暂停一段时间，确保你可以看到登录结果
        time.sleep(10)
    finally:
        # 关闭浏览器
        driver.quit()
