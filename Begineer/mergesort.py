# Code by copyassignment.com
# Function
# merge sort
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the middle of the array
        r = len(arr) // 2

        # Dividing array into two halves
        leftArray = arr[:r]
        rightArray = arr[r:]

        # Calling mergesort function on subparts of array
        mergeSort(leftArray)
        mergeSort(rightArray)

        i = j = k = 0

        # Copying data to temp arrays leftArray[] and rightArray[]
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
            else:
                arr[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1


# function to print the array
def display(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code
if __name__ == '__main__':
    arr = [6, 5, 12, 10, 9, 1]
    print("Original array")
    display(arr)
    mergeSort(arr)
    print("Sorted array")
    display(arr)