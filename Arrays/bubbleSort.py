# BUBBLE SORT
# Compare adjacent elements.
# Swap them if they are in the wrong order.
# Repeat the process for every pair of adjacent elements.
# Continue until no more swaps are needed.

arr = [3,2,6,8,1,9,5,0,4,7]

def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range (0, n -i-1):
            x = arr[j]
            y = arr[j+1]

            if x > y:
                #swap numbers
                arr[j], arr[j+1] = arr[j+1], arr[j]




bubble_sort(arr)