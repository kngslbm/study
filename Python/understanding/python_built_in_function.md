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
