import csv
#The station dictionary is used to store the most up-to-date gas stations.
#We can determine if a gas station entry in a heap is outdated by simply checking if it's included in the dictionary.
stationDictionary = {}
class MinHeap:
    def __init__(self):
        self.arr = []
    def insert(self, val):
        """Function to insert a value into the heap"""
        self.arr.append(val)
        #We assume that the parent is the last element of the array.
        i = len(self.arr) - 1
        #Each gas price is compared to its parent.
        while i > 0 and float(self.arr[(i - 1) // 2][8]) > float(self.arr[i][8]):
            #If the gas price of the parent is greater than the gas price of the child, they get swapped.
            self.arr[i], self.arr[(i - 1) // 2] = self.arr[(i - 1) // 2], self.arr[i]
            #We change the index so its equal to the position of our value.
            i = (i - 1) // 2

    def getMin(self):
        """Returns all the data about the gas station that has the smallest gas price."""
        while self.arr:
            if self.arr[0][8] == stationDictionary[(self.arr[0][0],self.arr[0][7])]:
                #Returning the first (smallest) value of the minHeap if the value is found in the dictionary.
                return self.arr[0]
            else:
                #Using lazy delete to remove values that are old (not found in the dictionary).
                self.removeFirst()
        return None
    def getMinPrice(self):
        """Same as getMin, but only returns the station name, fuel type and fuel cost."""
        while self.arr:
            if self.arr[0][8] == stationDictionary[(self.arr[0][0],self.arr[0][7])]:
                return (self.arr[0][0],self.arr[0][7],self.arr[0][8])
            else:
                self.removeFirst()
        return None

    def popMin(self):
        """Returns the first value from the heap and removes it"""
        while self.arr:
            first = self.arr[0]
            self.removeFirst()
            if first[8] == stationDictionary[(first[0], first[7])]:
                return first
        return None
    def removeFirst(self):
        """Function that removes the first (smallest) element of the heap and reorders it accordingly."""
        #The first value is replaced with the last value and the last value gets removed from the heap array.
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        i=0
        while True:
            leftChild = 2 * i + 1
            rightChild = 2 * i + 2
            smallest = i
            #Elements get compared with both of their children and swapped if one of them is smaller until a swap is not made.
            if leftChild < len(self.arr) and float(self.arr[leftChild][8]) < float(self.arr[smallest][8]):
                smallest = leftChild
            if rightChild < len(self.arr) and float(self.arr[rightChild][8]) < float(self.arr[smallest][8]):
                smallest = rightChild
            if smallest != i:
                self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
                #Saving the index of the smallest found value.
                i = smallest
            else:
                break
    def fullPop(self):
        """Function that gets and removes smallest element of heap until heap is empty"""
        while True:
            result = self.popMin()
            if result is None:
                break
def minimum(array):
    """Function that returns the gas station with the smallest gas price."""
    smallest = array[0]
    for i in range(1, len(array)):
        if float(array[i][8]) < float(smallest[8]):
            smallest = array[i]
    return smallest
def partition(array, low, high):
    """Function that sorts gas stations around the gas price of a specific pivot station."""
    #The middle element from list gets picked as the pivot.
    pivotIndex = (low + high) // 2
    pivot = float(array[pivotIndex][8])
    #The pivot gets moved to the back of the list.
    array[high], array[pivotIndex] = array[pivotIndex], array[high]
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
def quickSort(array, low, high):
    """Recursively uses partition to sort every element of the array until the partition is just a single element."""
    if low < high:
        pivotIndex = partition(array, low, high)
        quickSort(array, low, pivotIndex - 1)
        quickSort(array, pivotIndex + 1, high)

def load_csv(filename,heap95,heap98,heapdiesel,heapLPG):
    """Function that loads data from CSV and puts the gas stations in correct heaps."""
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            #Converting gas price from string to float for future comparisons
            row[8] = float(row[8])
            #Values get added to their respective heaps according to the fuel type.
            if row[7] == "Benzinas 95":
                heap95.insert(row)
            elif row[7] == "Benzinas 98":
                heap98.insert(row)
            elif row[7] == "Dyzelinas":
                heapdiesel.insert(row)
            elif row[7] == "LPG":
                heapLPG.insert(row)
            #Gas price is added to the station dictionary or replaced if that gas station is already in the dictionary.
            stationDictionary[(row[0],row[7])] = row[8]

