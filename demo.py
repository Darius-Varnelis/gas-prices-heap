from gas_prices import load_csv, MinHeap
heap95 = MinHeap()
heap98 = MinHeap()
heapdiesel = MinHeap()
heapLPG = MinHeap()
stationDictionary = []
load_csv("lithuanian_gas_stations.csv", heap95, heap98, heapdiesel, heapLPG)
print(heap95.getMin())
heap95.insert(['LT0279', 'Lietuva Šiauliai', 'Lietuva', 'UkmergÄ—s pl. 148', 'Šiauliai', 'Šiaulių apskritis', 'Lithuania', 'Benzinas 95', '1.4', '2024-03-30 13:32'])

