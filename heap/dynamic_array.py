# Name: Billy Fifield
# OSU Email: fifieldb@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2
# Due Date: 4/25/2022
# Description: A Dynamic Array assignment with methods for each part of the array
#              including resize, append, insert_at_index, remove_at_index, slice,
#              merge, map, filter, reduce, and find_mode.


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size
    
    def set_size(self, new_size) -> None:
        self._size = new_size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Set the new capacity for the array by creating a new arr with the new capacity
        and then setting the original arr equal to the new.
        :param: new_capacity - the new capacity for the new arr
        :return: None
        """
        if (new_capacity < 1) or (new_capacity < self._size):
            return

        # Create a new array using the new capacity.
        new_arr = StaticArray(new_capacity)
        for idx in range(self._size):
            new_arr[idx] = self._data[idx]

        # Set the original capcity equal to the new and the original arr equal to the new.
        self._capacity = new_capacity
        self._data = new_arr


    def append(self, value: object) -> None:
        """
        Add an object to the end of the array. If the capacity will increase, then do the same steps
        from the resize function. Otherwise, set the value as the new last index.
        :param: value - the new value to be added to the arr
        :return: None
        """

        # Check to see if the capacity will need to increase
        if self._size == self._capacity:
            new_capacity = self._capacity * 2
            new_arr = StaticArray(new_capacity)
            for idx in range(self._size):
                new_arr[idx] = self._data[idx]
            self._capacity = new_capacity
            self._data = new_arr

        # Add the value to the array
        self._data[self._size] = value
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert a value at a given index and increase the size of the array by 1.
        If the capacity needs to increase, a new array will be created with the new capacity
        before adding the value at the given index.
        :param: index - the index to add the value
        :param: value - the value to be added at the given index
        :return: None
        """

        # Validate the given index
        if (index < 0) or (index > self._size):
            raise DynamicArrayException

        # Check to see if the capacity needs to be increased.
        if self._size == self._capacity:
            new_capacity = self._capacity * 2
            new_arr = StaticArray(new_capacity)
            for idx in range(self._size):
                new_arr[idx] = self._data[idx]
            self._capacity = new_capacity
            self._data = new_arr

        temp = ''
        self._size += 1

        # Iterate through the array until the index equals the given index and then
        # shift the array over and insert the new value.
        for idx in range(self._size):
            if self._size == 1:
                self._data[idx] = value
            if (idx == self._size - 1) and (index == self._capacity - 1):
                self._data[idx] = value
            elif idx == index:
                temp = self._data[idx + 1]
                self._data[idx + 1], self._data[idx] = self._data[idx], value
            elif idx == (self._size - 1) and (index != 0) and (self._size - index != 2):
                self._data[idx] = temp
            elif idx > (index + 1):
                self._data[idx], temp = temp, self._data[idx]


    def remove_at_index(self, index: int) -> None:
        """
        Remove a value at a certain index and decrease the size of the array by 1.
        The capacity will be adjusted once the value is removed. The capacity will not
        fall below 10.
        :param: index - the index to remove a certain value
        :return: None
        """
        # Validate the given index
        if (index < 0) or (index > (self._size - 1)):
            raise DynamicArrayException

        # Check to decrease the capacity.
        if (self._capacity > 10) and (self._capacity / 4 > self._size):
            if self._size <= 5:
                self._capacity = 10
            else:
                self._capacity = self._size * 2

        # Remove the value at the index and shift the array over to erase the
        # previous value at the index.

        for idx in range(self._size - 1):
            if idx >= index:
                self._data[idx] = self._data[idx + 1]
        self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Creates and returns a new Dynamic Array using the data starting at the start_index for
        the length of the entered size.
        :param: start_index - the start of the index where the new array will begin.
        :param: size - the size of the new array.
        :return: new_DA - the new Dynamic Array
        """
        # validate the starting index and size
        if (start_index < 0) or (start_index > (self._size - 1)) or ((start_index + size) > self._size) or (size < 0):
            raise DynamicArrayException
        new_DA = DynamicArray()
        idx = 0
        new_idx = 0

        # Iterate through the array until the starting index is met and then add the values
        # to the new array for the entered size.
        for idx in range(start_index + size):
            if idx >= start_index:
                new_DA.append(self._data[idx])

        return new_DA

    def merge(self, second_da: "DynamicArray") -> None:
        """
        Merges two arrives by adding second_da to the end of the original array.
        Create a new capacity if necessary.
        :param: second_da - the array to be added to the end of the original array.
        :return: None
        """

        new_size = self._size + second_da.length()
        new_capacity = self._capacity

        # Increase the new capacity size
        while new_capacity < new_size:
            new_capacity *= 2
        new_arr = StaticArray(new_capacity)
        new_cap = self._capacity
        second_idx = 0

        # Add the new array to the end of the old array once the index reaches
        # the size of the old array.
        for idx in range(new_size):
            if idx >= self._size:
                self._size += 1
                new_arr[idx] = second_da[second_idx]
                second_idx += 1
            else:
                new_arr[idx] = self._data[idx]

        # Set the capacity and original array equal to the new capacity and new array.
        self._capacity = new_capacity
        self._data = new_arr

    def map(self, map_func) -> "DynamicArray":
        """
        Maps each value of the array to the map_func that is taken in as a parameter
        and creates and returns a new Dynamic Array with the new values.
        :param: map_func - the function to run each value of the array through.
        :return: new_da the new Dynamic Array created from the values from the map_func function.
        """
        new_da = DynamicArray()
        # Run each value of the array through the map_func and add the value to a Dynamic Array.
        for idx in range(self._size):
            new_da.append(map_func(self._data[idx]))

        return new_da

    def filter(self, filter_func) -> "DynamicArray":
        """
        Creates and returns a new Dynamic Array containing the values in the range provided in
        the filter_func that is taken in as a parameter.
        :param: filter_func - the function containing the range of the new array.
        :return: new_da - a new Dynamic Array containing the new values from the original
                array within the range of the filter_func.
        """
        new_da = DynamicArray()
        for idx in range(self._size):
            if filter_func(self._data[idx]) == True:
                new_da.append(self._data[idx])

        return new_da

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        A reducer method that takes a reduce function and an optional initializer as parameters
        and reduces the Dynamic Array using the provided function.
        :param: reduce_func - the reducer function the array will be passed through.
        :param: initializer - an optional initializer to include within reduce_func
        :return: result - An integer after passing the array through the function.
        """
        result = self._data[0]
        if initializer is None and self._size == 0:
            return None
        elif initializer is not None and self._size == 0:
            return initializer

        if initializer is not None:
            for idx in range(self._size):
                if idx == 0:
                    result = reduce_func(initializer, self._data[idx])

                else:
                    result = reduce_func(result, self._data[idx])
        else:
            for idx in range(self._size - 1):
                result = reduce_func(result, self._data[idx + 1])

        return result

    def pop(self) -> None:
        """
        A method that removes the last object in the array.
        :return: None
        """
        self._data[self._size - 1] = None
        self._size -= 1


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    A method that finds the mode of a Dynamic Array and returns a tuple containing
    the mode(s) and the frequency of the mode as well.
    :param: arr - a Dynamic Array
    :return: mode_tup - a tuple containing a dynamic array of the mode(s) and also
            the freqency of the mode(s).
    """
    new_da = DynamicArray()
    count = 1
    record_count = 1

    if arr.length() > 1:
        # Find the frequency of the mode.
        for idx in range(arr.length() - 1):
            if arr[idx] == arr[idx + 1]:
                count += 1
                if count >= record_count:
                    record_count = count
            else:
                count = 1

        count = 1

        # If the frequency of the mode is 1, then every element in the array will be added
        # to the new array since every value is the mode.
        if record_count == 1:
            for idx in range(arr.length()):
                new_da.append(arr[idx])

        # Use the frequency to find out if a value is repeated the same amount as the frequency
        # of the mode. This value will then be added to a new Dynamic Array.
        else:
            for idx in range(arr.length() - 1):
                if arr[idx] == arr[idx + 1]:
                    count += 1
                    if count == record_count:
                        new_da.append(arr[idx])
                else:
                    count = 1
    else:
        new_da.append(arr[0])

    mode_tup = (new_da, record_count)
    return mode_tup

# ------------------- BASIC TESTING -----------------------------------------


# if __name__ == "__main__":

    # print("\n# resize - example 1")
    # da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    # da.print_da_variables()
    # da.resize(8)
    # da.print_da_variables()
    # da.resize(2)
    # da.print_da_variables()
    # da.resize(0)
    # da.print_da_variables()
    #
    # print("\n# resize - example 2")
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    # print(da)
    # da.resize(20)
    # print(da)
    # da.resize(4)
    # print(da)

    # print("\n# append - example 1")
    # da = DynamicArray()
    # da.print_da_variables()
    # da.append(1)
    # da.print_da_variables()
    # print(da)
    #
    # print("\n# append - example 2")
    # da = DynamicArray()
    # for i in range(9):
    #     da.append(i + 101)
    #     print(da)

    # print("\n# append - example 3")
    # da = DynamicArray()
    # for i in range(600):
    #     da.append(i)
    # print(da.length())
    # print(da.get_capacity())
    #
    # print("\n# insert_at_index - example 1")
    # da = DynamicArray([100])
    # print(da)
    # da.insert_at_index(0, 200)
    # print(da)
    # da.insert_at_index(0, 300)
    # print(da)
    # da.insert_at_index(0, 400)
    # print(da)
    # da.insert_at_index(3, 500)
    # print(da)
    # da.insert_at_index(1, 600)
    # print(da)
    #
    # print("\n# insert_at_index example 2")
    # da = DynamicArray()
    # try:
    #     da.insert_at_index(-1, 100)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # da.insert_at_index(0, 200)
    # try:
    #     da.insert_at_index(2, 300)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # print(da)
    #
    # print("\n# insert at index example 3")
    # da = DynamicArray()
    # for i in range(1, 10):
    #     index, value = i - 4, i * 10
    #     try:
    #         da.insert_at_index(index, value)
    #     except Exception as e:
    #         print("Cannot insert value", value, "at index", index)
    # print(da)
    #
    # print("\n# remove_at_index - example 1")
    # da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    # print(da)
    # da.remove_at_index(0)
    # print(da)
    # da.remove_at_index(6)
    # print(da)
    # da.remove_at_index(2)
    # print(da)
    # #
    # print("\n# remove_at_index - example 2")
    # da = DynamicArray([1024])
    # print(da)
    # for i in range(17):
    #     da.insert_at_index(i, i)
    # print(da.length(), da.get_capacity())
    # for i in range(16, -1, -1):
    #     da.remove_at_index(0)
    # print(da)
    # #
    # print("\n# remove_at_index - example 3")
    # da = DynamicArray()
    # print(da.length(), da.get_capacity())
    # [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    # print(da.length(), da.get_capacity())
    # [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    # print(da.length(), da.get_capacity())
    # da.remove_at_index(0)  # step 3 - remove 1 element
    # print(da.length(), da.get_capacity())
    # da.remove_at_index(0)  # step 4 - remove 1 element
    # print(da.length(), da.get_capacity())
    # [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    # print(da.length(), da.get_capacity())
    # da.remove_at_index(0)  # step 6 - remove 1 element
    # print(da.length(), da.get_capacity())
    # da.remove_at_index(0)  # step 7 - remove 1 element
    # print(da.length(), da.get_capacity())
    #
    # for i in range(14):
    #     print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
    #     da.remove_at_index(0)
    #     print(" After remove_at_index(): ", da.length(), da.get_capacity())
    # #
    # print("\n# remove at index - example 4")
    # da = DynamicArray([1, 2, 3, 4, 5])
    # print(da)
    # for _ in range(5):
    #     da.remove_at_index(0)
    #     print(da)
    #
    # print("\n# slice example 1")
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # da_slice = da.slice(1, 3)
    # print(da, da_slice, sep="\n")
    # da_slice.remove_at_index(0)
    # print(da, da_slice, sep="\n")
    # #
    # print("\n# slice example 2")
    # da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    # print("SOURCE:", da)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    # for i, cnt in slices:
    #     print("Slice", i, "/", cnt, end="")
    #     try:
    #         print(" --- OK: ", da.slice(i, cnt))
    #     except:
    #         print(" --- exception occurred.")
    #
    # print("\n# merge example 1")
    # da = DynamicArray([1, 2, 3, 4, 5])
    # da2 = DynamicArray([10, 11, 12, 13])
    # print(da)
    # da.merge(da2)
    # print(da)
    # #
    # print("\n# merge example 2")
    # da = DynamicArray([1, 2, 3])
    # da2 = DynamicArray()
    # da3 = DynamicArray()
    # da.merge(da2)
    # print(da)
    # da2.merge(da3)
    # print(da2)
    # da3.merge(da)
    # print(da3)
    #
    # print("\n# map example 1")
    # da = DynamicArray([1, 5, 10, 15, 20, 25])
    # print(da)
    # print(da.map(lambda x: x ** 2))
    # #
    # print("\n# map example 2")
    #
    #
    # def double(value):
    #     return value * 2
    #
    #
    # def square(value):
    #     return value ** 2
    #
    #
    # def cube(value):
    #     return value ** 3
    #
    #
    # def plus_one(value):
    #     return value + 1
    #
    #
    # da = DynamicArray([plus_one, double, square, cube])
    # for value in [1, 10, 20]:
    #     print(da.map(lambda x: x(value)))

    # print("\n# filter example 1")
    #
    #
    # def filter_a(e):
    #     return e > 10
    #
    #
    # da = DynamicArray([1, 5, 10, 15, 20, 25])
    # print(da)
    # result = da.filter(filter_a)
    # print(result)
    # print(da.filter(lambda x: (10 <= x <= 20)))
    # #
    # print("\n# filter example 2")
    #
    #
    # def is_long_word(word, length):
    #     return len(word) > length
    #
    #
    # da = DynamicArray("This is a sentence with some long words".split())
    # print(da)
    # for length in [3, 4, 7]:
    #     print(da.filter(lambda word: is_long_word(word, length)))
    #
    # print("\n# reduce example 1")
    # values = [100, 5, 10, 15, 20, 25]
    # da = DynamicArray(values)
    # print(da)
    # print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    # print(da.reduce(lambda x, y: (x + y ** 2), -1))
    # da1 = DynamicArray()
    # print(da1)
    #
    # print("\n# reduce example 2")
    # da = DynamicArray([100])
    # print(da.reduce(lambda x, y: x + y ** 2))
    # print(da.reduce(lambda x, y: x + y ** 2, -1))
    # da.remove_at_index(0)
    # print(da.reduce(lambda x, y: x + y ** 2))
    # print(da.reduce(lambda x, y: x + y ** 2, -1))

    # print("\n# find_mode - example 1")
    # test_cases = (
    #     [1, 1, 2, 3, 3, 4],
    #     [1, 2, 3, 4, 5],
    #     ["Apple", "Banana", "Banana", "Carrot", "Carrot",
    #      "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
    #      "Fig", "Fig", "Grape"]
    # )
    #
    # for case in test_cases:
    #     da = DynamicArray(case)
    #     mode, frequency = find_mode(da)
    #     print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")
    #
    # case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    # da = DynamicArray()
    # for x in range(len(case)):
    #     da.append(case[x])
    #     mode, frequency = find_mode(da)
    #     print(f"{da}\nMode: {mode}, Frequency: {frequency}")
