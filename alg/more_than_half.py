def more_than_half(arr):
    result = arr[0]
    counter = 1
    for i, num in enumerate(arr):
        if i < 1: continue
        if counter == 0:
            result = num
            counter = 1
        elif num == result:
            counter += 1
        elif num != result:
            counter -= 1

    return result

import string
print(string.ascii_letters, string.punctuation, string.digits)

arr1 = [1, 2, 3, 2, 2, 2, 5, 4, 2]
result = more_than_half([5, 5, 5, 5, 5, 5, 5, 1, 2, 3, 3, 4, 4, 5, 4, 4])
print(result)
