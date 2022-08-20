# Name: Billy Fifield
# OSU Email: fifieldb@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2
# Due Date: 4/25/2022
# Description: A bag Dynamic Array and methods to get multiple aspects of the bag
#              including add, remove, count, clear, equal, __iter__, and __next__


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Takes a value as a parameter and adds it to the bag.
        :param: value - the value to be added
        :return: None
        """
        # Call the append method in the Dynamic Array class to add it to the bag.
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes a single value taken as parameter from the Dynamic Array. If the value
        is removed, it returns True. Otherwise, it returns False.
        :param: value - the value to be removed from the bag.
        :return: a bool: True - if the value is removed from the bag, otherwise returns False.
        """

        # Search for the value in the bag and then call the remove_at_index method
        # in the Dynamic Array class to remove it.
        for idx in range(self.size()):
            if self._da.get_at_index(idx) == value:
                self._da.remove_at_index(idx)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Takes a value as a parameter and returns the count of the number of times
        the value is in the Dynamic Array.
        :param: value - the value to search through the bag to see how many times the value
                    is in the bag.
        :return: count - the frequency of which the value is in the bag.
        """
        count = 0

        # Search for the value in the bag and increment count each time it is found.
        for idx in range(self.size()):
            if self._da.get_at_index(idx) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Clears the bag of all values in the Dynamic Array.
        :return: None
        """
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        Compares two bags and checks to see if both bags are equal.
        :param: second_bag - the second bag that the initial bag will be compared with.
        :return: a bool that is True if the bags are equal or False if they are not equal.
        """

        if self.size() != second_bag.size():
            return False

        # Check to see if the count of each value in the first bag is the same as the second bag.
        # Since they are of the same length, this will apply for vice-versa as well.
        for idx in range(self.size()):
            if self.count(self._da[idx]) != second_bag.count(self._da[idx]):
                return False

        return True

    def __iter__(self):
        """
        Creates and initializes a iterator to iterate through the bag.
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Returns the next value in the array from the iterator pointer.
        """
        try:
            value = self._da[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


# if __name__ == "__main__":

    # print("\n# add example 1")
    #
    # bag = Bag()
    # print(bag)
    # values = [10, 20, 30, 10, 20, 30]
    # for value in values:
    #     bag.add(value)
    # print(bag)

    # print("\n# remove example 1")
    # bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(bag)
    # print(bag.remove(7), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # #
    # print("\n# count example 1")
    # bag = Bag([1, 2, 3, 1, 2, 2])
    # print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))
    # #
    # print("\n# clear example 1")
    # bag = Bag([1, 2, 3, 1, 2, 3])
    # print(bag)
    # bag.clear()
    # print(bag)

    #

    # print("\n# equal example 1")
    # bag1 = Bag([10, 20, 30, 40, 50, 60])
    # bag2 = Bag([60, 50, 40, 30, 20, 10])
    # bag3 = Bag([10, 20, 30, 40, 50])
    # bag4 = Bag([1,2,2])
    # bag5 = Bag([2,1,2])
    # bag_empty = Bag()
    # #
    # print(bag1, bag2, bag3, bag_empty, sep="\n")
    # print(bag1.equal(bag2), bag2.equal(bag1))
    # print(bag1.equal(bag3), bag3.equal(bag1))
    # print(bag2.equal(bag3), bag3.equal(bag2))
    # print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    # print(bag_empty.equal(bag_empty))
    # print(bag1, bag2, bag3, bag_empty, sep="\n")
    #
    # bag1 = Bag([100, 200, 300, 200])
    # bag2 = Bag([100, 200, 30, 100])
    # print(bag1.equal(bag2))
    # print(bag4.equal(bag5))
    # print(bag5.equal(bag4))

    # print("\n# __iter__(), __next__() example 1")
    # bag = Bag([5, 4, -8, 7, 10])
    # print(bag)
    # for item in bag:
    #     print(item)
    #
    # print("\n# __iter__(), __next__() example 2")
    # bag = Bag(["orange", "apple", "pizza", "ice cream"])
    # print(bag)
    # for item in bag:
    #     print(item)
