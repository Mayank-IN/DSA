
class MergeSort:

    def mergesort(self, head):

        """Base Condition"""
        if head.next is None:
            return head

        mid = self.mid(head)
        nextid, mid.next = mid.next, None

        left_node = self.mergesort(head)
        right_node = self.mergesort(nextid)

        return self.merge(left_node, right_node)

    def merge(self, left_node, right_node):
        """Base Condition"""
        if left_node is None:
            return right_node
        elif right_node is None:
            return left_node

        if left_node.value <= right_node.value:
            result = left_node
            result.next = self.merge(result.next, right_node)
        else:
            result = right_node
            result.next = self.merge(left_node, result.next)

        return result

    @staticmethod
    def mid(head):
        middle = head
        temp = head

        while temp.next is not None and temp.next.next is not None:
            middle = middle.next
            temp = temp.next.next

        return middle
