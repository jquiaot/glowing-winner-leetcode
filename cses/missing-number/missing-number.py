import sys

def solve(n: int, nums: list[int]) -> int:
    """
    1. XOR all the numbers from 1 to n, inclusive
    2. For each number in nums, XOR it with all the XORed numbers.
    3. The remaining number should be the missing one.

    Time:
    - n = len(nums)
    - O(n) generate XOR of all numbers from 1..n
    - O(n) XOR all numbers from nums
    - => O(n)

    Space:
    - O(1) space to store XOR value
    - => O(1)
    """
    xor_all = 1
    for i in range(2, n+1):
        xor_all ^= i
    for num in nums:
        xor_all ^= num
    return xor_all

if __name__ == '__main__':
    line = sys.stdin.readline()
    n = int(line)
    line = sys.stdin.readline()
    nums = [int(c) for c in line.split(' ')]
    res = solve(n, nums)
    print(res)
