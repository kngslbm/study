## Linked List 직접 구현 연습



1차 시도
```py
# Node class 선언
class Node:
    # 입력받는 값과 포인터 변수 지정.
    def __init__(self, value, next):
        self.value = value    
        self.next = next      

# Linked list class 선언
class Linked_list:
    # head 생성, 값은 아직 None.
    def __init__(self):
        self.head = None      

    # 입력값을 리스트의 끝에 삽입하는 Method
    def append(self, value):
        # 아직 head가 없으면 새로운 Node를 head로 지정.
        if not self.head:
            self.head = Node(value, None)
            return

        # 이미 Node 가 있으면 next가 없을 때 까지 이동.
        node = self.head
        while node.next:
            node = node.next

        # 마지막 Node에 오면 그 Node의 next로 새로운 Node를 지정
        node.next = Node(value, None)

    # 리스트의 마지막 Node를 반환하는 Method
    def extract(self):
        node = self.head
        
        while node.next:
            node = node.next

        return node
    
    # 리스트의 마지막 노드를 삭제하는 Method.
    def remove(self):
        node = self.head
        
        while node.next:
            node = node.next
            
        node.pop() # node는 'Node class 객체'라서 안되겠지?
        # 링크드 리스트 삭제 구현 학습 필요
```


2차시도

head 뿐만 아니라 tail 도 구현해보고

```py
# Node class 선언
class Node:
    def __init__(self, value, next):
        self.value = value    # 입력받는 값과 포인터 변수 지정.
        self.next = next

# Linked list class 선언


class Linked_list:
    def __init__(self):
        self.head = None      # head 와 tail 변수 생성, 값은 아직 None.
        self.tail = None

    # 리스트의 끝에 삽입하는 Method
    def append(self, value):
        # 아직 head가 없으면 새로운 Node 를 head 이자 tail 로 지정.
        if not self.head:
            self.head = Node(value, None)
            self.tail = self.head
            return
```