from gas_prices import *

list_95 = []
CSV_file = "lithuanian_gas_stations.csv"

#Reading data into list
load_csv_list(CSV_file, list_95, "Benzinas 95")
heap95 = MinHeap()
heap98 = MinHeap()
heapdiesel = MinHeap()
heapLPG = MinHeap()
heaps = heap95, heap98, heapdiesel, heapLPG
load_csv_heap(CSV_file, heaps)
#Getting the cheapest gas station
print("Getting min price for gasoline 95:", heap95.get_min_price())

#Adding new smallest element to heap95
print("Updating gas station 'LT0279' with the price of 1.4 to the gasoline 95 heap... ")
append_to_heaps(['LT0279', 'Lietuva Šiauliai', 'Lietuva', 'Ukmergės pl. 148', 'Šiauliai', 'Šiaulių apskritis', 'Lithuania', 'Benzinas 95', '1.4', '2024-03-30 13:32'],heaps)
print("Getting min price for gasoline 95:", heap95.get_min_price())
print()

#Adding new price to the same gas station, but this time it is no longer the smallest one
print("Updating gas station 'LT0279' again with the price of 1.62 to the gasoline 95 heap... ")
append_to_heaps(['LT0279', 'Lietuva Šiauliai', 'Lietuva', 'Ukmergės pl. 148', 'Šiauliai', 'Šiaulių apskritis', 'Lithuania', 'Benzinas 95', '1.62', '2024-03-30 13:32'],heaps)
print("Getting min price for gasoline 95:")
print(heap95.get_min_price())

#Sorting list of all gasoline 95 stations
print("Sorting list of all gasoline 95 stations...")
print("Unsorted:")
print_table(list_95)
quick_sort(list_95, 0, len(list_95) - 1)
print("Sorted:")
print_table(list_95)