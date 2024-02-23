
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

