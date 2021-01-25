from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:\\Users\\jslee\\Desktop\\cloud-service-mycode\\selenium\\webdriver\\chromedriver.exe"
driver = webdriver.Chrome(path)

# url 주소를 브라우저에 띄우기
driver.get("https://www.facebook.com/")

elem_email = driver.find_element_by_id("email")
elem_email.send_keys('facebook email')
elem_pass = driver.find_element_by_id("pass")
elem_pass.send_keys('facebook pw')

# Enter 누르기 수행
elem_pass.send_keys(Keys.RETURN)

# Xpath를 통해 웹사이트 주소 얻어오기
profile_a = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a')
print('profile_a : ', profile_a.get_attribute('href'))
friends_a = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/a')
print('friends_a : ', friends_a.get_attribute('href'))

# 해당 웹사이트 접속
driver.get(profile_a.get_attribute('href'))
# driver.get(friends_a.get_attribute('href'))
