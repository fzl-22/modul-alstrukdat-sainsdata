class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def push_back(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    
    def push_front(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        
    
    def delete(self, data):
        if self.is_empty():
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current_node = self.head
        prev_node = None
        
        while current_node:
            if current_node.data == data:
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node =  current_node.next
        print("None")

def main():
    linked_list = LinkedList()
    
    linked_list.push_front(0)
    linked_list.push_front(3)
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_front(0)
    linked_list.push_back(3)
    linked_list.delete(2)
    linked_list.print_list()

if __name__ == "__main__":
    main()