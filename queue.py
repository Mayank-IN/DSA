from linkedlist import Linkedlist


class Queue:
    """Calling Methods from linked list"""

    def __init__(self):
        self.queue = Linkedlist()

    def __iter__(self):
        current = self.queue.head
        while current:
            yield current.value
            current = current.next

    def enqueue(self, value):
        self.queue.insert(value)

    def dequeue(self):
        if self.size():
            return self.queue.delete()
        else:
            return "Queue is Empty"

    def peek(self):
        if self.size():
            return self.queue.head.value
        else:
            return "Queue is Empty"

    def contains(self, value):
        if self.size():
            temp = self.queue.head
            while temp:
                if temp.value == value:
                    return True
                temp = temp.next
            return False
        else:
            return "Queue is Empty"

    def size(self):
        return self.queue.size()

    def center(self):
        return self.queue.center()

    def sort(self):
        self.queue.head = self.queue.sort()

    def reverse(self):
        return self.queue.reverse()

    def traverse(self):
        self.queue.traverse()


if __name__ == "__main__":
    obj = Queue()
    obj.enqueue(23)
    obj.enqueue(13)
    obj.enqueue(3)
    obj.enqueue(73)
    obj.traverse()
    print(obj.dequeue())
    obj.traverse()
    obj.enqueue(23)
    obj.sort()
    obj.traverse()
    for i in obj:
        print(i)
    x = iter(obj)
    print(next(x))
