from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


# def collect_main_div(driver):
#     wait = WebDriverWait(driver, timeout=10)
#     # Tìm thẻ div chính chứa tất cả các job
#     main_div = wait.until(
#         EC.presence_of_element_located(
#             (By.CSS_SELECTOR, 'div.lg\\:w-\\[77\\%\\].relative.w-11\\/12.lg\\:mx-0.mx-auto.py-3.md\\:py-0'))
#     )
#     print(main_div)
#
#     # Lấy nội dung HTML của main_div
#     main_div_html = main_div.get_attribute('outerHTML')
#
#     # Sử dụng BeautifulSoup để định dạng lại HTML
#     soup = BeautifulSoup(main_div_html, 'html.parser')
#     pretty_html = soup.prettify()  # Định dạng HTML rõ ràng hơn
#
#     # Lưu nội dung HTML vào file
#     with open("main_div.html", "w", encoding="utf-8") as file:
#         file.write(pretty_html)
#     print("Saved HTML content to main_div.html successfully")
#     return main_div
#
#
# def collect_title(main_div):
#     wait = WebDriverWait(driver, timeout=10)
#     # Tìm thẻ div với class "flex items-center gap-4"
#     div_element = wait.until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, 'div.flex.items-center.gap-4'))
#     )
#
#     # Lấy văn bản từ thẻ h1 bên trong thẻ div
#     h1_element = div_element.find_element(By.TAG_NAME, "h1")
#     div_text = h1_element.text
#     return div_text
#
#
# def collect_jobs(main_div):
#     # Tìm tất cả các thẻ div con tương ứng với mỗi job
#     job_divs = main_div.find_elements(By.CSS_SELECTOR,
#                                       'div.relative.lg\\:h-\\[115px\\].w-full.flex.rounded-sm.lg\\:mb-3.mb-2.lg\\:hover\\:shadow-md')
#
#     job_data = []
#     for job_div in job_divs:
#     # Lấy tiêu đề công việc từ thẻ con bên trong, giả sử là thẻ h3
#     try:
#         title_element = job_div.find_element(By.CSS_SELECTOR,
#                                              'h3.text-se-neutral-100-n font-medium text-[18px] leading-6 tracking-tighter line-clamp-2 lg:line-clamp-none lg:truncate lg:block')
#         job_title = title_element.text
#     except Exception as e:
#         job_title = "N/A"
#
#         # Lấy tên công ty từ thẻ con bên trong, giả sử là thẻ span hoặc div
#     try:
#         company_element = job_div.find_element(By.CSS_SELECTOR, 'span.company-name-selector')
#         company_name = company_element.text
#     except Exception as e:
#         company_name = "N/A"
#
#         # Lấy địa điểm từ thẻ con bên trong
#     try:
#         location_element = job_div.find_element(By.CSS_SELECTOR, 'span.location-selector')
#         job_location = location_element.text
#     except Exception as e:
#         job_location = "N/A"
#
#         # Lưu thông tin vào danh sách
#     job_data.append({
#         'title': job_title,
#         'company': company_name,
#         'location': job_location
#     })
#
#     print("Collected job data successfully")
#     return job_data


def page(driver):
    wait = WebDriverWait(driver, timeout=10)
    cnt=1
    while True:
        try:
            # Lấy mã nguồn HTML và phân tích bằng BeautifulSoup
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            # Xuất HTML đẹp (prettify) và lưu vào file
            with open(f'HTML\\{cnt}. output.html', 'w', encoding='utf-8') as file:
                file.write(soup.prettify())
            cnt=cnt+1
            # Tìm nút "Trang Kế Tiếp" và nhấp vào nó
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.svicon-chevron-right.text-base'))
                )
                next_button.click()
            except Exception as e:
                print(f"Nút 'Trang Kế Tiếp' không tìm thấy hoặc không còn nữa: {e}")
                break  # Nếu không còn nút, dừng thu thập

        except Exception as e:
            print(f"Lỗi: {e}")
            break