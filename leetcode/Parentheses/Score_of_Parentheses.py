# Leetcode ?. Score of Parentheses

class Solution:
    def scoreOfParentheses(self, S):
        def F(i, j):
            #Score of balanced string S[i:j]
            ans = bal = 0

            #Split string into primitives
            for k in range(i, j):
                bal += 1 if S[k] == '(' else -1
                if bal == 0:
                    if k - i == 1:
                        ans += 1
                    else:
                        ans += 2 * F(i+1, k)
                    i = k+1

            return ans

        return F(0, len(S))


        """
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()
        """



        # # My approach - not currently working
        # stack = []
        # lookup = {")": "(", "}":"{", "]":"["}
        # score = 0
        # for i in S:
        #     if i == "(" or i == "{" or i == "[":
        #         stack.append(i)
        #     # elif len(stack) < 1:
        #     # 	return False
        #     else:
        #         temp = stack.pop()
        #         if lookup[i] != temp:
        #             return False
        #         else:
        #             if stack:
        #                 score = score + (2 * len(stack))
        #             else:
        #                 score += 1
        # return not stack and score
		
p1 = Solution()
p1.scoreOfParentheses("(()(()))")

("(({}))")