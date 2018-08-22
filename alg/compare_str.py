s1 = 'abcazvzabddfbsdasdfasdfasdabdfaaaaaaabdabdhj'
s2 = 'abd'
j = 0
d = {}
i = 0
print(len(s1))

while i < len(s1):
    if s1[i] == s2[j]:
        if j >= len(s2) - 1:
            print('yes', i, j)
            j = -1
            # break
        i += 1
        j += 1
    else:
        if s2[0] != s1[i]:
            i += 1
        j = 0
