import sys

def solve(s: str) -> int:
    """
    1. Keep a counter of number of occurrences of some character
    2. Keep a counter of the longest sequence found
    3. When a new character is encountered, check current
       count against max count, and update as appropriate
    4. Return the longest sequence found
    """
    longest = 0
    cur_char = s[0]
    cur_len = 1
    i = 1
    while i < len(s):
        if s[i] != cur_char:
            if longest < cur_len:
                longest = cur_len
            cur_char = s[i]
            cur_len = 1
        else:
            cur_len += 1
        i += 1
    if longest < cur_len:
        longest = cur_len
    return longest
    
if __name__ == '__main__':
    line = sys.stdin.readline()
    line = line.strip()
    res = solve(line)
    print(res)
