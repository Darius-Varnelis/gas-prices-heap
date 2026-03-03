import csv
stationDictionary = {}
class MinHeap:
    def __init__(self):
        self.arr = []

    def insert(self, val):
        self.arr.append(val)
        i = len(self.arr) - 1
        while i > 0 and float(self.arr[(i - 1) // 2][8]) > float(self.arr[i][8]):
            self.arr[i], self.arr[(i - 1) // 2] = self.arr[(i - 1) // 2], self.arr[i]
            i = (i - 1) // 2

    def getMin(self):
        while self.arr:
            if self.arr[0][8] == stationDictionary[(self.arr[0][0],self.arr[0][7])]:
                return self.arr[0]
            else:
                self.removeFirst()
        return None
    def getMinPrice(self):
        while self.arr:
            if self.arr[0][8] == stationDictionary[(self.arr[0][0],self.arr[0][7])]:
                return (self.arr[0][0],self.arr[0][7],self.arr[0][8])
            else:
                self.removeFirst()

    def popMin(self):
        while self.arr:
            first = self.arr[0]
            self.removeFirst()
            if first[8] == stationDictionary[(first[0], first[7])]:
                return first
        return None
    def removeFirst(self):
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        i=0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.arr) and float(self.arr[left][8]) < float(self.arr[smallest][8]):
                smallest = left
            if right < len(self.arr) and float(self.arr[right][8]) < float(self.arr[smallest][8]):
                smallest = right
            if smallest != i:
                self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
                i = smallest
            else:
                break
def partition(array, low, high):
    pivotIndex = (low + high) // 2
    pivot = array[pivotIndex][8]
    array[high], array[pivotIndex] = array[pivotIndex], array[high]
    i = low
    for j in range(low, high):
        if array[j][8] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i
def quickSort(array, low, high):
    if low < high:
        pivotIndex = partition(array, low, high)
        quickSort(array, low, pivotIndex - 1)
        quickSort(array, pivotIndex + 1, high)

def load_csv(filename,heap95,heap98,heapdiesel,heapLPG):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[7] == "Benzinas 95":
                heap95.insert(row)
            elif row[7] == "Benzinas 98":
                heap98.insert(row)
            elif row[7] == "Dyzelinas":
                heapdiesel.insert(row)
            elif row[7] == "LPG":
                heapLPG.insert(row)
            stationDictionary[(row[0],row[7])] = row[8]
