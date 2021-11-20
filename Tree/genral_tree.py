class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def insertChild(self,child):
        child.parent = self
        self.children.append(child)

    def level(self):
        l = 0
        p = self.parent
        while p:
            p = p.parent 
            l+=1
        return l
    def printTree(self):
        print("    "*self.level()+"|-->"+self.data)
        if self.children:
            for child in self.children:
                child.printTree()

def tree():
    root = TreeNode("AutoMobile")

    car = TreeNode("Car")
    car.insertChild(TreeNode("Swift"))               
    car.insertChild(TreeNode("Vista"))
    car.insertChild(TreeNode("Alto"))

    bike = TreeNode("Bike")
    bike.insertChild(TreeNode("HF-Delux"))
    bike.insertChild(TreeNode("Shine"))
    bike.insertChild(TreeNode("Splender"))
    bike.insertChild(TreeNode("KTM"))

    sportvehicle = TreeNode("Sport Vehicle")
    sportvehicle.insertChild(TreeNode("Bolaro"))
    sportvehicle.insertChild(TreeNode("Sfari"))
    sportvehicle.insertChild(TreeNode("Scorpio"))


    root.insertChild(car)
    root.insertChild(bike)
    root.insertChild(sportvehicle)

    return root

if __name__ == "__main__":
    t = tree()
    t.printTree()

    