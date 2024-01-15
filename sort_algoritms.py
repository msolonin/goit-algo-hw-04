# -*- coding: utf-8 -*-
"""
Script for verification of time for each type of sorter
"""


import timeit
import random


ATTEMPTS = 2


def bubble_sort(lst):
    lst = lst[:]
    n = len(lst)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def insertion_sort(lst):
    lst = lst[:]
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def selection_sort(lst):
    lst = lst[:]
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def quick_sort(lst):
    lst = lst[:]
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def shell_sort(lst):
    lst = lst[:]
    n = len(lst)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst


def counting_sort(lst, position):
    size = len(lst)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        index = lst[i] // position % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        index = lst[i] // position % 10
        output[count[index] - 1] = lst[i]
        count[index] -= 1
        i -= 1

    for i in range(0, size):
        lst[i] = output[i]


def radix_sort(lst):
    lst = lst[:]
    max_num = max(lst)
    position = 1
    while max_num // position > 0:
        counting_sort(lst, position)
        position *= 10


def merge_sort(lst):
    lst = lst[:]
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged


if __name__ == '__main__':
    # Generate data for sorters:
    data_small = [random.randint(0, 1_000) for _ in range(1_000)]
    data_medium = [random.randint(0, 10_000) for _ in range(10_000)]

    # Start check for time of sorting for each sorter with small dataset:
    time_small_bubble = timeit.timeit(lambda: bubble_sort(data_small[:]), number=ATTEMPTS)
    time_small_insertion = timeit.timeit(lambda: insertion_sort(data_small[:]), number=ATTEMPTS)
    time_small_selection = timeit.timeit(lambda: selection_sort(data_small[:]), number=ATTEMPTS)
    time_small_merge = timeit.timeit(lambda: merge_sort(data_small[:]), number=ATTEMPTS)
    time_small_quicksort = timeit.timeit(lambda: quick_sort(data_small[:]), number=ATTEMPTS)
    time_small_shell = timeit.timeit(lambda: shell_sort(data_small[:]), number=ATTEMPTS)
    time_small_radix = timeit.timeit(lambda: radix_sort(data_small[:]), number=ATTEMPTS)
    time_small_timsort = timeit.timeit(lambda: sorted(data_small[:]), number=ATTEMPTS)
    time_small_timsort_s = timeit.timeit(lambda: data_small[:].sort(), number=ATTEMPTS)

    # Start check for time of sorting for each sorter with medium dataset:
    time_medium_bubble = timeit.timeit(lambda: bubble_sort(data_medium[:]), number=ATTEMPTS)
    time_medium_insertion = timeit.timeit(lambda: insertion_sort(data_medium[:]), number=ATTEMPTS)
    time_medium_selection = timeit.timeit(lambda: selection_sort(data_medium[:]), number=ATTEMPTS)
    time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium[:]), number=ATTEMPTS)
    time_medium_quicksort = timeit.timeit(lambda: quick_sort(data_medium[:]), number=ATTEMPTS)
    time_medium_shell = timeit.timeit(lambda: shell_sort(data_medium[:]), number=ATTEMPTS)
    time_medium_radix = timeit.timeit(lambda: radix_sort(data_medium[:]), number=ATTEMPTS)
    time_medium_timsort = timeit.timeit(lambda: sorted(data_medium[:]), number=ATTEMPTS)
    time_medium_timsort_s = timeit.timeit(lambda: data_medium[:].sort(), number=ATTEMPTS)

    print(f"{'| Algorithm': <20} | {'Time small data': <20} | {'Time medium data': <20}")
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19}")
    print(f"{'| Bubble sort': <20} | {time_small_bubble:<20.5f} | {time_medium_bubble:<20.5f}")
    print(f"{'| Insertion sort': <20} | {time_small_insertion:<20.5f} | {time_medium_insertion:<20.5f}")
    print(f"{'| Selection sort': <20} | {time_small_selection:<20.5f} | {time_medium_selection:<20.5f}")
    print(f"{'| Merge sort': <20} | {time_small_merge:<20.5f} | {time_medium_merge:<20.5f}")
    print(f"{'| Quicksort': <20} | {time_small_quicksort:<20.5f} | {time_medium_quicksort:<20.5f}")
    print(f"{'| Shell sort': <20} | {time_small_shell:<20.5f} | {time_medium_shell:<20.5f}")
    print(f"{'| Radix sort': <20} | {time_small_radix:<20.5f} | {time_medium_radix:<20.5f}")
    print(f"{'| Tim sort sorted': <20} | {time_small_timsort:<20.5f} | {time_medium_timsort:<20.5f}")
    print(f"{'| Tim sort sort': <20} | {time_small_timsort_s:<20.5f} | {time_medium_timsort_s:<20.5f}")
