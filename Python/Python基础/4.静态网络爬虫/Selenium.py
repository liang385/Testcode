import threading
import time
import json
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def run():
    # 获取服务,设置不打开网页
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # 不自动关闭浏览器
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.mi.com/shop")
    # 输出渲染后的html,包含动态数据
    # print(driver.page_source)
    # 列表对象，需要遍历
    # title=driver.find_elements(
    #     By.XPATH,
    #     value='//*[@id="header-wrapper"]/div/nav[1]/div/a'
    # )
    driver.maximize_window()

    # webdriver 提供 back 和 forward 方法来实现页面的后退与前进
    # driver.forward()
    # driver.back()
    # 键盘操作
    # 模拟完成单击鼠标左键的操作，一般点击进入子页面等会用到，单左键不需要用到 ActionChains
    button = driver.find_element(
        By.XPATH, value='//*[@id="search"]')
    # button.click()
    # 单右击 需要用ActionChains
    # ActionChains(driver).context_click(button).perform()
    # 双击
    # ActionChains(driver).double_click(button).perform()
    # 鼠标悬停
    # ActionChains(driver).move_to_element(button).perform()

    # webdriver 中 Keys 类几乎提供了键盘上的所有按键方法，
    # 我们可以使用 send_keys + Keys 实现输出键盘上的组合按键如 “Ctrl + C”、“Ctrl + V” 等
    # 在文本框输入
    button.send_keys("redmik")
    # back_space 删除
    button.send_keys(Keys.BACK_SPACE)
    # 回车
    button.send_keys(Keys.ENTER)



if __name__ == "__main__":
    run()
