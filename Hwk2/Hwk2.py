import sys
sys.setrecursionlimit(10000000)
import os
import time

sort_list = []

Partition_Size = 1000

#print(os.getcwd() + '/set10')

'''
#   This Section with take the randomized numbers generated in each .txt within the file named -> os.chdir(os.getcwd() + '/FOLDER_NAME') and read them in to a list modify as needed
os.chdir(os.getcwd() + '/set10')
for filename in os.listdir():
    f = open(filename, "r")
    print(filename)
    Lines = f.readlines()
    for line in Lines:
        sort_list.append(int(line))
    print(len(sort_list))
    sort_list.clear()
'''




#                 INSERTION SORT
# Function to do insertion sort                     Obtained from "https://www.geeksforgeeks.org/insertion-sort/" and was contributed by Mohit Kumra to geeksforgeeks
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 


#                       QUICK SORT
# Python program for implementation of Quicksort Sort       Obtained from "https://www.geeksforgeeks.org/insertion-sort/" and was contributed by Mohit Kumra to geeksforgeeks and improved by "https://github.com/anushkrishnav"
 
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# arrayay, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
 
 
def partition(array, low, high):
    i = (low-1)         # index of smaller element
    pivot = array[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if array[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            array[i], array[j] = array[j], array[i]
 
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)
 
# The main function that implements QuickSort
# array[] --> arrayay to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
 
 
def quickSort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
 
        # pi is partitioning index, array[p] is now
        # at right place
        pi = partition(array, low, high)
 
        # Separately sort elements before
        # partition and after partition
        if ((pi-1) - low) <= Partition_Size:
            # Traverse through low to pi-1      Taken from Insertion Sort above
            for i in range(low, pi-1): 
  
                key = array[i] 
  
                # Move elements of arr[0..i-1], that are 
                # greater than key, to one position ahead 
                # of their current position 
                j = i-1
                while j >= 0 and key < array[j] : 
                        arr[j + 1] = array[j] 
                        j -= 1
                array[j + 1] = key 
        else:
            print((pi-1) - low)
            quickSort(array, low, pi-1)

        if (high - (pi+1)) <= Partition_Size:
            # Traverse through low to pi-1      Taken from Insertion Sort above
            for i in range(pi+1, high): 
  
                key = array[i] 
  
                # Move elements of arr[0..i-1], that are 
                # greater than key, to one position ahead 
                # of their current position 
                j = i-1
                while j >= 0 and key < array[j] : 
                        arr[j + 1] = array[j] 
                        j -= 1
                array[j + 1] = key
        else:
            print((high - (pi+1)))
            quickSort(array, pi+1, high)



#               MERGE SORT
# Python program for implementation of MergeSort            Obtained from "https://www.geeksforgeeks.org/merge-sort/" and was contributed by Mayank Khanna to geeksforgeeks
#   Modified for use in this project
def mergeSort(array):
    if len(array) >1:
        mid = len(array)//2 # Finding the mid of the array
        L = array[:mid] # Dividing the array elements 
        R = array[mid:] # into 2 halves
 
        if len(L) <= Partition_Size:
            insertionSort(L)
        else:
            mergeSort(L) # Sorting the first half
        if len(R) <= Partition_Size:
            insertionSort(R)
        else:
            mergeSort(R) # Sorting the first half
 
        i = j = k = 0
         
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i+= 1
            else:
                array[k] = R[j]
                j+= 1
            k+= 1
         
        # Checking if any element was left
        while i < len(L):
            array[k] = L[i]
            i+= 1
            k+= 1
         
        while j < len(R):
            array[k] = R[j]
            j+= 1
            k+= 1
 
# Code to print the list
def printList(arr):
    for i in range(len(arr)):        
        print(arr[i], end =" ")
    print()




#-------------------------------------------------------------

#   Testing
f = open("set0_10.txt")

Lines = f.readlines()
for line in Lines:
    sort_list.append(int(line))
print(len(sort_list))

start = time.time()
quickSort(sort_list, 0, 999999)
end = time.time()
print("Time elapsed: ", end - start, " seconds")
#print(sort_list)
