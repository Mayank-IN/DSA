from math import ceil


class PriorityQueue:
    """Priority Queue is implemented using binary max heap

    reverse_flag :- indicate difference between max heap and min heap
    reverse_flag :
                    1 => Max Heap
                    -1 => Min Heap
    """

    def __init__(self):
        self.queue = []
        self.reverse_flag = 1

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        while self.size() != self.count:
            self.count += 1
            return self.queue[self.count]
        raise StopIteration

    def enqueue(self, value):
        self.queue.append(value*self.reverse_flag)
        self.bubble_up(self.size() - 1)

    def dequeue(self):
        self.queue[0], self.queue[self.size() - 1] = self.queue[self.size() - 1], self.queue[0]
        val = self.queue.pop()
        self.bubble_down(0)
        return val*self.reverse_flag

    """Bubbling up the value """
    def bubble_up(self, child):
        if child == 0:
            return
        """Calculate the position of parent"""
        parent = (child-1)//2
        """if child is greater than parent then swap it"""
        if self.queue[child] >= self.queue[parent]:
            self.queue[parent], self.queue[child] = self.queue[child], self.queue[parent]
            self.bubble_up(parent)  # Recursion Call

    """Bubbling down the value"""
    def bubble_down(self, parent):
        temp = parent

        """index of left child of the parent"""
        left = 2*parent + 1

        """index of right child of parent"""
        right = 2*parent + 2

        """if left child is greater than parent"""
        if left < self.size() and self.queue[left] >= self.queue[temp]:
            temp = left

        """if right is greater than left child"""
        if right < self.size() and self.queue[right] >= self.queue[temp]:
            temp = right

        """Swap parent with largest element at position temp"""
        if temp != parent:
            self.queue[temp], self.queue[parent] = self.queue[parent], self.queue[temp]
            self.bubble_down(temp)  # Recursion Call

    def peek(self):
        return self.queue[0]*self.reverse_flag

    def contains(self, value):
        if value in self.queue:
            return True
        return False

    def size(self):
        return len(self.queue)

    def reverse(self):
        """changing the reverse_flag"""
        self.reverse_flag *= -1
        reverse = self.queue  # temp queue
        self.queue = []       # make queue empty
        for val in reverse:
            self.enqueue(val)   # Reinserting the value in queue

    def center(self):
        if self.size():
            return self.queue[ceil(len(self.queue)/2)]*self.reverse_flag
        return "Empty Priority Queue"

    def traverse(self):
        if self.size():
            for val in self.queue:
                print(val*self.reverse_flag, "-->", end="")
            print("NULL")
        return "Empty Priority Queue"


if __name__ == "__main__":
    obj = PriorityQueue()
    obj.enqueue(23)
    obj.enqueue(53)
    obj.enqueue(73)
    obj.enqueue(3)
    obj.enqueue(13)
    obj.traverse()
    obj.traverse()
    print(obj.peek())
    print(obj.center())
    print(obj.size())
    print(obj.contains(23))
    print(obj.contains(233))
    obj.reverse()
    obj.traverse()
    obj.enqueue(83)
    obj.enqueue(2)
    obj.traverse()
    print(obj.dequeue())
    obj.traverse()
