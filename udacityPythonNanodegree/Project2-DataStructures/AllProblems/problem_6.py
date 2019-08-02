class Node(object):
    def __init__(self, value):
        self.next = None
        self.value = value

    def __repr__(self):
        return str(self.value)

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.num_entries = 0
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.num_entries += 1
            return
        
        node = Node(value)
        node.next = self.head
        self.head = node
        self.num_entries += 1
    
    def size(self):
        return self.num_entries

    def __str__(self):
        out_string = ""
        node = self.head
        while node is not None:
            out_string += str(node.value)+" -> "
            node = node.next
        return out_string

def union(list1, list2):
    union = []
    node1 = list1.head
    node2 = list2.head
    while node1 is not None:
        if node1.value not in union:
            union.append(node1.value)
        node1 = node1.next
    
    while node2 is not None:
        if node2.value not in union:
            union.append(node2.value)
        node2 = node2.next
    return union
    
def intersection(list1, list2):
    inter = []
    node1 = list1.head    
    while node1 is not None:
        node2 = list2.head
        while node2 is not None:
            if node1.value == node2.value and node1.value not in inter:
                inter.append(node1.value)                
                break
            node2 = node2.next
        node1 = node1.next
    return inter

# Test case 1
# Union and Intersection is not Null
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2
# Union is not null, intersection is Null
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3
# Both union and intersection is Null
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
