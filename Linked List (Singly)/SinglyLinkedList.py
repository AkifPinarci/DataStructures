
class Node:
  def __init__(self, value = None):
    self.value = value
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def addBack(self,data):
        NewNode = Node(data)
        if self.head.value == None:
            self.head = NewNode
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = NewNode

    def addFront(self,data):
        NewNode = Node(data)
        if self.head.value == None:
            self.head = NewNode
        else:
            NewNode.next = self.head
            self.head = NewNode

    def length(self):
        length = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            length += 1
             
        return length
    
    def display(self):
        elems =[]
        cur = self.head
        while cur:
            elems.append(cur.value)
            if cur.next == None:
                break
            cur = cur.next
        print(elems)
    
    def get(self, index):
        if index >= self.length():
            return None
        curIndex = 0
        cur = self.head
        while True:
            cur = cur.next
            if curIndex == index:
                return cur.value
            index += 1

    def deleteIndex(self, index):
        if index >= self.length():
            return None
        curIndex = 0
        cur = self.head
        while True:
            temp = cur
            cur = cur.next
            if curIndex == index:
                temp.next = cur.next
                break
            curIndex += 1
        
    def remove(self, data):
        cur = self.head
        temp = cur
        if self.head.value == data:
            self.head = self.head.next
        else:
            while cur.next != None:
                temp = cur
                cur = cur.next
                if cur.value == data:
                    temp.next = cur.next
                    break
    
    def removeAllElem(self, data):
        cur = self.head
        temp = cur
        if self.head.value == data:
            self.head = self.head.next
        while cur.next != None:
            temp = cur
            cur = cur.next
            if cur.value == data:
                temp.next = cur.next
                cur = temp

            


            
linkedlist = LinkedList()
linkedlist.display()
linkedlist.addFront(0)
linkedlist.addBack(1)
linkedlist.addBack(2)
linkedlist.addBack(3)
linkedlist.addBack(4)
linkedlist.addBack(4)
linkedlist.addBack(3)
linkedlist.addFront(0)
linkedlist.addFront(0)
linkedlist.addFront(0)
linkedlist.addFront(0)
linkedlist.addFront(5)
linkedlist.addBack(5)
linkedlist.display()

linkedlist.removeAllElem(0)
linkedlist.display()
