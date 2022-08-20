# Name: Billy Fifield
# OSU Email: fifieldb@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 05/02/2022
# Description: Queue Class using a singly Linked List.


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Adds a value to the queue.
        :param: value - the value to be added to the queue.
        :return: None
        """
        enq_node = SLNode(value)
        # enq_node.next = None
        if self.is_empty() is True:
            self._head = enq_node
            self._tail = self._head.next

        else:
            self._tail.next = enq_node

        self._tail = enq_node


    def dequeue(self) -> object:
        """
        Gets the first value that was entered into the queue.
        :returns: the value that is next to come out of the queue and removes it from the queue.
        """
        if self.is_empty() is True:
            raise QueueException

        deq_val = self._head.value
        self._head = self._head.next

        return deq_val

    def front(self) -> object:
        """
        Gets the first value that was entered into the queue.
        :returns: the value that is next to come out of the queue without removing it from the queue.
        """
        if self.is_empty() is True:
            raise QueueException

        return self._head.value

# ------------------- BASIC TESTING -----------------------------------------


# if __name__ == "__main__":
#
#     print("\n# enqueue example 1")
#     q = Queue()
#     print(q)
#     for value in [1, 2, 3, 4, 5]:
#         q.enqueue(value)
#     print(q)
#
#     print("\n# dequeue example 1")
#     q = Queue()
#     for value in [1, 2, 3, 4, 5]:
#         q.enqueue(value)
#     print(q)
#     for i in range(6):
#         try:
#             print(q.dequeue())
#         except Exception as e:
#             print("No elements in queue", type(e))
#     #
#     print('\n#front example 1')
#     q = Queue()
#     print(q)
#     for value in ['A', 'B', 'C', 'D']:
#         try:
#             print(q.front())
#         except Exception as e:
#             print("No elements in queue", type(e))
#         q.enqueue(value)
#     print(q)
