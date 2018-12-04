def merge(left, right, nums):
    l, r = len(left), len(right)
    i, j, k = 0, 0, 0
    while i < l and j < r:
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    while i < l:
        nums[k] = left[i]
        i += 1
        k += 1
    while j < r:
        nums[k] = right[j]
        j += 1
        k += 1


def merge_sort(nums):
    l = len(nums)
    if l < 2:  # base case
        return
    mid = l / 2
    left = nums[:mid]
    right = nums[mid:]
    merge_sort(left)  # split left
    merge_sort(right)  # split right
    merge(left, right, nums)


lists = [1, 4, 1, 6, 8, 5, 3, 7]
merge_sort(lists)
print(lists)
