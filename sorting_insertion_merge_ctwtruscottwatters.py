#pylint:disable= 'unmatched ')' (<unknown>, line 79)'
import time
def sort(left, right, cmp):
	i, j = 0, 0
	result = []
	while i < len(left) and j < len(right):
		if cmp(left[i], right[j]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1
	return result
	
def mergeSort(L, cmp):
	if len(L) < 2:
		return L[:]
	else:
		left = mergeSort(L[:len(L) // 2], cmp)
		right = mergeSort(L[len(L) // 2:], cmp)
		return sort(left, right, cmp)
		
L1= [x for x in range(10, 0, -1)]
L2 = [x for x in range(30, 0, -1)]
L3 = [x for x in range(100, 0, -1)]
print("L: {}\nL2: {}\L3: {}".format(L1, L2, L3))
merge_time_ten = time.perf_counter()
Sorted = mergeSort(L1, lambda l, r: l < r)
merge_time_ten = time.perf_counter() - merge_time_ten
print("L sorted: {}".format(Sorted))
merge_time_thirty = time.perf_counter()
Sorted2 = mergeSort(L2, lambda l, r: l < r)
merge_time_thirty = time.perf_counter() - merge_time_thirty
print("L2 sorted: {}".format(Sorted2))

merge_time_hundred = time.perf_counter()
Sorted3 = mergeSort(L3, lambda l, r: l < r)
merge_time_hundred = time.perf_counter() - merge_time_hundred
print("L3 sorted: {}".format(Sorted3))

# Charles Thomas Wallace Truscott Watters. Massachusetts Institute of Technology

def InsertionSort(L):
	t = time.perf_counter()
	for j in range(1, len(L)):
		key = L[j]
		i = j - 1
		while i >= 0 and L[i] > key:
			L[i + 1] = L[i]
			i -= 1
		L[i + 1] = key
	t2 = time.perf_counter() - t
	return L
L = [x for x in range(10, 0, -1)]
L2 = [x for x in range(30, 0, -1)]
L3 = [x for x in range(100, 0, -1)]
print("Unsorted List One: {}\nUnsorted List Two: {}\nUnsorted List Three {}".format(L, L2, L3))
ins_time_ten = time.perf_counter()
L = InsertionSort(L)
ins_time_ten = time.perf_counter() - ins_time_ten
print("L sorted: {}".format(L))
ins_time_thirty = time.perf_counter()
L2 = InsertionSort(L2)
ins_time_thirty = time.perf_counter() - ins_time_thirty
print("L2 sorted: {}".format(L2))
ins_time_hundred = time.perf_counter()
L3 = InsertionSort(L3)
ins_time_hundred = time.perf_counter() - ins_time_hundred
print("L3 sorted: {}".format(L3))
#print("The first took {} seconds and the second took {}".format(tl1, tl2))

print("Merge Sort, a log2 algorithm takes {} microseconds for a list of size ten and {} for a list of size thirty and {} for a list of size 100".format(merge_time_ten * 10 ** 5, merge_time_thirty * 10 ** 5, merge_time_hundred * 10 ** 5))

print("Insertion sort, an quadratic algorithm takes {} microseconds for a list of size ten and {} microseconds for a list of size thirty and {} microseconds for a list of size one hundred".format(ins_time_ten * 10 ** 5, ins_time_thirty * 10 ** 5, ins_time_hundred * 10 ** 5))
import numpy as np
print("Merge Sort, Ratios (microseconds per instruction): a list of size ten {};  a list of size thirty {}; a list of size one hundred {}".format((merge_time_ten * 10 ** 5) / ((15 + 23) * np.log2(10)), (merge_time_thirty * 10 ** 5) /((15 + 23) * np.log2(30)), (merge_time_hundred * 10 ** 5) / ((15 + 23) * np.log2(100))))

print("Insertion sort, Ratios (microseconds per instruction): a list of size ten {}; a list of size thirty {}; a list of size one hundred {}".format((ins_time_ten * 10 ** 5) / (15 * 10 ** 2)  , (ins_time_thirty * 10 ** 5) / (15 * 30 ** 2), (ins_time_hundred * 10 ** 5) / (15 * 100 ** 2)))

print("Merge Sort is {}% faster in instructions per microsecond than Insertion Sort for an input size of one hundred".format(round((((ins_time_hundred * 10 ** 5)) / (15 * 100 ** 2) / (merge_time_hundred * 10 ** 5) / (38 * np.log2(100))) * 10 ** 7 * 100, 2)))
"""
Dimensional Analysis of Computational Complexity (Algorithmic Complexity)

Charles Thomas Wallace Truscott Watters, MITx """