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
            
   def _search_(self , key):
        troot = self.root
        if key == troot.data:
            return True
        elif key < troot.data:
            troot = troot.left
        elif key > troot.data:
            troot = troot.right
        return False

    def __recursivesearch__(self , troot, key):
        if troot:
            if key == troot.data:
                return True
            elif key < troot.data:
                return self.__recursivesearch__(troot.left , key)
            elif key > troot.data:
                return self.__recursivesearch__(troot.right , key)
        else:
            return False
            
    def __deletion__(self , key):
        p = self.root
        pp = None
        while p and p.data != key:
            pp = p
            if key < p.data:
                p = p.left
            else:
                p = p.right
        if not p:
            return False
        if p.left and p.right:
            maxi = p.left
            while maxi.right:
                maxi = maxi.right
            p.data = maxi.data
        c = None
        if p.left:
            c = p.left
        else:
            c = p.right
        if p == self.root:
            self.root = None
        else:
            if p == pp.left:
                pp.left = c
            else:
                pp.right = c


    

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

