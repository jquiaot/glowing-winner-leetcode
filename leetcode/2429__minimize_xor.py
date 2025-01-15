class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        >>> s = Solution()
        >>> s.minimizeXor(3, 5)
        3
        >>> s.minimizeXor(1, 12)
        3
        """
        return self.minimizeXor1(num1, num2)

    def minimizeXor1(self, num1: int, num2: int) -> int:
        """
        1. Convert num2 to binary
        2. Count number of set bits
        3. Start cancelling out higher-order bits based on number of set bits
        4. If we still have set bits left over, flip lower-order bits until
           all set bits are used

        n1 = 1, n2 = 12
        n2 => 1100 => 2 set bits
        n1 => 0001
          - first set bit at 0001 to cancel out b1
          - no other set bits in n1 to cancel, so need to set bits starting
            from smallest possible position, which is 0010
          => 0011 => 3
        """

        n2_bits = format(num2, 'b')

        count_n2_bits = sum([int(c) for c in n2_bits])

        n1_bits = format(num1, 'b')

        answer_bits = [0 for i in range(len(n1_bits))]

        n = count_n2_bits
        for i in range(len(n1_bits)):
            if n1_bits[i] == '1':
                answer_bits[i] = 1
                n -= 1
            if n <= 0:
                break

        # print(f"answer_bits={answer_bits}, n={n}")
        j = len(n1_bits) - 1
        while n > 0 and j >= 0:
            if answer_bits[j] == 0:
                answer_bits[j] = 1
                n -= 1
            j -= 1

        while n > 0:
            answer_bits.insert(0, 1)
            n -= 1
        return int(''.join([str(i) for i in answer_bits]), 2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
