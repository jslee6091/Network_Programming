### Selenium

1. selenium_test.py
   - google 검색창에 단어를 입력하고 검색을 실행하는 코드
   - get(url) : 접속하고자 하는 웹페이지의 url을 입력하여 띄우는 역할을 한다.
   - find_element_by_name() : 웹페이지의 HTML 소스에서 특정 name을 갖는 element를 반환함.
   - send_keys() : 원하는 element를 얻은 후 key를 전달하는 것. 여기서는 구글 검색창에 입력할 단어를 전달한다.
   - submit() : 검색을 실행하는 함수



2. selenium_test2.py
   - facebook 홈페이지에 로그인 후 프로필과 친구목록 페이지에 접속하는 코드
   - send_keys(Keys.RETURN) : Enter 키 누르게 하는 함수
   - find_element_by_xpath() : 접속하고자 하는 페이지의 xpath를 갖는 element를 반환함.
   - get_attribute('href') : xpath를 통해 얻은 element의 href 값을 반환한다. 이를 get 함수를 이용하여 해당 페이지에 접속할 수 있다.

