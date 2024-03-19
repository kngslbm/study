## 조건문

if, elif, else 로 조건에 따른 동작을 지정할 수 있다.

elif 를 여러개 작성해 다양한 조건을 지정할 수도 있다.

```python
shirt=70
pants=80
set=100

money= ?

if money>=set:
    print("i'll buy a set.")
elif money>=pants:
    print("i'll buy a pants.")
elif money>=shirt:
    print("i'll buy a shirt.")
else:
    print("I don't have enough money.")
```

money 변수에 넣는 값에 따라 무엇을 살지 결정된다.

100 이상 = set

80이상 = pants

70이상 = shirt

70미만 = "i don't have enough money."

---

## 반복문(for)

for ~ if ~ :로 특정 동작을 반복할 수 있다.

```python
closet = ['shirt','pants','tie','belt','socks']

for clothes in closet:
    print(clothes)

#output
# shirt
# pants
# tie
# belt
# socks
```

리스트의 모든 요소를 한번씩 가져온다.

---

### 추가 연습

people 이라는 리스트에서 '20세 이상'만 출력하려면

```python
people = [
    {"name": "bob", "age": 20},
    {"name": "carry", "age": 38},
    {"name": "john", "age": 7},
    {"name": "smith", "age": 17},
    {"name": "ben", "age": 27},
    {"name": "bobby", "age": 57},
    {"name": "red", "age": 32},
    {"name": "queen", "age": 25}
]

for person in people:
    if person["age"] > 19 :
        print(person["name"])
```

for ~ in ~ 으로 people 리스트의 모든 값을 가져와 if 로 age 값이 19 보다 클 경우에 출력하는 조건을 건다.

앞에서부터 4명만 출력하려면.

```python
for i, person in enumerate(people):
    print(person["name"])
    if i==3:
        break
```

enumerate 로 객체의 인덱스를 구할 수 있다. 인덱스값이 i 가 [3] 이 되면 멈추게 한 코드이다.

break를 통해서 반복문을 멈출 수 있다.

아주 긴 반복문을 수정할 때 짧게 동작시켜보면서 효율적으로 작업할 수 있을 듯 하다.

---

### 추가 연습2

num_list 에서 짝수만 출력하려면

```python
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

for num in num_list :
    if num%2 == 0 :
        print(num)
```

for문으로 반복, if 로 (2로 나눈 나머지가 0일 때,) 짝수만 출력.

짝수의 갯수를 출력하려면

```python
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
cnt = 0
for num in num_list :
    if num%2 == 0 :
        cnt += 1
print(cnt)
```

cnt라는 변수를 만들고 조건이 맞을 때 1씩 +  해준다.

cnt를 출력한다.

리스트 전체의 합을 출력하려면

```python
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
sum = 0
for num in num_list :
    sum += num
print(sum)
```

변수 만들고 반복문에서 num만큼을 변수에 더하고, 변수 출력

가장 큰 수만 출력하려면

```python
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
biggest = 0
for num in num_list :
    if num > biggest :
        biggest = num
print(biggest)
```

변수 생성, 반복문에서 num 이 변수보다 크면 변수로 가리키고 변수 출력

---

## 함수

def ~ () 로 함수를 선언하다.

선언된 함수 속 미리 짜여진 동작을 언제든 실행 시킬 수 있다.

```python
def buy_clothes(money):
    if money>=set:
        print("i'll buy a set.")
    elif money>=pants:
        print("i'll buy a pants.")
    elif money>=shirt:
        print("i'll buy a shirt.")
    else:
        print("I don't have enough money.")

shirt=70
pants=80
set=100

buy_clothes(150)  #output i'll buy a set.
buy_clothes(70)   #output i'll buy a shirt.
buy_clothes(50)   #output I don't have enough money.
buy_clothes(85)   #output i'll buy a pants.
```

입력한 값에 따라 함수 내 미리 짜여진 조건문이 동작하여 알맞은 값을 출력한다.

---

셔츠를 구매하는 함수를 만들어 보면

```python
def buy_shirt(money):
    shirt = 70
    if money >= shirt:
        change = money - shirt
        print("change :",change)
        return change
    else:
        print("you don't have enough money")

buy_shirt(150) #output change : 80
buy_shirt(70)  #output change : 0
buy_shirt(50)  #output you don't have enough money
```

return 으로 함수를 통해 도출된 값을 돌려줄 수 있다.

거스름돈을 잘 걸러주는 걸 확인할 수 있다.

---

## 슬라이싱

슬라이싱은 시퀸스 객체의 일부를 추출할 떄 사용된다.

슬라이싱의 기본적인 형식은 [start:stop:step] 이다.

- start 는 슬라이싱을 시작하며 포함시킬 인덱스이다. 기본값은 0 이다.

- stop 은 포함시키지 않고 앞에서 슬라이싱을 멈출 인덱스이다. 기본값은 시퀸스의 길이이다.

- step 은 슬라이싱을 할 때 건너뛸 간격이다. 기본값은 1 이다.

주민등록번호를 입력하면 성별을 알려주는 함수를 만들어보면 아래와 같다.

```python
def check_gender(pin):
    gender = pin.split("-")[1][:1]
    if int(gender)%2 == 0:
        print("female")
    else:
        print("male")
check_gender("900101-2234567") # female
check_gender("200101-3012345") # male
```

함수 내 변수 gender 를 만들고, split 메서드로 주민등록번호를 앞뒤로 분할하고 리스트로 만든다.

분할된 리스트에서 뒷번호를 지정하고 슬라이싱을 활용하여 뒷번호 첫자리를 뽑아낸다.

조건문으로 알맞은 성별을 출력한다.

---

## 집합

set() 사용하여 리스트를 집합으로 만들 수 있다.

집합에서 중복된 요소는 없어진다.

~~chat GPT 한테 중복되는 요소가 있는 아무 리스트를 만들어 달라고 했다.~~

list 를 a 변수에 집합으로 만들고 a 를 출력하면 중복된 과일이 없어진다.

```python
list = ["apple", "banana", "orange", "grape", "kiwi", "kiwi", "melon", "strawberry", "banana", "grape"]
a = set(list)
print(a)

#output {'strawberry', 'grape', 'orange', 'apple', 'banana', 'kiwi', 'melon'}
```

---

~~chat GPT 한테 이번에는 두 개의 동물 리스트를 만들되, 두 리스트에 일부 중복되는 동물도 포함되도록 만들어 달라고 했다.~~

두 리스트의 교집합과 합집합을 구하려면,

set() 을 사용해 리스트를 집합으로 바꿔주고 집합연산을 사용한다.

```python
animal_list1 = ["lion", "tiger", "leopard", "cheetah", "elephant", "giraffe", "zebra"]
animal_list2 = ["elephant", "giraffe", "monkey", "snake", "kangaroo", "koala", "panda"]

a = set(animal_list1)
b = set(animal_list2)

print(a & b)
print(a | b)

#output
#{'giraffe', 'elephant'}
#{'tiger', 'giraffe', 'zebra', 'panda', 'koala', 'kangaroo', 'lion', 'elephant', 'monkey', 'cheetah', 'snake', 'leopard'}
```

---

animal_list1 에 대한 animal_list2 의 차집합을 구하려면

set을 사용해 두 리스트를 집합으로 만들고,

animal_list1 에서 animal_list2 를 빼준다.

```python
animal_list1 = ["lion", "tiger", "leopard", "cheetah", "elephant", "giraffe", "zebra"]
animal_list2 = ["elephant", "giraffe", "monkey", "snake", "kangaroo", "koala", "panda"]

cha = set(animal_list1) - set(animal_list2)

print(cha)

#output {'lion', 'leopard', 'cheetah', 'tiger', 'zebra'}
```

---

## f-string

f"~{}~" 으로 문자열 사이에 변수를 넣을 수 있다.

~chat GPT 한테 여러개의 딕셔너리로 이루어진 리스트를 만들어 달라고 했다.~

리스트에서 누가 몇살인지를 문자열로 출력하려고 할 때,

f-string 을 사용하면 보다 직관적이고 가독성이 좋게, 그리고 효율적으로 코드를 쓸 수 있다.

```python
dictionary_list = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "David", "age": 40, "city": "Houston"},
    {"name": "Eva", "age": 28, "city": "San Francisco"},
    {"name": "Frank", "age": 45, "city": "Seattle"},
    {"name": "Grace", "age": 33, "city": "Boston"}
]

for dic in dictionary_list:
    name = dic["name"]
    age = dic["age"]
    print(f"{name}is {age} years old")

#output
# Aliceis 30 years old
# Bobis 25 years old
# Charlieis 35 years old
# Davidis 40 years old
# Evais 28 years old
# Frankis 45 years old
# Graceis 33 years old
```

---

## try - except

try - except 를 사용하면 오류가 나도 멈추지 않고 이어가게 할 수 있다.

Eva 의 age 값을 없애면 오류가 나지만,

try - except 를 사용해 오류를 넘길 수 있다.

```python
dictionary_list = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "David", "age": 40, "city": "Houston"},
    {"name": "Eva", "city": "San Francisco"},
    {"name": "Frank", "age": 45, "city": "Seattle"},
    {"name": "Grace", "age": 33, "city": "Boston"}
]

for dic in dictionary_list:
    try:
        name = dic["name"]
        age = dic["age"]
        print(f"{name}is {age} years old")
    except:
        print(f"{name}'s age is unknown")

#output
# Aliceis 30 years old
# Bobis 25 years old
# Charlieis 35 years old
# Davidis 40 years old
# Eva's age is unknown
# Frankis 45 years old
# Graceis 33 years old
```

<br>
특정 에러를 지정하여 에러 종류에 따라 다른 로직으로 처리하는 것도 가능하다.

```py
# 각 변수 지정에 따른 발생 오류
number = 'a' # ValueError
---
number = 0   # ZeroDivisionError
---
number = '1' # Exception 

try:
    int(number)  
    10 / number   

except ValueError: # int로 변환하는 과정에서 에러가 발생했을 떄
    print(f"{number}은(는) 숫자가 아닙니다.")
    
except ZeroDivisionError: # 0으로 나누면서 에러가 발생했을 때
    print("0으로는 나눌수 없습니다.")
    
except Exception as e: # 위에서 정의하지 않은 에러가 발생했을 때(추적이 어려워 권장하지 않음)
    print(f"예상하지 못한 에러가 발생했습니다. error : {e}")

# except 문법 또한 if / elif 와 같이 연달아서 작성이 가능하다.
```

---

## 삼항연산자

python 에서 삼항연산자를 쓰면 두 세 줄의 코드를 한 줄로 줄일 수 있다.

```python
num = 5

if num % 2 == 0:
    result = "even num"
else:
    result = "odd num"

print(f"{num} is {result}")
```

num 의 값으로 들어온 숫자가 짝수인지 홀수인지를 알려주는 if 문을 삼항연산자로 쓰면

```python
num = 5

result = "even num" if num % 2 == 0 else "odd num"

print(f"{num} is {result}")
```

결과는 같다

---

list 안의 숫자들을 모두 두 배로 만들기 위한 반복문이다.

```python
list = [1, 4, 6, 7, 15, 27, 46]

listwice = []

for num in list:
    listwice.append(num*2)

print(listwice)
```

마찬가지로 for 문도 삼항연잔자로 쓰면 간단하게 쓸 수 있다.

```python
list = [1, 4, 6, 7, 15, 27, 46]

listwice = [ num*2 for num in list]

print(listwice)
```

## map 함수, lambda함수, filter함수

map() 함수는 주어진 함수에, 주어진 반복가능한 객체의 각 요소를 넣어 값을 돌려준다.

people 리스트 속 사람들을 나이에 따라 adult 와 kid 로 변환하는 코드이다.

```python
people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 15, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "David", "age": 40, "city": "Houston"},
    {"name": "Eva", "age": 18, "city": "San Francisco"},
    {"name": "Frank", "age": 45, "city": "Seattle"},
    {"name": "Grace", "age": 13, "city": "Boston"}
]

kidoradult = []

for person in people:
    if person["age"] < 20:
        result = "kid"
        kidoradult.append(result)
    else:
        result = "adult"
        kidoradult.append(result)

print(kidoradult)
```

map() 함수를 사용해 간단하게 만들어보면,

adult 와 kid 로 변환할 함수를 만들고 함수와 리스트(반복가능한 객체)를 준다.

이렇게 만들어진 map 함수를 list() 함수로 감싸 리스트 형태를 만들어 주면 잘 출력된다.

```python
def kidoradult(person):
    if person["age"] < 20:
        return "kid"
    else:
        return "adult"

result = list(map(kidoradult, people))

print(result)

#output ['adult', 'kid', 'adult', 'adult', 'kid', 'adult', 'kid']
```

if 문을 삼항연산자로 쓰면 더 간단해 진다.

```py
def kidoradult(person):
    return "kid" if person["age"] < 20 else "adult"

result = list(map(kidoradult, people))

print(result)

#output ['adult', 'kid', 'adult', 'adult', 'kid', 'adult', 'kid']
```

lambda 함수를 사용하면 더더욱 간단하게 쓸 수도 있다.

lambda 함수는 익명 함수를 만드는 방법으로, 이름이 없고 한 줄의 간단한 함수를 만들 때 사용된다.

보편적으로 변수는 x 로 지정하며, 형식은 ( x : 반환할 값 ) 이다.

```py
result = list(map(lambda x : "kid" if x["age"] < 20 else "adult", people))

print(result)

#output ['adult', 'kid', 'adult', 'adult', 'kid', 'adult', 'kid']
```

list 에서 kid 나 adult 만을 출력하려면 filter 함수를 사용하면 된다.

filter 함수는 주어진 함수에서 True 를 반환하는 요소 만을 데리고 새로운 이터레이터를 만든다.

필요한 요소만을 골라 처리할 떄 사용된다.

```py
result = list(filter(lambda x : x["age"] < 20, people))

print(result)

#output [{'name': 'Bob', 'age': 15, 'city': 'Los Angeles'}, {'name': 'Eva', 'age': 18, 'city': 'San Francisco'}, {'name': 'Grace', 'age': 13, 'city': 'Boston'}]
```

kid 로 분류됐던 age 가 20 미만인 사람들만 출력된다.

---

## 매개변수의 다양한 지정법

함수에 인수를 넣을 때, 몇 가지 방법으로 매개변수를 지정할 수 있다.

```py
def cal(a, b):
    return a + b*2

print(cal(2,3))

#output 8
```

위와 같은 함수에서 어떤 인수를, 어떤 매개변수에 넣을 지를 순서에 상관없이 특정할 수 있다.

```py
def cal(a, b):
    return a + b*2

print(cal(b=2,a=3))

#output 7
```

---

매개변수의 디폴트 값을 지정할 수도 있다.

```py
def cal(a, b=2):
    return a + b*2

print(cal(3))

#output 7
```

이때, 디폴트 값을 지정한 매개변수는 그렇지 않은 매개변수의 앞에 위치할 수 없다.

즉 왼쪽의 함수는 오류가 있는 함수이며 오른쪽과 같이 정의하는 것이 올바르다.

```py
def cal(a=3, b):                   def cal(b, a=3):
    return a + b*2                     return a + b*2


print(cal(2))                      print(cal(2))

#output error                      #output 7
```

---

매개변수의 갯수를 미리 정하지 않고 입력받은 인수를 모두 받을 수도 있다.
이때 통상적으로 args 를 쓴다.

```py
def greet(*args):
    for arg in args:
        print(f"{arg}, How are you?")

greet("james", "lebron", "stephen")

#output
# james, How are you?
# lebron, How are you?
# stephen, How are you?
```

키워드 인수를 받을 수도 있다.

```py
def greet(**kwargs):
    print(kwargs)

greet(first = "lebron", last = "james")
greet(first = "stephen", last = "curry")

#output
# {'first': 'lebron', 'last': 'james'}
# {'first': 'stephen', 'last': 'curry'}
```

---

## Class 와 Instance

class 는 객체를 만드는 템플릿이며, class 로 만들어진 실제 객체를 instance 라고 한다.

class 에는 속성과 메서드를 담을 수 있다.

속성은 객체의 상태를 나타내는 변수이고

메서드는 객체의 동작을 나타내는 함수이다.

예를 들어 "사람" 이라는 클래스를 만들고,

이름과 체력 같은 "속성"을 주고 걷기나 먹기 같은 "동작"을 줄 수 있다.

```py
class person:
    def __init__(self, name, stamina):
        self.name = name
        self.stamina = stamina

    def walk(self):
        self.stamina = self.stamina - 10
        print(f"{self.name} is walking")
        print(f"stamina : {self.stamina}")

    def eat(self):
        self.stamina = self.stamina + 10
        print(f"{self.name} is eating")
        print(f"stamina : {self.stamina}")

person1 = person("lebron", 100)
person2 = person("curry", 100)

person1.walk()
person2.eat()


#output
# lebron is walking
# stamina : 90
# curry is eating
# stamina : 110
```

## 그 외

문자열 순회하며 대소문자 여부 판별
```py
s = "Hello World"
upper_case_chars = []
lower_case_chars = []

for char in s:
    if char.isupper():
        upper_case_chars.append(char)
    elif char.islower():
        lower_case_chars.append(char)
```

---

문자열도 반복가능한객체이다. 글자마다 각각의 객체로 반복 가능.
예를 들어 map 함수를 활용한 아래와 같은 코드에서 문자열도 반복가능한 객체이기 때문에 모든 글자에 int 함수가 적용된다.
```py
num_str = "123456789"
sum(map(int, num_str))   # 각 숫자들을 합한 값 45 출력
```
