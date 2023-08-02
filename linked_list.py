class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - data and a link to the next node in the list
    """
    
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return "<Node data: %s>" %self.data
    
class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        
        """
        Returns the number of nodes in the list
        Takes linear time
        """
        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.next_node
            
        return count
    
    def add(self, data):
        """Adds a new node containing data at the head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def search(self, key):
        """Search for the first node that matches the key
        Returns the node or 'None' if not found
        Takes O(n) time
        """
        current = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
                
        return None    
        
    def insert(self, data, index):
        """Inserts a new node at index position
        Takes overall O(n) time

        Args:
            data (_type_): _description_
            index (_type_): _description_
        """
        if index == 0:
            self.add(data)
        
        elif index > 0:

            new = Node(data)
            
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            
            prev = current
            next = current.next_node
            
            prev.next_node = new
            new.next_node = next
    
    
    def remove(self, key):
        """Removes node containig data that matches the key
        Takes O(n) time 

        Args:
            key (_type_): _description_

        Returns:
            Node or Nonde if key doesn't exist
        """
        current = self.head
        previous = None
        
        found = False
        
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
                
        return current
    
    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            
            while position < index:
                current = current.next_node
                position += 1
                
            return current
    
    def __repr__(self):
        """ 
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
            
        return  '-> '.join(nodes)
    