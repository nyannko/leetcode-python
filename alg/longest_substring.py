class Solution(object):

    def substring(self, s):
        # alphabet = list(string.ascii_letters + string.digits + string.punctuation)
        alphabet = [chr(i) for i in range(127)]
        last = {char: -1 for char in alphabet}
        start = max_len = 0
        for i, item in enumerate(s):
            if last[s[i]] >= start:
                max_len = max(max_len, i - start)
                start = last[s[i]] + 1
            last[s[i]] = i
        return max(len(s) - start, max_len)

    """
    ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', 
    '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', 
    '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', 
    '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", 
    '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', 
    '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 
    'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 
    'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
    """
