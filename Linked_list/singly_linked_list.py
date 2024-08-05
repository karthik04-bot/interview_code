#Create nodes
#Create linked lists
#Add node to linked lists
#print linked list


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = newNode

    def insert_head_node(self,headnode):
        tempnode = self.head
        self.head = headnode
        self.head.next = tempnode
        del tempnode

    def insert_node_in_btn(self,newNode, position):
        currentnode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentnode
                break
            else:
                previousNode = currentnode
                currentnode = currentnode.next
                currentPosition += 1

    def printlist(self):
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode= currentnode.next



firstNode = Node("karthik")
linklist = LinkedList()
linklist.insert_node(firstNode)
secondNode = Node("bilebal")
linklist.insert_node(secondNode)
headnode = Node("Happy")
linklist.insert_head_node(headnode)
insert_node = Node("life")
linklist.insert_node_in_btn(insert_node , 1)

































# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert(self, newNode):
#         #head=>john->None
#         if self.head is None:
#             self.head = newNode
#         else:
#             #self.head.next = newNode
#             lastnode = self.head
#             while True:
#                 if lastnode.next is None:
#                     break
#                 else:
#                     lastnode = lastnode.next
#             lastnode.next = newNode
#
#     def printList(self):
#         currentNode = self.head
#         while True:
#             if currentNode is None:
#                 break
#             print(currentNode.data)
#             currentNode= currentNode.next
#
# #Node => data, next
# #firstnode.data => John and firstnode.next => None
# linkedList = LinkedList()
# firstnode = Node("John")
# linkedList.insert(firstnode)
# secondnode = Node("Ben")
# linkedList.insert(secondnode)
# linkedList.printList()
#
