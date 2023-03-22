class Node(object):

    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.prev = next_node
        self.next = prev_node

class Doubly_LinkedList(object):

    def __init__(self, head=None):
        self.head=head
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data):
        current_node = self.head

        #要素の1つめが取り除くものだった時
        if current_node and current_node.data == data:
            # 要素が1つのリストだった時
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            
            else:
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return

        # 取り除く要素の位置まで進める
        while current_node and current_node.data != data:
            current_node = current_node.next
        
        # 要素がリストになかった時
        if current_node is None:
            return
        
        # 最後の要素が取り除くものだった時
        if current_node.next is None:
            prev_node = current_node.prev
            prev_node.next = None
            current_node = None
            return
        
        # 前後が存在して普通に取り除くとき
        else:
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next, next_node.prev = next_node, prev_node
            current_node = None
            return 
        
    def reverse_iter(self):
        previous_node = None
        current_node = self.head
        while current_node:
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            current_node = current_node.prev
            
            if previous_node:
                self.head = previous_node.prev
    
    def reverse_rec(self):
        def _reverse_rec(current_node):
            if not current_node:
                return None
            
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            if current_node.prev is None:
                return current_node
            
            return _reverse_rec(current_node.prev)
        
        self.head = _reverse_rec(self.head)

    def sort(self):
        if self.head == None:
            return
        
        current_node = self.head
        while current_node.next:
            next_node = current_node.next
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                next_node = next_node.next
            current_node = current_node.next

if __name__ == "__main__":
    l = Doubly_LinkedList()
    l.append(5)
    l.append(3)
    l.append(1)
    l.append(2)
    l.append(4)
    l.print()
    l.sort()
    l.print()
    

