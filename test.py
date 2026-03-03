from gas_prices import *
import csv
import time
heap95 = MinHeap()
heap98 = MinHeap()
heapdiesel = MinHeap()
heapLPG = MinHeap()
load_csv("lithuanian_gas_stations.csv", heap95, heap98, heapdiesel, heapLPG)
newCSV = []
with open("lithuanian_gas_stations.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    csvfile.seek(0)
    for row in reader:
        if row[7] == "Benzinas 95":
            newCSV.append(row)
start = time.time()
#Popping every single element from heap which results in a sorted list of elements
while True:
    result = heap95.popMin()
    if result == None:
        break
end = time.time()
print(f"Heap popping time: {end - start} seconds")
start = time.time()
#If we want to simply get a sorted list, using a method like quick sort is faster than popping every single
#element from the heap even if the result we receive is the same.
quickSort(newCSV, 0, len(newCSV)-1)
end = time.time()
print(f"QuickSort time: {end - start} seconds")
