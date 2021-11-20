class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head = None
    
    def insertAtBegining(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head.prev = node
            self.head = node 

    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            point = self.head
            while point.next:
                point = point.next
            node = Node(data)
            point.next = node
            node.prev = point
    
    def insertAt(self, index,data):
        if index == 0:
            self.insertAtBegining(data)
        elif index<0 or index >= self.length():
            print("Invalid Index !")
        else:
            flag = 0
            point = self.head
            while point:
                if flag == index-1:
                    node = Node(data)
                    node.next= point.next
                    node.prev = point 
                    point.next.prev = node
                    point.next = node
                    break
                flag+=1
                point = point.next

    def length(self):
        count = 0
        point = self.head
        while point:
            count +=1
            point = point.next
        return count
    def printLL(self):
        if self.head is None:
            print("Doubly linklist is empty")
            return
        point = self.head
        LL =""
        while point:
            LL = LL+ str(point.data)+" <--> "
            point = point.next
        print(LL)

if __name__ == "__main__":
    dll = DLL()
    dll.insertAtEnd(12)
    dll.insertAtBegining(38)
    dll.insertAtEnd(33)
    dll.insertAt(2,23)
    dll.printLL()
    print(dll.length())