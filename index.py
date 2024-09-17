from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import os
import sys

print('start 1234')

# 设置ChromeDriver的路径
# chrome_driver_path = './chromedriver-mac-arm64/chromedriver'  # 替换实际的ChromeDriver路径

base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
chrome_driver_path = os.path.join(base_path, './chromedriver-mac-arm64/chromedriver')

service = Service(chrome_driver_path)

# 初始化WebDriver
driver = webdriver.Chrome(service=service)

# 打开github
driver.get('https://github.com/')

# 等待页面加载完成（设置最大页面打开等待时间）
wait = WebDriverWait(driver, 20)

# 点击搜索按钮
searchButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.header-search-button")))
searchButton.click()
time.sleep(1)

query_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#query-builder-test")))
query_input.send_keys("13xxx")
time.sleep(2)
query_input.send_keys(Keys.ENTER)  # 模拟按下 Enter 键

input('press any key end')