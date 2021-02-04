class Solution:
    def findLHS(self, nums):
        carry = 0
        result = []
        temp = []
        a, j = 0,0

        """
        for i in range(len(nums)):
            target = nums[i]
            a, j = i -1, i + 1
            temp.append(target)
            while j < len(nums) and nums[j] in range(nums[i] - 1, nums[i] + 2):
                temp.append(nums[j])
                j += 1
            while a >= 0 and nums[a] in range(nums[i] -1, nums[i] + 2):
                temp.append(nums[a])
                a -= 1
            if len(temp) > 1: result.append(len(temp))
            temp = []
        """

        for i in range(len(nums)):
            target = nums[i]
            a, j = i -1, i + 1
            temp.append(target)
            while j < len(nums) - 1:
                if nums[j] in range(nums[i] - 1, nums[i] + 1):
                    temp.append(nums[j])
                j += 1
            while a >= 0:
                if nums[a] in range(nums[i] -1, nums[i] + 1):
                    temp.append(nums[a])
                a -= 1
            if len(temp) > 1: result.append(len(temp))
            temp = []



        print(result)


Run = Solution()
Run.findLHS([1,1,1,1])

([1,3,2,2,5,2,3,7])