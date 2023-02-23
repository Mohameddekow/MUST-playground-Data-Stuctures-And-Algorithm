# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

class ValidAnagramSolution: 
    def solution(self, s: str, t:str) -> bool:
        sDictionary = {}
        tDictionary = {}

        # create a dictionary for string s{ key = letter: value = it's counts}
        for i in s:
            sDictionary[i] = sDictionary.get(i, 0) + 1



        # create a dictionary for string t{ key = letter: value = it's counts}
        for j in t:
            tDictionary[j] = tDictionary.get(t, 0)  + 1



        return sDictionary.values() == tDictionary.values()
        # return sDictionary == tDictionary


anagamClass = ValidAnagramSolution()

anagram = anagamClass.solution("anagram", "nagaram")