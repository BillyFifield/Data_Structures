# Name: Billy Fifield
# OSU Email: fifieldb@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 5
# Due Date: 5/23/2022
# Description: A Min Heap that includes methods such as: add, is_empty, get_min, remove_min,
#              build_heap, size, clear, and a heapsort function outside of the MinHeap class.

from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def get_parent(self, index) -> None:
        """
        A method to get the parent node of a certain node.
        :param: index - the index of the child node
        :return: None
        """
        return (index - 1) // 2

    def get_left(self, index) -> int:
        """
        A method to get the index of left child node.
        :param: index - the index of the parent node.
        :return: the index of the left child node.
        """
        return (2 * index) + 1

    def get_right(self, index) -> int:
        """
        A method to get the index of the right child node.
        :param: index - the index of the parent node.
        :return: the index of the right child node
        """
        return (2 * index) + 2

    def perc_up(self, index) -> None:
        """
        A method that perculates up the heap until the node is at the top of the heap or the node is greater
        than it's parent node.
        :param: index - the index of the node that will perculate up (if applicable)
        :return: None
        """
        new_index = index

        # Move up the heap until the node is at the top, or it's parent node is smaller than the node.
        while self._heap[new_index] < self._heap[self.get_parent(new_index)]:
            parent = self.get_parent(new_index)
            self._heap[new_index], self._heap[parent] = self._heap[parent], self._heap[new_index]
            new_index = parent
            if new_index == 0:
                break

    def perc_down(self, index) -> None:
        """
        A method that perculates down the heap until the node is less than both of it's child nodes or is 
        at the bottom of the heap.
        :param: index - the starting index the node that will perculate down (if applicable)
        :return: None
        """

        new_index = index
        idx_range = self._heap.length() - 1
        try:
            # Move down the heap until the node is at the bottom or the node is less than both of it's child nodes.
            while new_index < self._heap.length():
                left = self.get_left(new_index)
                right = self.get_right(new_index)
                
                if left > idx_range and right > idx_range:    # Check the range of the child nodes.
                    return
                
                # Check if the left node is less than the node and the right node is out of range (at the bottom of the heap).
                elif left <= idx_range and self._heap[left] < self._heap[new_index] and right > idx_range:
                    self._heap[new_index], self._heap[left] = self._heap[left], self._heap[new_index]
                    return

                # Check if the right node is less than the node.
                elif self._heap[left] > self._heap[right] and self._heap[new_index] > self._heap[right] and right <= idx_range:
                    self._heap[new_index], self._heap[right] = self._heap[right], self._heap[new_index]
                    new_index = right
               

                # Check if the left node is less than the node.
                elif self._heap[left] <= self._heap[right] and self._heap[new_index] > self._heap[left] and left <= idx_range:
                    self._heap[new_index], self._heap[left] = self._heap[left], self._heap[new_index]
                    new_index = left
                    
                else:
                    return
        except:
            return

    def add(self, node: object) -> None:
        """
        An add method that will add a node to the heap | runtime = O(log N)
        :param: node - the node that will be added to the heap.
        :return: None
        """
        self._heap.append(node)

        index = self._heap.length() - 1

        # Move the new node upde the heap if applicable.
        if index != 0 and self._heap[index] < self._heap[self.get_parent(index)]:
            self.perc_up(index)



    def is_empty(self) -> bool:
        """
        A method that checks to see if the heap is empty | runtime = O(1)
        :return: True if the heap is empty, otherwise returns False.
        """
        if self._heap.length() == 0:
            return True
        else:
            return False

    def get_min(self) -> object:
        """
        A method that returns the minimum object in the heap | runtime = O(1)
        :return: the minimum object (the object at the top of the heap)
        """
        if self.is_empty():
            raise MinHeapException

        return self._heap[0]

    def remove_min(self) -> object:
        """
        A method that returns the minimum object and then removes it from the heap | runtime = O(log N)
        :return: None
        """
        if self.is_empty():
            raise MinHeapException

        min = self.get_min()
    
        # Swap the first and last nodes in the index. Remove the now new last node and then percolate
        # the new first node down the heap.
        self._heap[0], self._heap[self._heap.length() - 1] = self._heap[self._heap.length() - 1], self._heap[0]
        self._heap.pop()
        self.perc_down(0)

        return min

    def build_heap(self, da: DynamicArray) -> None:
        """
        A method that builds a heap from a Dynamic Array | runtime = O(N)
        :param: da - the Dynamic Array that will be used to create the heap.
        :return: None
        """
        
        # Create a heap with the Dynamic Array.
        new_heap = DynamicArray()
        for idx in range(da.length()):
            new_heap.append(da[idx])
        
        self._heap = new_heap
        idx = self.get_parent(self._heap.length() - 1)     # Find index starting at the parent of the last node.

        while idx >= 0:
            left = self.get_left(idx)
            right = self.get_right(idx)

            # Check to see if the right index is out of range. If so, check if left is in range and if that node is 
            # less than the current node.
            if right >= self._heap.length():
                if self._heap[idx] > self._heap[left]:
                    self._heap[idx], self._heap[left] = self._heap[left], self._heap[idx]
                    idx -= 1
                else:
                    idx -= 1

            # Check if the left child is less than the parent node.
            elif self._heap[idx] > self._heap[left] and self._heap[left] <= self._heap[right]:
                self._heap[idx], self._heap[left] = self._heap[left], self._heap[idx]
                new_left = self.get_left(left)
                new_right = self.get_right(left)

                # Check if the child nodes of the left child of the original node is less than either child.
                # If so, then start the loop back over so the left child can be moved down the heap.
                if new_right < self._heap.length():
                    if self._heap[left] > self._heap[new_left] or self._heap[left] > self._heap[new_right]:
                        idx = left
                    else:
                        idx -= 1
                
                # If the right child is out of range, check if the left child is less than the parent node.
                elif new_right >= self._heap.length() and new_left < self._heap.length():
                    if self._heap[new_left] < self._heap[left]:
                        idx = left
                    else:
                        idx -= 1
                else:
                    idx -= 1

            # Check if the right child is less than the parent node.
            elif self._heap[idx] > self._heap[right] and self._heap[right] < self._heap[left]:
                self._heap[idx], self._heap[right] = self._heap[right], self._heap[idx]
                new_left = self.get_left(right)
                new_right = self.get_right(right)

                # Check if the child nodes of the right child of the original node is less than either child.
                # If so, then start the loop back over so the right child can be moved down the heap.
                if new_right < self._heap.length():
                    if self._heap[right] > self._heap[new_left] or self._heap[right] > self._heap[new_right]:
                        idx = right
                    else:
                        idx -= 1

                # If the right child is out of range, check if the left child is less than the parent node.
                elif new_right >= self._heap.length() and new_left < self._heap.length(): 
                    if self._heap[new_left] < self._heap[right]:
                        idx = right
                    else:
                        idx -= 1
                else:
                    idx -= 1
            else:
                idx -= 1

        return


    def size(self) -> int:
        """
        A method that returns the size of the heap | runtime = O(1)
        :return: the size of the heap
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        A method that clears the heap | runtime = O(1)
        :return: None
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    A method that takes a Dynamic Array and sorts it using heap sort | runtime = O(N log N)
    :param: da - the Dynamic Array that will be sorted using heap sort.
    :return: None
    """
    # Pass the dynamic array to the build heap function to change the order of the DA to a Min Heap.
    build_helper(da)
    idx = da.length() - 1
    if idx == 1:
        if da[0] < da[idx]:
            da[idx], da[0] = da[0], da[idx]
    else:
        parent = 0    # Keep track of how many nodes have been sorted to the end of the array so they do not get replaced.

        # Swap values with the first node and the last node, and then percolate the new first node down to the appropriate spot.
        while idx > 0:
            da[idx], da[0] = da[0], da[idx]
            parent += 1
            if (da.length() - parent - 1) > 1:
                _percolate_down(da, parent)
                idx -= 1
            else:
                idx -= 1
                if da[0] < da[idx]:
                    da[idx], da[0] = da[0], da[idx]
                idx -= 1




# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def build_helper(da: DynamicArray) -> None:
    """
    A build heap helper function that will convert a Dynamic Array into a Min Heap.
    :param: da - the Dynamic Array that will be converted.
    :return: None
    """
    left = (2 * 0) + 1
    right = (2 * 0) + 2
    parent = ((da.length() - 1) - 1) // 2 

    idx = parent
    while idx >= 0:
        left = (2 * idx) + 1
        right = (2 * idx) + 2
        # Check to see if the right index is out of range. If so, check if left is in range and if that node is 
        # less than the current node.
        if right >= da.length():
            if da[idx] > da[left]:
                da[idx], da[left] = da[left], da[idx]
                idx -= 1
            else:
                idx -= 1

        # Check if the left child is less than the parent node.
        elif da[idx] > da[left] and da[left] <= da[right]:
            da[idx], da[left] = da[left], da[idx]
            new_left = (2 * left) + 1
            new_right = (2 * left) + 2

            # Check if the child nodes of the left child of the original node is less than either child.
            # If so, then start the loop back over so the left child can be moved down the heap.
            if new_right < da.length():
                if da[left] > da[new_left] or da[left] > da[new_right]:
                    idx = left
                else:
                    idx -= 1

            # If the right child is out of range, check if the left child is less than the parent node.
            elif new_right >= da.length() and new_left < da.length():
                if da[new_left] < da[left]:
                    idx = left
                else:
                    idx -= 1
            else:
                idx -= 1

        # Check if the right child is less than the parent node.     
        elif da[idx] > da[right] and da[right] < da[left]:
            da[idx], da[right] = da[right], da[idx]
            new_left = (2 * right) + 1
            new_right = (2 * right) + 2

            # Check if the child nodes of the right child of the original node is less than either child.
            # If so, then start the loop back over so the right child can be moved down the heap.
            if new_right < da.length():
                if da[right] > da[new_left] or da[right] > da[new_right]:
                    idx = right
                else:
                    idx -= 1
            
            # If the right child is out of range, check if the left child is less than the parent node.
            elif new_right >= da.length() and new_left < da.length():
                if da[new_left] < da[right]:
                    idx = right
                else:
                    idx -= 1
            else:
                idx -= 1
        else:
            idx -= 1
        
    # return da

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    A helper function that perculates down the heap until the node is less than both of it's child nodes or is at the bottom of the heap.
    :param: da = the heap that will get traversed.
    :parent: parent = the parent of the node to keep track of the end of the heap.
    :return: None
    """

    new_index = 0
    idx_range = da.length() - 1 - parent
    try:
        # Move down the heap until the node is at the bottom or the node is less than both of it's child nodes.
        while new_index < idx_range:
            left = (2 * new_index) + 1
            right = (2 * new_index) + 2
            if left > idx_range and right > idx_range:    # Check the range of the child nodes.
                return
            
            # Check if the left node is less than the node and the right node is out of range (at the bottom of the heap).
            elif left <= idx_range and da[left] < da[new_index] and right > idx_range:
                da[new_index], da[left] = da[left], da[new_index]
                return

            # Check if the right node is less than the node.
            elif da[left] > da[right] and da[new_index] > da[right] and right <= idx_range:
                da[new_index], da[right] = da[right], da[new_index]
                new_index = right
                if new_index >= idx_range:
                    return

            # Check if the left node is less than the node.
            elif da[left] <= da[right] and da[new_index] > da[left] and left <= idx_range:
                da[new_index], da[left] = da[left], da[new_index]
                new_index = left
                if new_index >= idx_range:
                    return

            else:
                return
    except:
        return


# ------------------- BASIC TESTING -----------------------------------------


# if __name__ == '__main__':

#     print("\nPDF - add example 1")
#     print("-------------------")
#     h = MinHeap()
#     print(h, h.is_empty())
#     for value in range(300, 200, -15):
#         h.add(value)
#         print(h)

    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)

    # print("\nPDF - is_empty example 1")
    # print("-------------------")
    # h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    # print(h.is_empty())

    # print("\nPDF - is_empty example 2")
    # print("-------------------")
    # h = MinHeap()
    # print(h.is_empty())

    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())

    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    
    # h = MinHeap([-84962, -28092, -20617, 76433])
    # while not h.is_empty() and h.is_empty() is not None:
    #     print(h, end=' ')
    #     print(h.remove_min())

    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([29527, 74862, 8560, -26567, -75330, -89359])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)

    # print("--------------------------")
    # print("Inserting 500 into input DA:")
    # da[0] = 500
    # print(da)

    # print("Your MinHeap:")
    # print(h)
    # if h.get_min() == 500:
    #     print("Error: input array and heap's underlying DA reference same object in memory")

    # print("\nPDF - heapsort example 1")
    # print("------------------------")
    # da = DynamicArray([-57929, 21862, 6694, 37300, -57929, -4728, -98308])
    # print(f"Before: {da}")
    # heapsort(da)
    # print(f"After:  {da}")

    # print("\nPDF - heapsort example 2")
    # print("------------------------")
    # da = DynamicArray(['G', 'yybbWR_', 'zKqXhN_lMfC', 'uqsqWpaG', '[HWQSsly', 'gtX^]', 'O_Oi`^iIhbL', 'nfB_qtg', 'nFnAJve^', 'nfB_qtg'])
    # print(f"Before: {da}")
    # heapsort(da)
    # print(f"After:  {da}")

    # print("\nPDF - size example 1")
    # print("--------------------")
    # h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    # print(h.size())

    # print("\nPDF - size example 2")
    # print("--------------------")
    # h = MinHeap([])
    # print(h.size())

    # print("\nPDF - clear example 1")
    # print("---------------------")
    # h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    # print(h)
    # print(h.clear())
    # print(h)
