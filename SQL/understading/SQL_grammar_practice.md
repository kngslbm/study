## SELECT, FROM

SQL의 문법은 "어떤 테이블에서 어떤 데이터를 가져오는가" 가 핵심이다.

FROM 으로 데이터를 가져올 테이블을 지정하고

SELECT 로 어떤 칼럼을 가져올지 지정한다.

```sql
select 칼럼1, 칼럼2
from 테이블;
```

---

\*을 사용하면 모든 칼럼을 가져올 수도 있다.

```sql
select *
from 테이블;
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
from 테이블;
```

---

## WHERE

WHERE 로 여러 조건을 지정하고 필터링하면 원하는 데이터만 가져올 수 있다.

같은 값 혹은 크고 작은 값을 가져오기 위해 비교연산자를 사용할 수 있다.

예를 들어 customers 라는 테이블에서 age 가 20보다 작은 데이터만 가져온다면 아래와 같다.

```sql
select *
from customers
where age<20;
```

| 비교연산자 | 의미                     |
| ---------- | ------------------------ |
| =          | 같다                     |
| <>         | 같지 않다 (다르다)       |
| >, <       | 크다, 작다               |
| >=, <=     | 크거나 같다, 작거나 같다 |

---

그 외에도 " between ", " in ", " like " 같은 다양한 필터가 존재한다.

각 필터의 조건은 아래와 같다.

between : a 와 b 사이

```sql
where age between 10 and 20;
```

in : in() 안에 포함시킨 것만

```sql
where age in (15, 20, 35);
```

like : 완전히 일치하지 않아도 비슷한 것들

```sql
where name like "김%";   #"김"으로 시작하는 모든 데이터
```

```sql
where name like "%원";   #"원"으로 끝나는 모든 데이터
```

```sql
where name like "%민%";   #"민"이 포함된 모든 데이터
```

## 논리연산

여러 조건을 하나의 Query 문에 적용시킬 때 사용하는 연산이 논리연산이다.

논리연산의 종류에는 " AND " , " OR " ," NOT " 이 있다.

AND : 두 조건 모두 충족하는 데이터만

```sql
where age>20 and gender="female";   #20세 이상의 여성일 경우만
```

OR : 하나의 조건만 충족해도

```sql
where age>20 or gender="female";   #20세 이상이거나 여성일 경우만
```

NOT : 조건이 아닌 데이터만

```sql
where not gender="female";   #여성이 아닐 경우만
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
from game;
```

FGA (전체 슛 시도 횟수) 에서 FGM (전체 골 성공 횟수) 를 빼서 miss 라는 이름의 골 실패 횟수를 구하면 아래와 같다.

```sql
select FGA - FGM as miss
from game;
```

곱하기 ( a\*b ) 와 나누기 ( a/b ) 도 가능하다.

---

계산의 편의를 위한 SUM , AVG 같은 함수도 사용 가능하다.

SUM 은 합계를, AVG 는 평균을 구할 수 있다.

```sql
select sum(PTS) as team_points_total,
       avg(PTS) as team_points_average
from game;
```

---

COUNT 함수를 사용하여 데이터의 갯수를 구할 수도 있다.

데이터의 단순 갯수가 아닌, 몇개의 데이터값으로 구성되었는지를 구할 떄는 DISTINCT 를 쓴다.

예를 들어 oreders 라는 테이블에서 총 주문 건수를 별명 count_of_orders 로 구하고,

주문한 고객ID 의 갯수를 별명 count_of_customers 로 구하면 아래와 같다.

```sql
select count(1) count_of_orders,
       count(distinct customer_id) count_of_customers
from orders;
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
from game;
```

---

## GROUP BY

함수 계산을 할 떄 그룹으로 묶어 한번에 계산하는 것도 가능하다.

예를 들어 orders 이라는 테이블에서 type (칼럼) 별로 price (칼럼) 의 평균을 구하려면 아래와 같다.

```sql
select type,   # 원하는 범주가 될 칼럼
       avg(price) avg_price_by_type   # 계산할 칼럼
from orders
group by type;   # 원하는 범주가 될 칼럼
```

---

group by 에 아래와 같이 숫자를 쓸 수도 있다.

```sql
group by 1, 2  # 첫번 째, 두번 째 칼럼을 그룹화
```

select 에서 선택한 칼럼을 순서대로 지정하는 것이다.

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
order by avg(price) desc;   #내림차순 정렬
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

## HAVING

WHERE 는 단일 행에 대해 필터링을 할 떄 사용되고,

HAVING은 GROUP BY 로 그룹화된 데이터를 필터링 할 때 사용된다.

예를 들어 type 별 평균 가격이 100 이상인 데이터만 가져오려면 아래와 같다.

```sql
select type,
       avg(price) avg_price_by_type
from orders
group by type
having avg(price)>100;
```

---

## REPLACE

REPLACE 함수를 사용하여 특정 문자를 다른 문자로 바꿀수 있다.

예를 들어 김포가 서울에 편입되어 addr 칼럼에 저장된 주소 데이터를 변경해야된다면 아래와 같다.

```sql
select addr "원래 주소",
       replace(addr, "김포", "서울") "바뀐 주소"
from 테이블
where addr like "%김포%";   # 바뀐 주소들만 보여주기 위한 조건 구문
```

---

## SUBSTRING

SUBSTRING 함수를 사용하면 데이터 전체가 아닌 특정 부분의 문자만을 조회할 수도 있다.

예를 들어 addr 칼럼에 " 서울시 강남구 논현동 ", " 부산시 금정구 남산동 " 식의 주소 데이터가 있는데,

"서울", "부산" 식의 어떤 지역인지에 대해서만 데이터를 가져온다면 아래와 같다.

```sql
select substr(addr, 1, 2)  # substring, substr 둘다 가능(칼럼명, 시작위치, 글자수)
from 테이블;
```

---

## CONCAT

CONCAT 을 사용하면 여러 칼럼에서 원하는 문자를 가져와 조합하여 사용할 수도 있다.

예를 들어 addr 칼럼의 지역명과 restaurant 칼럼의 음식점 이름을 붙여서 출력하려면 아래와 같다.

```sql
select concat("[", substr(addr,1,2),"]",restaurant)   # [지역]음식점이름
from 테이블;
```

---

## IF , CASE

조건에 따라 특정 방법을 적용시키고 싶을 때 IF 와 CASE 를 사용할 수 있다.

예를 들어 IF 구문을 사용해 order 라는 칼럼에서 type 이 food 인 데이터는 "음식"으로 출력하고,
나머지는 "기타"라고 출력하고 싶다면 아래와 같다.

```sql
select if(type="food", "음식", "기타")   #if(조건, True일 경우, False일 경우)
from orders;
```

---

CASE 구문은 여러 개의 조건을 걸고 그에 따른 각각의 결과를 반환하기 위해서 쓰인다.

예를 들어 type에 따라 다른 조건과 각각의 결과를 반환하게 하고,
어느 조건에도 해당하지 않으면 "기타"를 반환하게 하려면 아래와 같다.

```sql
select case when type="food" then "음식"
       case when type="clothes" then "의류"
       case when type="electronic" then "전자제품"
       else "기타" end   # 구문을 끝낼 때는 " end "를 써줘야 한다.
from orders;
```

---

또한 case 문은 상식적이지 않은 데이터를 제외시킬 수 있게끔, 범위를 지정하는 데에도 사용하기 좋다.

예를 들어 2017-10-05 에 오픈해 2020-01-01 에 문을 닫은 곳에서 주문날짜를 확인하는데,

그 외의 날짜 데이터가 나온다면 상식적이지 않을 것이다.

이때 범위를 지정하고 상식적이지 않은 데이터를 범위 안으로 넣으려면 아래와 같다.

```sql
select order_date,
       case when order_date<2017-10-05 then 2017-10-05
            when order_date>2020-01-01 then 2020-01-01
from orders
```

---

## CAST

일반적으로 데이터베이스 시스템은 다양한 형태의 데이터 타입을 지원한다. ( 문자, 숫자, 날짜 등 )

cast 함수를 사용하면 데이터 타입을 변환할 수 있다.

예를 들어 "123" 이라는 문자열을 숫자로 변환하려면 아래와 같다.

```sql
select cast("123" as int);   # cast(변환할 값 as 변환할 데이터 타입)
```

as 뒤에 오는 데이터 타입은 사용하는 데이터베이스 매니지먼트 시스템에 따라 지원하는 데이터 타입이 다를 수 있기 때문에 해당 시스템 문서를 참조하는 것이 좋다.

---

## SUBQUERY

SubQuery는 하나의 Query 문에 들어가 있는 또 다른 Query 문을 말한다.

서브쿼리를 사용하면 복잡한 검색이나 필터링이 가능하고 유연성과 가독성을 향상시킬 수 있다.

서브쿼리는 주로 두가지 경우, "필터링 조건으로써" 혹은 "결과의 집합으로써" 사용된다.

---

예를 들어 orders1 테이블에서 주문 금액이 100보다 큰 고객을 선별하여,

orders2 테이블에서 동일한 고객의 주문을 조회하려면 아래와 같다.

```sql
# 필터링 조건으로써 서브쿼리
select *
from orders2
where customer = (select customer from orders1 where price > 100);
```

---

그리고 예를 들어 2024년 2월 6일 이후 주문건에 대해서만 선별을 하고,

해당 주문들의 평균 주문금액을 구하려면 아래와 같다.

```sql
# 결과의 집합으로써 서브쿼리
select avg(price) recent_avg_price
from(
     select *
     from orders1
     where order_date > "2024-02-06"
    ) recent_orders;
```

---

## JOIN

join 을 사용하면 두 개 이상의 테이블에서 데이터를 함께 검색하고 결합하여 조회할 수 있다.

주로 관계형 데이버베이스에서 많이 사용된다.

다양한 유형의 join 이 있지만 가장 일반적인 유형은 아래 그림을 보면 이해하기 쉽다.

![sql join 이해를 위한 단순 그림](https://github.com/kngslbm/study/assets/148850117/cfcb21c3-ba17-4474-9ea4-cc6be1588656)


left join 또는 right join 은 해당하는 한 쪽 테이블의 모든 행을 반환하고 나머지 한쪽에서 일치하는 행이 있다면 반환한다. 값이 없을 경우 NULL 로 채워진다.

inner join 은 두 테이블 간에 일치하는 행만 반환한다.

full join 은 양쪽 테이블의 모든 행을 반환하고 일치하는 행이 있다면 역시 반환한다. 일치하지 않는 데이터의 값은 NULL 로 채워진다.

그 외에도 두 테이블의 가능한 조합을 모두 반환하는 cross join 도 있다. 이 경우 두 테이블의 행을 곱한 수만큼의 결과가 나온다.

---

예를 들어 orders 테이블과 payments 테이블에서 고객명이 일치하는 데이터만 조회하려면 아래와 같다.

```sql
select *
from orders a inner join payments b on a.customer = b.customer;

# 형식은 (테이블 join유형 join 테이블 on 공통칼럼 = 공통칼럼)
# 공통칼럼은 결합을 위한 공통된 값이기 때문에 칼럼명은 달라도 괜찮다
# join 을 사용할 떄 칼럼은 (테이블.칼럼) 형식으로 써야함
```

---

## COALESCE

coalesce 는 NULL 값을 다른 값으로 대체할 떄 사용되는 함수이다.

예를 들어 orders 테이블에 payments 테이블을 left join 했을 때,

payments 테이블에 고객 정보가 없을 경우 NULL 값 대신 "Unknown" 이 반환되게 하려면 아래와 같다.

```sql
select coalesce(b.customer, "Unknown")    # coalesce(칼럼, 대체값)
from orders a left join payments b on a.customer = b.customer;
```

---

반대로 결과에 포함시키고 싶지 않은 데이터를 NULL 값으로 처리해 제외시킬 수도 있다.

예를 orders 테이블에서 rating 의 평균을 구하는데 "Not given" 값은 제외시키고 계산하려면 아래와 같다.

```sql
select avg(if (rating<>"Not given", rating, null))   # "Not given" 값은 제외시키고 평균값 계산
from (
       select cast(rating as int)                    # rating 칼럼을 숫자형을 변경
       from orderss
     ) a;
```

위에 처럼 Query 문 안에서 NULL 값을 필요에 따라 사용할 수도 있다.

---

## PIVOT TABLE

pivot table 은 두 개 이상의 기준으로 데이터가 집계된 표를 말한다.

기본 구조는 아래 그림과 같다.

<img width="616" alt="pivottable기본구조" src="https://github.com/kngslbm/study/assets/148850117/b219c578-7e3d-4622-b763-edec58bf0df4">


예를 들어 orders 라는 테이블에서 각 판매자마다 일별 주문량을 피벗테이블로 보기 좋게 만들면 아래와 같다.

```sql
select seller,
       max(if(day="01",cnt,0)) "day1",      # day값이 해당날짜일 경우 cnt값을, 아닐 경우 0 을 가져온다. 그리고 최댓값을 선별하게되면, 주문이 하나라도 있으면 당연히 0이 아닌 해당시간의 주문량이 선별되는 원리이다.
       max(if(day="02",cnt,0)) "day2",
       max(if(day="03",cnt,0)) "day3",
       ...
from(
     select seller,
            substr(order_date,9,2) day,     # substr으로 일(day)에 해당하는 데이터 선별.
            count(1) cnt
     from orders
    )a                                      # subQuery 로 계산 결과를 다시 사용
order by 2 desc;                            # day1 주문량이 많은 순으로 정렬
```

---

## WINDOW FUNCTION

윈도우 함수는 데이터 집합에 창을 형성해 연산하는 특별한 종류의 함수들이다.

핵심 개념은 "파티션"을 통해 데이터를 나누고 함수를 적용할 수 있다는 것과,

"정렬"이 가능해 데이터의 순차적 연산이 가능하다는 것이다.

> 추가로 현재 행을 기준으로 앞 뒤와의 관계를 이해하고, 이전행과 다음행의 범위를 정의하여 함수가 데이터를 어떻게 처리할 지를 결정하는 "프레임"이라는 개념이 있다. (프레임에 대해서는 아직 개념을 완전히 이해하지는 못해서 부정확할 수 있다. 이후 완전히 이해하게 된다면 수정될 수도 있다.)

예를 들어 "RANK" 라는 윈도우 함수를 사용하여 orders 라는 테이블에서 type 별로 seller 의 순위를 조회하면 아래와 같다.

```sql
select type,     # 형식 : window_function(argument) over (partition by 칼럼 order by 정렬 기준)
       seller,
       rank() over (partition by type           # partition by ~ : ~ 별로 파티션을 나누어 rank 함수를 적용
                    order by cnt desc) "순위"   # order by ~ : 정렬 기준
from(
     select type,
            seller,
            count(1) cnt
     from orders
     group by 1, 2
    ) a;
```

---

또 다른 예로 윈도우 함수 "SUM" 을 이용하여 orders 라는 테이블에서 type별 누적 주문량을 구하려면 아래와 같다.

```sql
select type,
       seller,
       sum(cnt) over (patition by type order by cnt) "누적 주문량"
from (
      select type,
             seller,
             count(1) cnt
      from orders
      group by 1, 2
     ) a;
```

---

## LIMIT

limit 함수를 사용하면 행의 수를 제한하여 조회할 수 있다.

대량의 데이터를 다룰 때 유용하다.

예를 들어 orders 라는 테이블에서 마지막 5개의 주문만을 조회하려면 아래와 같다.

```sql
select order_number
from orders
order by order_date desc
limit 5;
```
---
