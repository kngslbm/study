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

    // 버킷 리스트 클릭 이벤트
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

