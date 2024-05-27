from node import Node
from merge_sort import MergeSort


class Stack:

    def __init__(self):
        self.stack = None
        self.length = 0
        self.capacity = None
        self.current_index = 0

    def __iter__(self):
        self.capacity = self.stack
        self.current_index = 0
        return self

    def __next__(self):
        """If list is empty"""
        if self.capacity is None and self.stack is None or self.current_index >= self.length:
            raise StopIteration
        elif self.capacity is None and self.stack is not None:
            """Initialising the head of the list"""
            self.capacity = self.stack
        elif self.capacity is None:
            """Last element condition"""
            raise StopIteration
        """else"""
        value = self.capacity.value
        self.current_index += 1
        self.capacity = self.capacity.next
        return value

    def push(self, value):
        new_node = Node(value)    # create new node
        new_node.next, self.stack = self.stack, new_node
        self.length += 1    # increase the size of list

    def pop(self):
        temp, self.stack = self.stack, self.stack.next
        self.length -= 1    # decrease the size of list
        return temp.value

    def peek(self):
        return self.stack.value

    def contains(self, value):
        temp = self.stack
        while temp:
            if value is temp.value:
                return True
            temp = temp.next
        return False

    def size(self):
        return self.length

    def centre(self):
        """if stack is not empty
        Iterate till the mid
        """
        if self.length:
            temp = self.stack
            mid = self.length/2
            while mid:
                temp = temp.next
                mid -= 1
            return temp.value
        else:
            return "List is empty"

    def traverse(self):
        """If  stack is not empty"""
        if self.length:
            print("Values in Stack:-")
            temp = self.stack
            while temp:
                print(temp.value, "--->", end="")
                temp = temp.next
            print("NULL")
        else:
            print("Stack is Empty")

    def reverse(self):
        """If stack is not empty"""
        if self.size():
            temp = self.stack.next
            self.stack.next = None
            while temp:
                temp2 = temp.next
                temp.next = self.stack
                self.stack = temp
                temp = temp2
        else:
            return "Stack is Empty"

    def sort(self):
        self.stack = MergeSort().mergesort(self.stack)


if __name__ == "__main__":
    obj = Stack()
    obj.push(12)
    obj.push(22)
    obj.push(32)
    obj.push(42)
    obj.push(52)
    obj.traverse()
    print("Deleted Value = ", obj.pop())
    obj.traverse()
    print("Centre Value = ", obj.centre())
    print("Peek ", obj.peek())
    print(obj.contains(12))
    print(obj.contains(45))
    obj.traverse()
    obj.sort()
    obj.traverse()
    print(next(obj))
    print(next(obj))
    for i in obj:
        print(i)
    obj.reverse()
    obj.traverse()
