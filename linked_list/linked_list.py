class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
    def remove(self, data):
        # head == dataのときheadをremove
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return 

        previous_node = None
        # current_node == dataになるまで動かす
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
            
        # current_node == dataが存在しないとき
        if current_node is None:
            return
        # current_node
        previous_node.next = current_node.next
        current_node = None
        
if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.insert(0)
    l.remove(2)
    l.remove(1)
    l.print()