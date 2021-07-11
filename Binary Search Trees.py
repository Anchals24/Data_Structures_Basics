class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None


class Binarysearchtree:
    def __init__(self):
        self.root = None

    def insertion(self , troot , ele):
        temp = None # "temp" : it will be used to find out the position >> where to insert.
        while troot:
            temp = troot
            if ele == troot.data:
                return
            elif ele < troot.data:
                troot = troot.left
            elif ele > troot.data:
                troot = troot.right

        new = Node(ele)
        if self.root :
            if ele < temp.data:
                temp.left = new
            else:
                temp.right = new
        else:
            self.root = new

    

    def __recursiveinsertion__(self , troot , ele):
        if troot:
            if ele < troot.data:
                troot.left = self.__recursiveinsertion__(troot.left , ele)
            elif ele > troot.data:
                troot.right = self.__recursiveinsertion__(troot.right , ele)
        else:
            n = Node(ele)
            troot = n
        return troot
    
    def inorder(self , troot):
        if troot:
            self.inorder(troot.left)
            print(troot.data , end = " ")
            self.inorder(troot.right)


BST = Binarysearchtree()
#BST.insertion(BST.root , 40)
#BST.insertion(BST.root , 30)
#BST.insertion(BST.root , 89)
BST.root = BST.__recursiveinsertion__(BST.root, 16)
BST.__recursiveinsertion__(BST.root , 12)
BST.__recursiveinsertion__(BST.root , 10)
BST.__recursiveinsertion__(BST.root , 20)
BST.__recursiveinsertion__(BST.root , 32)

BST.inorder(BST.root)

#create a program : without using troot!

