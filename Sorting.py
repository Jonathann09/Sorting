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


print("===========================")
print("        MERGE SORT         ")
print("===========================")

#MERGE SORT

def mergeSort(myList):
    if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]
            print("left: ", left, "right: ", right )
            #recursive call on each half
            mergeSort(left)
            mergeSort(right)
    
            i = 0
            j = 0
            
            k = 0
    
            while i < len(left) and j < len(right):
              if left[i] <= right[j]:
               myList[k] = left[j]
              i += 1
            else:
             myList[k] = right[j]
             j += 1
             k += 1
            while i < len(left):
              myList[k] = left[1]
              i + 1
              k += 1        
            while j < len(right):
              myList[k]=right[j]
              j += 1
              k += 1
              print(myList)
mylist = [24, 71, 8, 1, 16, 56, 68, 18, 19, 53] 
mergeSort(mylist)
   
   

print("===========================")
print("        QUICK SORT         ")
print("===========================")

#QUICK SORT


def quickSort(array, left, right):
     if left < right:
        pi = partition(array, left, right)
        
        quickSort(array, left, pi - 1)
        
        quickSort(array, pi + 1, right)
        

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    print("Pivot", pivot)
    while i < j:
            while i < right and arr[i] < pivot:
                 i += 1
                 print("i", i, "arr(i)",arr[i])
            while j > left and arr[j] >= pivot:
                 j -= 1
                 print("j", j, "arr[j]",arr[j])
            if i < j:
                 arr[i], arr[j] = arr[j], arr[i]
                 print(arr)
    if arr[i]> pivot:
           arr[i], arr[right] = arr[right], arr[i]
           print(arr)
    return i
data = [24, 71, 8, 1, 16, 56, 68, 18, 19, 53] 
print(data)
quickSort(data, 0, len(data) -1)
       


   