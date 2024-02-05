## SELECT, FROM

SQL의 문법은 "어떤 테이블에서 어떤 데이터를 가져오는가" 가 핵심이다.

FROM 으로 데이터를 가져올 테이블을 지정하고

SELECT 로 어떤 칼럼을 가져올지 지정한다.

```sql
select 칼럼1, 칼럼2
from 테이블
```

---

\*을 사용하면 모든 칼럼을 가져올 수도 있다.

```sql
select *
from 테이블
```

---

컬럼을 가져올 때 별명을 지정하여 가져올 수도 있다.

칼럼명 뒤 한 칸을 띄우고 별명을 적어도 되고,

"칼럼명 as 별명" 의 형식도 가능하다.

영문과 언더바로 이루어진 별명 일 경우 그냥 작성이 가능하나,

한글과 특수문자가 포함될 때는 따옴표로 감싸주어야 한다.

```sql
select 칼럼1 nickname,
       칼럼2 as "별명"
from 테이블
```

---

## WHERE

WHERE 로 여러 조건을 지정하고 필터링하면 원하는 데이터만 가져올 수 있다.

같은 값 혹은 크고 작은 값을 가져오기 위해 비교연산자를 사용할 수 있다.

예를 들어 customers 라는 테이블에서 age 가 20보다 작은 데이터만 가져온다면 아래와 같다.

```sql
select *
from customers
where age<20
```

| 비교연산자 | 의미 |
| = | 같다 |
| <> | 같지 않다 (다르다) |
| >, < | 크다, 작다 |
| >=, <= | 크거나 같다, 작거나 같다 |

---

그 외에도 " between ", " in ", " like " 같은 다양한 필터가 존재한다.

각 필터의 조건은 아래와 같다.

between : a 와 b 사이

```sql
where age between 10 and 20
```

in : in() 안에 포함시킨 것만

```sql
where age in (15, 20, 35)
```

like : 완전히 일치하지 않아도 비슷한 것들

```sql
where name like "김%"   #"김"으로 시작하는 모든 데이터
```

```sql
where name like "%원"   #"원"으로 끝나는 모든 데이터
```

```sql
where name like "%민%"   #"민"이 포함된 모든 데이터
```

## 논리연산

여러 조건을 하나의 Query 문에 적용시킬 때 사용하는 연산이 논리연산이다.

논리연산의 종류에는 " AND " , " OR " ," NOT " 이 있다.

AND : 두 조건 모두 충족하는 데이터만

```sql
where age>20 and gender="female"   #20세 이상의 여성일 경우만
```

OR : 하나의 조건만 충족해도

```sql
where age>20 or gender="female"   #20세 이상이거나 여성일 경우만
```

NOT : 조건이 아닌 데이터만

```sql
where not gender="female"   #여성이 아닐 경우만
```

---

지금까지 SQL 의 문법 구조을 정리하면 아래와 같다.

```sql
select # "데이터 조회" 의 명령어로 필수 구문
from   # "어디에서 데이터를 조회할까" 의 명령어로 필수 구문
where  # 조건을 지정해주는 구문
```

---

## 계산된 데이터를 조회하는 방법

데이터에 숫자 연산을 적용하여 조회할 수도 있다.

예를 들어 game 이라는 테이블에서 PTS 와 AST 의 합을 total 이라는 별명으로 가져온다면 아래와 같다.

```sql
select PTS + AST as total
from game
```

FGA (전체 슛 시도 횟수) 에서 FGM (전체 골 성공 횟수) 를 빼서 miss 라는 이름의 골 실패 횟수를 구하면 아래와 같다.

```sql
select FGA - FGM as miss
from game
```

곱하기 ( a\*b ) 와 나누기 ( a/b ) 도 가능하다.

---

계산의 편의를 위한 SUM , AVG 같은 함수도 사용 가능하다.

SUM 은 합계를, AVG 는 평균을 구할 수 있다.

```sql
select sum(PTS) as team_points_total,
       avg(PTS) as team_points_average
from game
```

---

COUNT 함수를 사용하여 데이터의 갯수를 구할 수도 있다.

데이터의 단순 갯수가 아닌, 몇개의 데이터값으로 구성되었는지를 구할 떄는 DISTINCT 를 쓴다.

예를 들어 oreders 라는 테이블에서 총 주문 건수를 별명 count_of_orders 로 구하고,

주문한 고객ID 의 갯수를 별명 count_of_customers 로 구하면 아래와 같다.

```sql
select count(1) count_of_orders,
       count(distinct customer_id) count_of_customers
from orders
```

count 함수의 괄호 안에는 보편적으로 " 1 " 을 쓴다.

전체 데이터의 갯수를 구하는 것이기 때문에 특정 칼럼을 쓰는 대신

전체를 지칭한다는 의미에서 " \* " 나 " 1 " 을 써도 되기 때문이다.

---

함수 MIN 과 MAX 를 사용해 최솟값과 최댓값을 구할 수도 있다.

예를 들어 game 테이블에서 PTS 가 가장 높은 선수를 별명 best 로,

가장 낮은 선수를 worst 로 구하면 아래와 같다.

```sql
select min(PTS) best,
       max(PTS) worst
from game
```

---

## GROUP BY

함수 계산을 할 떄 그룹으로 묶어 한번에 계산하는 것도 가능하다.

예를 들어 orders 이라는 테이블에서 type (칼럼) 별로 price (칼럼) 의 평균을 구하려면 아래와 같다.

```sql
select type,   # 원하는 범주가 될 칼럼
       avg(price) avg_price_by_type   # 계산할 칼럼
from orders
group by type   # 원하는 범주가 될 칼럼
```

---

## ORDER BY

ORDER BY 를 사용하면 가져온 데이터들을 정렬할 수 있다.

예를 들어 위에서 가져온 type 별 평균가격을 정렬하여 가져오려면 아래와 같다.

```sql
select type,   
       avg(price) avg_price_by_type   
from orders
group by type   
order by avg(price)   #오름차순 정렬 
----------------------------------------
order by avg(price) desc   #내림차순 정렬
```

---

지금까지 SQL 의 문법 기본 구조를 정리하면 아래와 같다.

구문들의 순서를 지키는 것이 중요하다.

```sql
select    # "데이터 조회" 의 명령어로 필수 구문
from      # "어디에서 데이터를 조회할까" 의 명령어로 필수 구문
where     # 조건을 지정해주는 구문
group by  # 범주를 지정하는 구문
order by  # 정렬을 위한 구문
```

---
