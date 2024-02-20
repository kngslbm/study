
## pprint

pprint 는 "pretty-print" 의 약자로 말그대로 보기좋은 결과를 출력해주는 모듈이다.

주로 대규모 데이터나 리스트, 딕셔너리가 중첩된 구조를 가진 데이터를 확인할 떄 사용되며,

여러 출력 형식 옵션을 제공한다.

```py
import pprint

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


## time


## datetime