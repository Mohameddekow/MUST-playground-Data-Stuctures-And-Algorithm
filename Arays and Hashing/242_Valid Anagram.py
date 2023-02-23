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

        # return false if the len is not equal
        if len(s) != len(t):
            print(False)
            return False

        # create a dictionary for both string s and t{ key = letter: value = it's counts}
        for i in range(len(s)):
            sDictionary[s[i]] = sDictionary.get(s[i], 0) + 1
            tDictionary[t[i]] = tDictionary.get(t[i], 0)  + 1

        for i in sDictionary:
            if sDictionary[i] != tDictionary.get(i, 0):
                print(False)

                return False

        print(True)
        return True


anagamClass = ValidAnagramSolution()

anagram = anagamClass.solution("anagram", "nagaram") #return true as expected