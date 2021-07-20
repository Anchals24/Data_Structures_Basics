class Heaps:
    def __init__(self):
        self.maxsize = int(input())
        self.Heapdata = [-1] * self.maxsize
        self.csize = 0
    

    def insert(self , e):
        if self.csize == self.maxsize:
            print("Heap is full , can't insert.")
            return
        self.csize = self.csize + 1
        hsize = self.csize
        while e > self.Heapdata[hsize//2] and hsize > 1:
            self.Heapdata[hsize] =  self.Heapdata[hsize//2]
            hsize = hsize//2
        self.Heapdata[hsize] = e


    def leng(self):
        return len(self.Heapdata)
    
    def isempty(self):
        if len(self.Heapdata) == 0:
            return True
        return False
        
    def maxele(self):
        if self.csize == 0: 
            return "Heap is Empty"
        return self.Heapdata[1]

Heap = Heaps()
#print(Heap.isempty())
Heap.insert(5)
Heap.insert(22)
Heap.insert(12)
Heap.insert(19)
Heap.insert(100)
print(Heap.Heapdata)
Heap.insert(800)
print(Heap.Heapdata)
print("max element is : " , Heap.maxele())
#print(Heap.isempty())
