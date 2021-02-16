# Leetcode ?. Letter Case Permutation

class Solution:
    def letterCasePermutation(self, S):
        res = ['']
        for ch in S:
            tmp = []
            for i in res:
                if ch.isalpha():
                    tmp.append(i + ch.upper())            
                    tmp.append(i + ch.lower())
                else:
                    tmp.append(i + ch)
            res = tmp
        return res

                

Run = Solution()
Run.letterCasePermutation("a1b2")