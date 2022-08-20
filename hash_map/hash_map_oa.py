# Name: Billy Fifield
# OSU Email: fifieldb@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 6
# Due Date: 6/5/2022
# Description: A HashMap that uses an open addressing hash table with quadratic
#              probing to handle collisions. Methods include put, table_load,
#              empty_buckets, resize_table, get, contains_key, remove, clear, and get_keys


from a6_include import (DynamicArray, HashEntry,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()
        for _ in range(capacity):
            self._buckets.append(None)

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

    def probe_index(self, init_idx: int, j: int) -> int:
        """
        A Quadratic Probe method that will be called when there is a collision within
        the OA Hash Map.
        :param: init_idx - the initial index.
        :param: j - helps finding the next open spot.
        :return: index - the new index after probing.
        """
        index = (init_idx + (j * j))
        return index


    def put(self, key: str, value: object) -> None:
        """
        A put method to insert a key and value into a Hash Map
        :param: key - the key to be inserted.
        :param: value - the value to be paired with the key inside the Hash Table.
        :return: None
        """

        hash = self._hash_function(key)
        load = self.table_load()
        
        if load >= (1/2):
            new_cap = self._capacity * 2
            self.resize_table(new_cap)
        
        index = hash % self._capacity

        # Check to see if the bucket is already empty. If so, insert the key and value.
        if self._buckets[index] is None:
            self._buckets[index] = HashEntry(key, value)
            self._size += 1

        # Check to see if the key of the hash table is equal to the received key. If so,
        # replace the value with the new value.

        elif self._buckets[index].is_tombstone is True:
            self._buckets[index].key = key
            self._buckets[index].value = value
            self._buckets[index].is_tombstone = False
            self._size += 1

        elif self._buckets[index].key == key:
            self._buckets[index].value = value

        # Quadratic probe until an open spot if sound within the hash map.
        else:
            j = 0
            while self._buckets[index] is not None:
                j += 1
                new_index = self.probe_index(index, j)

                # Check to see if the new index is out of bounds and adjust it if it is.
                if new_index >= self._capacity:
                    new_index %= self._capacity
                
                # Check to see if the bucket is empty. If so, the insert the key and value.
                if self._buckets[new_index] is None:
                    self._buckets[new_index] = HashEntry(key,value)
                    self._size += 1
                    break

                # If the current spot is a tombstone, insert the key and value and set tombstone
                # to false.
                elif self._buckets[new_index].is_tombstone is True:
                    self._buckets[new_index].key = key
                    self._buckets[new_index].value = value
                    self._buckets[new_index].is_tombstone = False
                    self._size += 1
                    break
                

                # Check to see if the key of the hash table is equal to the received key. If so,
                # replace the value with the new value.
                elif self._buckets[new_index].key == key:
                    self._buckets[new_index].value = value
                    break
                
        

    def table_load(self) -> float:
        """
        A method to calculate the table's load balance.
        :return: the load balance.
        """
        return self._size / self._capacity

    def empty_buckets(self) -> int:
        """
        A method that returns the number of empty buckets.
        :return: empty_count - the number of empty buckets.
        """
        empty_count = 0
        
        # Iterate through the Hash Map and count how many buckets are empty.
        for idx in range(self._capacity):
            if self._buckets[idx] is None:
                empty_count += 1
            elif self._buckets[idx].is_tombstone is True:
                empty_count += 1
        
        return empty_count

    def resize_table(self, new_capacity: int) -> None:
        """
        A method that resizes the Hash Map to the new capacity.
        :param: new_capacity - the new capacity of the Hash Map.
        :return: None
        """
        # remember to rehash non-deleted entries into new table

        # Validate the new capacity
        if new_capacity < 1 or new_capacity < self._size:
            return

        old_cap = self._capacity
        self._capacity = new_capacity
        load = self.table_load()
        if load >= (1/2):
            self._capacity = self._capacity * 2

        old_bucket = DynamicArray()

        # Save the list of buckets
        for idx in range(old_cap):
            old_bucket.append(self._buckets[idx])

        # Erase all variables of self._buckets
        for idx in range(self._capacity):
            if idx >= old_cap:
                self._buckets.append(None)
            else:
                self._buckets[idx] = None
        
        self._size = 0

        # For the buckets that are not None or a tombstone, add them to the orginal list of buckets
        # while rehashing it with the new capacity.
        for idx in range(old_cap):
            if old_bucket[idx] is not None and old_bucket[idx].is_tombstone is False:
                self.put(old_bucket[idx].key, old_bucket[idx].value)



    def get(self, key: str) -> object:
        """
        A method that returns the value of a given key.
        :param: key - the key of the value to be returned.
        :return: If the key is not found, return None. Otherwise,
                 return the value at the given key.
        """
        hash = self._hash_function(key)
        index = hash % self._capacity

        # See if the hash index of the given key is empty. If so,
        # return None because the key doesn't exist.
        if self._buckets[index] is None:
            return

        # If the bucket at the hash index of the given key is equal to the key and
        # it is not a tombstone, return the value of that key. If there is a tombstone,
        # return None.
        if self._buckets[index].key == key:
            if self._buckets[index].is_tombstone is True:
                return
            else:
                return self._buckets[index].value

        # Probe the key until the key is found or an empty space is found.
        else:
            j = 0
            while self._buckets[index] is not None:
                j += 1
                new_index = self.probe_index(index, j)
                if new_index >= self._capacity:
                    new_index %= self._capacity

                if self._buckets[new_index] is None:
                    return

                elif self._buckets[new_index].key == key:
                    if self._buckets[new_index].is_tombstone is True:
                        return
                    else:
                        return self._buckets[new_index].value


    def contains_key(self, key: str) -> bool:
        """
        A method that checks to see if the given key is in the Hash Map.
        :param: key - the key to be seached in the Hash Map.
        :return: True if the key is found. Else, false.
        """
        hash = self._hash_function(key)
        index = hash % self._capacity

        # Check if the bucket at the hash index is None and return False.
        if self._buckets[index] is None:
            return False

        # If the bucket at the hash index has the same key and return True.
        if self._buckets[index].key == key:
            return True

        # Probe until the key is found and return True. Or, if the key is not found,
        # return False.
        else:
            j = 0
            while self._buckets[index] is not None:
                j += 1
                new_index = self.probe_index(index, j)
                if new_index >= self._capacity:
                    new_index %= self._capacity

                if self._buckets[new_index] is None:
                    return False

                elif self._buckets[new_index].key == key:
                    return True


    def remove(self, key: str) -> None:
        """
        A method to create a tombstone at a certain key.
        :param: key - the key of the bucket to create a tombstone.
        :return: None
        """
        hash = self._hash_function(key)
        index = hash % self._capacity

        # Check if the bucket at the hash index is None and return None.
        if self._buckets[index] is None:
            return

        # Check if the bucket at the hash index has the same key. If so,
        # create a tombstone and decrease the size of the Hash Map.
        if self._buckets[index].key == key:
            if self._buckets[index].is_tombstone is True:
                return
            self._buckets[index].is_tombstone = True
            self._size -= 1
            return

        # Probe until the key is found. If found, a tombstone is created and the
        # size of the Hash Map is decreased. Otherwise, return None.
        else:
            j = 0
            while self._buckets[index] is not None:
                j += 1
                new_index = self.probe_index(index, j)
                if new_index >= self._capacity:
                    new_index %= self._capacity

                if self._buckets[new_index] is None:
                    return

                elif self._buckets[new_index].key == key:
                    if self._buckets[new_index].is_tombstone is True:
                        return
                    self._buckets[new_index].is_tombstone = True
                    self._size -= 1
                    return

    def clear(self) -> None:
        """
        A method to clear the Hash Map.
        :return: None
        """
        new_buckets = HashMap(self._capacity, self._hash_function)
        self._buckets = new_buckets.get_buckets()
        self._size = 0

    def get_keys(self) -> DynamicArray:
        """
        A method to get the keys of the Hash Map.
        :return: keys_arr - a Dynamic Array containing all of the keys of the Hash Map.
        """
        keys_arr = DynamicArray()
        for idx in range(self._capacity):
            if self._buckets[idx] is not None and self._buckets[idx].is_tombstone is False:
                keys_arr.append(self._buckets[idx].key)

        return keys_arr


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    # print("\nPDF - put example 1")
    # print("-------------------")
    # m = HashMap(50, hash_function_1)
    # for i in range(150):
    #     m.put('str' + str(i), i * 100)
    #     if i % 25 == 24:
    #         print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    # print("\nPDF - put example 2")
    # print("-------------------")
    # m = HashMap(40, hash_function_2)
    # for i in range(50):
    #     m.put('str' + str(i // 3), i * 100)
    #     if i % 10 == 9:
    #         print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

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

    # print("\nPDF - resize example 1")
    # print("----------------------")
    # m = HashMap(20, hash_function_1)
    # m.put('key1', 10)
    # print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    # m.resize_table(30)
    # print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        if m.table_load() >= 0.5:
            print("Check that capacity gets updated during resize(); "
                  "don't wait until the next put()")

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

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
