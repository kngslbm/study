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

        #
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value, None)

    def extract(self):
        node = self.head

        while node.next:
            node = node.next

        return node

    def remove(self, value):
        node = self.head

        while node.next:
            node = node.next
            if node.value == value:
                break


l1 = Linked_list()

l1.append(1)

print(l1.extract().value)
