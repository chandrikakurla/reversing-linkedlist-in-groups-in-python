#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linkedlist class
class LinkedList:
    def __init__(self):
        self.head=None
    #function for creating newnode and inserting it into linkedlist
    def insert(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        lastnode=self.head
        while(lastnode.next is not None):
            lastnode=lastnode.next
        lastnode.next=newnode
    #function for printing linkedlist elements
    def printllist(self,headnode):
        if headnode is None:
            print("linkedlist is empty")
            return
        currentnode=headnode
        while(currentnode is not None):
            print(currentnode.data)
            currentnode=currentnode.next
    #function for reversing linkedlist in groups
    def rev_llist_in_groups(self,headnode,n):
        currentnode=headnode
        previousnode=None
        nextnode=None
        count=0
        while(currentnode is not None and count<n ):
            nextnode=currentnode.next
            currentnode.next=previousnode
            previousnode=currentnode
            currentnode=nextnode
            count+=1
        if currentnode is not None:
            headnode.next=self.rev_llist_in_groups(currentnode,n)
        return previousnode

if __name__=="__main__":
    llist=LinkedList()
    for i in range(1,11):
        llist.insert(i)
    print("linkedlist before reversing")
    llist.printllist(llist.head)
    print("linkedlist after reversing in groups of given size")
    llist.head=llist.rev_llist_in_groups(llist.head,1)
    llist.printllist(llist.head)


    

