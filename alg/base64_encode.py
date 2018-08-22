translate_dict = {
    'A': 0, 'Q': 16, 'g': 32, 'w': 48,
    'B': 1, 'R': 17, 'h': 33, 'x': 49,
    'C': 2, 'S': 18, 'i': 34, 'y': 50,
    'D': 3, 'T': 19, 'j': 35, 'z': 51,
    'E': 4, 'U': 20, 'k': 36, '0': 52,
    'F': 5, 'V': 21, 'l': 37, '1': 53,
    'G': 6, 'W': 22, 'm': 38, '2': 54,
    'H': 7, 'X': 23, 'n': 39, '3': 55,
    'I': 8, 'Y': 24, 'o': 40, '4': 56,
    'J': 9, 'Z': 25, 'p': 41, '5': 57,
    'K': 10, 'a': 26, 'q': 42, '6': 58,
    'L': 11, 'b': 27, 'r': 43, '7': 59,
    'M': 12, 'c': 28, 's': 44, '8': 60,
    'N': 13, 'd': 29, 't': 45, '9': 61,
    'O': 14, 'e': 30, 'u': 46, '+': 62,
    'P': 15, 'f': 31, 'v': 47, '/': 63
}

# convert all char to visible char according to table.
# base 64 8-bit char ------> 6-bit char, output length = input length * (3/4), for example, 10, 11, 12
# have both 16-bit char output, 10 with two =, 11 with one = , while 12 with zero =.
# base 64 encode let char get longer.....
def base64_encode(s):
    new_str = ''
    for i in s:
        str1 = bin(ord(i))[2:].zfill(8)
        new_str += str(str1)

    print(new_str, len(new_str))

    i = 0
    l = []
    while i < len(new_str):
        new_char = new_str[i:i + 6]
        i = i + 6
        if len(new_char) < 6:
            print(new_char)
            new_char += '0' * (6 - len(new_char))
            print(new_char)
        print(new_char)
        l.append(int(new_char, 2))
    print(l)

    encode_str = ''
    for i in l:
        for k, v in translate_dict.items():
            if v == i:
                encode_str += k

    if len(s) % 3 == 1:
        encode_str += '=='
    elif len(s) % 3 == 2:
        encode_str += '='
    print(encode_str)


base64_encode('aasaaaaaaa')


