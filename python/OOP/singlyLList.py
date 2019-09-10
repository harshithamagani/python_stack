class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class SLList:
    def __init__(self):
        self.head=None
    
    def add_to_front(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node

def add_to_back(self,value):
    new_node=Node(value)
    if self.head==None:
        self.head=new_node
        else:
            runner = self.head
            while runner.next != None:
                runner=runner.next
            runner.next=new_node

def remove_from_front(self):
    if self.head.next != None:
        head=None
    else:
        current = self.head.next
        head=current
                
def remove_from_back(self):
    if self.head.next==None:
        self.head=None
    else:
        current=self.head
        prev=None
        while current.next != None:
            prev=current
            current=current.next
        prev.next=None

def print_values(self):
    runner = self.head
    while runner != None:
        print(runner.value)
        runner=runner.next





