# Name: Billy Fifield
# OSU Email: fifieldb@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 05/02/2022
# Description: Stack class using a singly Linked List.


from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
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
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Pushes the specified value onto the stack of the linked list.
        :param: value - the value to be pushed onto the stack.
        :return: None
        """
        front_node = SLNode(value)
        if self.is_empty() is True:
            self._head = front_node

        else:
            # Point the new node.next to what comes after self._head.
            front_node.next = self._head

            # Make whatever is after the sentinel node equal to the new node.
            self._head = front_node

    def pop(self) -> object:
        """
        Pops the value on top of the stack of the linked list.
        :return: None
        """
        if self.is_empty() is True:
            raise StackException

        pop_val = self._head.value
        self._head = self._head.next

        return pop_val

    def top(self) -> object:
        """
        Shows the value on top of the stack of the linked list without removing the value.
        :return: the value on top of the stack.
        """
        if self.is_empty() is True:
            raise StackException

        return self._head.value

# ------------------- BASIC TESTING -----------------------------------------


# if __name__ == "__main__":
#
#     print("\n# push example 1")
#     s = Stack()
#     print(s)
#     for value in [1, 2, 3, 4, 5]:
#         s.push(value)
#     print(s)
#
#     print("\n# pop example 1")
#     s = Stack()
#     try:
#         print(s.pop())
#     except Exception as e:
#         print("Exception:", type(e))
#     for value in [1, 2, 3, 4, 5]:
#         s.push(value)
#     for i in range(6):
#         try:
#             print(s.pop())
#         except Exception as e:
#             print("Exception:", type(e))
#     #
#     print("\n# top example 1")
#     s = Stack()
#     try:
#         s.top()
#     except Exception as e:
#         print("No elements in stack", type(e))
#     s.push(10)
#     s.push(20)
#     print(s)
#     print(s.top())
#     print(s.top())
#     print(s)
