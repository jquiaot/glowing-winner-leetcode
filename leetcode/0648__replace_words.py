from typing import List, Optional

"""
In English, we have a concept called root, which can be followed by some other
word to form another longer word - let's call this word derivative. For
example, when the root "help" is followed by the word "ful", we can form a
derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words
separated by spaces, replace all the derivatives in the sentence with the root
forming it. If a derivative can be replaced by more than one root, replace it
with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by
the battery"

Output: "the cat was rat by the bat"

Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"

Output: "a a b c"

Constraints:

- 1 <= dictionary.length <= 1000

- 1 <= dictionary[i].length <= 100

- dictionary[i] consists of only lower-case letters.

- 1 <= sentence.length <= 10^6

- sentence consists of only lower-case letters and spaces.

- The number of words in sentence is in the range [1, 1000]

- The length of each word in sentence is in the range [1, 1000]

- Every two consecutive words in sentence will be separated by exactly one space.

- sentence does not have leading or trailing spaces.

"""
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        >>> s = Solution()
        >>> s.replaceWords(['a', 'b', 'c'], 'aaaaa bbbbbb ccccc')
        'a b c'
        >>> s.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery")
        'the cat was rat by the bat'
        >>> s.replaceWords(["catt","cat","bat","rat"], "the cattle was rattled by the battery")
        'the cat was rat by the bat'
        """
        return self.replaceWords1(dictionary, sentence)

    def replaceWords1(self, dictionary: list[str], sentence: str) -> str:
        """
        Build a trie (prefix tree) which we can use to determine whether
        there is a root for a given word.

        Time:
        - n = len(dictionary) (i.e., number of words)
        - m = avg len of a word in dictionary
        - p = number of words in sentence

        - Building the trie: O(n) * O(m) (need to traverse all letters of
          all words in dictionary
        - Searching for prefix: O(p) * O(m) (for each word in sentence,
          traverse trie to find prefix)
        
        Space:
        - Trie space: O(m * n) i.e., number of chars in dictionary =
          num words in dictionary * avg number of chars in each word
        - => O(m * n)
        """
        t = Trie()
        # print("START")
        for word in dictionary:
            t.insert(word)
        # print("BUILT TRIE")

        words = sentence.split(' ')
        # print(f"{words}")
        newWords = []
        for word in words:
            # print(f"EXAMINE {word}")
            prefix = t.findFirstMatch(word)
            if prefix is None:
                newWords.append(word)
            else:
                newWords.append(prefix)
        return ' '.join(newWords)

class TrieNode:
    def __init__(self, letter: str = None, isWordEnd: bool = False):
        self.letter = letter
        self.isWordEnd = isWordEnd
        self.children = {} # letter to child

    def getChild(self, letter: str) -> Optional['TrieNode']:
        if letter in self.children:
            return self.children[letter]
        return None

    def addChild(self, letter: str, newChild: 'TrieNode'):
        self.children[letter] = newChild

    def __str__(self):
        return f"TrieNode[{self.letter}]"

    def __repr__(self):
        return self.__str__()

class Trie:
    def __init__(self):
        self.root = TrieNode(None, False)

    def insert(self, word: str) -> None:
        # print(f"INSERT {word}")
        self.insertInternal(self.root, word)

    def insertInternal(self, node: TrieNode, wordOrPart: str) -> None:
        if len(wordOrPart) == 0:
            return
        else:
            nextNode = TrieNode(wordOrPart[0], len(wordOrPart) == 1)
            # print(f"CREATING nextNode={nextNode}")
            if node.getChild(wordOrPart[0]) is None:
                node.addChild(wordOrPart[0], nextNode)
            else:
                nextNode = node.getChild(wordOrPart[0])
            if len(wordOrPart) > 1:
                self.insertInternal(nextNode, wordOrPart[1:])
            else:
                nextNode.isWordEnd = True

    def findFirstMatch(self, word: str) -> Optional[str]:
        n = self.root
        # print(f"n={n}, word={word}")
        for i in range(len(word)):
            c = word[i]
            child = n.getChild(c)
            if child is None:
                return None
            elif child.isWordEnd:
                return word[0:i + 1]
            else:
                n = child
        return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
