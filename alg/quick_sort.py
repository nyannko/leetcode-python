from random import randint


def partition(num, first, last):
    p_index = first
    # randomize pivot
    random_index = randint(first, last)
    num[random_index], num[last] = num[last], num[random_index]
    pivot = num[last]
    for i in range(first, last):
        if num[i] <= pivot:
            num[i], num[p_index] = num[p_index], num[i]  # put the small element in front
            p_index += 1
    num[last], num[p_index] = num[p_index], num[last]
    return p_index


def quick_sort(num, first, last):
    if first < last:
        index = partition(num, first, last)
        quick_sort(num, first, index - 1)
        quick_sort(num, index + 1, last)


def start_quick_sort(num):
    quick_sort(num, 0, len(num) - 1)


num1 = [3, 5, 7, 8, 4]
num2 = [3, 3, 5, 7, 8, 4, 90, 80, 12, 34, 22, 1, 0]
start_quick_sort(num1)
start_quick_sort(num2)
print(num1, num2)
