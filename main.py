import random

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n-1):
        for j in range(n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return arr, comparisons, swaps

def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return arr, comparisons, swaps
