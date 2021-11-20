class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None

    def insertAtBegining(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAtEnd(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        point = self.head
        while point.next != None:
            point = point.next
        point.next = node
    
    def insertAt(self, index,data):
        if index == 0:
            self.insertAtBegining(data)
            return
        elif index<0 or index>self.length():
            print("Invalid Index !")
            return
        flag = 0 
        point = self.head
        while point:
            if flag == index-1 :
                node = Node(data)
                node.next = point.next
                point.next = node 
                break
            point = point.next
            flag +=1

    def insertFormList(self,arr):
        for i in arr:
            self.insertAtEnd(i)
    
    def deleteFirst(self):
        if self.head == None:
            print("No node available for delete")
            return
        temp = self.head
        self.head = self.head.next
        del temp
    
    def deleteEnd(self):
        if self.head == None or self.head.next == None:
            self.head = None
            return
        point = self.head
        while point.next.next:
            point= point.next
        point.next = None

    def deleteAt(self, index):
        if index<0 or index>=self.length():
            print("Invalid Index !")
            return  
        if index == 0:
            self.head = self.head.next
            return
        flag = 0
        point = self.head
        while point:
            if flag == index-1:
                point.next = point.next.next
                break
            point = point.next
            flag+=1

    def length(self):
        count = 0
        point = self.head
        while point:
            count+=1
            point = point.next
        return count

    def printLL(self):
        if self.head == None :
            print("Singly linklist is empty")
            return
        point = self.head
        LL = ""
        while point:
            LL = LL + str(point.data) + " --> "
            point = point.next
        print(LL)

if __name__ == "__main__":
    sll = SLL()
    # sll.insertAtBegining(12)
    # sll.insertAtBegining(14)
    # sll.insertAtEnd(10)
    # sll.insertAtBegining(24)
    # sll.insertAtEnd(67)
    # sll.deleteFirst()
    sll.insertFormList([2,3,6,4])
    # sll.deleteAt(0)
    # sll.deleteEnd()
    sll.insertAt(0,123)
    sll.printLL()
    # print(sll.length())
    