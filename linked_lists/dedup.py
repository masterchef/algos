import time
class Node(object):
  def __init__(self, value, next_node = None):
    self.value = value
    self.next = next_node

  def next(self):
    return self.next

  def delete(self, value):
    n = self
    if n.value == value:
      return n.next

    while n and n.next:
      if n.next.value == value:
        n.next = n.next.next
        return self
      n = n.next

  def __str__(self):
    result = str(self.value)
    if self.next:
      result += ',' + str(self.next)
    return result

def sumTwo(node1, node2, remainder = 0):
  # Return the non empty node
  if not node1:
    return node2
  elif not node2:
    return node1

  result = Node(None)
  new_value = node1.value + node2.value + remainder
  if new_value >= 10:
    new_value = new_value - 10
    remainder = 1
  print 'adding:', node1.value, '+', node2.value, '+', remainder
  result.value = new_value
  result.next = sumTwo(node1.next, node2.next, remainder)
  return result


node4 = Node(5)
node3 = Node(1, node4)
num1 = Node(3, node3)

node4 = Node(2)
node3 = Node(9, node4)
num2 = Node(5, node3)

print num1, '+', num2, sumTwo(num1, num2)