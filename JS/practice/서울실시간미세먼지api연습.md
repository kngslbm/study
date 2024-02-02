fetch 메서드는 api를 통해 data에 접근할 수 있다.

fetch 메서드를 활용해 서울의 미세먼지 정보를 제공하는 웹페이지를 만들어본다.

html과 CSS로 만든 사이트의 기본 모습

[##_Image|kage@4akE4/btsDpu9SFhw/KqLZGqpy6WpxFKNBxXz7nk/img.png|CDM|1.3|{"originWidth":617,"originHeight":330,"style":"alignCenter","filename":"edited_첫페이지.PNG"}_##]

## **목표**

업데이트 버튼을 누를 때마다 (구이름 : 미세먼지 상태) 의 형태로 서울시 모든 구의 리스트를 생성하게 한다.

'미세먼지 상태' 는 '보통' 과 '나쁨'으로 표시되게 하며

'나쁨'일 경우 폰트색은 red로 표시되도록 한다.

## **시작**

먼저 jQuery를 사용하기 위해  import한다.

<script src\="[https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js](https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js)"\></script\>

함수를 만든다. 이름은 miseUpdate

<script\>

        function miseUpdate() {

        }

</script\>

'업데이트' 버튼에 onclick 기능을 추가하고 'miseUpdate' 함수와 연결한다.

        <button onclick\="miseUpdate()"\>업데이트</button\>

서울시에서 제공하는 openAPI를 가져와 변수 url로 선언한다.

<script\>

        function miseUpdate() {

            let url = '[http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'](http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

        }

</script\>

서울시 openAPI를 확인한다. 

[##_Image|kage@BbMZK/btsDmrfpRVW/3Jby9Vkl0vWqBu4OdJDZnK/img.png|CDM|1.3|{"originWidth":356,"originHeight":513,"style":"alignCenter","filename":"서울시미세먼지openapi.PNG"}_##]

데이터는 json이라는 형식으로 되어있으며, 딕셔너리 형태를 띠고있다.

'RealtimeCityAir'  안에 'row' 가 서울 모든 구의 정보를 각각 담고 있고

'row'안에 구이름을 나타내는 ' MSRSTE\_NM'과 미세먼지 상태를 나타내는 ' IDEX\_NM '를 사용할 것이다.

fetch 메서드를 사용해 서울시openAPI 데이터에 접근한다. 

<script\>

        function miseUpdate() {

            let url = '[http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'](http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

            fetch(url).then(res \=> res.json()).then(data \=> {

  

                })

        }

</script\>

가져와서 사용할 데이터를 'rows'변수로 지정한다.

    <script\>

        function miseUpdate() {

            let url = '[http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'](http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

            fetch(url).then(res \=> res.json()).then(data \=> {

                let rows = data\['RealtimeCityAir'\]\['row'\]

            })

        }

    </script\>

'rows'에 있는 서울시 모든 구의 데이터를 사용하기 위해 반복문을 쓴다

    <script\>

        function miseUpdate() {

            let url = '[http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'](http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

            fetch(url).then(res \=> res.json()).then(data \=> {

                let rows = data\['RealtimeCityAir'\]\['row'\]

                rows.forEach(a \=> {

                })

            })

        }

    </script\>

사용할 데이터 '서울시 모든 구의 이름'과 '미세먼지 현황'을 변수로 등록한다 

    <script\>

        function miseUpdate() {

            let url = '[http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'](http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

            fetch(url).then(res \=> res.json()).then(data \=> {

                let rows = data\['RealtimeCityAir'\]\['row'\]

                rows.forEach(a \=> {

                    let gu\_name = a\["MSRSTE\_NM"\] 

                    let mise = a\["IDEX\_NM"\]

                })

            })

        }

    </script\>

서울시 모든 구의 미세먼지 현황을 보여줄 리스트<ui></ui>를 <body>부분에 작성하고 id를 부여한다.

        <h1\>서울 미세먼지 현황</h1\>

  

        <hr />

  

        <div class\="question-box"\>

            <p\>서울시 OpenAPI(실시간 미세먼지 상태)를 이용해 모든 구의 미세먼지가 표시됩니다.</p\>

            <p\>업데이트 버튼을 누를 때마다 정보가 업데이트 됩니다.</p\>

            <button onclick\="miseUpdate()"\>업데이트</button\>

            <ul id\="miseLIst"\>

            </ul\>

        </div\>

미세먼지 현황을 보여줄 리스트를 html 형식으로 변수 'temp\_html'에 등록하고

.append 기능을 사용해 리스트를 추가할 수 있게 한다.  

    <script\>

        function miseUpdate() {

            let url = '[http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'](http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

            fetch(url).then(res \=> res.json()).then(data \=> {

                let rows = data\['RealtimeCityAir'\]\['row'\]

                rows.forEach(a \=> {

                    let gu\_name = a\["MSRSTE\_NM"\]

                    let mise = a\["IDEX\_NM"\]

                    let temp\_html = \`<li>${gu\_name} : ${mise}</li>\`

                    $('#miseList').append(temp\_html)

                })

            })

        }

    </script\>

'업데이트'버튼을 누르면 서울시 모든 구의 미세먼지 현황 리스트가 잘 나타난다.

[##_Image|kage@m4iCU/btsDnvu7Laf/zmHnlgYkFtl0RMyXqVRPW1/img.png|CDM|1.3|{"originWidth":618,"originHeight":753,"style":"alignCenter","filename":"작동1.PNG"}_##]

하지만 한번 더 누르면 이전 데이터가 누적되고 계속 쌓여간다.

[##_Image|kage@b6LWGl/btsDqo2yxmZ/PkbwiKD96kkLDDXZQz163K/img.png|CDM|1.3|{"originWidth":619,"originHeight":931,"style":"alignCenter","filename":"리스트누적.PNG"}_##]

.empty  기능을 사용해 'miseUpdate' 함수의 첫 작업으로 'miseList'를 모두 지우게 한다.

    <script\>

        function miseUpdate() {

            let url = '[http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'](http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

            $('#miseList').empty()

            fetch(url).then(res \=> res.json()).then(data \=> {

                let rows = data\['RealtimeCityAir'\]\['row'\]

                rows.forEach(a \=> {

                    let gu\_name = a\["MSRSTE\_NM"\]

                    let mise = a\["IDEX\_NM"\]

                    let temp\_html = \`<li>${gu\_name} : ${mise}</li>\`

                    $('#miseList').append(temp\_html)

                })

            })

        }

    </script\>

조건문을 사용해 변수 'mise'의 값이 '나쁨'일 경우 id 값 'bad'를 가진 <span>태그로 감싼 html을 출력하게 한다

    <script\>

        function miseUpdate() {

            let url = '[http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'](http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

            $('#miseList').empty()

            fetch(url).then(res \=> res.json()).then(data \=> {

                let rows = data\['RealtimeCityAir'\]\['row'\]

                rows.forEach(a \=> {

                    let gu\_name = a\["MSRSTE\_NM"\]

                    let mise = a\["IDEX\_NM"\]

                    let temp\_html = \`\`

                    if (mise == "나쁨") {

                        temp\_html = \`<li>${gu\_name} : <spen id="bad">${mise}</span></li>\`

                    } else {

                        temp\_html = \`<li>${gu\_name} : ${mise}</li>\`

                    }

                    $('#miseList').append(temp\_html)

                })

            })

        }

    </script\>

id 'bad'의 폰트 컬러는 빨간색으로 한다.

    <style\>

        #bad {

            color : red;

        }

    </style\>

완성!

[##_Image|kage@yeeny/btsDqmcEUqA/q14gcopYpVWjJMjhPjumP0/img.png|CDM|1.3|{"originWidth":614,"originHeight":764,"style":"alignCenter","filename":"완성.PNG"}_##]
