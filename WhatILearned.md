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

# Merge Intervals

Problem: Given a set of intervals, may or may not be mutually exclusive; Type 1. find a set of merge or intersection intervals. Type 2. find the max "load".

Solution: ALWAYS SORT BY START

Type 1 merge. Keep track of the current merged interval start and end. If the next interval starts before the merged end, merge(take max of ends, min of starts) the new interval. Otherwise, append the merged interval start and end.

```python
def merge_intervals(intervals):
    cur_start = intervals[0].start
    cur_end = intervals[0].end
    i = 1
    while i < len(intervals):
        if intervals[i].start <= cur_end:
            cur_end = max(intervals[i].end, cur_end)
        else:
            results.append(interval(cur_start, cur_end))
```

Type 1 intersection. Given two sets of intervals, if the top intervals intersect, append the intersection(take min of ends, max of starts). Otherwise, iterate the list that ends first.

```python
def intersect_intervals(intervals):
  while i < len(intervals_a) and j < len(intervals_b):
      if intervals intersect:
          results.append(#intersection)

      if intervals_a[i][end] < intervals_b[j][end]:
          i += 1
      else:
          j += 1
```

Type 2. Use priority queue to keep track of concurrent intervals. For each new interval, remove all intervals that finish before the new interval, then append. Keep track of max load.

```python
def max_load(intervals):
    cur_meetings = []

    for meeting in meetings:
        while cur_meetings and cur_meetings[0].end <= meeting.start:
            heappop(cur_meetings)
        heappush(cur_meetings, meeting)
        max_rooms = max(max_rooms, len(cur_meetings))
```

# Cyclic Sort

Problem: Given an array of size n with intergers from 1 to n; find the missing number or the duplicate number.

Solution: For each item in the array, swap it to the correct index if it's not at the correct index. Then go through the array to find dups and missing numbers.

```python
def cyclic_sort(arr):
 i = 0

 while i < len(arr):
     # correct index, -1 because nubmer from 1 to n
     j = arr[i] - 1

     if arr[j] != arr[i]:
         arr[j], arr[i] = arr[i], arr[j]
     else:
         i+=1

 for i in range(len(nums)):
     if nums[i] != i + 1:
         # return missing or dup
```

# Reversal of Linked List

Problem: Given a linked list reverse elements within it.

Solution: Iterate through the list and keep track of the previous node while using a temp to keep track of the next reversal node.

```python
def reverse(head):
 prev = None
 cur = head

 while cur:
     temp = cur.next
     cur.next = prev
     prev = cur
     cur = temp

 return prev
```

# BFS Binary Tree

Problem: Given a binary tree, do BFS traversal.

Solution: Loop through the queue while adding child nodes to end of queue. Continue until queue is empty. Keep track of the number of nodes in current level and next level to determine when to jump levels.

```python
def BFS(root):
 cur_level, next_level = 1, 0

 queue = [root]

 while queue:
     cur_node = queue.pop()
     cur_level -= 1
     # do something with current node

     if cur_node.left:
         queue.insert(0, cur_node.left)
         next_count += 1

     if cur_node.right:
         queue.insert(0, cur_node.right)
         next_count += 1

     if cur_count == 0:
         cur_count, next_count = next_count, 0
         # next level reached
```

# DFS Binary Tree

Problem: Given a binary tree, do DFS traversal.

Solution: Recurse through the root node calculating the path data as you go. Stop when you hit a leaf.

```python
def DFS(root):
    if not root:
        return

    if not root.left and not root.right:
        # reached leaf node

    DFS(root.left)
    DFS(root.right)
```

# Two Heaps

Problem: Two types: 1. Find median of data stream. 2. Min max two relating arrays.

Solution: 1. Use a max and a min heap to keep track of a sorted array; rebalance the heaps as arrays grow. 2. Use two heaps to track the contents of each of arrays. Always fix and loop through one heap while popping the other.

```python
def TWO_HEAPS_MEDIAN(nums):

    min_heap = []
    max_heap = []
    results = []

    for num in nums:
        # max_heap contains the odd lengths
        if not max_heap num <= -max_heap[0]:
            heappush(max_heap, -num)
        else:
            heappush(min_heap, num)

        # rebalance
        if len(min_heap) - 1 == len(max_heap):
            heappush(max_heap, -heappop(min_heap))
        elif len(min_heap) = len(max_heap) - 2:
            heappush(min_heap, -heappop(max_heap))

        # calculate median
```

```python
def TWO_HEAPS(arr1, arr2):

    heap1 = []
    heap2 = []

    for i in arr1:
        heappush(heap1, (arr1[i], i))
        heappush(heap2, (arr2[i], i))

    while heap1:
        dat1, i = heappop(heap1)

        while heap2 and heap2[0][0] < dat1:
            heappop(heap2)

        if not heap2:
            break

        # found dat1/i relation with in arr2.
```
