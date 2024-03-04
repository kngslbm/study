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
