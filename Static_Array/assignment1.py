# Author: Billy Fifield
# Date: 4/8/2022
# Description: Assignment 1

import random
from static_array import *


# ---------------------------- PROBLEM 1 - MIN_MAX ---------------------------------

def min_max(arr: StaticArray) -> tuple:
	"""
	A function that takes an array from StaticArray as a parameter
	and returns the minimum and maximum number as a tuple.

	:param: arr - static array
	:return: a tuple containing the minimum and maximum number of the static array
	"""

	# Create intial min and max
	min = arr.get(0)
	max = arr.get(0)

	# Iterate through arr to find the lowest and highest value.
	for idx in range(arr.length()):
		if arr.get(idx) > max:
			max = arr.get(idx)
		elif arr.get(idx) < min:
			min = arr.get(idx)

	result = (min, max)
	return result

# arr = StaticArray(5)
# for i, value in enumerate([7, 8, 6, -5, 4]):
# 	arr[i] = value
# print(arr)
# result = min_max(arr)
# print(f"Min: {result[0]: 3}, Max: {result[1]: 3}")

# ---------------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
	"""
	A funcion that takes a Static Array as a parameter and iterates through
	the array checking if each value is either divided by 3, 5, or 3 and 5. If the value
	is divisible by 3, then that value becomes 'fizz' in a new static array. If the value is
	divisible by 5, then that value becomes 'buzz' in the new static array. If the value is
	divisible by both 3 and 5, the that value becomes 'fizzbuzz' in the new static array.
	If the value is not divisible by either 3 or 5, then that value gets added to the new
	array. This static array is then returned.

	:param: arr - static array
	:return: a new static array containing 'fizz' if divisible by 3, 'buzz' if the value
		is divisible by 5, or 'fizzbuzz' if divisible by 3 and 5. Otherwise, the value from the
		originial static array.
	"""

	new_arr = StaticArray(arr.length())

	for idx in range(arr.length()):
		# Check to see if value is divisible by both 3 and 5
		if (arr.get(idx) % 3 == 0) and (arr.get(idx) % 5 == 0):
			new_arr[idx] = 'fizzbuzz'

		# Check to see if value is only divisible by 3
		elif arr.get(idx) % 3 == 0:
			new_arr[idx] = 'fizz'

		# Check to see if value is only divisible by 5
		elif arr.get(idx) % 5 == 0:
			new_arr[idx] = 'buzz'

		else:
			new_arr[idx] = arr.get(idx)

	return new_arr

# source = [_ for _ in range(-5, 20, 4)]
# arr = StaticArray(len(source))
# for i, value in enumerate(source):
# 	arr[i] = value
# print(fizz_buzz(arr))
# print(arr)

# ---------------------------- PROBLEM 3 - REVERSE ---------------------------------

def reverse(arr: StaticArray) -> None:
	"""
	A function that takes a static array as a parameter and reverses the array
	without creating a new static array.

	:param: arr - static array
	:return: none
	"""

	for idx in range(int(arr.length() / 2)):
		arr[idx], arr[arr.length() - 1 - idx] = arr[arr.length() - 1 - idx], arr[idx]


# source = [_ for _ in range(-20, 20, 7)]
# arr = StaticArray(len(source))
# for i, value in enumerate(source):
# 	arr.set(i, value)
# print(arr)
# reverse(arr)
# print(arr)
# reverse(arr)
# print(arr)

# ---------------------------- PROBLEM 4 - ROTATE ---------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
	"""
	A function that rotates a static array either to the left (negative) or
	to the right (positive) number of steps. The rotated array will become a new
	static array that will be returned.

	:param: arr - static array, steps - integer of how many steps to move
	:return: a new static array of the old array rotated the number of steps entered.
	"""

	new_arr = StaticArray(arr.length())

	# Check to see if the rotate direction is left (negative)
	if steps < 0:
		# Find the remainder to see how many steps need to be moved
		convertRem = ((steps * (-1)) % arr.length())
		rem = arr.length() - convertRem

	else:
		# Find the remainder to see how many steps need to be moved
		rem = steps % arr.length()

	for idx in range(arr.length()):
		new_ind = idx + rem        # Add the remainder to rotate the values

		# Enter the values into the new Static Array, new_arr
		if new_ind >= arr.length():
			new_arr[new_ind % arr.length()] = arr.get(idx)
		else:
			new_arr[new_ind] = arr.get(idx)
	return new_arr

# source = [_ for _ in range(-20, 20, 7)]
# arr = StaticArray(len(source))
# for i, value in enumerate(source):
# 	arr.set(i, value)
# print(arr)
# for steps in [1, 2, 0, -1, -2, 28, -100, 2**28, -2**31]:
# 	space = " " if steps >= 0 else ""
# 	print(f"{rotate(arr, steps)} {space}{steps}")
# print(arr)

# ---------------------------- PROBLEM 5 - SA_RANGE ---------------------------------

def sa_range(start: int, end: int) -> StaticArray:
	"""
	A function that takes two integers as parameters and creates and returns a new static array
	for every integer between and including the two parameters.

	:param: start - starting integer, end - ending integer
	:return: an array containing the integers between the parameters.
	"""

	# Check to see if start and end need to be converted because they are negative to
	# 	create a range for the new_arr.
	if ((start < 0) and (end < 0)) and (start < end):
		ind_range = end + (start * (-1)) + 1
	elif ((start < 0) and (end < 0)) and (start > end):
		ind_range = start + (end * (-1)) + 1
	elif (start < 0):
		ind_range = (start - end) * (-1) + 1
	elif (end < 0):
		ind_range = (end - start) * (-1) + 1
	elif (start > end):
		ind_range = start - end + 1
	else:
		ind_range = end - start + 1

	new_arr = StaticArray(ind_range)

	# Create the new Static Array, new_arr
	for idx in range(ind_range):
		new_arr[idx] = start
		if start > end:
			start -= 1
		else:
			start += 1

	return new_arr

# cases = [(1, 3), (-1, 2), (0, 0), (0, -3), (-95, -89), (-89, -95)]
# for start, end in cases:
# 	print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

# ---------------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
	"""
	A function that takes a static array as a parameter and determines if the array
	is strictly ascending order, strictly descending order, or otherwise. If the array
	is strictly ascending, it returns 1. If the array is strictly descending order, it returns
	-1. Otherwise, it returns 0.

	:param: arr - static array
	:return: 1 if array is strictly ascending, -1 if stricly descending, 0 if otherwise
	"""

	if arr.length() == 1:
		return 1

	# Check to see if the first two values are strictly ascending
	elif arr[0] < arr[1]:
		# Iterate through the array to see if all values are stricly ascending
		for idx in range(arr.length() - 1):
			if arr[idx] >= arr[idx + 1]:
				return 0
		return 1
	# Check to see if the first two values are stricly descending
	elif arr[0] > arr[1]:
		# Iterate through the array to see if all values are stricly descending
		for idx in range(arr.length() - 1):
			if arr[idx] <= arr[idx + 1]:
				return 0
		return -1

	else:
		return 0

# test_cases = (
# 	[-100, -8, 0, 2, 3, 10, 20, 100],
# 	['A', 'B', 'Z', 'a', 'z'],
# 	['Z', 'T', 'K', 'A', '5'],
# 	[1, 3, -10, 20, -30, 0],
# 	[-10, 0, 0, 10, 20, 30],
# 	[100, 90, 0, -90, -200],
# 	['apple']
# )
# for case in test_cases:
# 	arr = StaticArray(len(case))
# 	for i, value in enumerate(case):
# 		arr[i] = value
# 	result = is_sorted(arr)
# 	space = " " if result >= 0 else " "
# 	print(f"Result:{space}{result}, {arr}")

# ---------------------------- PROBLEM 7 - FIND_MODE ---------------------------------

def find_mode(arr: StaticArray) -> tuple:
	"""
	A function that takes a static array as a parameter and finds the mode of the
	array and the frequency of the mode. It will return a tuple of the mode and frequency.
	If there are multiple values of the same frequency, the first value will be returned
	as the mode.

	:param: arr - static array
	:return: tuple containing the mode and frequency of the mode
	 """
	mode = arr[0]
	count = 1
	record_count = 1
	# Check to make sure there are more than one values in arr
	if arr.length() > 1:
		# Iterate through the arr and keep track of how many of each value there are.
		# If a value is more frequent then the others, then the number of times it appears
		# gets stored as record_count.
		for idx in range(arr.length() - 1):
			if arr[idx] == arr[idx + 1]:
				count += 1
				if count > record_count:
					mode = arr[idx]
			elif arr[idx] != arr[idx + 1]:
				if count > record_count:
					record_count = count
				count = 1
		if count > record_count:
			record_count = count
	mode_tup = (mode, record_count)
	return mode_tup

# test_cases = (
# [1,3,4,4,4,4,5,5,5,6,6,6,6,7,7],
# [1, 20, 30, 40, 500, 500, 500],
# [2, 2, 2, 2, 1, 1, 1, 1],
# ["zebra", "sloth", "otter", "otter", "moose", "koala"],
# ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
# )
# for case in test_cases:
# 	arr = StaticArray(len(case))
# 	for i, value in enumerate(case):
# 		arr[i] = value
# 	mode, frequency = find_mode(arr)
# 	print(f"{arr}\nMode: {mode}, Frequency: {frequency}\n")

# ------------------------ PROBLEM 8 - REVERSE_DUPLICATES ----------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
	"""
	A function that takes a static array as a parameter and creates a new static array
	with the same values except for the duplicate values.

	:param: arr - static array
	:return: a new static array without the duplicates from the original static array
	"""

	counter = 0      # Will be the size of the new array

	# Find the total values that have duplicates to create a size of the new array
	# 	that will remove the duplicates.
	for idx in range(arr.length()):
		if idx == 0:
			counter += 1
		elif arr[idx] != arr[idx - 1] :
			counter += 1

	new_arr = StaticArray(counter)
	len_count = 0

	# Iterate through the array and check to see if the following number is the same value,
	#	If it is, then skip to the next index until a new value appears.
	for idx in range(arr.length()):
		if arr.length() == 1:
			new_arr[len_count] = arr[idx]
		elif idx == (arr.length() - 1):
			if arr[idx] != arr[arr.length() - 2]:
				new_arr[len_count] = arr[idx]
		elif (idx > 0) and (arr[idx] == arr[idx - 1]):
			continue
		elif (idx > 0) and (arr[idx] != arr[idx - 1]):
			new_arr[len_count] = arr[idx]
			len_count += 1
		else:
			new_arr[len_count] = arr[idx]
			len_count += 1

	return new_arr

# test_cases = (
# 	[1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
# 	[5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
# )
# for case in test_cases:
# 	arr = StaticArray(len(case))
# 	for i, value in enumerate(case):
# 		arr[i] = value
# 	print(arr)
# 	print(remove_duplicates(arr))
# print(arr)

# ---------------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
	"""
	A function that takes a non-sorted static array as a parameter and returns a new static array
	containing the same values in non-ascending order.
	:param: arr - a static array of random integers
	:return: new_arr - a new static array containing the same integers but in non-ascending order
	"""
	new_arr = StaticArray(arr.length())
	max = arr[0]
	min = arr[0]

	# Find the minimum valuue and maximum value by comparing each value in the array
	for idx in range(arr.length()):
		if arr[idx] > max:
			max = arr[idx]
		elif arr[idx] < min:
			min = arr[idx]

	diff = None

	# Create the size the count array by finding the difference between the minimum value
	#	and maximum value and adding one.
	if max < 0 or (max > 0 and min < 0):
		diff = (min * (-1)) + max
	elif max == 0:
		diff = min * (-1)
	else:
		diff = max - min

	count_arr = StaticArray(diff + 1)
	new_idx = 0
	next_idx = 0
	count_check = 0

	# Check to see if the values are all negative or the max value being zero.
	if max <= 0:
		new_min = min * (-1)
		new_max = max * (-1)

		# Iterate through the array to create the count_arr containing the number of values
		#	Each value will be multiplied by -1 to become positive, and then subtracted by the
		#	new_max will will get the lowest number to be stored in the 0 index and increment from there.
		for idx in range(arr.length()):
			if count_arr[arr[idx] * (-1) - new_max] is not None:
				count_arr[arr[idx] * (-1) - new_max] += 1
				idx += 1
			else:
				count_arr[arr[idx] * (-1) - new_max] = 1
				idx += 1

		# Iterate through the count_arr and determine how many of each value need to be stored
		# 	in new_arr. If the value in count_arr is more than one, then the next_idx will not increase
		#	so the value can be stored again in new_arr. Each value is increased by new_max and then
		#	multiplied by -1 to become negative again.
		while next_idx in range(count_arr.length()):
			if count_check > 1:
				new_arr[new_idx] = new_arr[new_idx - 1]
				count_check -= 1
				new_idx += 1
				if count_check == 1:
					next_idx += 1
			elif count_arr[next_idx] is not None:
				count_check = count_arr[next_idx]
				new_arr[new_idx] = (next_idx + new_max) * (-1)
				new_idx += 1
				if count_check == 1:
					next_idx += 1
			else:
				next_idx += 1

	# Check to see if the values are both positive and negative.
	elif max > 0 and min < 0:
		new_min = min * (-1)

		# Iterate through the array to create the count_arr containing the number of values
		#	Each value will be subtracted by new_min to become zero or positive. This means the
		#	smallest value will be at 0 and can be stored at index 0 of count_arr.
		for idx in range(arr.length()):
			if count_arr[arr[idx] + new_min] is not None:
				count_arr[arr[idx] + new_min] += 1
				idx += 1
			else:
				count_arr[arr[idx] + new_min] = 1
				idx += 1

		# Iterate through the count_arr and determine how many of each value need to be stored
		# 	in new_arr. If the value in count_arr is more than one, then the next_idx will not increase
		#	so the value can be stored again in new_arr. Each value is decreased by new_min to become
		#	it's original value.
		while next_idx < (count_arr.length()):
			if count_arr[next_idx] == 0 and next_idx != 0:
				new_arr[new_arr.length() - new_idx - 1] = new_arr[new_idx - 1]
				count_check -= 1
				new_idx += 1
				if count_check == 1:
					next_idx += 1

			elif count_arr[next_idx] > 0:
				count_check = count_arr[next_idx]
				new_arr[new_arr.length() - new_idx - 1] = next_idx - new_min
				new_idx += 1
				if count_check == 1:
					next_idx += 1

			else:
				next_idx += 1

	# If all values in the array are positive.
	else:

		# Iterate through the array to create the count_arr containing the number of values
		#	Each value will be subtracted by min so the minimum value will be zero and can be stored
		#	in the 0 index of count_arr.
		for idx in range(arr.length()):
			if count_arr[arr[idx] - min] is not None:
				count_arr[arr[idx] - min] += 1
				idx += 1
			else:
				count_arr[arr[idx] - min] = 1
				idx += 1

		# Iterate through the count_arr and determine how many of each value need to be stored
		# 	in new_arr. If the value in count_arr is more than one, then the next_idx will not increase
		#	so the value can be stored again in new_arr. Each value is increased by min to become
		#	it's original value.
		while next_idx < (count_arr.length()):
			if count_check > 1:
				new_arr[new_arr.length() - new_idx - 1] = new_arr[new_arr.length() - new_idx]
				count_check -= 1
				new_idx += 1
				if count_check == 1:
					next_idx += 1

			elif count_arr[next_idx] is not None:
				count_check = count_arr[next_idx]
				new_arr[new_arr.length() - new_idx - 1] = next_idx + min
				new_idx += 1
				if count_check == 1:
					next_idx += 1

			else:
				next_idx += 1


	return new_arr


# array_size = 5_000_000
# min_val = random.randint(-10**9, 10**9 - 998)
# max_val = min_val + 998
# case = [random.randint(min_val, max_val) for _ in range(array_size)]
# arr = StaticArray(len(case))
# for i, value in enumerate(case):
# 	arr[i] = value
# print(f'Started sorting large array of {array_size} elements')
# result = count_sort(arr)
# print(f'Finished sorting large array of {array_size} elements')


# test_cases = (
# 	[4,7,2,9,5,2],
# 	[5, 4, 3, 2, 1],
# 	[0, -5, -3, -4, -2, -1, 0],
# 	[-3, -2, -1, 0, 1, 2, 3],
# 	[1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
# 	[10100, 10721, 10320, 10998],
# 	[-100320, -100450, -100999, -100001],
# )
# for case in test_cases:
# 	arr = StaticArray(len(case))
# 	for i, value in enumerate(case):
# 		arr[i] = value
# 	before = arr if len(case) < 50 else 'Started sorting large array'
# 	print(f"Before: {before}")
# 	result = count_sort(arr)
# 	after = result if len(case) < 50 else 'Finished sorting large array'
# 	print(f"After: {after}")

# ---------------------------- PROBLEM 10 - SORTED_SQUARES -----------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
	"""
	A function that takes a sorted static array as a parameter and returns a new static array
	containing the squares of the integers and sorted in non-descending order.
	:param: arr - a sorted, static array
	:return: new_arr - a new, non-descending static array of the squares for each value
	"""

	new_arr = StaticArray(arr.length())

	# Check to see if the value at idx 0 is negative and the final value is positive
	if (arr[0] < 0) and (arr[arr.length() - 1] > 0):
		square_arr = StaticArray(arr.length())

		# Create a new static array containing the squares in the same indices
		for idx in range(arr.length()):
			square_arr[idx] = arr[idx] * arr[idx]

		firstIdx = 0
		lastIdx = 0

		#	Iterate through square_arr by comparing the first and last values. Whichever is larger,
		#	will get stored as the last value in new_arr. Each number will be compared and the larger
		#	will be stored in the last available spot of new_arr.
		for next_idx in range(arr.length()):
			if square_arr[firstIdx] >= square_arr[square_arr.length() - lastIdx - 1]:
				new_arr[new_arr.length() - next_idx - 1] = square_arr[firstIdx]
				firstIdx += 1
			elif square_arr[firstIdx] < square_arr[square_arr.length() - lastIdx - 1]:
				new_arr[new_arr.length() - next_idx - 1] = square_arr[square_arr.length() - lastIdx - 1]
				lastIdx += 1

	else:
		max = arr[0]
		min = arr[0]

		# Iterate through arr to find the min and max values
		for idx in range(arr.length()):
			if arr[idx] > max:
				max = arr[idx]
			elif arr[idx] < min:
				min = arr[idx]

		if min >= 0:
			# Calculate the squares of the value and store them in the same index of new_arr.
			for next_idx in range(arr.length()):
				new_arr[next_idx] = arr[next_idx] * arr[next_idx]

		elif max <= 0:
			# Calculate the squares of each value and store them starting at the end of new_arr.
			for next_idx in range(arr.length()):
				new_arr[next_idx] = arr[arr.length() - next_idx - 1] * arr[arr.length() - next_idx - 1]


	return new_arr


test_cases = (
	[1, 2, 3, 4, 5],
	[-5, -4, -3, -2, -1, 0],
	[-3, -2, -2, 0, 1, 2, 3],
)
for case in test_cases:
	arr = StaticArray(len(case))
	for i, value in enumerate(sorted(case)):
		arr[i] = value
	print(arr)
	result = sorted_squares(arr)
	print(result)
