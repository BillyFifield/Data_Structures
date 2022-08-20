# Name: Billy Fifield
# OSU Email: fifieldb@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 4
# Due Date: 5/16/2022
# Description: A Binary Search Tree with add, remove, contains, inorder_traversal,
#           find_min, find_max, is_empty, and make_empty methods.


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.
        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the BST tree is correct.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object, node = None) -> None:
        """
        A method to add a value to a BST.
        :param: value - the value to be added
        :node: node - the current node (used for the recursive call)
        :return: None
        """

        # Initialize current node
        if node is None:
            node = self._root

        if self._root is None:
            self._root = BSTNode(value)

        # Check to see if the current node's value is greater than the value. If the node to
        # the left is None, then this node becmoes a node with the new value. Otherwise, the current
        # node moves left.
        elif (node.value > value):
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self.add(value, node.left)

        # The value is greater than or equal to the current node. If the node to the right is None,
        # then this node becomes a node with the new value. Otherwise, the current node moves right.
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self.add(value, node.right)

    def remove(self, value: object, parent = None, node = None) -> bool:
        """
        A method to remove a value from the BST.
        :param: value - the value to be removed.
        :param: parent - the parent node (used in the recursive call).
        :param: node - the current node (used in the recursive call).
        :return True if the value has been removed, otherwise returns False.
        """
        # Initialize the parent node and the current node.
        result = ''
        if parent is None and node is None:
            parent = self._root
            node = self._root

        if self._root is None:
            return False
        elif self._root.value == value and self._root.left is None and self._root.right is None:
            self._root = None 
            return True

        # Iterate through the tree, comparing the value with the values in the tree.
        # Once the value is found, then remove the node.
        else:
            if node is not None and node.value > value and node == self._root:
                result = self.remove(value, parent, node.left)
                if result == True:
                    return True
            elif node is not None and node.value > value:
                result = self.remove(value, node, node.left)
                if result == True:
                    return True
            elif node is not None and node.value < value and node == self._root:
                result = self.remove(value, parent, node.right)
                if result == True:
                    return True
            elif node is not None and node.value < value:
                result = self.remove(value, node, node.right)
                if result == True:
                    return True
            elif node is not None and node.value == value:
                if node.left is None and node.right is None:
                    result = self._remove_no_subtrees(parent, node)
                    if result == True:
                        return True
                elif (node.left is None and node.right is not None) or (node.right is None and node.left is not None):
                    if parent.value == value:
                        if parent.left is not None:
                            self._root = parent.left
                        elif parent.right is not None :
                            self._root = parent.right
                        return True
                    else:
                        if parent.left is not None and parent.value == value:
                            parent = parent.left
                        elif parent.right is not None and parent.value == value:
                            parent = parent.right
                        else:
                            result = self._remove_one_subtree(parent, node, value)
                            if result == True:
                                return True
                else:
                    result = self._remove_two_subtrees(parent, node, value)
                    if result == True:
                        return True
        
        return False

    # Consider implementing methods that handle different removal scenarios. #
    # Remove these comments.                                                 #
    # Remove these method stubs if you decide not to use them.               #
    # Change these methods in any way you'd like.                            #

    def _remove_no_subtrees(self, parent: BSTNode, node: BSTNode) -> None:
        """
        A method to remove a node with no subtrees.
        :param: parent - the parent of the node to be removed.
        :param: node - the node to be removed.
        """
        # remove node that has no subtrees (no left or right nodes)
        if parent.left is not None and parent.left == node:
            parent.left = None
        elif parent.right is not None and parent.right == node:
            parent.right = None
        return True
        

    def _remove_one_subtree(self, parent: BSTNode, node: BSTNode, value) -> None:
        """
        A method that removes a node with one subtree.
        :param: parent - the parent of the current node.
        :param: node - the node to be removed
        :value: the value of the node to be removed.
        :return: None
        """
        # remove node that has a left or right subtree (only)
        if node.left is None:
            new_node = node.right
        else:
            new_node = node.left

        if parent.right is not None and value == parent.right.value:
            parent.right = new_node
        elif parent.left is not None and value == parent.left.value:
            parent.left = new_node

            
        return True

    def _remove_two_subtrees(self, parent: BSTNode, node: BSTNode, value) -> None:
        """
        A method that removes a node if there are two subtrees to the node.
        :param: parent = the parent of the current node
        :param: node - the current node.
        :return: None
        """
        # remove node that has two subtrees
        # need to find inorder successor and its parent (make a method!)
        succ = node.right
        p_succ = node.right
        
        if node.right is None and node.left is not None:
            node.right = node.left
            node.left = None
        else:
            if succ.left is None:
                if parent.left == node:
                    tmp = node.left
                    node = node.right
                    node.left = tmp
                    parent.left = node
                elif parent.right == node:
                    tmp = node.left
                    node = node.right
                    node.left = tmp
                    parent.right = node
                else:
                    tmp = node.left
                    node = node.right
                    node.left = tmp
                    self._root = node
            else:
                if parent.left == node:
                    succ = node.right.left
                    while succ.left is not None:
                        succ = succ.left
                        p_succ = p_succ.left
                    tmp_val = succ.value
                    if succ.right is not None:
                        p_succ.left = succ.right
                    else:
                        p_succ.left = None
                    node.value = tmp_val
                    parent.left = node
                elif parent.right == node:
                    succ = node.right.left
                    while succ.left is not None:
                        succ = succ.left
                        p_succ = p_succ.left
                    tmp_val = succ.value
                    if succ.right is not None:
                        p_succ.left = succ.right
                    else:
                        p_succ.left = None
                    node.value = tmp_val
                    parent.right = node
                else:
                    succ = node.right.left
                    while succ.left is not None:
                        succ = succ.left
                        p_succ = p_succ.left
                    tmp_val = succ.value
                    if succ.right is not None:
                        p_succ.left = succ.right
                    else:
                        p_succ.left = None
                    parent.value = tmp_val
                    self._root = parent

        return True

    def contains(self, value: object, node = None) -> bool:
        """
        A method that checks to see if a value is inside the BST.
        :param: value - the value to check for inside the BST.
        :param: node - the current node (used in the recursive call).
        :return: True if the BST contains the value, otherwise returns False.
        """
        # Initialize the current node.
        if node is None:
            node = self._root

        if self._root is None:
            return False

        else:
            # If the current node's value is larger than the value, then move left in the tree.
            # However, if the node to the left is None, then return False.
            if node.value > value:
                if node.left is None:
                    return False
                return self.contains(value, node.left)

            # If the current node's value is less than the value, then move right in the tree.
            # However, if the node to the right is None, then return False.
            elif node.value < value:
                if node.right is None:
                    return False
                return self.contains(value, node.right)

            # If the current node is equal to the value, return True.
            elif node.value == value:
                return True
            


    def inorder_traversal(self, node = None) -> Queue:
        """
        A method that returns the values of the BST in order inside a Queue.
        :param: node - the current node (used in the recursive call).
        :return: node_queue - the Queue containing the ordered values from the tree.
        """
        # Initialize the current node.
        if node is None:
            node = self._root

        # Initialize the Queue and Stack
        node_queue = Queue()
        node_stack = Stack()

        if self._root is None:
            return node_queue

        else:
            # First move left on the tree, pushing the nodes onto the stack. Once every node
            # going left has been pushed onto the stack, and then they can be popped and moved into the
            # queue while also moving back right.

            while node is not None or node_stack.is_empty() == False:
                if node is not None:
                    node_stack.push(node)
                    node = node.left

                elif node_stack.is_empty() == False:
                    node = node_stack.pop()
                    node_queue.enqueue(node.value)
                    node = node.right
        
        return node_queue

    def find_min(self, node = None) -> object:
        """
        A method that returns the minimum value in the tree.
        :param: node - the current node (used in the recursive call).
        :return: the minimum value of the BST.
        """
        # Initialize the current node.
        if node is None:
            node = self._root

        if self._root is None:
            return None
        
        # Move left until the next left value is None, and then return the value of the
        # current node.
        else:
            if node.left is None:
                return node.value
            else:
                return self.find_min(node.left)

    def find_max(self, node = None) -> object:
        """
        A method that returns the maximum value in the tree.
        :param: node - the current node (used in the recursive call).
        :return: the maximum value of the BST.
        """
        # Initialize the current node.
        if node is None:
            node = self._root

        if self._root is None:
            return None
        
        # Move right until the next right value is None, and then return the value of the
        # current node.
        else:
            if node.right is None:
                return node.value
            else:
                return self.find_max(node.right)

    def is_empty(self) -> bool:
        """
        A method that checks if the BST is empty.
        :return: True if the BST is empty, otherwise returns False.
        """
        if self._root is None:
            return True
        
        return False

    def make_empty(self) -> None:
        """
        A method that makes the BST empty by setting the root node to None.
        :return: None
        """
        self._root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    # print("\nPDF - method add() example 1")
    # print("----------------------------")
    # test_cases = (
    #     (1, 2, 3),
    #     (3, 2, 1),
    #     (1, 3, 2),
    #     (3, 1, 2),
    # )
    # for case in test_cases:
    #     tree = BST(case)
    #     print(tree)

    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # test_cases = (
    #     (10, 20, 30, 40, 50),
    #     (10, 20, 30, 50, 40),
    #     (30, 20, 10, 5, 1),
    #     (30, 20, 10, 1, 5),
    #     (5, 4, 6, 3, 7, 2, 8),
    #     (range(0, 30, 3)),
    #     (range(0, 31, 3)),
    #     (range(0, 34, 3)),
    #     (range(10, -10, -2)),
    #     ('A', 'B', 'C', 'D', 'E'),
    #     (1, 1, 1, 1),
    # )
    # for case in test_cases:
    #     tree = BST(case)
    #     print('INPUT  :', case)
    #     print('RESULT :', tree)

    # print("\nPDF - method add() example 3")
    # print("----------------------------")
    # for _ in range(100):
    #     case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #     tree = BST()
    #     for value in case:
    #         tree.add(value)
    #     if not tree.is_valid_bst():
    #         raise Exception("PROBLEM WITH ADD OPERATION")
    # print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test = BST((97, -24, -87, 80, -75, -9, -40, -100, -67, -65))
    # test.add(32)
    # test.add(77)
    # test.add(49)
    # test.add(17)
    # test.add(-2)
    # test.add(55)
    # test.add(89)
    # test.add(1)

    # test.remove(32)
    # test.remove(49)
    # test_cases = (
    #     # ((1, 2, 3), 1),
    #     # ((1, 2, 3), 2),
    #     # ((1, 2, 3), 3),
    #     # ((50, 40, 60, 30, 70, 20, 80, 45), 0),
    #     # ((50, 40, 60, 30, 70, 20, 80, 45), 45),
    #     # ((50, 40, 60, 30, 70, 20, 80, 45), 40),
    #     ((32, 77, 49, 17, -2, 55, 89, -1), 32),
    #     ((77, 49, 17, -2, 55, 89, -1), 49),

    # )
    # for case, del_value in test:
    # tree = BST(test)
    print('INPUT  :', test)
    test.remove(97)
    print('INPUT  :', test)
    test.remove(-87)
    print('INPUT  :', test)
    test.remove(-75)
    # test.remove(del_value)
    print('RESULT :', test)

    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # test_cases = (
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 20),
    #     ((50, 40, 60, 30, 70, 20, 80, 15), 40),
    #     ((50, 40, 60, 30, 70, 20, 80, 35), 20),
    #     ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    # )
    # for case, del_value in test_cases:
    #     tree = BST(case)
    #     print('INPUT  :', tree, "DEL:", del_value)
    #     tree.remove(del_value)
    #     print('RESULT :', tree)

    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # case = range(-9, 16, 2)
    # tree = BST(case)
    # for del_value in case:
    #     print('INPUT  :', tree, del_value)
    #     tree.remove(del_value)
    #     print('RESULT :', tree)

    # print("\nPDF - method remove() example 4")
    # print("-------------------------------")
    # case = range(0, 34, 3)
    # tree = BST(case)
    # for _ in case[:-2]:
    #     root_value = tree.get_root().value
    #     print('INPUT  :', tree, root_value)
    #     tree.remove(root_value)
    #     if not tree.is_valid_bst():
    #         raise Exception("PROBLEM WITH REMOVE OPERATION")
    #     print('RESULT :', tree)

    # print("\nPDF - method contains() example 1")
    # print("---------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.contains(15))
    # print(tree.contains(-10))
    # print(tree.contains(15))

    # print("\nPDF - method contains() example 2")
    # print("---------------------------------")
    # tree = BST()
    # print(tree.contains(0))

    # print("\nPDF - method inorder_traversal() example 1")
    # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.inorder_traversal())

    # print("\nPDF - method inorder_traversal() example 2")
    # print("---------------------------------")
    # tree = BST([8, 10, -4, 5, -1])
    # print(tree.inorder_traversal())

    # print("\nPDF - method find_min() example 1")
    # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree)
    # print("Minimum value is:", tree.find_min())

    # print("\nPDF - method find_min() example 2")
    # print("---------------------------------")
    # tree = BST([8, 10, -4, 5, -1])
    # print(tree)
    # print("Minimum value is:", tree.find_min())

    # print("\nPDF - method find_max() example 1")
    # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree)
    # print("Maximum value is:", tree.find_max())

    # print("\nPDF - method find_max() example 2")
    # print("---------------------------------")
    # tree = BST([8, 10, -4, 5, -1])
    # print(tree)
    # print("Maximum value is:", tree.find_max())

    # print("\nPDF - method is_empty() example 1")
    # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print("Tree is empty:", tree.is_empty())

    # print("\nPDF - method is_empty() example 2")
    # print("---------------------------------")
    # tree = BST()
    # print("Tree is empty:", tree.is_empty())

    # print("\nPDF - method make_empty() example 1")
    # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print("Tree before make_empty():", tree)
    # tree.make_empty()
    # print("Tree after make_empty(): ", tree)

    # print("\nPDF - method make_empty() example 2")
    # print("---------------------------------")
    # tree = BST()
    # print("Tree before make_empty():", tree)
    # tree.make_empty()
    # print("Tree after make_empty(): ", tree)
