def mergeTwoList(list1,list2):
    array1 = []
    curr = list1.head
    while curr is not None:
        array1.append(curr.value)
        curr = curr.next
    curr = list2.head
    while curr is not None:
        array1.append(curr.value)
        curr = curr.next
    array1.sort()
    curr = None
    print("[",end="")
    for value in array1:
        if curr is None:
            curr = ListNode(value)
        else:
            node = ListNode(value)
            curr.next = node
            curr = node
        print(f"{curr.value}->", end = "")


    print("None]")



        


class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def append(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            return
        else:
            curr = self.head
            while True:
                if curr.next is None:
                    curr.next = node
                    break
                else:
                    curr = curr.next
    def insert(self,value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            return
        else:
            tmp = self.head
            self.head = node
            node.next = tmp

    def PrintLinkedList(self):
        curr = self.head
        while curr is not None:
            print(f"{curr.value}->",end = "")
            curr = curr.next
        print("None")
    

list1 = LinkedList()
list2 = LinkedList()
list1.append(9)
list1.append(3)
list1.append(10)
list2.append(3)
list2.append(9)
list2.append(2)
list1.PrintLinkedList()
list2.PrintLinkedList()
mergeTwoList(list1,list2)





