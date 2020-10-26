import time
import sys
sys.setrecursionlimit(1000000000)

# Python program for implementation of Quicksort Sort from https://www.geeksforgeeks.org/python-program-for-quicksort/
 
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
 
PARITION_SIZE_CUTOFF = int(sys.argv[1])

def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # Greater than or equal to becuase we want to run the quicksort as long as parition sizes are bigger than the cutoff, once they are smaller do insertionsort
        if (high - low) <= PARITION_SIZE_CUTOFF:
            insertionSort(arr)
        else:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = partition(arr, low, high)
            
            # Separately sort elements before
            # partition and after partition
            quickSort(arr, low, pi-1)
            quickSort(arr, pi+1, high)

# Insertion sort implemention from https://www.tutorialspoint.com/insertion-sort-in-python-program
def insertionSort(arr):
    for i in range(1, len(arr)):
      key = arr[i]
      # Move elements of arr[0..i-1], that are greater than key to one position ahead of their current position
      j = i - 1
      while j >= 0 and key < arr[j] :
         arr[j + 1] = arr[j]
         j -= 1
      arr[j + 1] = key

def main():
    # Driver code to test above 
    arr = [] 
    avg_time = 0
    total_time = 0
    for i in range(10):
        # Read in test data from every test file (make sure test files are in the same directory as code )
        file_name = ('set' + str(i) + '.txt') # This will equate to 'set1.txt', 'set2.txt', etc. 
        with open(file_name, 'r') as f:
            for line in f:
                data = line.split()
                arr.append(int(data[0]))
        # Length of array 
        n = len(arr) 
  
        # Run the sort
        start_time = time.time()
        quickSort(arr,0,n-1)
        print("--- %s seconds ___" % (time.time() - start_time))
        total_time += (time.time() - start_time)
        arr.clear()
    avg_time = total_time / 10
    print('Average runtime for ' + str(PARITION_SIZE_CUTOFF) + ' partitions is: ' + str(avg_time))

# Run sort
main()