def RemoveDups(Linkedlist):
  head = Linkedlist
  track = []
  while head:
    if head.data in track:
      head = head.next
    else:
      track.append(head.data)
      head.next
  return Linkedlist

class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next

Linkedlist = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
print(RemoveDups(Linkedlist))
