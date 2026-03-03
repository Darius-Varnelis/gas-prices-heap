from gas_prices import load_csv, MinHeap
heap95 = MinHeap()
heap98 = MinHeap()
heapdiesel = MinHeap()
heapLPG = MinHeap()
load_csv("lithuanian_gas_stations.csv",heap95,heap98,heapdiesel,heapLPG)
print(heap98.getMin())
