
import math
class Solution:
    def isPowerOfThree(self, n):
        # print(math.sqrt(n))
        # print(math.sqrt(n).is_integer())

        y = 3

        pow = 1
        while pow < n:
            pow = pow * y
        
        print(pow == n)


Run = Solution()
Run.isPowerOfThree(27)
(27)