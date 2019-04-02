class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # insert at end of heap
        new_index = len(self.storage)
        self.storage.append(value)
        found_spot = False

        while not found_spot:
            # compare with parent
            parent_index = (new_index - 1) // 2
            if parent_index < 0:
                parent_index = 0
            # swap if larger than parent
            if self.storage[new_index] > self.storage[parent_index]:
                self.storage[new_index], self.storage[parent_index] = self.storage[parent_index], self.storage[new_index]
                new_index = parent_index
            # continue compare/swap until parent is larger
            else:
                found_spot = True

    def delete(self):
        # remove element from front of list
        # copy last value to beginning, remove last index off list
        # compare with largest child
        # swap if smaller than largest child
        # repeat comparisons until child is smaller
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass


heap = Heap()
heap.insert(5)
heap.insert(2)
heap.insert(7)
heap.insert(12)
heap.insert(1)
heap.insert(22)
print(heap.storage)
