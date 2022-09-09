from typing import Optional

# init linkedlist in python
class Node():
    def __init__(self, val, node=None):
        self.val = val
        self.next = node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def initLinkedList(self, data):
        self.head = Node(data[0])
        cur = self.head

        for i in data[1:]:
            cur.next = Node(i)
            cur = cur.next

    def isEmpty(self):
        if self.head.next == None:
            return True
        else:
            return False

    def getLength(self):
        if self.isEmpty():
            exit(0)

        p = self.head
        lenOfList = 0
        while p:
            lenOfList += 1
            p = p.next
        return lenOfList

    def traverse(self):
        if self.isEmpty():
            exit(0)
        p = self.head
        while p:
            print(p.val)
            p = p.next




def findLongestList(head: Optional[Node]) -> Optional[Node]:
    l = r = head
    length = 1
    res = -float('infinity')
    while r and r.next:
        tmp = r.next
        # if increase
        if tmp.val > r.val:
            if length > res:
                res = length
                # cut the linkedlist
                head = l
                r.next = None

            length = 1  # init the length to 1
            r = tmp  # r continue to traverse
            l = r  # l is the start of new sublist

        # if tmp.val <= r.val
        # move to the next node, length++
        else:
            length += 1
            r = r.next

    return head


data = [5,4,3,5,4,3,2]
l = Node(-1)
dummy = l
for i in data:
    l.next = Node(i)
    l = l.next

head = dummy.next
# while head:
#     print(head.val)
#     head = head.next

sublist = findLongestList(head)
while sublist:
    print(sublist.val)
    sublist = sublist.next