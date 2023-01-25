print("Urrete, Jonathan U.")
print("BSCOE 2-2")
print("===================")
print()

#BUBBLE SORT

def bubbleSort(arr):
      
    n = len(arr)
    
    for i in range(n):
      
        for j in range(0, n - i - 1):
           
           print ( "j", j)
           print ( "j+1",j+1)
           print(arr)
           if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)

elements = [24, 71, 8, 1, 16, 56, 68, 18, 19, 53]

bubbleSort(elements)

print('Sorted Array:')
print(elements)