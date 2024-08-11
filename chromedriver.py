import time
from telnetlib import EC

import requests
from selenium import webdriver
from selenium.common import WebDriverException, NoSuchDriverException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


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

    # Kiểm tra trạng thái của URL
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code == 200:
            # URL hợp lệ, tiếp tục mở trang web
            driver.get(url)
    except requests.RequestException as e:
        print("Nơi xảy ra lỗi: Hàm configure_and_open_browser")
        print(f"Chi tiết lỗi: {e}")
        print("Gợi ý cách sửa lỗi: Sai địa chỉ web")
        sys.exit("Trang web không tồn tại")

    print(f"Step 1: Opened web successfully at {url}")
    return driver


def perform_search_and_filter(driver):

        # Tìm phần tử thanh tìm kiếm bằng XPath, dựa vào name và placeholder
    search_input = driver.find_element(By.XPATH,
                                           value='//input[@name="q" and @placeholder="Nhập vị trí muốn ứng tuyển"]')




    search_input.send_keys('Thực tập')
    search_input.submit()

    print("Step 2: Input value")
    time.sleep(5)

    # Tìm phần tử icon và click vào để mở danh sách gợi ý
    icon_element = driver.find_element(By.CSS_SELECTOR, 'i.svicon-chevron-down.text-sm.text-primary.ml-2')
    icon_element.click()
    time.sleep(5)

    # Tìm phần tử input và nhập giá trị "TP.HCM"
    input_element = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Lọc theo tỉnh thành"]')
    input_element.send_keys("TP.HCM")
    time.sleep(5)

    # Đợi cho phần tử button với văn bản "TP.HCM" xuất hiện
    wait = WebDriverWait(driver, timeout=5)
    button_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "TP.HCM")]')))
    button_element.click()
    print(f"Step 2: Opened web successfully at ")

