# Name: Billy Fifield
# OSU Email: fifieldb@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 05/02/2022
# Description: Queue Class using a Static Array.


from static_array import StaticArray


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue based on Static Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        size = self._current_size
        out = "QUEUE: " + str(size) + " element(s). ["

        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)

        if size > 0:
            out += str(self._sa[front_index])

        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size == 0

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size

    def _increment(self, index: int) -> int:
        """
        Move index to next position
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # employ wraparound if needed
        index += 1
        if index == self._sa.length():
            index = 0

        return index

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Adds a value to the queue.
        :param: value - the value to be added to the queue.
        :return: None
        """

        if self.is_empty() is True:
            self._sa[0] = value
            self._current_size += 1


        elif self.size() < self._sa.length():
            self._sa[self.size()] = value
            self._current_size += 1

        else:
            enq_arr = StaticArray(self.size() * 2)

            for idx in range(self.size()):
                enq_arr[idx] = self._sa[idx]
            enq_arr[self._current_size] = value
            self._current_size += 1
            self._sa = enq_arr



    def dequeue(self) -> object:
        """
        Gets the first value that was entered into the queue.
        :returns: the value that is next to come out of the queue and removes it from the queue.
        """
        if self.is_empty() is True:
            raise QueueException

        val = self._sa[0]
        if self.size() == 1:
            self._current_size -= 1
            self._sa = StaticArray()

        else:
            new_arr = StaticArray(self.size() - 1)
            idx = 1
            new_idx = 0
            while idx < self.size():
                new_arr[new_idx] = self._sa[idx]
                new_idx += 1
                idx += 1
            self._current_size -= 1
            self._sa = new_arr
        return val

    def front(self) -> object:
        """
        Gets the first value that was entered into the queue.
        :returns: the value that is next to come out of the queue without removing it from the queue.
        """
        if self.is_empty() is True:
            raise QueueException
        return self._sa[self._front]

    # The method below is optional, but recommended, to implement. #
    # You may alter it in any way you see fit.                     #

    def _double_queue(self) -> None:
        """
        TODO: Write this implementation
        """
        pass


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
#     for i in range(q.size() + 1):
#         try:
#             print(q.dequeue())
#         except Exception as e:
#             print("No elements in queue", type(e))
#     for value in [6, 7, 8, 111, 222, 3333, 4444]:
#         q.enqueue(value)
#     print(q)
#
#     print('\n# front example 1')
#     q = Queue()
#     print(q)
#     for value in ['A', 'B', 'C', 'D']:
#         try:
#             print(q.front())
#         except Exception as e:
#             print("No elements in queue", type(e))
#         q.enqueue(value)
#     print(q)
