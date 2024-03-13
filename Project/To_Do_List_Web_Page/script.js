// 페이지 로드 시 이전 상태 복원
document.addEventListener("DOMContentLoaded", (event) => {
  const postit = document.querySelectorAll(".postit");
  postit.forEach((postit, index) => {
    // 로컬 스토리지에서 상태 읽기
    const isDone = localStorage.getItem("postit" + index) === "done";
    if (isDone) {
      postit.classList.add("done");
    }
  });
});

// To Do list 클릭 이벤트
const postit = document.querySelectorAll(".postit");
postit.forEach((postit, index) => {
  postit.addEventListener("click", function () {
    // 클래스 토글
    postit.classList.toggle("done");

    // 로컬 스토리지에 상태 저장
    if (postit.classList.contains("done")) {
      localStorage.setItem("postit" + index, "done");
    } else {
      localStorage.setItem("postit" + index, "");
    }
  });
});

// BGM
let audio1 = null; // audio1을 전역 변수로 선언하여 play와 pause에서 모두 접근할 수 있도록 함
let isPlaying = false; // 음악이 재생 중인지 여부를 나타내는 변수

document.querySelector(".btn1").addEventListener("click", function () {
  // 음악이 재생 중이면 멈추고, 재생 중이 아니면 재생
  if (isPlaying) {
    audio1.pause(); // 재생 중인 음악을 멈춤
    isPlaying = false; // 재생 중인지 여부를 false로 변경
  } else {
    audio1 = new Audio("bgm.mp3");
    audio1.loop = true; // 반복재생
    audio1.volume = 0.5; // 음량 설정
    audio1.play(); // bgm.mp3 재생
    isPlaying = true; // 재생 중인지 여부를 true로 변경
  }
});

// To Do 항목 추가
document.getElementById("addButton").addEventListener("click", function () {
  // 입력 필드에서 값을 가져옴
  const todoText = document.getElementById("todoInput").value.trim();

  // 값이 비어있지 않은 경우에만 추가
  if (todoText !== "") {
    // 새로운 To Do 항목을 생성
    const newTodo = document.createElement("div");
    newTodo.classList.add("postit", "center");

    // To Do 리스트에 추가
    const todoList = document.querySelector(".flex-row");

    // 새로운 To Do 항목 추가
    todoList.appendChild(newTodo);
    newTodo.textContent = todoText;

    // To Do 항목의 클래스를 순서대로 부여
    const existingTodos = todoList.querySelectorAll('.postit');
    const newClassIndex = existingTodos.length % 4; // 현재 클래스 인덱스 계산
    newTodo.classList.add(`post${newClassIndex + 1}`);

    // 입력 필드 초기화
    document.getElementById("todoInput").value = "";

    // 클릭 이벤트 추가
    newTodo.addEventListener("click", function () {
      newTodo.classList.toggle("done");
      // 로컬 스토리지에 상태 저장
      const index = Array.from(todoList.children).indexOf(newTodo);
      if (newTodo.classList.contains("done")) {
        localStorage.setItem("postit" + index, "done");
      } else {
        localStorage.setItem("postit" + index, "");
      }
    });
  }
});


// To Do 항목 삭제
document.getElementById("deleteButton").addEventListener("click", function () {
  // To Do 리스트를 가져옴
  const todoList = document.querySelector(".flex-row");

  // 가장 최근에 추가된 To Do 항목을 찾아 삭제
  const lastAddedTodo = todoList.lastElementChild;
  if (lastAddedTodo) {
    // 마지막에 추가된 To Do 항목 삭제
    todoList.removeChild(lastAddedTodo);

    // 삭제된 To Do 항목의 로컬 스토리지 항목도 삭제
    const index = Array.from(todoList.children).indexOf(lastAddedTodo);
    localStorage.removeItem("postit" + index);
  }
});