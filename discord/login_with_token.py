from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from wallet.WebDriverHelper import WebDriverHelper


def login_with_token(driver, token):
    # 打开 Discord 的登录页面
    driver.open_new_tab('https://discord.com/login')

    # 等待页面加载完成
    driver.wait_for_page_load()

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
    driver.execute_cript(script, token)

    # 等待页面重新加载并完成登录
    driver.wait_for_page_load()

if __name__ == "__main__":

    # 使用封装的工具类helper
    helper = WebDriverHelper(driver_path='chromedriver', browser='chrome')

    try:
        # 替换为你的 Discord token
        discord_token = 'yourToken'

        # 使用 token 登录 Discord
        login_with_token(helper, discord_token)

        # 暂停一段时间，确保你可以看到登录结果
        time.sleep(10)
    finally:
        # 关闭浏览器
        helper.quit()
