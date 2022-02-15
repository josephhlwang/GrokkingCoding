# What I've Learned

# Pattern Sliding Window

 Problem: Given list, find continuous pattern.

 Solution: Think about: 1, condition to shrink window; 2, condition to return result.
 Keep track of left_index pointer.

 Program Structure:

 ```python
def sliding_window(list, pattern):

    # var to keep track of left index
    left = 0

    # var to keep track of when to shrink window
    # use dicts, count or sets
    counter = 0

    # track min max
    min_len = 0

    for i in range(len(list)):
        
        # update counter
        if list[i] matches condition
             do something to counter
 
        if counter matches end condition
            return min_len
        
        # window needs shrinking
        while shrink condition:
            # move left counter
            left+=1
            do something to counter

        # update min max
        min_len = min(min_len,1+right-left)

 ```

 # Pattern Two Pointers

 Problem: Given list, do something with sorted list.

 Solution: If each element needs to be visited twice, iterate both pointers from one side of the list. If you're adding, iterate one pointer at each side of the list.

 Program Structure:

 ```python
def two_pointers(list):
    left = 0
    right = len(list)-1

    while l<r:
        if solution:
            return solution
        elif left needs moving:
            left+=1
        else:
            right-=1
 ```

  # Pattern Fast and Slow Pointers

  Problem: Given a linked list, detect cycle, find halfpoint

  Solution: If a cycle exists, a 2x fast pointer and a 1x slow pointer ran from the same starting node will end up at the same node. To find half point, run a 2x fast pointer and a 1x slow pointer until fast pointer reaches then end; the slow pointer is the halfpoint.

   ```python
def fast_slow_pointers(head):
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            #cycle exists

            
 ```