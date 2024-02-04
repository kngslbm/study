## Web Page 에 DB 적용 연습

구글 Firebase를 이용하여 이전에 만들었던 '영화 기록 web page'에 DB를 적용시켜본다.

현재 '영화기록' web page' 첫 화면

[##_Image|kage@dU2lSY/btsDsZ2uifz/O8Dx3JKlSUz8DE31f3Eupk/img.png|CDM|1.3|{"originWidth":843,"originHeight":911,"style":"widthContent","filename":"캡처.PNG"}_##]

postingbox를 통해 새로운 영화기록을 남겨도

[##_Image|kage@bDSkCR/btsDrlEWFhu/wBvCVIdIKckB2YXePta4KK/img.png|CDM|1.3|{"originWidth":843,"originHeight":919,"style":"alignCenter","filename":"영화기록 완성.PNG"}_##]

page를 새로고침하면 data가 사라진다.

[##_Image|kage@dxiDj8/btsDqiom5mA/S8l3Bafi0SyCx5KdFeZFS0/img.png|CDM|1.3|{"originWidth":843,"originHeight":911,"style":"alignCenter","filename":"캡처.PNG"}_##]

page에 일시적으로 data를 추가한 것이지 따로 data를 저장하는 곳이 없기 때문이다.

## 목표

Data Base라는 창고를 만들고 web page에 적용 시켜, data가 휘발되지 않게 만들어본다.

## 시작

일단 FIrebase에서 나의 DB를 만든다.

[##_Image|kage@kCoHA/btsDqLDQU8W/hhBgFSSmKEsdLuleNHeugK/img.png|CDM|1.3|{"originWidth":1893,"originHeight":783,"style":"alignCenter","filename":"firebase.PNG"}_##]

먼저 DB를 사용하기 위해서는 script 태그의 type을 "module"로 지정해야한다.

```js
<script type = "module">
```

나의 firebase DB를 web page와 연결하는 코드를 추가한다.

```js
<script type = "module">

import { initializeApp } from "[https://www.gstatic.com/firebasejs/9.22.0/firebase-app.js](https://www.gstatic.com/firebasejs/9.22.0/firebase-app.js)";
import { getFirestore } from "[https://www.gstatic.com/firebasejs/9.22.0/firebase-firestore.js](https://www.gstatic.com/firebasejs/9.22.0/firebase-firestore.js)";
import { collection, addDoc } from "[https://www.gstatic.com/firebasejs/9.22.0/firebase-firestore.js](https://www.gstatic.com/firebasejs/9.22.0/firebase-firestore.js)";
import { getDocs } from "[https://www.gstatic.com/firebasejs/9.22.0/firebase-firestore.js](https://www.gstatic.com/firebasejs/9.22.0/firebase-firestore.js)";

const firebaseConfig = {
    apiKey: "AIzaSyBEyDRRNcUv0tXxl9a5XK6pbEid60a9i7A",
    authDomain: "slbm-6d65c.firebaseapp.com",
    projectId: "slbm-6d65c",
    storageBucket: "slbm-6d65c.appspot.com",
    messagingSenderId: "658896919313",
    appId: "1:658896919313:web:f6cd90292c80c3b2f54ab0",
    measurementId: "G-00T5CC35CT"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

```

"postingbtn" 이라는 id를 가진 코드가 클릭되면 지정된 data가 DB에 저장되게 한다.

```js
$("#postingbtn").click(async function () {
  let doc = {};
  await addDoc(collection(db, "movies"), doc);
});
```

script 태그의 type이 module이 되면 'onclick' 같은 기능은 작동하지 않는다.

```js
<button onclick\="makeCard()" type\="button" class\="btn btn-light"\>기록하기</button>
```

onclick기능을 삭제하고 id 값 'postingbtn'을 준다

```js
<button id\="postingbtn" type\="button" class\="btn btn-light"\>기록하기</button\>
```

postingbox에 입력된 data들을 변수로 지정하고 DB에 저장될 수 있게 한다.

```js
$("#postingbtn").click(async function () {
  let image = $("#image").val();
  let title = $("#title").val();
  let star = $("#star").val();
  let comment = $("#comment").val();
  let doc = {
    image: image,
    title: title,
    star: star,
    comment: comment,
  };
  await addDoc(collection(db, "movies"), doc);
});
```

입력한 data가 DB에 저장되는지 확인한다.

[##_Image|kage@pEZHn/btsDsYWOf0d/8DLvQkXeqeTJep1X7gNbX1/img.jpg|CDM|1.3|{"originWidth":848,"originHeight":910,"style":"alignCenter","filename":"Inkeddb테스트_LI.jpg"}_##]

잘 저장되었다.

[##_Image|kage@FSmMk/btsDom6eXfS/lyMNYjOQzj1wXBQ9KkLXF0/img.png|CDM|1.3|{"originWidth":1152,"originHeight":521,"style":"alignCenter","filename":"db저장됨.PNG"}_##]

새로운 데이터가 저장되면 알림을 띄우고 page를 리로드 하는 코드를 추가한다.

```js
$("#postingbtn").click(async function () {
  let image = $("#image").val();
  let title = $("#title").val();
  let star = $("#star").val();
  let comment = $("#comment").val();
  let doc = {
    image: image,
    title: title,
    star: star,
    comment: comment,
  };
  await addDoc(collection(db, "movies"), doc);
  alert("기록 되었습니다");
  window.location.reload();
});
```

잘 작동한다.

[##_Image|kage@pGpDY/btsDpv2Wj7A/I6wfYRbu3dyIgsrvzI7KHK/img.png|CDM|1.3|{"originWidth":852,"originHeight":907,"style":"alignCenter","filename":"알림 테스트.PNG"}_##]

DB에서 저장된 data를 가져와 새로운 카드를 만들게 한다.

```js
let docs = await getDocs(collection(db, "movies"));
docs.forEach((doc) => {
  let row = doc.data();

  let image = row["image"];
  let title = row["title"];
  let comment = row["comment"];
  let star = row["star"];
  let temp_html = `<div class="col">
        <div class="card h-100">
            <img src="${image}"
                class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">${title}</h5>
                <p class="card-text">${star}</p>
                <p class="card-text">${comment}</p>
            </div>
        </div>
    </div>`;
  $(cardList).append(temp_html);
});
```

기존에 있던 makeCard 함수는 삭제한다.

```js
function makeCard() {
  let image = $("#image").val();
  let title = $("#title").val();
  let comment = $("#comment").val();
  let star = $("#star").val();
  let temp_html = `<div class="col">
        <div class="card h-100">
            <img src="${image}"
                class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">${title}</h5>
                <p class="card-text">${star}</p>
                <p class="card-text">${comment}</p>
            </div>
        </div>
    </div>`;
  $(cardList).append(temp_html);
}
```

script 태그의 타입이 module로 바뀌면 자동적으로 page 로딩이 끝나고 script 태그를 읽는다.

```js
$(document).ready(function () {
  let url = "http://spartacodingclub.shop/sparta_api/weather/seoul";
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      let temperature = data["temp"];
      let temp_html = ``;
      if (temperature > 19) {
        temp_html = `따뜻해요`;
      } else {
        temp_html = `쌀쌀해요`;
      }
      $("#seoulTemperature").text(temp_html);
    });
});
```

즉, 준비가 되면 데이터를 가져오라는 명령어는 불필요하다. 삭제

```js
let url = "http://spartacodingclub.shop/sparta_api/weather/seoul";
fetch(url).then(res => res.json()).then(data => {
    let temperature = data['temp'];
    let temp_html = ``;
    if (temperature > 19) {
        temp_html = `따뜻해요`;
    } else {
        temp_html = `쌀쌀해요`;
    }
    $('#seoulTemperature').text(temp_html);
})
```

onclick 기능은 작동하지 않기 때문에 postingbox를 열고 닫는 버튼도 수정한다.

함수 수정 전
```js
function openclose() {
    $('#postingbox').toggle();
}
```
함수 수정 후
```js
$("#moviesAdd").click(async function () {
    $('#postingbox').toggle();
});
```

버튼 태그 수정 전
```js
<button onclick="openclose()" type="button" class="btn btn-outline-light">영화 기록하기</button>
```
버튼 태그 수정 후
```js
<button id="moviesAdd" type="button" class="btn btn-outline-light">영화 기록하기</button>
```
완성.

[##_Image|kage@bd2S8x/btsDp8l5Gd7/KE8s9vfvIGYzJWXkrf8fkk/img.png|CDM|1.3|{"originWidth":848,"originHeight":944,"style":"alignCenter","filename":"db 연결 성공.PNG"}_##]

page를 새로고침해도 영화카드들이 사라지지 않는다.

data들이 DB에 잘 저장되었고 page가 data를 가져올 수 있기 때문이다.

[##_Image|kage@uAfr7/btsDqgKU3Jp/7EYYOrUKQ1fYpSVq5ERaxk/img.png|CDM|1.3|{"originWidth":1146,"originHeight":605,"style":"alignCenter","filename":"db 잘작동.PNG"}_##]
