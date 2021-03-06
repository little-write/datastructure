'''
bubble sort, insertion sort, and selection sort
'''

from typing import List

#冒泡排序
def bubble_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    for i in range(length):
        made_swap = False
        for j in range(length-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                made_swap = True
        if not made_swap:
            break

#插入排序
def insertion_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    for i in range(1,length):
        value = a[i]
        j = i-1
        while j >= 0 and a[j] > value:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = value

#选择排序
def selection_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    for i in range(length):
        min_index = i
        min_val = a[i]
        for j in range(i, length):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

if __name__ == '__main__':
    array = [5,6,-1,4,2,8,10,7,6]
    bubble_sort(array)
    print(array)

    array = [5,6,-1,4,2,8,10,7,6]
    insertion_sort(array)
    print(array)

    array = [5,6,-1,4,2,8,10,7,6]
    selection_sort(array)
    print(array) 

			
