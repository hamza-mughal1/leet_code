class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n: int):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    # delete
    left.next = left.next.next

    return dummy.next





node5 = ListNode(val = 5)
node4 = ListNode(val = 4, next = node5)
node3 = ListNode(val = 3, next = node4)
node2 = ListNode(val = 2, next = node3)
head = ListNode(val = 1, next = node2)

h2 = removeNthFromEnd(head, 2)