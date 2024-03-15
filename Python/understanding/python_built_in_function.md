## zip

zip 은 여러 반복가능한 객체를 병렬 순회할 수 있다.

여러개의 iterable 객체를 전달받아 각 객체에서 하나의 요소 씩 꺼내 여러 iterator 를 생성한다.

```py
for item1, item2 in zip(list1, list2):
```

## enumerate

enumerate 는 반복가능한 iterable 객체를 받아 iterator 를 반환한다.

이 때 각 반복은 요소와 인덱스를 튜플 형태로 함께 반환한다.

주로 for 문과 같이 쓰인다.

[1,2,3,4,5] 가 담긴 리스트의 요소와 인덱스 값을 반복문으로 가져오면 아래와 같다.

```py
numbers = [1,2,3,4,5]

for i, number in enumerate(numbers):    # for 인덱스,요소 in enumerate(반복가능객체, strart=0):
    print(number,[i])                   # start=0 : 인덱스 시작값을 설정한다. 기본값은 0 이다

   #result
   # 1 [0]
   # 2 [1]
   # 3 [2]
   # 4 [3]
   # 5 [4]
```
---

## divmod

divmod 는 두개의 숫자를 인자로 받아 몫과 나머지를 튜플로 반환한다.

```py
divmod(x, y)   # 기본형식. x 나누기 y 를 수행
```

---

## range

range 는 연속된 정수 시퀸스를 생성하는 함수이다.

주로 for 문과 같이 쓰인다.

range 함수는 리스트나 튜플을 반환하지 않고 range 객체를 반환한다. 

그렇기 때문에 list 함수를 통해 리스트로 변환할 수 있다.

```py
# 기본 형식 : range(시작숫자, 종료숫자, 증가량) 종료숫자는 필수 입력, 시작숫자 기본값=0, 증가량 기본값=1

# 0부터 9까지의 숫자를 출력
for i in range(10):
    print(i)

# 1부터 10까지의 숫자를 리스트로 생성
numbers = list(range(1, 11))

# 2부터 10까지 2씩 증가하는 숫자를 출력 (2,4,6,8)
for i in range(2, 10, 2):
    print(i)
```

---

## len

len 은 문자열의 글자 수 or 시퀸스 객체의 요소 갯수를 반환한다.

```py
# 기본 형식
len(string)     # 글자 수 반환
len(secuence)   # 요소 갯수 반환
```



---

## count

count 는 시퀸스 객체에서 특정 요소의 등장 횟수를 반환한다.

```py
secuence.count(특정요소)  # 기본 형식
```


---

## sort

sort 는 list의 Method 이다.

전달받은 리스트를 정렬한다. 기존의 리스트를 정렬하여 변경하기 때문에 따로 값을 반환하지 않는다.

```py
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# 리스트를 오름차순으로 정렬합니다.
numbers.sort()  # 기본값은 reverse=False
print(numbers)  # 출력: [1, 1, 2, 3, 4, 5, 5, 6, 9]

# 리스트를 내림차순으로 정렬합니다.
numbers.sort(reverse=True)
print(numbers)  # 출력: [9, 6, 5, 5, 4, 3, 2, 1, 1]
```
string 은 알파벳 순으로 정렬한다. 

sort 메서드의 시간복잡도는 O(n log n) 이다.

---

## sorted

sorted 는 반복가능한 객체를 전달받아 정렬된 리스트로 반환한다.

sort 와 달리 새로운 리스트를 반환하는 것이기 때문에 기존의 리스트는 그대로다.

```py
sorted(iterable, key=None, reverse=False)  # 기본구조 와 기본값
```
iterable: 정렬하려는 순서가 있는 데이터 (리스트, 튜플, 문자열 등)

key: 정렬 기준을 제공하는 함수. 기본값은 None이며, 이 경우에는 요소 자체를 기준으로 정렬.

reverse: 기본값은 False이며, 이 경우에는 오름차순으로 정렬. True로 설정하면 내림차순으로 정렬.

---

## index

index 는 list의 Method 이다.

전달받은 특정 요소의 index 값을 반환한다.

첫번 째로 일치하는 index 를 반환하며, 일치하지 않을 시 'ValueError' 를 발생시킨다.

```py
list.index(특정 요소)   # 기본 형식
```


---

## type

type 은 객체object의 자료형type/class을 반환한다.

```py
type(object) # type 함수 기본형식
```

```py
integer = 10
float_ = 1.23
string = "hello world"
list_ = [1, 2, 3]
tuple_ = (1, 2, 3)
set_ = {1, 2, 3}
dictionary = {"key": "value"}
boolean = True

print(type(integer)) # <class 'int'>
print(type(float_)) # <class 'float'>
print(type(string)) # <class 'str'>
print(type(list_)) # <class 'list'>
print(type(tuple_)) # <class 'tuple'>
print(type(set_)) # <class 'set'>
print(type(dictionary)) # <class 'dict'>
print(type(boolean)) # <class 'bool'>
```

---

## split

split 은 **문자열**string을 특정 **구분자**separator를 기준으로 나누어 **리스트**list로 반환한다.


```py
string.split(separator, maxsplit) # 기본 형식 

# separator 특정 구분자 기준으로 요소를 나눈다. 값을 지정하지 않으면 기본값은 공백을 기준으로 나눈다.
# maxsplit 은 최대 분할 횟수이다. 값을 지정하지 않은면 기본값 -1(모든 가능한 분할 수행)이 적용된다.
```

---

## [ : : ]

python 의 슬라이싱 연산자이다.

```py
[start:stop:step]   # 기본 형식
```
start: 슬라이싱을 시작할 위치. 이 위치의 요소는 포함되며 기본값은 처음(inedex 0).

stop: 슬라이싱을 끝낼 위치. 이 위치의 요소는 포함되지 않으며 기본값은 시퀀스의 끝.

step: 슬라이스의 간격. 기본값은 1.

<br>
[::-1] 로 요소를 뒤에서부터 반환할 수도 있다. 문자열도 가능하다

---

## *arguments ( 가변인자)

가변인자를 사용하면 함수에 여러개의 인자를 전달할 수 있다.

```py
print(*args)   # 전달받은 여러개의 인자를 공백으로 구분하여 출력.
```

```py
def greet(*args):
    for arg in args:
        print(args)

greet('가', '나', '다')
```


---

## replace

replace 는 문자열의 특정 부분을 다른 문자로 변경하여 새로운 문자열을 반환한다.

```py
string.replace(old, new, count)  # 기본 형식
```

old : new 로 변경할 부분

new : 변경할 문자

count : 대체할 최대 횟수. 기본값은 가능한 모든 경우를 대체

---

## join

join 은 **반복가능한 객체**iterable object를 하나의 **문자열**string 로 합쳐 반환한다.

```py
my_team = ["han", "shin", "kim", "kang"]

result = " and ".join(my_team)

print(result)   # 출력 : "han and shin and kim and kang"
```

join 은 **문자열 메서드**string method 이기 때문에 만약 대상이 되는 iterable object 의 요소들이 string 이 아니라면, 먼저 string 으로 변환해야 한다.
```py
numbers = [1, 2, 3, 4, 5]
result = ', '.join(map(str, numbers)) # map으로 nubers의 각 요소를 string으로 반환하고 join으로 결합.
print(result)  # '1, 2, 3, 4, 5'
```

---

## bool

bool 은 인자로 전달받은 값을 boolean 으로 변환한다.

```py
# False
print(bool(""))
print(bool(0))
print(bool([]))

# True
print(bool("sample"))
print(bool([1, 2]))
print(bool(1))
print(bool(-1))
```

---

## any & all

any 혹은 all 은 시퀸스의 값을 효율적으로 검사할 수 있다.


```py
예시 코드 작성 예정
```

---

## eval

eval 함수는 문자열로 표현된 python 표현식을 실행하고 결과값을 반환한다.

보안 취약점과 가독성 저하의 가능성 때문에 사용이 권장되진 않는다.

```py
result = eval(expression)  # 기본형식

eval("2+3") # = 5
```
