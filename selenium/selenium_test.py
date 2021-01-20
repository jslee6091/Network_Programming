from selenium import webdriver

path = "C:\\Users\\jslee\\Desktop\\cloud-service-mycode\\selenium\\webdriver\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.google.com")
search_box = driver.find_element_by_name("q")
search_box.send_keys("django")
search_box.submit()
