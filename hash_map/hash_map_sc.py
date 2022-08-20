# Name: Billy Fifield
# OSU Email: fifieldb@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 6
# Due Date: 6/5/2022
# Description: A chained Hash Map class that contains put, get, remove, contains_key, clear
#              empty_buckets, resize_table, table_load, get_keys, and find_mode methods.


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()
        for _ in range(capacity):
            self._buckets.append(LinkedList())

        self._capacity = capacity
        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity
    
    def get_buckets(self):
        return self._buckets

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        A method that puts a key/value pair into a hash table. If the key already exists, then the value will be replaced.
        :param: key - the key of the value to be added to the hash table.
        :param: value - the value to be added to the hash table.
        :return: None
        """
        hash = self._hash_function(key)
        index = hash % self._capacity
        bucket = self._buckets.get_at_index(index)

        # Check if the key is already in the hash table. If it is, then remove the existing value and replace it with
        # with the new value.
        if bucket.contains(key):
            bucket.remove(key)
            bucket.insert(key, value)

        # Otherwise, add the key/value pair to the hash table.
        else:
            bucket.insert(key,value)
            self._size += 1
            
    def mode_put(self, key: str, value: object) -> None:
        """
        A method that puts a key/value pair into a hash table. If the key already exists, then the value will be incremented.
        :param: key - the key of the value to be added to the hash table. TO BE USED FOR FIND_MODE.
        :param: value - the value to be added to the hash table.
        :return: None
        """
        hash = self._hash_function(key)
        index = hash % self._capacity
        bucket = self._buckets.get_at_index(index)

        # See if the key is already in the bucket. If so, increment the value.
        for node in bucket:
            if node.key == key:
                node.value += 1
                return

        # Otherwise, add the key/value pair to the hash table.
        bucket.insert(key,value)
        self._size += 1

    def empty_buckets(self) -> int:
        """
        A method to calculate the number of empty buckets.
        :return: empty_count - the number of empty buckets.
        """
        empty_count = 0

        # Iterate through the Hash Map, counting the number of empty buckets.
        for idx in range(self._capacity):
            bucket = self._buckets.get_at_index(idx)
            if bucket.length() == 0:
                empty_count += 1

        return empty_count

    def table_load(self) -> float:
        """
        A method to calculate the load factor of the table (the average number of elements in each bucket).
        :return: the load factor of the table (size / capacity)
        """
        return self._size / self._capacity

    def clear(self) -> None:
        """
        A method to clear the Hash Map.
        :return: None
        """
        for idx in range(self._capacity):
            self._buckets.set_at_index(idx, LinkedList())

        self._size = 0


    def resize_table(self, new_capacity: int) -> None:
        """
        TA method that takes a new capacity for the hash table, and creates a new table
        using the new capacity and the same key-value pairs from the original hash table.
        :param: new_capacity - the new capacity for the new hash table
        :return: None
        """

        # Validate the new capacity.
        if new_capacity < 1:
            return

        new_map = HashMap(new_capacity, self._hash_function)
        old_cap = self._capacity
        
        # Iterate through and if the bucket is not None, put the node of the
        # bucket into the new map.
        for idx in range(old_cap):
            bucket = self._buckets.get_at_index(idx)
            if bucket.length() != 0:
                for node in bucket:
                    new_map.put(node.key, node.value)


        self._capacity = new_capacity
        self._buckets = new_map.get_buckets()    # Set buckets equal to the buckets of the created Hash Map.

        

    def get(self, key: str) -> object:
        """
        A method that takes a key as parameter and returns the bucket for that key.
        :param: key - the key of the bucket that will be returned.
        :return: Value of the bucket containing the given key.
        """
        hash = self._hash_function(key)
        index = hash % self._capacity
        bucket = self._buckets.get_at_index(index)

        if bucket.contains(key):
            return bucket.contains(key).value
        
    def contains_key(self, key: str) -> bool:
        """
        A method that checks to see if a key is in the hash table.
        :param: key - the key to be searched in the hash table.
        :return: True - if the key is in the table, False - if the key is not in the table
        """
        hash = self._hash_function(key)
        index = hash % self._capacity
        bucket = self._buckets.get_at_index(index)

        if bucket.contains(key):
            return True
        
        return False


    def remove(self, key: str) -> None:
        """
        A method to remove a bucket that is associated with the key taken as parameter.
        :param: key - the key of the bucket to be removed.
        :return: None
        """
        hash = self._hash_function(key)
        index = hash % self._capacity
        bucket = self._buckets.get_at_index(index)

        # Check if the key is already in the hash table. If it is, then remove the existing value and replace it with
        # with the new value.
        if bucket.contains(key):
            bucket.remove(key)
            self._size -= 1

    def get_keys(self) -> DynamicArray:
        """
        A method to get all of the keys in the hash table.
        :return: new_da - a Dynamic Array containing all of the keys of the table.
        """
        new_da = DynamicArray()

        # Iterate through each bucket in the Hash Map, placing the keys inside the buckets
        # into the created Dynamic Array.
        for idx in range(self._capacity):
            bucket = self._buckets.get_at_index(idx)
            for node in bucket:
                new_da.append(node.key)
        
        return new_da


def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    A method that takes a Dynamic Array as parameter and returns the mode and frequency
    of the mode as a tuple. A new Hash Map will be created containing the key and the value being the 
    frequency of the key in the bucket.
    :param: da - the array that the mode will be found from.
    :return: mode_tup - the tuple containing an array of the mode(s) and the frequency of the mode(s)      
    """

    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap

    map = HashMap(da.length() // 3, hash_function_1)

    max = 0       # The frequency of the mode.
    new_da = DynamicArray()

    # Create a new Hash Map by using the mode_put method.
    for idx in range(da.length()):
        map.mode_put(da[idx], 1)

    buckets = map.get_buckets()

    # Iterate through the Hash Map and see which keys have the highest values (frequencies).
    # Add these keys to a Dynamic Array to keep track of which key(s) are the mode.
    for idx in range(map.get_capacity()):
        bucket = buckets.get_at_index(idx)
        for node in bucket:
            if node.value == max:
                new_da.append(node.key)
                max = node.value
            elif node.value > max:
                new_da = DynamicArray()
                new_da.append(node.key)
                max = node.value
    
    mode_tup = (new_da, max)
    return mode_tup




# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    # print("\nPDF - empty_buckets example 1")
    # print("-----------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    # m.put('key1', 10)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    # m.put('key2', 20)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    # m.put('key1', 30)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())
    # m.put('key4', 40)
    # print(m.empty_buckets(), m.get_size(), m.get_capacity())

    # print("\nPDF - empty_buckets example 2")
    # print("-----------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('key' + str(i), i * 100)
    #     if i % 30 == 0:
    #         print(m.empty_buckets(), m.get_size(), m.get_capacity())

    # print("\nPDF - table_load example 1")
    # print("--------------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.table_load())
    # m.put('key1', 10)
    # print(m.table_load())
    # m.put('key2', 20)
    # print(m.table_load())
    # m.put('key1', 30)
    # print(m.table_load())

    # print("\nPDF - table_load example 2")
    # print("--------------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(50):
    #     m.put('key' + str(i), i * 100)
    #     if i % 10 == 0:
    #         print(m.table_load(), m.get_size(), m.get_capacity())

    # print("\nPDF - clear example 1")
    # print("---------------------")
    # m = HashMap(100, hash_function_1)
    # print(m.get_size(), m.get_capacity())
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key1', 30)
    # print(m.get_size(), m.get_capacity())
    # m.clear()
    # print(m.get_size(), m.get_capacity())

    # print("\nPDF - clear example 2")
    # print("---------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.get_size(), m.get_capacity())
    # m.put('key1', 10)
    # print(m.get_size(), m.get_capacity())
    # m.put('key2', 20)
    # print(m.get_size(), m.get_capacity())
    # m.resize_table(100)
    # print(m.get_size(), m.get_capacity())
    # m.clear()
    # print(m.get_size(), m.get_capacity())

    # print("\nPDF - resize example 1")
    # print("----------------------")
    # m = HashMap(20, hash_function_1)
    # m.put('key1', 10)
    # print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    # m.resize_table(30)
    # print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    # print("\nPDF - resize example 2")
    # print("----------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 13)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.get_size(), m.get_capacity())

    # for capacity in range(111, 1000, 117):
    #     m.resize_table(capacity)

    #     m.put('some key', 'some value')
    #     result = m.contains_key('some key')
    #     m.remove('some key')

    #     for key in keys:
    #         # all inserted keys must be present
    #         result &= m.contains_key(str(key))
    #         # NOT inserted keys must be absent
    #         result &= not m.contains_key(str(key + 1))
    #     print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    # print("\nPDF - get example 1")
    # print("-------------------")
    # m = HashMap(30, hash_function_1)
    # print(m.get('key'))
    # m.put('key1', 10)
    # print(m.get('key1'))

    # print("\nPDF - get example 2")
    # print("-------------------")
    # m = HashMap(150, hash_function_2)
    # for i in range(200, 300, 7):
    #     m.put(str(i), i * 10)
    # print(m.get_size(), m.get_capacity())
    # for i in range(200, 300, 21):
    #     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
    #     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    # print("\nPDF - contains_key example 1")
    # print("----------------------------")
    # m = HashMap(10, hash_function_1)
    # print(m.contains_key('key1'))
    # m.put('key1', 10)
    # m.put('key2', 20)
    # m.put('key3', 30)
    # print(m.contains_key('key1'))
    # print(m.contains_key('key4'))
    # print(m.contains_key('key2'))
    # print(m.contains_key('key3'))
    # m.remove('key3')
    # print(m.contains_key('key3'))

    # print("\nPDF - contains_key example 2")
    # print("----------------------------")
    # m = HashMap(75, hash_function_2)
    # keys = [i for i in range(1, 1000, 20)]
    # for key in keys:
    #     m.put(str(key), key * 42)
    # print(m.get_size(), m.get_capacity())
    # result = True
    # for key in keys:
    #     # all inserted keys must be present
    #     result &= m.contains_key(str(key))
    #     # NOT inserted keys must be absent
    #     result &= not m.contains_key(str(key + 1))
    # print(result)

    # print("\nPDF - remove example 1")
    # print("----------------------")
    # m = HashMap(50, hash_function_1)
    # print(m.get('key1'))
    # m.put('key1', 10)
    # print(m.get('key1'))
    # m.remove('key1')
    # print(m.get('key1'))
    # m.remove('key4')

    # print("\nPDF - get_keys example 1")
    # print("------------------------")
    # m = HashMap(10, hash_function_2)
    # for i in range(100, 200, 10):
    #     m.put(str(i), str(i * 10))
    # print(m.get_keys())

    # m.resize_table(1)
    # print(m.get_keys())

    # m.put('200', '2000')
    # m.remove('100')
    # m.resize_table(2)
    # print(m.get_keys())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "melon", "peach", "tomato", "tomato"])
    map = HashMap(da.length() // 3, hash_function_1)
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode: {mode}, Frequency: {frequency}")

    # print("\nPDF - find_mode example 2")
    # print("-----------------------------")
    # test_cases = (
    #     ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu", "Ubuntu"],
    #     ["one", "two", "three", "four", "five"],
    #     ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    # )

    # for case in test_cases:
    #     da = DynamicArray(case)
    #     map = HashMap(da.length() // 3, hash_function_2)
    #     mode, frequency = find_mode(da)
    #     print(f"Input: {da}\nMode: {mode}, Frequency: {frequency}\n")
