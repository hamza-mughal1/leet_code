# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

seven = ListNode(7, None)
six = ListNode(6, seven)
five = ListNode(5, six)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)

def with_rec(head):
    global final_node
    final_node = None
    def rec(head):
        global final_node
        if head.next == None:
            final_node = head
            return head
        rec(head.next).next = head
        head.next = None
        return head
    
    rec(head)
    return final_node

def with_itr(head):
    if head == None:
        return None
    elif head.next == None:
        return head
    
    elif head.next.next == None:
        head.next.next = head.val
        te = head.next
        head.next = None
        te.next = head
        return te


    temp = head
    temp2 = head.next
    temp3 = temp2.next
    temp.next = None

    while temp3.next != None:
        temp2.next = temp
        temp = temp2
        temp2 = temp3
        temp3 = temp3.next

    temp2.next = temp
    temp3.next = temp2

    return temp3

head = with_itr(one)

for i in range(1):
    print(head.val)
    head = head.next