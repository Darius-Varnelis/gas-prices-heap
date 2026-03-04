from gas_prices import *
import csv
import time
import timeit
import copy
heap95 = MinHeap()
heap98 = MinHeap()
heapdiesel = MinHeap()
heapLPG = MinHeap()
load_csv("lithuanian_gas_stations.csv", heap95, heap98, heapdiesel, heapLPG)
newCSV = []
with open("lithuanian_gas_stations.csv") as csvfile:
    reader = csv.reader(csvfile)
    csvfile.seek(0)
    next(reader)
    for row in reader:
        if row[7] == "Benzinas 95":
            newCSV.append(row)
start = time.time()
#Popping every single element from heap which results in a sorted list of elements


heap_copies = [copy.deepcopy(heap95) for _ in range(100)]
i = 0
def run():
    global i
    heap_copies[i].fullPop()
    i += 1

time1 = timeit.timeit(run, number=100)
print(f"Average heap popping time: {time1/100} seconds")
#If we want to simply get a sorted list, using a method like quick sort is faster than popping every single
#element from the heap even if the result we receive is the same.

time2 = timeit.timeit(lambda: quickSort(newCSV.copy(), 0, len(newCSV)-1), number=100)
print(f"Average QuickSort time: {time2/100} seconds")
print(f"QuickSort is {time1/time2} times faster", '\n')
#Testing how much time it takes on average to get the smallest element from minHeap (O(1))
time1 = timeit.timeit(lambda: heap95.getMin(), number=100)
print(f"Average time to get smallest element from heap: {time1/100} seconds")
# Testing how much time it takes to find min element using linear search on list (O(n))
time2 = timeit.timeit(lambda: minimum(newCSV), number=100)
print(f"Average time to find smallest element from list: {time2/100} seconds")
print(f"Heap is {time2/time1} times faster")