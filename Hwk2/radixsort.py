import time

# Python program for implementation of Radix Sort from https://www.geeksforgeeks.org/python-program-for-radix-sort/
   
# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
def countingSort(arr, exp1): 
   
    n = len(arr) 
   
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
   
    # initialize count array as 0 
    count = [0] * (10) 
   
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
   
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
   
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
   
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
 
# Method to do Radix Sort
def radixSort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10

def main():
    # Driver code to test above 
    arr = [] 
    avgRunTime = 0
    for i in range(10):
        # Read in test data from every test file (make sure test files are in the same directory as code )
        file_name = ('set' + str(i) + '.txt') # This will equate to 'set1.txt', 'set2.txt', etc. 
        with open(file_name, 'r') as f:
            for line in f:
                data = line.split()
                arr.append(int(data[0]))
        # Length of array 
        n = len(arr) 
  
        # Run the sort and print the running time
        start_time = time.time()
        radixSort(arr)
        print("--- %s seconds ___" % (time.time() - start_time))
        arr.clear()
    avg_time = (time.time() - start_time) / 10.0
    print('Average runtime of all 10 test cases is: ' + str(avgRunTime))

# Run the merge - insertion sort
main()