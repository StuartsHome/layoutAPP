
# Leetcode 781. Rabbits in Forest

class Solution:
    def numRabbits(self, answers):
        memo = {}
        total = 0
        total2 = 0
        for i in answers:
            if i in memo:
                memo[i] += 1
                total += i
            else:
                memo[i] = 1
                total += i
        for i in memo.values():
            total2 += i
        print(total2)
        print(memo, total)
        
        
       

Run = Solution()
Run.numRabbits([10,10,10])

([1, 1, 2])

