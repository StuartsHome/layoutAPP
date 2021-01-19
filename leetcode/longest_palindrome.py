


# Leetcode 5. Longest Palindromic Substring



class Solution:
    def longestPalindrome(self, s):


        # reverse s

        #rev_s = ""
        rev_s = ""
        copy_s = s
        word = ""
        
        for i in s[::-1]:
            rev_s += i
        
        #print(rev_s)

        """
        while copy_s.find(rev_s) != 0:
            aa = len(rev_s) - 1
            rev_s = rev_s[:aa]
            bb = len(copy_s) -1
            copy_s = copy_s[:bb]
            #rev_rev = reversed(copy_s)
            if copy_s == rev_s:
                print(copy_s)
                break
            print(rev_s, copy_s)
        """
        for i in range(len(s)):
            word = s[i]
            counter = i
            while len(word) < len(s) and s.find(word) == 0:
                counter += 1
                word += s[i + counter]



Run = Solution()
Run.longestPalindrome("babad")
        
        
        
   