import csv
import pandas as pd
#The station dictionary is used to store the most up-to-date gas stations.
#We can determine if a gas station entry in a heap is outdated by simply checking if it's included in the dictionary.
stationDictionary = {}

class MinHeap:

    def __init__(self):
        self.arr = []

    def insert(self, val):
        """Function to insert a value into the heap"""
        #Converting gas price to float for faster comparisons later
        val[8] = float(val[8])
        # Gas price is added to the station dictionary or replaced if that gas station is already in the dictionary.
        stationDictionary[(val[0], val[7])] = val[8]
        self.arr.append(val)
        #We assume that the parent is the last element of the array.
        i = len(self.arr) - 1
        #Each gas price is compared to its parent.
        while i > 0 and float(self.arr[(i - 1) // 2][8]) > float(self.arr[i][8]):
            #If the gas price of the parent is greater than the gas price of the child, they get swapped.
            self.arr[i], self.arr[(i - 1) // 2] = self.arr[(i - 1) // 2], self.arr[i]
            #We change the index so its equal to the position of our value.
            i = (i - 1) // 2

    def get_min(self):
        """Returns all the data about the gas station that has the smallest gas price."""
        while self.arr:
            if self.arr[0][8] == stationDictionary[(self.arr[0][0],self.arr[0][7])]:
                #Returning the first (smallest) value of the minHeap if the value is found in the dictionary.
                return self.arr[0]
            else:
                #Using lazy delete to remove values that are old (not found in the dictionary).
                self.remove_first()
                print("Removed stale element")
        return None

    def get_min_price(self):
        """Same as getMin, but only returns the station name, fuel type and fuel cost."""
        while self.arr:
            if self.arr[0][8] == stationDictionary[(self.arr[0][0],self.arr[0][7])]:
                return self.arr[0][0], self.arr[0][7], self.arr[0][8]
            else:
                print(f"{self.arr[0][0]}, {self.arr[0][7]}, {self.arr[0][8]} is stale.")
                self.remove_first()
                print("Removed stale element")
        return None

    def pop_min(self):
        """Returns the first value from the heap and removes it"""
        while self.arr:
            first = self.arr[0]
            self.remove_first()
            if first[8] == stationDictionary[(first[0], first[7])]:
                return first
        return None

    def remove_first(self):
        """Function that removes the first (smallest) element of the heap and reorders it accordingly."""
        #The first value is replaced with the last value and the last value gets removed from the heap array.
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        i=0
        while True:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            smallest = i
            #Elements get compared with both of their children and swapped if one of them is smaller until a swap is not made.
            if left_child < len(self.arr) and float(self.arr[left_child][8]) < float(self.arr[smallest][8]):
                smallest = left_child
            if right_child < len(self.arr) and float(self.arr[right_child][8]) < float(self.arr[smallest][8]):
                smallest = right_child
            if smallest != i:
                self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
                #Saving the index of the smallest found value.
                i = smallest
            else:
                break

    def full_pop(self):
        """Function that gets and removes smallest element of heap until heap is empty"""
        while True:
            result = self.pop_min()
            if result is None:
                break

def minimum(array) -> list:
    """Function that returns the gas station with the smallest gas price."""
    smallest = array[0]
    for i in range(1, len(array)):
        if float(array[i][8]) < float(smallest[8]):
            smallest = array[i]
    return smallest

def partition(array, low, high) -> int:
    """Function that sorts gas stations around the gas price of a specific pivot station."""
    #The middle element from list gets picked as the pivot.
    pivot_index = (low + high) // 2
    pivot = float(array[pivot_index][8])
    #The pivot gets moved to the back of the list.
    array[high], array[pivot_index] = array[pivot_index], array[high]
    #'i' denotes the position of the first element larger than the pivot.
    i = low
    for j in range(low, high):
        if float(array[j][8]) <= pivot:
            #Each value is compared to the pivot, and if it is not bigger than it, it gets swapped with the
            #element at value i.
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i

def quick_sort(array, low, high) -> None:
    """Recursively uses partition to sort every element of the array until the partition is just a single element."""
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)

def load_csv_heap(filename, heaps) -> None:
    """Function that loads data from CSV and puts the gas stations in correct heaps."""
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            append_to_heaps(row,heaps)

def append_to_heaps(value, heaps) -> None:
    """Function that appends gas station to heaps."""
    heap95, heap98, heap_diesel, heap_lpg = heaps
    #Converting to float for faster comparisons.

    if value[7] == "Benzinas 95":
        heap95.insert(value)
    elif value[7] == "Benzinas 98":
        heap98.insert(value)
    elif value[7] == "Dyzelinas":
        heap_diesel.insert(value)
    elif value[7] == "LPG":
        heap_lpg.insert(value)

def load_csv_list(filename, arr, fuel_type: str) -> None:
    """Function that loads data from CSV and puts the data in the list, filtering by fuel type."""
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[7] == fuel_type:
                row[8] = float(row[8])
                arr.append(row)

def print_table(arr) -> None:
    df = pd.DataFrame([[row[0],row[7],row[8]] for row in arr],
                      columns= ["ID", "Fuel Type","Fuel Cost"])
    print(df)