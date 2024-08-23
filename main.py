from gc import collect
from selenium.webdriver.support.wait import WebDriverWait

from chromedriver import *
from etl import *

def main():
    # Step 1: Nhập url cần scrap data
    url = "https://vieclam24h.vn"
    driver = configure_and_open_browser(url)

    # Step 2: Lọc và tìm kiếm dữ liệu
    content = "Thực tập"
    location = "TP.HCM"
    perform_search_and_filter(driver, content, location)
    time.sleep(3)

    page(driver)
    # # Step 3: Thu thập main_div
    # main_div=collect_main_div(driver)
    #
    # # Thu thập title
    # title=title_data(driver)
    # print(title)
    # time.sleep(3)
    #
    #
    #
    #
    #
    # print(collection(driver))



    # Đóng trình duyệt sau khi hoàn tất
    time.sleep(5)  # Dừng 5 giây để xem trang web
    print("Final step: Completed")
    driver.quit()


if __name__ == "__main__":
    main()
