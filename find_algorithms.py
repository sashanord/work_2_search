
"""Простой поиск"""
def simple_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return -1

"""Бинарный поиск"""
def binary_search(arr, start, end, key):
    if start > end:
        return -1

    middle = start + (end - start) // 2

    if arr[middle] == key:
        return middle
    if arr[middle] > key:
        return binary_search(arr, start, middle - 1, key)

    return binary_search(arr, middle + 1, end, key)

"""Быстрая сортировка для использования позднее для бинарного поиска"""
def quick_sort(arr, start, end):
    if start >= end:
        return

    i = start
    j = end
    p = arr[start + (end - start) // 2]

    while i <= j:
        while arr[i] < p:
            i += 1
        while arr[j] > p:
            j -= 1
        if i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

            i += 1
            j -= 1

    if start < j:
        quick_sort(arr, start, j)
    if end > i:
        quick_sort(arr, i, end)