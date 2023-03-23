
#Is palindrome?

def solution3(word):
    word1 = str(word)
    return word1 == word1[::-1]

class Solution(object):
    def solution3(self, word):
        word1 = str(word)
        return word1 == word1[::-1]

C = Solution()

print(C.solution3(-121))