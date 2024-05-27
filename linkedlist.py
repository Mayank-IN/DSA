from node import Node
from merge_sort import MergeSort


class Linkedlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    """Insertion at given position"""

    def insert_at(self, position, value):
        if self.length + 1 >= position >= 1:
            new_node = Node(value)

            """Inserting at head"""
            if position == 1:
                new_node.next = self.head
                self.head = self.tail = new_node

            elif position == self.length + 1:
                """Insertion at end point"""
                self.tail.next = self.tail = new_node

            else:
                """Inserting between the in list"""
                temp = self.head
                position -= 2
                while position:
                    temp = temp.next
                    position -= 1
                new_node.next = temp.next
                temp.next = new_node
            self.length += 1
        else:
            print("Can't Insert : Position is Out of Bound")

    """Simple Insertion means Insertion at last"""

    def insert(self, value):
        self.insert_at(self.length + 1, value)

    """Deletion at given position"""

    def delete_at(self, position):
        if self.length >= position >= 1:
            temp = self.head
            if position == 1:
                self.head = temp.next
                self.length -= 1
                if position == self.length:
                    self.tail = None
                return temp.value

            position -= 2
            """Traversing the List just before the deleted position"""
            while position:
                temp = temp.next
                position -= 1
            if temp.next is self.tail:
                self.tail = temp
            val = temp.next.value
            temp.next = temp.next.next
            self.length -= 1
            return val
        elif self.head is None:
            return "List is Empty"
        else:
            return "Can't delete : Position is Out of Bound"

    """Deletion at the end"""

    def delete(self):
        """Deletion at end means deletion at last position"""
        return self.delete_at(1)

    """Return the middle value in list"""
    def center(self):
        if self.length == 0:
            return "Empty"
        else:
            mid = self.length / 2
            temp = self.head
            while temp:
                if mid == 0:
                    return temp
                mid -= 1
                temp = temp.next

    def reverse(self):
        """if List is empty"""
        if self.head is None:
            print("List is Empty")
            return
        """else"""
        self.tail = self.head
        temp = self.head.next
        self.head.next = None
        while temp:
            temp2 = temp.next
            temp.next = self.head
            self.head = temp
            temp = temp2

    def size(self):
        return self.length

    def traverse(self):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        while temp:
            print(str(temp.value), "-->", end="")
            temp = temp.next
        print("NULL")

    def sort(self):
        self.head = MergeSort().mergesort(self.head)
        return self.head


if __name__ == "__main__":
    obj = Linkedlist()
    obj.insert(12)
    obj.insert(13)
    obj.insert(14)
    obj.insert(15)
    obj.insert(127)
    obj.traverse()
    obj.reverse()
    obj.traverse()
    print(obj.size())
    print(obj.delete())
    obj.traverse()
    obj.insert_at(3, 45)
    obj.insert_at(1, 45)
    obj.insert_at(8, 45)
    obj.traverse()
    print(obj.center().value)
    print(obj.head.value)
    obj.sort()
    obj.traverse()
    print(obj.delete_at(6), "\n")
    for i in obj:
        print(i)
