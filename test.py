from gas_prices import *
import time
import timeit
import copy
heap95 = MinHeap()
heap98 = MinHeap()
heapdiesel = MinHeap()
heapLPG = MinHeap()
heaps = heap95, heap98, heapdiesel, heapLPG
CSV_file = "lithuanian_gas_stations.csv"
load_csv_heap(CSV_file, heaps)
list_95 = []
#Reading data into test list for comparisons
load_csv_list(CSV_file, list_95, "Benzinas 95")
start = time.time()
#Popping every single element from heap which results in a sorted list of elements.

#Creating 100 identical copies of heap95 for testing as each fullPop permanently empties the heap.
heap_copies = [copy.deepcopy(heap95) for _ in range(100)]
i = 0
def run():
    global i
    heap_copies[i].full_pop()
    i += 1
#Running fullPop on all test heaps and measuring average time (O(n log n)).
time1 = timeit.timeit(run, number=100)
print("List sort test: ")
print(f"Average heap popping time: {time1/100} seconds")
#If we want to simply get a sorted list, using a method like quick sort is faster than popping every single
#element from the heap even if the result we receive is the same.

#Running quickSort on a copy of newCSV 100 times and displaying the average time (O(n log n)).
time2 = timeit.timeit(lambda: quick_sort(list_95.copy(), 0, len(list_95) - 1), number=100)
print(f"Average QuickSort time: {time2/100} seconds")
print(f"QuickSort is {time1/time2} times faster", '\n')
print("Min element test: ")
#Testing how much time it takes on average to get the smallest element from minHeap (O(1)).
time1 = timeit.timeit(lambda: heap95.get_min(), number=100)
print(f"Average time to get smallest element from heap: {time1/100} seconds")
# Testing how much time it takes to find min element using linear search on list (O(n)).
time2 = timeit.timeit(lambda: minimum(list_95), number=100)
print(f"Average time to find smallest element from list: {time2/100} seconds")
print(f"Heap is {time2/time1} times faster")
