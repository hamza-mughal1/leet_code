class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self,val):
        if self.head == None:
            node = Node(val,None)
            self.head = node
            return
        node = self.head
        while node:
            if node.next == None:
                node.next = Node(val,None)
                return
            node = node.next
    
    def print(self):
        if self.head == None:
            print("linked_list is empty!")
            return
        lis = []
        node = self.head
        while node:
            lis.append(node.val)
            node = node.next
        print(lis)
        return

    def insert_at_beginning(self,val):
        if self.head == None:
            node = Node(val,None)
            self.head = node
            return
        
        node = Node(val,self.head)
        self.head = node
        return

    def len(self):
        num = 0
        node = self.head
        while node:
            if node.next == None:
                return num
            node = node.next
            num+=1
        return num

    def insert_at_index(self,val,index):
        if (self.head == None) or (0 > index) or  (index > self.len()+1):
            raise IndexError("index is not valid!")
        
        num = 0
        node = self.head
        while node:
            if num+1 == index:
                node.next = Node(val,node.next)
                return
            num+=1
            node = node.next

linked_list = LinkedList()
linked_list.insert_at_end(5)
linked_list.insert_at_end(6)
linked_list.insert_at_end(7)
linked_list.insert_at_end(5)
linked_list.insert_at_end(6)
linked_list.insert_at_end(7)
linked_list.insert_at_beginning("h")
linked_list.insert_at_beginning("i")
linked_list.insert_at_index("t", 0)

linked_list.print()
print(linked_list.len())