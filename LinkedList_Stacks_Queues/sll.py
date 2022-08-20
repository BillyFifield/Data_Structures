# Name: Billy Fifield
# OSU Email: fifieldb@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 5/2/2022
# Description: A singly linked list including methods of: insert_front, insert_back,
#              insert_at_index, remove_at_index, remove, count, find, and slice.


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Insert a value at the front of the list (after the sentinel node).
        :param: value - the value to be inserted at the front of the list.
        :return: None
        """

        front_node = SLNode(value)

        # Point the new node.next to what comes after self._head.
        front_node.next = self._head.next

        # Make whatever is after the sentinel node equal to the new node.
        self._head.next = front_node


    def insert_back(self, value: object) -> None:
        """
        Insert a value at the end of the list.
        :param: value - the value to be inserted at the end of the list.
        :return: None
        """

        back_node = SLNode(value)
        if self.length() == 0:
            back_node.next = self._head.next
            self._head.next = back_node

        else:
            current = self._head.next
            index = 0

            # Iterate through the list until the final node is found, and then point
            # the final node.next to the new node.
            while index < self.length():
                if index == (self.length() - 1):
                    back_node.next = current.next
                    current.next = back_node
                    index += 1
                current = current.next
                index += 1


    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert a node containing a certain value at a specified index.
        :param: index - the index to insert the new node.
        :param: value - the value of the new node to be inserted.
        :return: None
        """
        index_node = SLNode(value)

        # Validate the index.
        if index < 0 or index > self.length():
            raise SLLException

        if index == 0:
            index_node.next = self._head.next
            self._head.next = index_node

        else:
            current = self._head.next
            next = 0

            # Iterate through the list until it is one less than the specified index and
            # then point the current_node.next to the new node and point that node to current.next
            while next <= (index - 1):
                if next == (index - 1):
                    index_node.next = current.next
                    current.next = index_node

                current = current.next
                next += 1

    def remove_at_index(self, index: int) -> None:
        """
        Remove a node at a specified index.
        :param: index - the index of the node to be removed.
        :return: None
        """

        # Validate the index.
        if index < 0 or index >= self.length():
            raise SLLException

        if index == 0:
            self._head.next = self._head.next.next

        else:
            next = 0
            current = self._head.next

            # Iterate through the list until one before the index is found.
            # Once found, set node.next equal to node.next.next.
            while next <= (index - 1):
                if next == (index - 1):
                    current.next = current.next.next

                current = current.next
                next += 1

    def remove(self, value: object) -> bool:
        """
        Remove the first node that is equal to the specified value and return True. If value
        is not found, return False.
        :param: value - the first node with this value will be removed from the list.
        :return: True if the value has been removed, otherwise False.
        """
        # Check to see if the list is empty.
        if self._head.next == None:
            return False

        current = self._head.next

        # Check to see if the first node after the sentinel is equal to value and remove it.
        if current.value == value:
            self._head.next = self._head.next.next
            return True

        # Create a count and iterate through the list until the value is found. The count
        # will allow us to know where the value is at in the list.
        count = 0
        for idx in range(self.length()):
            if current.value == value:
                break
            count += 1
            current = current.next

        # If the count has equal to the length of the list, then the value is not in the list.
        if count == self.length():
            return False

        # Iterate through the list for the length of the count - 1 and set that node.next to node.next.next
        new_current = self._head.next
        for idx in range(count):
            if idx == (count - 1):
                new_current.next = new_current.next.next
                return True
            new_current = new_current.next


    def count(self, value: object) -> int:
        """
        Find the frequency of the specified value in the list.
        :param: value - the value to find the frequency of.
        :return: the count of the frequency of the specified value.
        """

        # Create a count starting at 0 and increment by 1 for each time the value of a node
        # is equal to the specified value.
        count = 0
        current = self._head.next
        for idx in range(self.length()):
            if current.value == value:
                count += 1

            current = current.next

        return count

    def find(self, value: object) -> bool:
        """
        Check to see if a specified value is in the list.
        :param: value - the value to check in the list.
        :return: True if the value is in the list, otherwise False.
        """

        current = self._head.next
        for idx in range(self.length()):
            if current.value == value:
                return True
            current = current.next

        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Create a new singly linked list starting at the specified index of the original list
        for the specified size.
        :param: start_index - the index of the list that will begin the new list
        :param: size - the size of the new list.
        :return: new_lst - the new linked list after slicing the original list.
        """
        new_lst = LinkedList()

        # Validate the index and index + size.
        if start_index < 0 or start_index >= self.length() or (start_index + size) > self.length() or size < 0:
            raise SLLException

        if size == 0:
            return new_lst

        # Iterate through the list until the starting index is found. And then add the value
        # of each node to the new linked list for the specified size.
        current = self._head.next
        count = 0
        for idx in range(self.length()):
            if idx >= start_index:
                new_lst.insert_back(current.value)
                count += 1
                if count == size:
                    return new_lst

            current = current.next


# if __name__ == '__main__':

    # print('\n# insert_front example 1')
    # lst = LinkedList()
    # print(lst)
    # lst.insert_front('A')
    # lst.insert_front('B')
    # lst.insert_front('C')
    # print(lst)
    #
    # print('\n# insert_back example 1')
    # lst = LinkedList()
    # print(lst)
    # lst.insert_back('C')
    # lst.insert_back('B')
    # lst.insert_back('A')
    # print(lst)



    # print('\n# insert_at_index example 1')
    # lst = LinkedList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))

    # print('\n# remove_at_index example 1')
    # lst = LinkedList([1, 2, 3, 4, 5, 6])
    # print(lst)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    # print(lst)

    # print('\n# remove example 1')
    # lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(lst)
    # for value in [7, 3, 3, 3, 3]:
    #     print(lst.remove(value), lst.length(), lst)
    #
    # print('\n# remove example 2')
    # lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(lst)
    # for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
    #     print(lst.remove(value), lst.length(), lst)
    #
    # print('\n# count example 1')
    # lst = LinkedList([1, 2, 3, 1, 2, 2])
    # print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    # #
    # print('\n# find example 1')
    # lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Clause"])
    # print(lst)
    # print(lst.find("Waldo"))
    # print(lst.find("Superman"))
    # print(lst.find("Santa Clause"))
    #
    # print('\n# slice example 1')
    # lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # ll_slice = lst.slice(1, 3)
    # print(lst, ll_slice, sep="\n")
    # ll_slice.remove_at_index(0)
    # print(lst, ll_slice, sep="\n")
    #
    # print('\n# slice example 2')
    # lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    # print("SOURCE:", lst)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    # for index, size in slices:
    #     print("Slice", index, "/", size, end="")
    #     try:
    #         print(" --- OK: ", lst.slice(index, size))
    #     except:
    #         print(" --- exception occurred.")
