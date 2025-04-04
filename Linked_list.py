class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self,head = None, tail = None):
        self.head = head
        self.tail = tail

#insert at head
    def insertAtHead(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


#insert at tail
    def insertAtTail(self,data):
        new_node = Node(data)
        #find the last node
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while (curr_node.next):
            curr_node = curr_node.next
        curr_node.next = new_node

#insert at a specific position
    def insertAtPosition(self, data, position):
        if position == 0:
            self.insertAtHead(data)
            return
        new_node = Node(data)
        curr_node = self.head
        for _ in range(position - 1):
            if curr_node is None:
                return
            curr_node = curr_node.next
        if curr_node is None:
            return
        new_node.next = curr_node.next
        curr_node.next = new_node


# Delete node at the beginning
    def deleteAtHead(self):
        if self.head is None:
            return
        self.head = self.head.next


# Delete node at the end
    def deleteAtTail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        curr_node = self.head
        while curr_node.next.next:
            curr_node = curr_node.next
        curr_node.next = None

# Delete node at a specific position
    def deleteAtPosition(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return
        curr_node = self.head
        for _ in range(position - 1):
            if curr_node is None:
                return
            curr_node = curr_node.next
        if curr_node is None or curr_node.next is None:
            return
        curr_node.next = curr_node.next.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



linkedList = LinkedList()
linkedList.insertAtHead(10)
linkedList.insertAtHead(20)
linkedList.insertAtHead(30)
linkedList.print_list()


linkedList.insertAtTail(40)
linkedList.insertAtTail(50)
linkedList.print_list()