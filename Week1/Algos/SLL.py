class Node:
    def __init__(self, val=None):
        self.val = val
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.val)
            printval = printval.nextval
    def insert_node_at_begining(self, val):
        newNode = Node(val)
        newNode.nextval = self.head
        self.head = newNode
    def remove_head(self):
        if self.head:
            self.head = self.head.nextval
        else:
            return None
    def return_head(self):
        if self.head:
            return self.head.val
        else:
            return None

list = SLinkedList()
list2 = SLinkedList()
list.head = Node(7)
e2 = Node(81)
e3 = Node(3)

# Link first Node to second node
list.head.nextval = e2

# Link second Node to third node
e2.nextval = e3
print("first list")
list.listprint()
list.insert_node_at_begining(44)
print("second list")
list.listprint()
print("third list")
list.remove_head()
list.listprint()
print(list2.return_head())
print(list.return_head())

