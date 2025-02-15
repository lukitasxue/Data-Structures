# BUBBLE SORT
# Compare adjacent elements.
# Swap them if they are in the wrong order.
# Repeat the process for every pair of adjacent elements.
# Continue until no more swaps are needed.

arr = [3,2,6,8,1,9,5,0,4,7]

def bubble_sort(arr):
    index_length = len(arr) - 1 # there is no number to compare for the last set
    finished = False

    while not finished:
        finished = True
        for i in range(0, index_length):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                finished = False #swap ocurred, so we need other pass
        
    return arr
            




print(bubble_sort([3,2,6,8,1,9,5,0,4,7]))