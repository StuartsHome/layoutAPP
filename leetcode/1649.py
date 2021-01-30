# 1649. Create Sorted Array through Instructions

class Solution:
    def createSortedArray(self, instructions):
        m = max(instructions)
        c = [0] * (m + 1)

        def update(x):
            while (x <= m):
                c[x] += 1
                x += x & -x

        def get(x):
            res = 0
            while (x > 0):
                res += c[x]
                x -= x & -x
            return res

        res = 0
        for i, a in enumerate(instructions):
            res += min(get(a - 1), i - get(a))
            update(a)
        print(res % (10**9 + 7))



Run = Solution()
Run.createSortedArray([1,2,3,6,5,4])
([1,5,6,2])