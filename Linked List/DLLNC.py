class Node:
    def __init__(self,element,n,p):
        self._element = element
        self._next = n
        self._prev = p  
class DLLNC:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size = 0
    def __len__(self):
        return self._size
    def isEmpty(self):
        return self._size == 0
    def addElementHead(self,e):
        baru = Node(e, None, None)
        if self.isEmpty()==True:
            self._head = baru
            self._tail = baru
            self._head._next = None
            self._head._prev = None
            self._tail._next = None
            self._tail._prev = None
        else:
            baru._next = self._head
            self._head._prev = baru
            self._head = baru
            self._size += 1
        print("Data masuk head!")
    def addElementTail(self,e):
        baru = Node(e, None, None)
        if self._tail == None:
            self._head = baru
            self._tail = baru
            self._head._next = None
            self._head._prev = None
            self._tail._next = None
            self._tail._prev = None
        else:    
            self._tail._next = baru
            baru._prev = self._tail
            self._tail = baru
            self._tail._next = None
            self._size += 1
        print("Data masuk tail!")
    def deleteFirst(self):
        if self.isEmpty()==False:
            d = ""
            if self._head._next==None:
                d = self._head._element
                self._head=None
                self._tail=None
            else:
                hapus = self._head
                d = hapus._element
                self._head = self._head._next
                self._head._prev = None
                del hapus
            self._size -= 1
            print(d," terhapus!")
        else:
            print("Kosong!")
    def deleteLast(self):
        if self.isEmpty() == False:
            d = None
            bantu = self._head
            if(self._head._next != None):
                hapus = self._tail
                self._tail = self._tail._prev
                d = hapus._element
                self._tail._next = None
                del hapus
            else:
                d = self._tail._element
                self._head=tail=None
            self._size -= 1
            print(d, " terhapus!")
        else:
            print("Kosong!")
    def printAll(self):
        if self.isEmpty()==False:
            bantu = self._head
            while(bantu!=self._tail._next):
                print(bantu._element," ",end='')
                bantu = bantu._next
            print()
        else:
            print("Kosong")
DD = DLLNC()
DD.addElementHead(14)
DD.addElementHead(8)
DD.addElementHead(20)
DD.addElementTail(11)
DD.addElementHead(21)
DD.printAll()
DD.deleteFirst()
DD.printAll()
