#print, get length, insert b, insert e, insert at, remove at,  insert_values
from itertools import count


class Node:
    
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head= None
    
    def insert_at_beg(self,data):
        node= Node(data, self.head)
        self.head= node
    
    def insert_at_end(self,data):
        if self.head is None:
            node=Node(data, self.head)
            self.head=node
            return
        
        itr= self.head
        while itr.next:
            itr=itr.next
        node = Node(data, None)
        itr.next=node

    def length(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count=count+1
        return count
    
    def printl(self):
        if self.head is None:
            raise Exception("Empty List")
        itr=self.head
        l=''
        while itr:
            l=l+str(itr.data)+"-->"
            itr=itr.next
        print(l)

    def insert_at(self,index,data):
        if index<0 or index> self.length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beg(data)
            return
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                node= Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count=count+1

    def remove_at(self,index):
        if index<0 or index> self.length():
            raise Exception("Invalid Index")
        count=0
        itr=self.head
        while itr:
            if count== index-1:
                itr.next = itr.next.next
                break
            count=count+1
            itr=itr.next



    def insert_values(self,data_list=[]):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)

    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        if self.head is None:
            raise Exception("Null List")
        itr=self.head
        while itr:
            if itr.data == data_after:
                node= Node(data_to_insert,itr.next)
                itr.next= node
                break
            itr=itr.next

    def remove_by_value(self, datas):
        # Remove first node that contains data
        if self.head is None:
            return

        if self.head.data == datas:
            self.head = self.head.next
            return    
        itr = self.head
        while itr.next:
            if itr.next.data == datas:
                itr.next=itr.next.next
                break
            itr=itr.next
        


                

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.printl()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.printl()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.printl()
    ll.remove_by_value("figs")
    ll.printl()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.printl()
