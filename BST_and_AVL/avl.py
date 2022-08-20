# Name: Billy Fifield
# OSU Email: fifieldb@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 4
# Due Date: 5/16/2022
# Description: AVL Tree that includes an add and remove method that also rebalances
#           the BST.


import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object, node = None, p_node = None) -> None:
        """
        A method that adds a value to an AVL Tree and balances the tree with the new value.
        :param: value - the value to be added
        :param: node - the current node (used for recursion)
        :param: p_node - the parent node (used for recursion)
        :return: None
        """
        
        # Check to see if value should be the root
        if self._root == None:
            self._root = AVLNode(value)
            self._root.height = 1
            return

        if node == None:
            node = self._root
        
        # Iterate through the tree, comparing values until the place to add the value is found.
        while node is not None:
            if node.value > value:
                p_node = node
                if node.left is None:
                    node.left = AVLNode(value)
                    node = node.left
                    node.parent = p_node
                    break

                else:
                    node = node.left

            
            elif node.value < value:
                p_node = node
                if node.right is None:
                    node.right = AVLNode(value)
                    node = node.right
                    node.parent = p_node
                    break

                else:
                    node = node.right
            
            elif node.value == value:
                return

        if node.parent.left is None or node.parent.right is None:
            self._update_height(node)

        left = ''
        right = ''

        # Check to see if the tree is out of balance. If so, call the rebalance method
        # to determine if the tree needs to rotate left or right.
        if node.parent.parent is not None:
            if node.parent.parent.left == None:
                left = 0
            else:
                left = node.parent.parent.left.height
            
            if node.parent.parent.right == None:
                right = 0
            else:
                right = node.parent.parent.right.height

            if right > left:
                if node.parent.parent.left is not None:
                    left += 1
                if abs(node.parent.parent.height - left) >= 2:
                    self._rebalance(node.parent, value, 'right')
    
            elif left > right:
                if node.parent.parent.right is not None:
                    right += 1
                if abs(node.parent.parent.height - right) >= 2:
                    self._rebalance(node.parent, value, 'left')



    def remove(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        pass

    # Experiment and see if you can use the optional                         #
    # subtree removal methods defined in the BST here in the AVL.            #
    # Call normally using self -> self._remove_no_subtrees(parent, node)     #
    # You need to override the _remove_two_subtrees method in any case.      #
    # Remove these comments.                                                 #
    # Remove these method stubs if you decide not to use them.               #

    def _remove_two_subtrees(self, parent: AVLNode, node: AVLNode) -> None:
        """
        TODO: Write your implementation
        """
        pass

    # It's highly recommended to implement                          #
    # the following methods for balancing the AVL Tree.             #
    # Remove these comments.                                        #
    # Remove these method stubs if you decide not to use them.      #
    # Change these methods in any way you'd like.                   #

    def _balance_factor(self, node: AVLNode) -> int:
        """
        A method that finds the balance factor of a node.
        """
        if node is None:
            return 0
        
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_height(self, node: AVLNode) -> int:
        """
        A method that gets the height of a node.
        """
        if node is None:
            return 0
        else:
            return node.height

    def _rotate_left(self, node: AVLNode, num_of_rotations) -> AVLNode:
        """
        A method that rotates a tree left around a certain node.
        """
        tmp_r = node.right
        tmp_l = None
        if tmp_r.left is not None:
            tmp_l = tmp_r.left

        if node == self._root:
            node.right = node.right.left
            tmp_r.left = node
            tmp_r.left.parent = tmp_r
            tmp_r.parent = None

        
        else:
            p_tmp = node.parent
            node.right = node.right.left
            tmp_r.left = node
            tmp_r.left.parent = tmp_r
            tmp_r.parent = p_tmp
            tmp_r.parent.right = tmp_r

        if tmp_l is not None:
            tmp_r.left.right = tmp_l

        if tmp_r.left.left is None and tmp_r.left.right is None:
            tmp_r.left.height = 0
        else:
            tmp_r.left.height = 1 + max(self._get_height(tmp_r.left.left), self._get_height(tmp_r.left.right))
        tmp_r.height = 1 + max(self._get_height(tmp_r.left), self._get_height(tmp_r.right))
        if num_of_rotations == 1:
            while tmp_r is not None:
                tmp_r = tmp_r.parent
            return tmp_r

        return tmp_r

    def _rotate_right(self, node: AVLNode, num_of_rotations) -> AVLNode:
        """
        A method that rotates a tree right around a certain node.
        """
        tmp_l = node.left
        tmp_r = None
        if tmp_l.right is not None:
            tmp_r = tmp_l.right

        if node == self._root:
            node.left = node.left.right
            tmp_l.right = node
            tmp_l.right.parent = tmp_l
            tmp_l.parent = None

        else:
            p_tmp = node.parent
            node.left = node.left.right
            tmp_l.right = node
            tmp_l.right.parent = tmp_l
            tmp_l.parent = p_tmp
            tmp_l.parent.left = tmp_l


        if tmp_r is not None:
            tmp_l.right.left = tmp_r

        
        if tmp_l.right.left is None and tmp_l.right.right is None:
            tmp_l.right.height = 0
        else:
            tmp_l.right.height = 1 + max(self._get_height(tmp_l.right.left), self._get_height(tmp_l.right.right))
        tmp_l.height = 1 + max(self._get_height(tmp_l.left), self._get_height(tmp_l.right))
        if num_of_rotations == 1:
            while tmp_l is not None:
                tmp_l = tmp_l.parent
            return tmp_l
        return tmp_l

    def _update_height(self, node: AVLNode) -> None:
        """
        A method that updates the heights for a certain node and it's ancestors.
        """
        if node == self._root:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        elif node.left is None and node.right is None:
            node.height = 0
            self._update_height(node.parent)
        else:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            self._update_height(node.parent)
        

    def _rebalance(self, node: AVLNode, val, side) -> None:
        """
        A method to rebalance the tree by finding which way the tree needs to be rotated.
        """

        if side == 'left' and val > node.parent.left.value:
            new_node = self._rotate_left(node, 2)
            self._root = self._rotate_right(new_node.parent, 1)

        elif side == 'left':
            self._root = self._rotate_right(node.parent, 1)

        elif side == 'right' and val < node.parent.right.value:
            new_node = self._rotate_right(node, 2)
            self._root = self._rotate_left(new_node.parent, 1)

        elif side == 'right':
            self._root = self._rotate_left(node.parent, 1)

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)

    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # test_cases = (
    #     (10, 20, 30, 40, 50),   # RR, RR
    #     (10, 20, 30, 50, 40),   # RR, RL
    #     (30, 20, 10, 5, 1),     # LL, LL
    #     (30, 20, 10, 1, 5),     # LL, LR
    #     (5, 4, 6, 3, 7, 2, 8),  # LL, RR
    #     (range(0, 30, 3)),
    #     (range(0, 31, 3)),
    #     (range(0, 34, 3)),
    #     (range(10, -10, -2)),
    #     ('A', 'B', 'C', 'D', 'E'),
    #     (1, 1, 1, 1),
    # )
    # for case in test_cases:
    #     tree = AVL(case)
    #     print('INPUT  :', case)
    #     print('RESULT :', tree)

    # print("\nPDF - method add() example 3")
    # print("----------------------------")
    # for _ in range(100):
    #     case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #     tree = AVL()
    #     for value in case:
    #         tree.add(value)
    #     if not tree.is_valid_avl():
    #         raise Exception("PROBLEM WITH ADD OPERATION")
    # print('add() stress test finished')

    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # test_cases = (
    #     ((1, 2, 3), 1),  # no AVL rotation
    #     ((1, 2, 3), 2),  # no AVL rotation
    #     ((1, 2, 3), 3),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 0),
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    # )
    # for case, del_value in test_cases:
    #     tree = AVL(case)
    #     print('INPUT  :', tree, "DEL:", del_value)
    #     tree.remove(del_value)
    #     print('RESULT :', tree)

    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # test_cases = (
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
    #     ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
    #     ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
    #     ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    # )
    # for case, del_value in test_cases:
    #     tree = AVL(case)
    #     print('INPUT  :', tree, "DEL:", del_value)
    #     tree.remove(del_value)
    #     print('RESULT :', tree)

    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # case = range(-9, 16, 2)
    # tree = AVL(case)
    # for del_value in case:
    #     print('INPUT  :', tree, del_value)
    #     tree.remove(del_value)
    #     print('RESULT :', tree)

    # print("\nPDF - method remove() example 4")
    # print("-------------------------------")
    # case = range(0, 34, 3)
    # tree = AVL(case)
    # for _ in case[:-2]:
    #     root_value = tree.get_root().value
    #     print('INPUT  :', tree, root_value)
    #     tree.remove(root_value)
    #     print('RESULT :', tree)

    # print("\nPDF - method remove() example 5")
    # print("-------------------------------")
    # for _ in range(100):
    #     case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #     tree = AVL(case)
    #     for value in case[::2]:
    #         tree.remove(value)
    #     if not tree.is_valid_avl():
    #         raise Exception("PROBLEM WITH REMOVE OPERATION")
    # print('remove() stress test finished')

    # print("\nPDF - method contains() example 1")
    # print("---------------------------------")
    # tree = AVL([10, 5, 15])
    # print(tree.contains(15))
    # print(tree.contains(-10))
    # print(tree.contains(15))

    # print("\nPDF - method contains() example 2")
    # print("---------------------------------")
    # tree = AVL()
    # print(tree.contains(0))

    # print("\nPDF - method inorder_traversal() example 1")
    # print("---------------------------------")
    # tree = AVL([10, 20, 5, 15, 17, 7, 12])
    # print(tree.inorder_traversal())

    # print("\nPDF - method inorder_traversal() example 2")
    # print("---------------------------------")
    # tree = AVL([8, 10, -4, 5, -1])
    # print(tree.inorder_traversal())

    # print("\nPDF - method find_min() example 1")
    # print("---------------------------------")
    # tree = AVL([10, 20, 5, 15, 17, 7, 12])
    # print(tree)
    # print("Minimum value is:", tree.find_min())

    # print("\nPDF - method find_min() example 2")
    # print("---------------------------------")
    # tree = AVL([8, 10, -4, 5, -1])
    # print(tree)
    # print("Minimum value is:", tree.find_min())

    # print("\nPDF - method find_max() example 1")
    # print("---------------------------------")
    # tree = AVL([10, 20, 5, 15, 17, 7, 12])
    # print(tree)
    # print("Maximum value is:", tree.find_max())

    # print("\nPDF - method find_max() example 2")
    # print("---------------------------------")
    # tree = AVL([8, 10, -4, 5, -1])
    # print(tree)
    # print("Maximum value is:", tree.find_max())

    # print("\nPDF - method is_empty() example 1")
    # print("---------------------------------")
    # tree = AVL([10, 20, 5, 15, 17, 7, 12])
    # print("Tree is empty:", tree.is_empty())

    # print("\nPDF - method is_empty() example 2")
    # print("---------------------------------")
    # tree = AVL()
    # print("Tree is empty:", tree.is_empty())

    # print("\nPDF - method make_empty() example 1")
    # print("---------------------------------")
    # tree = AVL([10, 20, 5, 15, 17, 7, 12])
    # print("Tree before make_empty():", tree)
    # tree.make_empty()
    # print("Tree after make_empty(): ", tree)

    # print("\nPDF - method make_empty() example 2")
    # print("---------------------------------")
    # tree = AVL()
    # print("Tree before make_empty():", tree)
    # tree.make_empty()
    # print("Tree after make_empty(): ", tree)
