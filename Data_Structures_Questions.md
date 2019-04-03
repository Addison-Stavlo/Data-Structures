Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
   Constant. It only adds 1 item to the Linked List and assignment is independent of queue size.

2. What is the runtime complexity of `dequeue`?
   Constant. It only removes 1 item from the Linked List and assigning the new start value is independent of queue size.

3. What is the runtime complexity of `len`?
   Constant. It doesnt need to do any counting, just retrieve a stored property of the class.

## Binary Search Tree

1. What is the runtime complexity of `insert`?
   assuming even probability distribution of insertion objects, log(n).  
    can make worst-case inputs to force this to be O(n)

2. What is the runtime complexity of `contains`?
   assuming even probability distribution of insertion objects, log(n).  
    can make worst-case inputs to force this to be O(n)

3. What is the runtime complexity of `get_max`?
   assuming even probability distribution of insertion objects, log(n).  
    can make worst-case inputs to force this to be O(n)

## Heap

1. What is the runtime complexity of `_bubble_up`?
   worst case log(n), it will only need log2(n) operations to bubble the height of the tree

2. What is the runtime complexity of `_sift_down`?
   worst case log(n), it will only need log2(n) operations to bubble the height of the tree

3. What is the runtime complexity of `insert`?
   since it tiggers the bubble_up method, at worst log(n)

4. What is the runtime complexity of `delete`?
   since it triggers the \_sift_down function, at worst log(n)

5. What is the runtime complexity of `get_max`?
   constant. it always grabs the top-level node value.

## Doubly Linked List

1.  What is the runtime complexity of `ListNode.insert_after`?
    Constant

2.  What is the runtime complexity of `ListNode.insert_before`?
    Constant

3.  What is the runtime complexity of `ListNode.delete`?
    Constant

4.  What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    Constant

5.  What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    Constant

6.  What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    Constant

7.  What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    Constant

8.  What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    Constant

9.  What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    Constant

10. What is the runtime complexity of `DoublyLinkedList.delete`?
    Constant

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

        the delete method runs much faster than the array method.  for my test it was ~4 times faster but this difference could be larger with larger sized arrays.
