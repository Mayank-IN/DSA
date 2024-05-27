from node import Node


class HashTable:

    def __init__(self, size=50):
        self.size = size
        self.hash_table = [None] * self.size
        self.length = 0

    def __iter__(self):
        for node in self.hash_table:
            if node:
                temp = node
                while temp:
                    key, value = temp.key, temp.value
                    yield key, value
                    temp = temp.next

    """Hash Function"""
    def hash_code(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_code(key)   # index for key value to add
        new_node = Node(value, key)   # new node is created

        """If key already exist"""
        if index in self.hash_table:
            self.hash_table[index].next = new_node
        else:
            self.hash_table[index] = new_node
        self.length += 1     # increase the size of priority queue

    def delete(self, key):
        index = self.hash_code(key)
        temp = self.hash_table[index]
        while temp:
            if temp.key == key:
                if temp.next is None:
                    self.hash_table[index] = None
                    return key, temp.value
            elif temp.next.key == key:
                val = temp.next.value
                temp.next = temp.next.next
                return key, val
            else:
                return "No such key"
            temp = temp.next

    def contains(self, key):
        index = self.hash_code(key)
        temp = self.hash_table[index]
        while temp:
            if temp.key == key:
                return True
            temp = temp.next
        return False

    def get_value_by_key(self, key):
        index = self.hash_code(key)
        temp = self.hash_table[index]
        while temp:
            if temp.key == key:
                return temp.value
            temp = temp.next
        return "Invalid key"

    def size(self):
        return self.length

    def traverse(self):
        for item in self.hash_table:
            if item:
                temp = item
                while temp:
                    print(f"key: {temp.key}, value: {temp.value}")
                    temp = temp.next


if __name__ == "__main__":
    obj = HashTable()
    obj.insert("anuj", 23)
    obj.insert("may", 26)
    obj.insert("anj", 2)
    obj.insert("anu", 323)
    obj.insert("anuj", 2453)
    print(obj.get_value_by_key("anuj"))
    obj.traverse()
    # print(obj.size())
    print(obj.contains("anuj"))
    print(obj.delete("anuj"))
    obj.traverse()
    x = iter(obj)
    print(next(x))
    print(next(x))
    print(next(x))
