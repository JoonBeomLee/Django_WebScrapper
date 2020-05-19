# Python Django Web Scraper
노마드코더) Python Django 연습 Web Scraper 제작

# Module 1 
    - Python 이론

# 1-0 Data Types of Python
    - string
    - boolean(True | False)
    - int 
    - float
    - None (=Null)
    - 변수 선언 snake case 방식 사용 ex)a_test

# 1-1 List in Python
    - list [a, b, c]
    - mutable sequence 값 수정 가능

# 1-2 Tuples and Dicts
    - tuple (a, b, c)
    - immutable sequence 값 수정 불가능
    - dictionary {"a" : "test1", "b" : "test2"}
    - 다양한 타입 저장 가능

# 1-3 Built in Function
    - https://docs.python.org/3.7/library/index.html 참조

# 1-4 Creating a Your First Python Function
    - def function_name():  # 선언
    -     print("test")
    - function_name()       # 호출

# 1-5 Function Arguments
    - def function_test(a, b):      # 인자 전달
    - def function_test(a, b=0):    # 인자 default값 지정 가능

# 1-6 Returns
    - def function_test():
    -     a = "Test"
    -     return a
    -     a = "Test2"
    -                               # return 아래는 실행 x 
    - result = function_test()
    - print(result)                 # 함수에서 전달받은 "Test" 출력

# 1-8 Keyworded Arguments
    - def function_test(big, small):   
    -   return big / small
    - 
    - function_test(small=2, big=10)    # 인자 순서가 바뀌어도 선언된 인자명으로 매핑
    
# 1-10 Conditionals Part 1
    - if (CONDITION1):
    - elif (CONDITION2):                # elif = else if
    - else:

# 1-12 for in
    - for a in list:                # list값을 하나씩 조회 len(list) 만큼 수행
    -   print(a)                    # 하나씩 조회된 값 출력

# 1-13 Modules
    - import module_name                    # module 전체 호출
    - import module_name as module_name2    # module 이름 바꾸어 사용
    - from module_name import a, b          # module에서 a, b 함수만 호출

# Module 2
    - Building a Job Scrapper

# 2-0 What is Web Scrapping
    - 특정 페이지에서 원하는 값을 추출

# 2-1 What are We Building
    - StackOverFlow, Indeed 에서 구직데이터 추출
    - 데이터 추출 -> 엑셀로 저장

# 2-2 Navigating with Python
    - requests 모듈사용
    - result = requests.get(url)        # url내 데이터 전달
    - result.text                       # html 값

# 2-3 Extracting Indeed Pages
    - beautifulsoup 모듈사용             # html parsing 가능 
    - from bs4 import BeautifulSoup     # 호출 예시
    - bs4.find()                        # 특정 태그 검색

# 2-4 Extracting Indeed Pages part 2
    - bs4.string()                      # 태그내 문자열만 반환

# 2-5 Requesting Each Page
    - range(n)                          # 0 ~ n

# 2-6 Extracting Titles
    - bs4.find("tag", {"요소" : "요소명"})  # 타겟의 요소별 결과값 반환

# 2-7 Extracting Companies
    - html 분석을 통해 대상의 규칙을 파악
    - 분석한 요소를 통해 타겟 추출
    - str.strip("target")                  # str내 target 제거 | () 공백 제거 

# 2-8 Extracting Locations and Finishing up
    - div 태그 내 Location 값을 가진 Class값을 통해 Location 반환
    - div 태그 내 JobId 값을 가진 Class값을 통해 JobId 반환 
    - 추후 url로 참조시 사용

# 2-9 StackOverFlow Pages
    - getPages -> getRequest -> getTarget

# 2-10 StackOverFlow Extract Jobs
    - bs4.get_text(strip=true)          # 태그내 텍스트 반환 후 공백제거

# 2-11 StackOverFlow Extract Job part 1
    - bs4.find_all("target", recursive=False)            # 요소내 Target 전체 반환 | recursive=False target만 반환

# 2-12 StackOverFlow Extract Job part 2
    - "\n" | "\r"                      # 둘다 개행 문자

# 2-13 StackOverFlow Finish
    - 코드 정리

# 2-14 What is CSV
    - CSV (Comma Separated Values)
    - import CSV                      # csv 모듈 사용

# 2-15 Saving to CSV
    - open("fileName", mode="r|w|a")    # 파일 오픈      
    - csv. writerow("")                 # csv파일에 row 작성  
    - dict.values()                     # dictionary 값 반환
    - list(dict)                        # dict -> list 형 변환 가능

# 2-16 OMG This is Awesome
    - 코드정리

# Module 3 
    - Get Read for Django

# 3-0 Django is AWESOME
    - Django = Python 웹 프레임워크

# 3-1 *args **kwargs
    - function(*args)           # 인자 복수 전달 가능
    - function(**kewargs)       # keyword 인자 전달 가능 ex) function(a1="Asd", b1="Bsd")

# 3-2 Intro to Object Oriented Programming
    - class class_name():           # class 정의
    - class_test = class_name()     # class 선언

# 3-3 Methods part 1
    - class class_name():
    -   test_var = "test"
    -   def method1(self):              # self인자 전달 필요
    -       print(self.test_var)        # 전달 받은 self의 변수 참조 가능
    -
    - test = class_name
    - test.method1()                    # test가 method1의 self로 전달

# 3-4 Methods part 2
    - dir(class)                                            # class 내부 출력
    -
    - def __init__(self, *args, **kwargs):                  # 생성자 | class_name(args=1...)으로 호출 가능
    -   self.args1 = kwargs.get("args1", "default_value")   # args1을 전달 | 없을 경우 초기화될 기본 값 지정 가능

# 3-5 Extending Classes
    - class parents():                                          # 부모 클래스
    -   args = "parents"
    -   def __init__(self, **kwargs):
    -       p_args1 = kwargs.("args1", "parents' args1")
    -   
    - class child(parents)                                      # 부모 클래스 ->(상속) 자식 클래스 || parents, ... 다중 상속 가능
    -   def __init__(self, **kwargs):                           # 부모 클래스내 생성자 참조
    -       suepr().__init__(**kwargs)                          # 부모 클래스에 정의된 변수 참조 가능 | 없을 때 참조시 에러 발생
    -   
    -   def check(self):
    -       print(self.args)                                    # 부모 클래스에 있는 args1="parents" 값 출력
    -
    - child1 = child()  
    - print(child1.p_args1)                                     # 생성자 상속 안되있으면 오류 발생

# Module 4
    - 2020 Bonus Class

# 4-0 Welcome to 2020 Update
    - Flask 활요한 웹 페이지 제작

# 4-1 Introduction to Flask
    - from flask import Flask               # Flask 모듈 사용
    -
    - app = Flask("title")                  # Web Page 선언 ("title") 페이지 명
    - @app.route("dir")                     # route("dir") = dir 로 접근시
    - def target():                         # @바로 아래 함수 호출
    -   return "Asd"     
    -
    - app.run(host="localhost")             # 정의된 app을 실행         

# 4-2 Dynamic URLs and Templates   
    - @app.route("/<var_name>")             # url로 전달 받은 경로 사용 가능
    - def function(var_name):
    -   return f."Welcome {var_name}"       # 전달받은 변수 사용 가능
    -
    -
    - render_template("page_file")          # 출력할 페이지명 전달

# 4-3 Forms and Query Arguments  
    - import request                            # 페이지이동시 전달된 값 호출 가능
    - url = "test.com/args_input?args1=test     # get방식으로 전달된 args1
    - request.args.get("args1")                 # 변수 명으로 접근
    -
    - render_template("page", args1="test")     # 위의 url과 같은 값으로 인자 전달
    - <h1>{{args1}}<h1>                         # {{args_name}} 을 통해 호출 가능

# 4-4 Scrapper Integration
    - import redirect
    - redirect("url")                           # 해당 페이지로 이동 

# 4-5 Faster Scrapper       
    - 검색결과 DB에 저장하여 같은 키워드 검색시 DB참조를 통해 시간 단축

# 4-6 Rendring Jobs!
    - {% %}                 # html내에서 python 코드 작성 가능
    - {{ }}                 # 변수 출력만 가능
