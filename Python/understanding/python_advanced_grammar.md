## 가상 환경 virtual environment

시스템의 기본 파이썬 설치와 별도로 독립적인 파이썬 환경을 만드는 기능이다.

파이썬에서 가상 환경을 만들어 작업하면 여러가지 이점이 있다.

1. **패키지 관리** : 격리된 환경에서 각 프로젝트마다 필요한 라이브러리와 패키지를 관리할 수 있다.

2. **개발 효율 향상** : 각 프로젝트 별로 맞춤화된 환경을 구축하여 개발의 효율을 높인다.
 
3. **공유 용이성** : 프로젝트 환경을 쉽게 복제하여 공유하고 협업할 수 있다.


<br>

가상 환경 생성 코드:
```
python -m venv (가상 환경 폴더명)
```
<br>

가상 환경 활성화 코드:
```
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

가상 환경 비활성화 코드 :
```
deactivate
```

<br>

가상 환경 삭제
```
rm -rf (가상 환경 폴더명)
```

<br>

## 코드 컨벤션 code convention

코드 컨벤션은 코드를 작성할 때 일관성 있고, 가독성이 좋도록 일정한 스타일로 작성하자는 지침이다.

언어마다 여러 스타일의 코드 컨벤션이 존재하며,

협업을 할 때 있어 프로젝트의 특성이나 개발팀의 선호도에 맞춰 코드 컨벤션을 정하고 준수하는 것이 매우 중요하다. 

일반적으로 아래와 같은 내용을 포함한다.

1. **들여쓰기** indentation : 보통 2개나 4개의 공백을 사용하며, 코드 블록과 구조를 파악하기위해 필요하다. 특히 Python 에서의 들여쓰기는 중요한 문법 요소이다.

2. **네이밍 컨벤션** naming convention : 변수, 함수, 클래스 등의 이름을 작성할 때 일정한 규칙을 따른다. Python 에서는 변수와 함수는 snake 표기법을, 클래스는 Paskal 표기법을 따른다. 또한 해당 코드의 의미를 직관적으로 알 수 있게 네이밍 해야한다.

3. **주석** comments : 주석은 코드의 동작, 목적, 중요 사항에 대하여 명확하고 간결하게 작성해야한다.

4. **공백** spacing : 코드 간에 일정한 띄어쓰기 규칙을 지켜야한다.

5. **문서화** documentation : 필요한 경우 코드의 기능과 사용방법을 명확하게 기술하여 다른 사람들이 코드를 이해하고 사용할 수 있도록 문서화 해야한다.

<br>

## 변수의 유효 범위 variable scope

변수는 선언된 위치나 키워드에 따라 사용할 수 있는 범위가 정해진다.

함수 내에서 선언되어 다른 함수에 영향을 주지 않는 변수를 "지역 변수 local variable" 라고 하고,

함수 밖에서 선언되어 어디서든 접근할 수 있는 변수를 "전역 변수 global variable" 라고 한다.



```py
def func_one():
    num = 9   # 함수 내에서 선언된 지역 변수

def func_two():
    print(num)   # func_one에서 선언한 지역 변수에 접근할 수 없다

func_two()   # 결과 : 오류
```

```py
num = 9   # 함수 밖에서 선언된 전역 변수 

def func():
    print(num)   # 전역변수에 자유롭게 접근 할 수 있다.

func()   # 9가 출력된다.
```
```py
num = 10   #전역 변수 선언

def func():
    num = 9  # 전역 변수와 같은 이름의 변수를 함수 내에서 지역 변수로 재선언
    print(num)   

func()       # 함수 내에서 변수를 재선언 할 경우 지역 변수로 간주.(9를 출력)
print(num)   # 하지만 함수 밖 전역 변수에는 영향이 없다.(10을 출력)
```

함수 내에서 전역 변수를 선언하는 방법도 있다.

```py
num = 10   # 함수 밖에서 선언된 전역 변수

def func():
    global num    # 함수 내에서 전역 변수를 선언하는 법 : global (변수명)
    num = 9       # 전역 변수 선언
    
func()    # 함수 실행, 전역 변수 재선언.

print(num)   # 9를 출력
```

주의, pyhton 을 포함한 많은 프로그래밍 언어에서 전역 변수의 남용은 권장되지 않는다.

코드가 길어질수록 전역 변수에서 선언된 값이 어디서 변경되었는지 추적이 어렵고,

그 만큼 문제 발생시 디버깅도 힘들어지기 때문이다.

<br>

## 조건문 심화

다양한 연산자를 통해 비교 결과를 **불리언** boolean 으로 반환하고,

경우에 따라 실행될 로직을 정의할 수 있다.

아래 몇가지 연산자의 예시가 있다.

```py
# "in 연산자"는 시퀸스에 값이 포함되어 있는지를 확인한다.
1 in (1, 2, 3) # True
4 in [1, 2, 3] # False


# 논리 연산자
if condition1 and condition2:  
    # 두 조건을 모두 만족할 경우
elif condition1 or condition2:   
    # 두 조건 중 하나라도 만족할 경우
elif not condition:   
    # 조건의 boolean 반전
else:   
    # elif 로 조건을 추가하고, 모든 조건에 해당하지 않을 때 else 를 실행
```
조건문을 잘 활용하기 위해서는 boolean 개념에 대한 이해가 필요한다.  
```py
# python 에서 False 로 간주하는 값들 (그 외의 모든 값은 True 로 간주한다.)
False
None
0
0.0 
"" # 빈 string
[] # 빈 list
{} # 빈 dictionary
set() # 빈 set
```
any 또는 all 함수를 활용하면, 여러 조건/요소를 포함한 시퀸스에 대해 최종적인 boolean 을 효율적으로 반환할 수 있다.
```py
# any 는 요소들 중 하나라도 True일 경우 True 를 반환
if any([False, False, False, True, False]):
    # True가 1개 이상 존재하기 때문에 True

# all 은 요소들이 모두 True일 경우 True 를 반환
if all([True, True, True, False, True]):
    # False가 존재하기 때문에 False
```

<br>

## 함수의 인자와 리턴 타입

함수를 잘 사용하기 위해서는

함수마다 어떤 type 의 인자를 받는지,

또 그렇게 전달받은 값을 다시 어떤 type 으로 리턴하는지, 처럼

함수의 정확한 기능과 올바른 사용법을 이해하는 것이 필수적이다.

아래에 예시 코드를 보면 "list 를 정렬한다"라는 같은 기능을 가진 것처럼 보이는 두 함수가 어떤 사용법 차이를 가졌는지 확인 할 수 있다.

```py
# sort 는 return data 없이 함수를 호출한 list 자체를 정렬한다
sample_list = [3, 2, 4, 1, 5]
sample_list.sort() 

print(sample_list) # [1, 2, 3, 4, 5]

# sorted
sample_list = [3, 2, 4, 1, 5]
sorted_list = sorted(sample_list) # 정렬 된 list를 return 한다.

print(sorted_list) # [1, 2, 3, 4, 5]

# 잘못된 방법
sample_list = [3, 2, 4, 1, 5]
sorted_list = sample_list.sort() # .sort()의 return data는 None 이다.

print(sorted_list) # None
```

<br>

무엇보다 함수를 잘 사용하기 위해서는

'docstring' 과 함수의 '구현부 코드'를 자주 들여다보며 함수에 대한 이해를 높이는 것이 중요하다.

<br>

## 패킹과 언패킹

패킹과 언패킹은 python 에서 데이터를 다룰 때 중요한 개념이다.

패킹은 말그대로 여러개의 데이터를 하나의 변수에 묶는 것을 말하며,

언패킹은 패킹된 데이터에서 개별 요소를 추출해 각각의 변수로 분리하는 것을 말한다.

```py
packed_tuple = 1, 2, 3, 4, 5  # 튜플 패킹 예시
packed_list = [1, 2, 3, 4, 5]  # 리스트 패킹 예시

a, b, c = (1, 2, 3) # 튜플 언패킹 예시
x, y, z = [4, 5, 6] # 리스트 언패킹 예시

x, y = y, x # 언패킹을 사용하여 변수 값 교환도 가능하다.
```

언패킹 시 유용한 연산자로 '*' 과 '**' 이 있는데, 각각 리스트와 튜플을 언패킹할 때 사용된다.

활용 예시는 아래와 같다.

```py
# 리스트 언패킹
my_list = [1, 2, 3, 4, 5]
a, *rest = my_list   # *rest : '*' 이후 모든 요소를 변수 rest에 담는다.
print(a)    # 1
print(rest) # [2, 3, 4, 5]

# 가변인자를 받을 떄도 사용된다.
def my_function(*args): 
    print(args) 

my_function(1,2,3,4,5)  # 출력 : (1,2,3,4,5)

# 딕셔너리 언패킹
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_new_dict = {'d': 4, **my_dict}
print(my_new_dict)  # {'d': 4, 'a': 1, 'b': 2, 'c': 3}

# 가변인자를 받을 떄도 사용된다.
def my_function(a, b, **kwargs):
    print(a)        # 1
    print(b)        # 2
    print(kwargs)   # {'c': 3, 'd': 4}

my_function(1, 2, c=3, d=4)
```

<br>

## class 개념 심화

python 에는 특별한 용도로 사용되는 메서드, __init__ 함수가 있다.

__init__ 메서드는 클래스 생성자로 새로운 인스턴스가 생성될 때 자동으로 호출되며,

생성된 객체의 상태를 초기화하고 매개변수를 전달해 초기 상태를  세팅해준다.

```py
#예제

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Person 클래스의 인스턴스 생성
person1 = Person("Alice", 30)

# person1의 속성 확인
print(person1.name)  # 출력: Alice
print(person1.age)   # 출력: 30
```

<br>

'상속'을 사용하면 class 코드를 더욱 모듈화하고 재사용성을 높일 수 있다. 

이때 기존 class 를 '부모'혹은 'super' class 라고 하고, 새로운 class 를 '자식'혹은 'sub' class 라고 한다.

```py
class Animal:                 # Animal 클래스 생성 (super class)
    def __init__(self, name): # 인스턴스 생성시 매개변수를 name에 전달해 초기 세팅을 해준다.
        self.name = name

    def speak(self):
        raise NotImplementedError  # sub calss 로 하여금 speak 메서드의 재정의를 강제하고 해당 코드를 직접적으로 사용하는 것을 방지한다.

class Dog(Animal):          # Animal 클래스를 상속받아 Dog 클래스 생성(sub class)
    def speak(self):        # 상속받은 speak 메서드 재정의 (기존 __init__ 메서드는 유지)
        print("멍멍")

class Cat(Animal):          # Animal 클래스를 상속받아 Cat 클래스 생성(sub class)
    def speak(self):        # 상속받은 speak 메서드 재정의 (기존 __init__ 메서드는 유지)
        print("야옹")

dog1 = Dog('멍멍이')
cat1 = Cat('야옹이')

dog1.speak()  # 출력 : 멍멍
cat1.speak()  # 출력 : 야옹
```

<br>

## 정규표현식 Regular Expression (regex)

정규표현식은 문자열의 일정한 패턴을 표현하기 위한 일종의 형식언어이다.

python 에서 정규표현식을 활용해 다양한 작업을 수행할 수 있다.

정규표현식에서 특수한 의미를 가지는 글자를 '메타문자'라고 한다.

예를 들어 휴대전화번호를 입력받는데 입력된 번호가 정확한지 정규표현식을 사용하여 확인하면 아래와 같다.

```py
import re   #'re' 모듈을 통해 정규표현식을 지원한다.

def valid_phone_number(phone_number):
    # re.compile 함수로 정규표현식 패턴을 컴파일하여 패턴 객체 생성
    pattern = re.compile(r'^\d{3}-\d{4}-\d{4}$')

    if pattern.match(phone_number):
        print("올바른 전화번호 형식입니다.")
    else:
        print("잘못된 전화번호 형식입니다.")

def main():
    phone_number = input("전화번호를 입력하세요 (예: 010-1234-5678): ")
    valid_phone_number(phone_number)

if __name__ == "__main__":
    main()
```

정규표현식을 직접 작성하는 것은 매우 어렵고 힘든 일이다.

그렇기 때문에 미리 짜여진 정규표현식과 그것을 공유하는 커뮤니티가 활성화 되어있다.

필요한 정규표현식을 잘 찾아서 활용하는 것이 중요하다.

```py
# 그 외 re 모듈의 주요 함수
re.search(pattern, string)   # string 에서 pattern 과 일치하는 첫 번째 위치를 찾는다.
re.match(pattern, string)   # string 의 시작부터 pattern 과 일치하는지 확인한다.
re.findall(pattern, string)   # string 에서 pattern 과 일치하는 모든 부분을 찾는다.
re.sub(pattern, replacement, string)   #string 에서 pattern 과 일치하는 부분을 replacement 로 대체한다.
```














