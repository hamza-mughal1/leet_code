class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

f1 = ListNode(val=4)
f2 = ListNode(val=2,next=f1)
f3 = ListNode(val=1,next=f2)

s1 = ListNode(val=4)
s2 = ListNode(val=3,next=s1)
s3 = ListNode(val=1,next=s2)


def foo(head1, head2):
    dummy = ListNode()
    tail = dummy

    while head1 and head2:
        if head1.val <= head2.val:
            tail.next = head1
            head1 = head1.next
            tail = tail.next

        elif head2.val < head1.val:
            tail.next = head2
            head2 = head2.next
            tail = tail.next

    if head1 == None:
        tail.next = head2
    
    elif head2 == None:
        tail.next = head1

    return dummy.next



fi = foo( f3,s3)

while (fi):
    print(fi.val)
    fi = fi.next

