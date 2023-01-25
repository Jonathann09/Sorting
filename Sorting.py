print("Urrete, Jonathan U.")
print("BSCOE 2-2")



print("================== ")
print("    BUBBLE SORT    ")
print("===================")

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

print("===========================")
print("     INSERTION SORT        ")
print("===========================")

#INSERTION SORT

def Insertionsort(array):
     print(array)
     #Traverse through 1 to Len(array)
     for a in range(1, len(array)):
        b = a
        while b > 0 and array[b] < array[b -1]:
            array[b - 1], array[b] = array[b], array[b-1] 
            b -= 1
            print(array)
                
#Driver code
array = [24, 71, 8, 1, 16, 56, 68, 18, 19, 53]
Insertionsort(array)




