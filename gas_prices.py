import csv
class MinHeap:
    def __init__(self):
        self.arr = []

    def insert(self, val):
        self.arr.append(val)
        i = len(self.arr) - 1
        while i > 0 and self.arr[(i - 1) // 2][8] > self.arr[i][8]:
            self.arr[i], self.arr[(i - 1) // 2] = self.arr[(i - 1) // 2], self.arr[i]
            i = (i - 1) // 2

    def getMin(self):
        return self.arr[0] if self.arr else None


def load_csv(filename,heap95,heap98,heapdiesel,heapLPG):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[7] == "Benzinas 95":
                heap95.insert(row)
            elif row[7] == "Benzinas 98":
                heap98.insert(row)
            elif row[7] == "Dyzelinas":
                heapdiesel.insert(row)
            elif row[7] == "LPG":
                heapLPG.insert(row)
