class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

    def has_value(self, value):
        """to compare the value with the node data"""
        if self.data == value:
            return True
        else:
            return False

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        return

    def append_val(self, x):
        """add x to the end of the list"""
        if not isinstance(x, Node):
            x = Node(x)
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

        return

    def __str__(self):
        # [5->4->10->1]
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            return "[" + to_print[:-2] + "]"
        return "[]"

    def add_to_start(self, x):
        """add x to the left of the list making it the head"""

        if not isinstance(x, Node)
        x = Node(x)

        if self.head is None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x
        return

        # if self.head == None:
        #     self.head = node
        # else:
        #     node.next = self.head
        #     self.head = node        


    def search_val(self, x):
        """return indices where x was found"""

        if self.head == None:
            print('The list is empty')
        else:
            curr = self.head
            while curr:
                if curr.data == x:
                    return True
                curr = curr.next
            return False



    def remove_val_by_index(self, x):
        """remove and return value at index x provided as parameter"""
        pass

    def length(self):
        """return the length of the list, rep'd by number of nodes"""
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def reverse_list_recur(self, current, previous):
        """reverse the sequence of node pointers in the linked list"""
        # [1->2->3] reverse pointers [1<-2<-3] turn to: [3->2->1]
        if self.head == None:
            return
        elif current.next == None:
            self.tail = self.head
            current.next = previous
            self.head = current
        else:
            next = current.next
            current.next = previous
            self.reverse_list_recur(next, current)







node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

my_list = LinkedList()

print(my_list)
my_list.append_val(node1)
my_list.append_val(node2)
my_list.append_val(node3)
my_list.append_val(node4)
my_list.append_val(5)
print(my_list)
my_list.length()
print(my_list)
print(my_list.search_val(1))


my_list.reverse_list_recur(my_list.head, None)
print(my_list)
