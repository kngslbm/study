## problem explanation

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

### Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

### Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

### Constraints
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104


## problem solving

(heap 구현 연습을 위해 ' heapq ' 라이브러리는 사용하지 않을 예정.)

최소 힙을 구현하고, 입력받은 list 를 최소힙으로 구조화한다.

이후 모든 요소를 추출하면 값이 작은 순으로 정렬되고,

이때 전달받은 k 번째의 수를 반환한다.

```py
# 최소 힙 구현
class BinaryMinHeap:
    # 계산의 편의를 위해 index 를 1부터 사용. 0번 째 index는 None 값을 준다.
    def __init__(self):
        self.items = [None]
    
    # 계산의 편의를 위해 Magic Method ' len() '을 overriding.
    def __len__(self):
        return len(self.items) - 1

    # 마지막 요소를 올바른 위치에 정렬하기 위한 Method
    def percolate_up(self):
        cur = len(self)
        parent = cur // 2

        while parent > 0:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    # 첫번 째 요소를 올바른 위치에 정렬하기 위한 Method
    def percolate_down(self, cur):
        smallest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != cur:
            self.items[cur], self.items[smallest] = self.items[smallest], self.items[cur]
            self.percolate_down(smallest)

    # 입력값을 heap에 추가
    def insert(self, k):
        self.items.append(k)
        self.percolate_up()

    # 첫번 째 요소를 추출
    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self.percolate_down(1)

        return root

# 기본 제출 형식
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:   
        
        #최소힙 자료구조 선언
        minheap = BinaryMinHeap()

        #입력받은 리스트의 각 요소 최소힙 자료구조에 추가
        for elem in nums:
            minheap.insert(elem)

        #최소힙 요소 모두 추출.(값이 잡은 순으로 정렬) 뒤에서 k번째 수 반환. 
        return [minheap.extract() for _ in range(len(nums))][len(nums)-k]
```