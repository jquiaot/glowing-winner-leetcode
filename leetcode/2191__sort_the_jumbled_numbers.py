from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """
        1. Convert nums to strings
        2. Convert nums based on mappings
        3. Map converted num to original num
        4. Sort converted nums
        5. Build response

        Time:
        - n = len(nums)
        - m = average number of characters in nums
        - O(n * m) converting numbers to string values
        - O(n*lg(n)) sort converted values
        - O(n) build response
        - => O(n*lg(n)) as n grows large

        Space:
        - O(1) digit mapping dictionary
        - O(n) converted to regular number dict
        - O(n) list of converted numbers (de-duped)
        - => O(n)
        """
        mappingDict = {str(i):str(mapping[i]) for i in range(len(mapping))}
        convertedToRegularDict = {}
        convertedList = []
        for i in range(len(nums)):
            num = nums[i]
            convertedNum = self.getConvertedNum(mappingDict, num)
            if convertedNum in convertedToRegularDict:
                convertedToRegularDict[convertedNum].append(num)
            else:
                convertedList.append(convertedNum)
                convertedToRegularDict[convertedNum] = [num]
        convertedList.sort()

        result = []
        for convertedNum in convertedList:
            values = convertedToRegularDict[convertedNum]
            result.extend(values)
        return result

    def getConvertedNum(self, mappingDict: dict[str, str], num: int) -> int:
        numString = str(num)
        chars = []
        for c in numString:
            chars.append(mappingDict[c])
        i = 0
        while i < len(chars) and chars[i] == '0':
            i += 1
        if i < len(chars):
            return int(''.join(chars[i:]))
        else:
            return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
