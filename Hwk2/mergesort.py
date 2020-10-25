import sys
import os
import time

PARITION_SIZE_CUTOFF = 1000

# Python program for implementation of MergeSort from https://www.geeksforgeeks.org/python-program-for-merge-sort/ 
  
# Merges two subarrays of arr[]. 
# First subarray is arr[l..m] 
# Second subarray is arr[m+1..r] 
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 

    # Check if the partition size is greater than the specified cutoff
    if len(L) <= PARITION_SIZE_CUTOFF:
        insertionSort(L)
        insertionSort(R)
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 

    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,l,r): 
    if l < r: 
        # Same as (l+r)//2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1)) // 2
  
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 

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
        mergeSort(arr,0,n-1)
        print("--- %s seconds ___" % (time.time() - start_time))
        arr.clear
    avg_time = (time.time() - start_time) / 10
    print('Average runtime for ' + str(PARITION_SIZE_CUTOFF) + ' partitions is: ' + str(avg_time) + ' seconds')

# Run the merge - insertion sort
main()
