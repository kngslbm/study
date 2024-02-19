## enumerate

enumerate 는 반복가능한 객체를 받아 요소와 인덱스를 함께 반환할 수 있다.

주로 for 문과 같이 쓰인다.

[1,2,3,4,5] 가 담긴 리스트의 요소와 인덱스 값을 반복문으로 가져오면 아래와 같다.

```py
numbers[1,2,3,4,5]

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
