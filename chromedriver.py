import time
from telnetlib import EC

import requests
from selenium import webdriver
from selenium.common import WebDriverException, NoSuchDriverException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


def configure_and_open_browser(url):
    # Cấu hình ChromeDriver
    chrome_options = Options()
    # Chạy ở chế độ không hiển thị giao diện
    # chrome_options.add_argument("--headless")

    try:
        # Đặt đường dẫn đến ChromeDriver
        service = Service('H:\\Web Scraping\\2. Selenium\\vieclam24h\\chromedriver.exe')
        # Khởi tạo trình duyệt
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except (WebDriverException, NoSuchDriverException) as e:
        print("Nơi xảy ra lỗi: Hàm configure_and_open_browser")
        print(f"Chi tiết lỗi: {e}", end="")
        print("Gợi ý cách sửa lỗi: Sai đường dẫn")
        sys.exit("Chương trình kết thúc do lỗi")

    try:
        # Mở trang web
        driver.get(url)
    except Exception as e:
        print("Nơi xảy ra lỗi: Hàm configure_and_open_browser")
        print(f"Chi tiết lỗi: {e}")
        print("Gợi ý cách sửa lỗi: Sai địa chỉ web")
        sys.exit("Trang web không tồn tại")

    print(f"Step 1: Opened web successfully at {url}")
    return driver


def perform_search_and_filter(driver):
    # Tạo WebDriverWait
    wait = WebDriverWait(driver, timeout=10)

    # Nhập nội dung trong thanh tìm kiếm
    search_input = wait.until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="q" and @placeholder="Nhập vị trí muốn ứng tuyển"]')))
    search_input.send_keys('Thực tập')
    search_input.send_keys(Keys.RETURN)

    # Tìm phần tử icon và click vào để mở danh sách gợi ý
    icon_element = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.svicon-chevron-down.text-sm.text-primary.ml-2'))
    )
    time.sleep(2)
    icon_element.click()
    time.sleep(2)

    # Tìm phần tử input và nhập giá trị "TP.HCM"
    input_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Lọc theo tỉnh thành"]'))
    )
    input_element.send_keys("TP.HCM")

    # Đợi cho phần tử button với văn bản "TP.HCM" xuất hiện
    button_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "TP.HCM")]'))
    )
    button_element.click()

    print(f"Step 2: Opened web successfully")
