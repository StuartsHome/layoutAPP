# Leetcode ?. Score of Parentheses

class Solution:
    def scoreOfParentheses(self, S):
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()

        # My approach - not currently working
        stack = []
        lookup = {")": "(", "}":"{", "]":"["}
        score = 0
        for i in S:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            # elif len(stack) < 1:
            # 	return False
            else:
                temp = stack.pop()
                if lookup[i] != temp:
                    return False
                else:
                    if stack:
                        score = score + (2 * len(stack))
                    else:
                        score += 1
        return not stack and score
		
p1 = Solution()
p1.scoreOfParentheses("(()(()))")

("(({}))")