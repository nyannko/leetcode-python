l = [1, 2, 3, 3, 4, 5]


# two pointers
def remove_duplicate(l):
    index = 0
    for i in range(len(l)):
        if l[i] != l[index]:
            index += 1
            l[index] = l[i]
    print(index)
    print(l[:index + 1])


# two pointers
def remove_target(l, target=3):
    index = 0
    for i in range(len(l)):
        if l[i] != target:
            l[index] = l[i]
            index += 1
    print(l[:index])


# pop values and minus length by one
def remove_target1(l, target=3):
    i = 0
    length = len(l)
    while i < length:
        if l[i] == target:
            l.pop(i)
            length -= 1
        else:
            i += 1
    print(l)


# slice
def remove_target2(l, target=3):
    for i in l[:]:
        if i == target:
            l.remove(i)
    print(l)


def remove_target3(l, target=4):
    index = 0
    for i in range(len(l)):
        if l[i] < target:
            l[index] = l[i]
            index += 1
    print(l[:index])


remove_duplicate(list(l))
remove_target(list(l))
remove_target1(list(l))
remove_target2(list(l))
remove_target3(list(l))
