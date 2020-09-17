def find_smallest_missing_V1(arr):
  # O(n) solution
  idx = 0
  while True:
    if idx >= len(arr):
      return idx
    else:
      if arr[idx] != idx:
        return idx
      else:
        idx += 1

def find_smallest_missing(arr):
  # O(n) run time
  # cleaner code
    for i in range(0, len(arr)):
        if arr[i] != i:
            return i
    return len(arr)



def check(arr):
  # O(log n) solution using binary search
  # last num is greater than high
  low = 0
  high = len(arr) - 1

  # check if arr matches expected
  if arr[-1] == high:
    return len(arr)
  else:
    while low < high:
      mid = (high + low) // 2
      if mid == arr[mid]:
        # look for problems on the right
        low = mid + 1
      else:
        # look for problem on the left
        high = mid - 1
    
    return high




arr1 = [0, 1, 2, 3, 4, 5, 6]

print(check(arr1))
print(find_smallest_missing(arr1))

class Node:
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    return f"{self.value}"

def middle(node):
  mid_node = node
  cur_node = node
  inc_mid = False
  while cur_node.next:
    if inc_mid:
      mid_node = mid_node.next
    inc_mid = not inc_mid
    cur_node = cur_node.next
    
  return mid_node

def guided_middle(node):
  fast = node
  slow = node
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  return slow

narr = [5, 1, 3, 7, 11, 12, 2, 0, 21, 33, 15, 4, 6]
root = Node(narr[0])
n = root
for i in range(1, len(narr)):
  n.next = Node(narr[i])
  n = n.next

print(middle(root))
print(guided_middle(root))