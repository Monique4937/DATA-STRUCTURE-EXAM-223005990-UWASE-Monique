class HeapSort:
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        
        if left < n and arr[largest][1] < arr[left][1]:
            largest = left

        
        if right < n and arr[largest][1] < arr[right][1]:
            largest = right

        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def sort(self, arr):
        n = len(arr)

        
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  
            self.heapify(arr, i, 0)  


vendors = [
    ("Vendor A", 5),  
    ("Vendor B", 8),
    ("Vendor C", 3),
    ("Vendor D", 9),
    ("Vendor E", 7)
]

print("Vendors before sorting:")
for vendor in vendors:
    print(vendor[0], "Priority:", vendor[1])


heap_sort = HeapSort()
heap_sort.sort(vendors)

print("\nVendors after sorting by priority:")
for vendor in vendors:
    print(vendor[0], "Priority:", vendor[1])
