
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
        """ Store the data, and set next to None"""

    def __str__(self):
        return str(self.data)
        """ Return a string representation of the data """


class Storage:
    
    def __init__(self):
        self.head = None
        """ Creates an empty Storage class. Sets head to None. """

    def push(self, data):
        new_node = Node(data)
        self.head = new_node
        """ Create a Node to hold the data, then put it at the head of the list. """

    def pop(self):
        """ Remove the head Node and return its data. """

    def peek(self):
        """ Return the data from the head Node, without removing it. """
        return self.head.data

    def isempty(self):
        """ Return True if the list is empty, otherwise False """
        return self.head is None
