### Django Project

1. django 설치

   - ```
     pip install django 또는 conda install django
     ```

2. django 버전 확인

   - ```
     django-admin --version
     ```

   - ```
     또는 python shell에서
     >>>import django
     >>>django.VERSION
     ```

3. 프로젝트 생성

   - ```
     django-admin startproject project_name
     ```

4. 마이그레이션

   - ```
     python manage.py migrate
     ```

5. superuser 생성

   - ```
     python manage.py createsuperuser
     ```

6. 어플리케이션 생성

   - ```
     python manage.py startapp app_name
     ```

7. 마이그레이션 생성

   - ```
     python manage.py makemigrations
     ```

8. 서버 작동

   - ```
     python manage.py runserver 호스트번호(없을시 자동 8000)
     ```



### 프로젝트 진행

- Urlresolver
   - 웹서버에 요청이 오면 장고로 전달되고 장고가 웹 페이지의 주소를 가져와 무엇을 할지 확인
   - 각 URL에 대해 일일이 확인하기는 비효율적이므로 패턴으로 일치여부 판단
   - 일치하는 패턴의 경우 요청을 연관된 함수(view)에 넘김

  	* postman이 Urlresolver이다.



- MTV 코딩 순서 : project 생성 -> model 생성 -> url conf 생성 -> view 생성 -> template 생성

  

- settings.py
	
	- DB설정 - default: sqlite3
	- 템플릿 항목 설정
	- 정적파일항목설정 - STATIC_URL 등 관련 항목 지정
	- 어플리케이션 등록 - 프로젝트에 포함된 모든 어플리케이션등록
- 타임존 지정 - UTC 변경(한국)
	
	
	
- models.py
	
	- 테이블 정의
	- ORM - 테이블을 클래스로 매핑하여 CRUD 기능을 클래스 객체에 대해 수행, DB에 반영
	- 테이블을 클래스, 테이블의 칼럼은 클래스 변수로 매핑 - django.db.models.Model 클래스 상속
- models.py에서 DB변경 시 이를 실제DB에 반영 - django 1.7부터 migration 기능 사용(makemigrations,migrate etc..)
	
	
	
- urls.py
	
	- URL과 View 매핑
	- 프로젝트 URL과 App URL로 구성하는것 추천
- {% url %} 탬플릿 태그 사용
	
	
	
- views.py
	
	- 뷰 로직 생성
- 함수 또는 클래스로 생성 가능
	
	
	
- templates
	
	- 웹 화면(페이지) 별로 탬플릿 파일(*.html)필요
- TEMPLATES 설정의 DIR 항목에 지정된 디렉토리에 앱 탬플릿 파일 저장
	
	
	
- admin
	
	- 테이블 내용을 열람하고 수정하는 기능 제공하는 사이트
	- user 및 group 테이블 관리 - settings.py에 django.contrib.auth 어플리케이션 등록
	- 사용자가 비즈니스 로직 개발에 필요한 테이블 관리(CRUD)

API vs Framework vs Platform vs Library???



### Database

> Sqlite3

- ```
  $ python manage.py dbshell
  ```

- ```
  $ .table
  ```

  - DB에 있는 테이블 보여줌

  
  
- ```
  $ select * from bookmarkap_bookmark;
  ```

  - bookmarkap_bookmark의 모든 데이터를 선택하여 보여줌

  
  
-  ```
  $ PRAGMA table_info(bookmarkap_bookmark);
  ```

  - bookmarkap_bookmark 테이블의 정보를 보여줌(PRAGMA 해야함)

  
  
- ```
  $ select * from bookmarkap_bookmark where id = 1
  ```

  - id가 1인 bookmarkap_bookmark 데이터를 선택함

  
  
- ```
  $ select id, modify_date from blog_posts;
  ```

  - blog_posts의 정보들 중 id와 modify_date만 보여줌

  
  
- ```
  $ update blog_posts set modify_date=datetime(modify_date,'-3 month') where id=1;
  ```

  - blog_posts의 id=1인 데이터의 modify_date를 현재 날짜보다 3달 앞당긴 날짜로 바꿈
  
  

- ```
  $ delete from user;
  ```

  - user의 모든 데이터 삭제



- ```
  $ delete from user where 조건식;
  ```

  - 조건식을 만족하는 user의 데이터만 삭제



- ```
  $ alter table old_name rename to new_name;
  ```

  - table 이름을 기존의 old_name 에서 new_name으로 바꾸기



- ```
  $ create table table_name (column1, column2, ...);
  ```

  - 이름과 컬럼을 지정하여 새 table 만들기