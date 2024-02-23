
## pprint

pprint 는 "pretty-print" 의 약자로 말그대로 보기좋은 결과를 출력해주는 모듈이다.

주로 대규모 데이터나 리스트, 딕셔너리가 중첩된 구조를 가진 데이터를 확인할 떄 사용되며,

여러 출력 형식 옵션을 제공한다.

```py
from pprint import pprint

data = {
    'name': 'John',
    'age': 30,
    'languages': ['Python', 'JavaScript', 'Java'],
    'address': {
        'city': 'New York',
        'zipcode': '10001'
    }
}


pprint.pprint(data)

# 출력
# {'address': {'city': 'New York', 'zipcode': '10001'},
#  'age': 30,
#  'languages': ['Python', 'JavaScript', 'Java'],
#  'name': 'John'}
```

---

## random

random 은 python 의 표준 라이브러리 중 하나로 난수를 생성하고 무작위성을 활용할 수 있게 해준다.

```py
import random

result = random.random()         # 0 ~ 1 사이 실수 난수를 생성한다. (균일 분포라는 개념도 있다.)
result2 = random.randint(a, b)   # a ~ b 사이 정수 난수를 생성한다. (엄밀히 따지면 완전히 균일한 분포가 아니다.)
result3 = random.choice(seq)     # seq 에서 무작위로 항목을 선택한다.
result4 = random.shuffle(seq)    # seq 의 항목을 무작위로 뒤섞는다.
```

random 모듈은 그 외에도 난수 시퀸스를 통제하고 통계를 분석하는 등의 기능을 제공하니,

이후 필요에 따라 추가적인 학습이 필요하다.

---

## time

time 모듈은 python 에서 시간을 처리하는데 사용되는 표준 라이브러리이다.

```py
import random

time.time():       #현재 시각을 유닉스 타임스탬프로 반환한다.
time.monotonic()  # 시스템 부팅 이후 경과된 시간을 반환한다
time.sleep(n)     # n초 동안 코드의 실행을 잠시 멈추고 잠들게 한다.
time.alarm(n)     # n초 후 알람을 설정한다.
```
활용 예시 하나로 아래와 같이 코드실행시간을 구해 코드 개선에 활용할 수 있다.
```py
import time

start_time = time.time() # 현재 시각 저장

time.sleep(1) # 1초간 대기

end_time = time.time() # 함수 종료 시점 시각 저장

print(f"코드 실행 시간 : {end_time-start_time:.5f}")
# 코드가 종료된 시각 - 코드가 시작된 시각으로 실행 시간을 구할 수도 있다. (단위 : 초)
# :.5f 는 소수점 이후 5자리까지 표시하는 포맷팅
```


---

## datetime

datetime 은 다양한 날짜/시간 관련 작업을 수행하는 기능을 제공한다.

python 의 표준 라이브러리이다.

```py
from datetime import datetime

datetime.now()   # 현재 날짜와 시간을 datetime 객체로 생성. 
datetime.strptime(string, format)   # string 을 datetime 객체로 변환
datetime.strftime(datetime, format)   # datetime 객체를 string 으로 변환

# str > datetime 변환 예시
str_datetime = "24/02/21 11:15"
datetime_datetime = datetime.strptime(str_datetime, "%y/%m/%d %H:%M") 

```
timedelta 객체를 활용하여 두 시각 사이의 시간간격을 활용할 수도 있다.

timedelta 객체는 datetime 모듈에서 제공하는 두 시각 사이 시간간격을 표현하는 강력한 도구이다.

```py
from datetime import datetime, timedelta

datetime.timedelta(days, seconds, microseconds)   #timedelta 객체를 생성

# 활용 예시, 3일 전 날짜 구하기
three_days_ago = datetime.now() - timedelta(days=3)
print(three_days_ago) 
```
datetime 객체와 timedelta 객체는 불변 객체이기 때문에 객체 생성 후 값을 변경할 수 없다.

---

## itertools

itertools 는 'iterator' 를 만들고 다루는데 유용한 기능을 제공하는 python 의 표준 라이브러리이다.

'iterator' 는 루핑에 있어 효율적인 작업을 수행하며 메모리를 절약하는데 도움을 준다.

'데카르트곱' 을 구하는 예시 코드는 아래와 같다.

```py
from itertools import product 

sample1 = ["A", "B", "C", "D", "E"]
sample2 = [1, 2, 3, 4]

# product 함수는 여러개의 iterable 을 받아 가능한 모든 조합을 반환한다.
# 행 / 열을 구분하는 방법으로 enumerate 가 사용된다.
# enumerate 로 각 조합의 index 와 요소를 구한다. 이때 index 의 시작을 1로 한다.
for i, v in enumerate(product(sample1, sample2), 1):
    print(v, end=" ")   # 각 요소를 출력할 때 줄바꿈을 하지 않고 공백을 넣는다.
    if i % len(sample2) == 0:   # index 를 'sample2 의 길이'(4)로 나누어서 0 일 경우,
        print("")               # 그러니까 sample2 의 길이마다 새롭게 공백을 추가(줄바꿈 됨).

# result output
"""
('A', 1) ('A', 2) ('A', 3) ('A', 4) 
('B', 1) ('B', 2) ('B', 3) ('B', 4) 
('C', 1) ('C', 2) ('C', 3) ('C', 4) 
('D', 1) ('D', 2) ('D', 3) ('D', 4) 
('E', 1) ('E', 2) ('E', 3) ('E', 4) 
"""
```

순열을 구하는 예시 코드는 아래와 같다.

```py
from itertools import permutations

sample = ["A", "B", "C"]

# permutations 함수는 주어진 iterable 객체의 가능한 모든 순열을 반환한다.
for i in permutations(sample): # permutations(iterable, r) 와 같은 구조를 갖는다.
    print(i)                   # 'r' 은 생성할 순열의 길이이며, 기본값은 모든 요소를 갯수이다.) 

# result output
"""
('A', 'B', 'C')
('A', 'C', 'B')
('B', 'A', 'C')
('B', 'C', 'A')
('C', 'A', 'B')
('C', 'B', 'A')
"""
```

조합을 구하는 예시 코드는 아래와 같다.

```py
from itertools import combinations

sample = ["A", "B", "C"]

# combinations 함수는 전달받은 iterable 객체의 가능한 모든 조합을 반환한다.
for i in combinations(sample, 2):   # combinations(iterable, r) 과 같은 구조를 갖는다.
    print(i)                        # r 은 하나의 조합에 사용될 요소의 갯수이다. 

# result output
"""
('A', 'B')
('A', 'C')
('B', 'C')
"""
```

중복을 허용한 조합을 구할 수도 있다.

```py
from itertools import combinations_with_replacement

sample = ["A", "B", "C"]

# combinations_with_replacement 함수는 중복을 허용한 모든 가능한 조합을 반환한다.
for i in combinations_with_replacement(sample, 3):
    print(i)

# result output
"""
('A', 'A', 'A')
('A', 'A', 'B')
('A', 'A', 'C')
('A', 'B', 'B')
('A', 'B', 'C')
('A', 'C', 'C')
('B', 'B', 'B')
('B', 'B', 'C')
('B', 'C', 'C')
('C', 'C', 'C')
"""
```

---

## requests

requests 는 HTTP 요청을 보내는데 사용되는 라이브러리 입니다.

HTTP 요청을 보내고 응답을 처리하는데 간편하고 효율적이며,

그 외에도 여러 장점들로 python 표준 라이브러리인 'urllib' 보다 많은 사용자들에게 선호된다.

requests 는 다양한 HTTP method (GET, POST, PUT, DELETE 등) 를 지원한다.

서버로 부터 받은 응답은 'Response' 객체에 담겨 헤더, 본문, status code 등의 정보를 쉽게 엑세스 할 수 있다.

아래는 request 를 사용한 GET 요청 예시 코드이다.

```py
import requests   # requests 를 사용하기 위해선 pip install 이 우선적으로 이뤄져야 한다.
from pprint import pprint   # 응답을 정리해서 출력하기 위해 pprint 사용   

# 통신 할 base url 지정, 여기선 http 통신을 테스트 할 수 있는 웹사이트를 사용했다.
url = "https://jsonplaceholder.typicode.com/"

# url/users/1 경로에 get 요청
r = requests.get(f"{url}users/1")

pprint({
    "contents": r.text,     # 요청에 대해 응답받은 'Response' 객체의  text 정보를 엑세스
    "status_code": r.status_code,   # 요청에 대해 응답받은 'Response' 객체의 status code 정보를 엑세스
})

# result output (json 형태로 응답)
"""
{'contents': '{\n'
             '  "id": 1,\n'
             '  "name": "Leanne Graham",\n'
             '  "username": "Bret",\n'
             '  "email": "Sincere@april.biz",\n'
             '  "address": {\n'
             '    "street": "Kulas Light",\n'
             '    "suite": "Apt. 556",\n'
             '    "city": "Gwenborough",\n'
             '    "zipcode": "92998-3874",\n'
             '    "geo": {\n'
             '      "lat": "-37.3159",\n'
             '      "lng": "81.1496"\n'
             '    }\n'
             '  },\n'
             '  "phone": "1-770-736-8031 x56442",\n'
             '  "website": "hildegard.org",\n'
             '  "company": {\n'
             '    "name": "Romaguera-Crona",\n'
             '    "catchPhrase": "Multi-layered client-server neural-net",\n'
             '    "bs": "harness real-time e-markets"\n'
             '  }\n'
             '}',
 'status_code': 200}
"""
```
아래는 request 를 사용한 POST 요청 예시 코드이다.

```py
import requests   # requests 를 사용하기 위해선 pip install 이 우선적으로 이뤄져야 한다.
from pprint import pprint   # 응답을 정리해서 출력하기 위해 pprint 사용   

# 통신 할 base url 지정, 여기선 http 통신을 테스트 할 수 있는 웹사이트를 사용했다.
url = "https://jsonplaceholder.typicode.com/"

# 데이터 생성에 사용될 값 지정
data = {
    "name": "sparta",
    "email": "sparta@test.com",
    "phone": "010-0000-0000",
}


# url/users 경로에 data를 담아 post 요청
r = requests.post(f"{url}users", data=data)

pprint({
    "contents": r.text,
    "status_code": r.status_code,
})

# result output
"""
{'contents': '{\n'
             '  "name": "sparta",\n'
             '  "email": "sparta@test.com",\n'
             '  "phone": "010-0000-0000",\n'
             '  "id": 11\n'  # 요청하지 않은 정보가 포함되었다? = id 는 서버에서 부여하는 값. 
             '}',
 'status_code': 201}
"""
```

---

## json

json 모듈은 python 에서 json 형식의 데이터를 처리하기 위한 내장 모듈이다.

json 데이터(string)를 python 객체(dictionary)로 변환하거나 그 반대의 경우에 사용된다.

주요 함수와 method 예시는 아래와 같다.

```py
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
python_dict = json.loads(json_string)   # json.load 함수는 'json string' 을 'dictionary' 로 변환한다.
print(type(python_dict))   

# result output
"""
<class 'dict'>
"""
```
```py
import json

python_dict = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(python_dict)   # json.dumps 함수는 'dictionary' 을 'json string' 로 변환한다.
print(type(json_string))

# result output
"""
<class 'str'>
"""
```

---

## csv

csv 모듈은 python 에서 csv 형식의 데이터를 처리하기 위한 내장 모듈이다.

csv 데이터(string)를 읽고 쓰는데 사용된다.

csv 데이터를 list 로 변환하여 읽기 위한 코드 예시는 아래와 같다.

```py
import csv

# 경로와 파일을 지정하여 변수에 담는다. 
# 작업중이 파일과 같은 디렉토리의 파일은 경로를 지정하지 않고 파일명만 써도 된다.
csv_path = "C:/Users/강슬범/Desktop/github/study/Python/practice/data_for_practice_csv.csv"

# csv를 list 자료형으로 읽기
csv_file = open(csv_path, "r", encoding="utf-8") # open 함수 읽기 mode 로 파일을 연다.
csv_data = csv.reader(csv_file)   # csv.reader 함수는 각 행을 파싱하여 'list의 list' 로 반환한다.

for i in csv_data:
    print(i)

# 작업이 끝난 csv 파일을 닫는다.
csv_file.close()

# result output
"""
['email', ' age', ' name', ' city']
['sb@email.com', ' 1998', ' sb', ' seoul']
['mehtap@email.com', ' 1997', ' mehtap', ' seoul']
"""
```

csv 데이터를 dictionary 로 변환하여 읽기 위한 코드 예시는 아래와 같다.

```py
import csv

csv_path = "C:/Users/강슬범/Desktop/github/study/Python/practice/data_for_practice_csv.csv"

# csv를 dict 자료형으로 읽기
csv_file = open(csv_path, "r", encoding="utf-8") # open 함수 읽기 mode 로 파일을 연다.
csv_data = csv.DictReader(csv_file) # csv.DictReader class 는 각 행을 파싱하여 dictionary 로 반환한다.

for i in csv_data:
    print(i)

csv_file.close()

# result output
"""
{'email': 'sb@email.com', ' age': ' 1998', ' name': ' sb', ' city': ' seoul'}
{'email': 'mehtap@email.com', ' age': ' 1997', ' name': ' mehtap', ' city': ' seoul'}
"""
```

csv 파일에 데이터를 쓰기 위한 코드 예시는 아래와 같다.
```py
import csv

csv_path = "C:/Users/강슬범/Desktop/github/study/Python/practice/data_for_practice_csv.csv"

# csv 파일을 쓸 때는 newline='' 옵션을 지정해야 중간에 공백 라인이 생기는 것을 방지할 수 있다.
csv_file = open(csv_path, "a", encoding="utf-8", newline='')
csv_writer = csv.writer(csv_file)   # csv.writer 함수는 한번에 여러 행을 쓴다. 이때 데이터는 list 나 tuple 로 제공해야 한다.

csv_writer.writerow(["yasemin@email.com", '1993', "yasemin", "basel"]) # csv.writerow 는 한번에 한 행만 쓴다.
csv_writer.writerow(["ruki@email.com", '2003', "ruki", "basel"])

csv_file.close()

# 다시 csv 파일을 열어 읽어보면
csv_file = open(csv_path, "r", encoding="utf-8")
csv_data = csv.reader(csv_file)
for i in csv_data:
    print(i)

csv_file.close()

# result output
"""
['email', ' age', ' name', ' city']
['sb@email.com', ' 1998', ' sb', ' seoul']
['mehtap@email.com', ' 1997', ' mehtap', ' seoul']
['yasemin@email.com', '1993', 'yasemin', 'basel']   # 추가 된 행
['ruki@email.com', '2003', 'ruki', 'basel']         # 추가 된 행
"""
```