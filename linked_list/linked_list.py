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
    
    def reverse_iterative(self):
        previous_node = None
        current_node = self.head
        while current_node:
            #next_nodeの情報を残しておく
            next_node = current_node.next
            current_node.next = previous_node

            # 1つずらす
            current_node, previous_node = next_node, current_node

        self.head = previous_node
    
    def reverse_rec(self):
        def _reverse_rec(current_node, previous_node):
            if not current_node:
                return previous_node
            
            next_node = current_node.next
            current_node.next = previous_node
            return _reverse_rec(next_node, current_node)
        
        self.head = _reverse_rec(self.head, None)





if __name__ == "__main__":
    l = LinkedList()
    print(l.head)
    l.append(1)
    l.append(2)
    l.append(3)
    l.insert(0)
    l.print()
    # l.reverse_iterative()
    # l.print()
    l.reverse_rec()
    l.print()