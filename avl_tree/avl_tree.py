"""
Node class to keep track of
the data internal to individual nodes
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        # if self.node:
        #   self.height = 0
        # else:
        self.height = -1
        self.balance = 0

    """
  Display the whole tree. Uses recursive def.
  """

    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None:
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(
                self.balance) + "]", 'L' if self.is_leaf() else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
  Computes the maximum number of levels there are
  in the tree
  """

    def update_height(self):
        if self.node:
          if not self.node.right and not self.node.left:
            self.height = 0
          if self.node.right and self.node.left:
            self.node.right.update_height()
            self.node.left.update_height()
            self.height = max(self.node.right.height, self.node.left.height) + 1
          elif self.node.left:
            self.node.left.update_height()
            self.height = self.node.left.height + 1
          elif self.node.right:
            self.node.right.update_height()
            self.height = self.node.right.height + 1

        else:
          self.height = -1

    """
  Updates the balance factor on the AVLTree class
  """

    def update_balance(self):
        pass

    """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent. 
  """

    def _left_rotate(self):
        pass

    """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent. 
  """

    def _right_rotate(self):
        pass

    """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """

    def rebalance(self):
        pass

    """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """

    def insert(self, key):
      # if key > self.node.key:
      #   if self.node.right:
      #     self.node.right.insert(key)
      #   else:
      #     self.node.right = 
        pass

    def is_leaf(self):
        if self.node.left or self.node.right:
            return False
        else:
            return True
