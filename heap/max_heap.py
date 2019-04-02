class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # insert at end of heap
        # compare with parent
        # swap if larger than parent
        # continue compare/swap until parent is larger
        pass

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
