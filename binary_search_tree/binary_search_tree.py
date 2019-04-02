class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    def contains(self, target):
        if self.value == target:
            return True

        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    def get_max(self):
        pass

    def for_each(self, cb):
        pass

    def __str__(self):
        return str(self.value)
