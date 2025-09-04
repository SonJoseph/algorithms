'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("ba"); // return True

m b  d
\ |\ /
  a e
  |  \
  d   c
 '''
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class TrieNode:
    val: str
    children: defaultdict # val -> TrieNode
    isEndOfWord: bool

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("", defaultdict(TrieNode), False)

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                next = TrieNode(word[i], defaultdict(TrieNode), False)
                curr.children[word[i]] = next
                curr = next
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        # "",{"a"}, 0
        # "a",{}, 1
        # returns true if the word[i] exists in the root's children.
        # i.e. if the next letter exists. we assume at this point
        # root.val was equal to word[i-1] since root starts as "" -> {}
        def dfs(root, i):
            # if root is None:
            #     return False
            if i == len(word):
                # ended the search on the last character of a word.
                return root.isEndOfWord
            if word[i] == '.':
                return any(dfs(child, i+1) for child in root.children.values())
            if word[i] in root.children:
                next = root.children[word[i]]
                return dfs(next, i+1)
            else:
                return False

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)