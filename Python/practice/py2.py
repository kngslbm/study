class BinaryMinHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def percolate_up(self):
        cur = len(self)
        parent = cur // 2

        while parent > 0:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

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

    def insert(self, k):
        self.items.append(k)
        self.percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self.percolate_down(1)

        return root


def test_minheap_we_made(lst, k):
    minheap = BinaryMinHeap()

    for elem in lst:
        minheap.insert(elem)

    return [minheap.extract() for _ in range(len(lst))][len(lst)-k]


print(test_minheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 1))
