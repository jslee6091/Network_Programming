### Scrapy Basic

1. Scrapy  설치

   ```
   conda install scrapy 또는 pip install scrapy
   python 버전이 안맞을 경우 conda 대신 pip로 install 하면 됨
   ```

   

2. 프로젝트 생성

   - `scrapy startproject [project_name]`

   

3. 프로젝트 구조

   - ```
     tutorial/
     	scrapy.cfg
     
     	tutorial/			# project's Python module. you'll import your code from here
     		__init__.py
     
     		items.py		# project items definition file
     
     		middlewares.py	# project middlewares file
     
     		pipelines.py	# project pipelines file
     
     		settings.py		# project settings file
     
     		spiders/__init__.py	# a directory where you'll later put your spiders
     
     ```

   - 프로젝트를 생성하면 같은 이름의 디렉터리가 만들어지고 그 내부에 프로젝트 파일들이 있음



3. bot file 생성
   - scrapy genspider [bot_name] ["스크래핑하려는 웹사이트 주소"]
   - 웹사이트 주소는 입력 시 http 프로토콜 입력 x



4. 코드 작성 후 실행
   - `scrapy crawl [bot_name]`



### Scrapy Shell

- anaconda prompt에서 `scrapy shell` 입력하여 shell 시작

  1. 웹사이트 정보 추출

     - `>>>fetch('웹사이트주소')`

  2. 추출한 웹사이트를 브라우저에 띄우기

     - `>>>view(resonse)`

  3. 해당 웹사이트의 전체 소스 출력

     - `>>>print(response.text)`

  4. 웹사이트의 문서 추출

     - ```
       >>>response.xpath('xpath 값')
       ```

     - ```
       결과 예시 : [<Selector xpath='//*[@id="content"]/div/div[1]/ul/li[1]/a/div[2]/strong' data='<strong class="title">이마트는 왜 프로야구에 뛰어...'>]
       ```

     - ```
       주의) text가 있는 element를 copy 해야 함. 그렇지 않으면 text 추출 불가능
       ```

  5. 원하는 element의 text만 추출

     - html 소스의 text 부분만 추출한다.

     - ```
       >>>response.xpath('xpath 값/text()')
       ```

     - ```
       결과 예시 : [<Selector xpath='//*[@id="content"]/div/div[1]/ul/li[1]/a/div[2]/strong/text()' data='이마트는 왜 프로야구에 뛰어들었나?'>]
       ```

  6. 원하는 element의 text만 추출

     - html 소스의 text를 추출하여 리스트에 담는다.

     - ```
       >>>response.xpath('xpath 값/text()').extract()
       ```

     - ```
       결과 예시 : ['이마트는 왜 프로야구에 뛰어들었나?']
       ```

  7. xpath 값의 패턴을 입력하여 해당 페이지의 모든 기사 내용 추출

     - ```
       >>> response.xpath('xpath패턴').extract()
       ```

     - ```
       결과 예시 : ['이마트는 왜 프로야구에 뛰어들었나?', '"푸이그 야구 안 해도 5년은 잘 살겠지만, 계약했으면" 美 매체', 
       	'[GOAL LIVE] ‘기 성용 코너킥 골’ FC서울, 연습경기에서 2-0 승리', 'SK, 2021년 제주도 서귀포 스프링캠프 실시...선수 43명 명단 확정', 
       	'정찬성 "한 달만 20kg 쪘다...오르테가에 패배 후 폭식"', "'바이퍼' 박도현의 미스터리...LPL서 '환골탈태'"]
       ```

  8. css를 이용하여 원하는 정보 추출

     - css를 이용하여 원하는 element의 클래스 명을 통해 결과를 얻는다.

     - ```
       기사의 소속 뉴스 회사 이름만 추출하기
       >>>response.css('.writing::text').extract()
       ```

     - 회사 이름을 나타내는 element의 클래스 명은 모두 writing이므로 이를 입력한다.

     - ```
       기사의 내용 미리보기만 추출하기
       >>>response.css('.lede::text').extract()
       ```

     - 다른 원하는 내용이 있는 경우 html 파일에서 class 이름을 참조하면 된다.





### Xpath 패턴 생성하는 법

> 네이버 뉴스 페이지의 기사 제목들을 Xpath를 이용해 한꺼번에 추출하기 위한 패턴 생성

- 웹페이지의 여러 뉴스 기사들의 Xpath를 복사하여 패턴을 분석한다.

- ```
  - 첫번째 페이지 기사 제목
  //*[@id="main_content"]/div[2]/ul[1]/li[1]/dl/dt[2]/a
  
  //*[@id="main_content"]/div[2]/ul[1]/li[2]/dl/dt[2]/a
  
  //*[@id="main_content"]/div[2]/ul[1]/li[3]/dl/dt[2]/a
  
  //*[@id="main_content"]/div[2]/ul[1]/li[10]/dl/dt[2]/a
  
  //*[@id="main_content"]/div[2]/ul[2]/li[1]/dl/dt[2]/a
  
  //*[@id="main_content"]/div[2]/ul[2]/li[3]/dl/dt[2]/a
  
  //*[@id="main_content"]/div[2]/ul[2]/li[10]/dl/dt[2]/a
  ```

- Xpath는 기사의 개수에 따라 li[n]값이 1씩 증가한다.

- 기사의 개수가 10개를 넘어가면 ul[2]이 되고 li[10]은 li[1]로 바뀜.

- 즉, Xpath의 ul과 li 값만 변화한다.

- ```
  기사제목의 Xpath 패턴
  //*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a
  ```

- 이 패턴을 입력하면 해당 페이지의 모든 뉴스 기사 제목을 추출할 수 있다.





### 전달 파라미터

> 추가 정보

```
https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230

https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=230&sid1=105&date=20210119&page=2

https://news.naver.com/main/list.nhn?mode=LS2D&sid2=230&sid1=105&mid=shm&date=20210119&page=3
```

- ? 뒤의 정보가 의미하는 것 : 서버에 전달되는 파라미터의 정보(전달 파라미터)

- ? 앞의 정보가 의미하는 것 : 서버 주소에 대한 정보

- 전달 파라미터 (key) = (value)

- ```
  mode = LS2D
  mid = shm
  sid1 = 105
  sid2 = 230
  ```



