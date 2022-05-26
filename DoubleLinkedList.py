
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DLinkedList:

    def __init__(self):
        self.head= None

    def insert_at_beg(self,data):
        
        if self.head is None:
            node=Node(data)
            self.head = node
            return
        
        
        node=Node(data,next=self.head,prev=None)
        self.head=node
       
    
    def printl(self):
        itr = self.head
        ll=""
        while itr:
            ll=ll+str(itr.data)+'<-->'
            itr=itr.next
        print(ll)
    
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_beg(data)
            return
        itr=self.head
        while itr:
        
            if itr.next is None:
                node= Node(data,None,itr)
                itr.next=node
                break
            itr=itr.next
    
    def length(self):
        count=0
        itr=self.head
        while itr.next:
            itr=itr.next
            count=count+1
        
        return count
    
    def insert_at(self,data,index):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_beg(data)
        
        count=0
        itr=self.head
        while itr:
            if count ==index-1:
                node= Node(data,itr.next,itr.prev)
                itr.next=node
                break
            count=count+1
            itr=itr.next
    
    def remove_at(self,index):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head= self.head.next
            itr=self.head
            itr.prev= None
            return
        
        itr=self.head
        count=0
        while itr:
            if count==index:
                itr.prev.next=itr.next
                if itr.next:
                    itr.next.prev=itr.prev
                break
                # itr.next=itr.next.next
                # itr=itr.next
                # itr.prev=itr.prev.prev

                # break
            count+=1
            itr=itr.next
        
    def insert_values(self,data_list=[]):
        self.head=None
        for i in data_list:
            self.insert_at_end(i)
    
    def insert_after_value(self, data_after, data_to_insert):
        itr=self.head
        while itr:
            if itr.data==data_after:
                node=Node(data_to_insert,itr.next,itr)
                itr.next=node
                break
            itr=itr.next
    
    def remove_by_value(self,data):
        itr=self.head
        a=self.length()
        while itr.next:
            if itr.data==data:
                self.head=self.head.next
                self.head.prev= None
                
                break
            if itr.next.data== data:
                itr.next=itr.next.next
                itr=itr.next
                itr.prev= itr.prev.prev
                break
            itr=itr.next
        if self.length() == a:
            raise Exception("Value not found in list")

    def print_forward(self):
        itr=self.head
        ll=""
        while itr:
            ll=ll+str(itr.data)+"-->"
            itr=itr.next
        print(ll)

    def print_backward(self):
        itr=self.head
        ll=''
        while itr.next:
            itr=itr.next
        while itr:
            ll+=str(itr.data)+"<--"
            itr=itr.prev
        print(ll)
            
                            
            

            
if __name__ == "__main__":
    a=DLinkedList()
    a.insert_values(['Apple',"Banana","Orange","Jackfruit","Peach","Strawberry"])
    a.printl()
    a.insert_after_value("Banana","Lemon")
    a.printl()
    a.remove_by_value("Banana")
    a.remove_at(2)
    a.printl()
    a.print_forward()
    a.print_backward()
