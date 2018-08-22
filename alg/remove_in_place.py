l = [0,1,2,2,3,0,4,2]
val = 2
length = len(l)

for i in range(length):
    #print(i)
    if l[i] == val:
        i -= 1
        l.pop(i)

        length -= 1



# when the element is ready to move the index does not change


print(l)