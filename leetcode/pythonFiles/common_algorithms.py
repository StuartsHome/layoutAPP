

A = [44, 22, 55, 66, 33, 1, 10]


def bubble(n):
	for i in range(len(n)):
		for j in range(i + 1, len(n)):
			if n[i] > n[j]:
				t = n[i]
				n[i] = n[j]
				n[j] = t
	return n

bubble(A)


A = [1, 10, 22, 33, 44, 55, 66]
def binary(n, target):
	upper = len(n)
	lower = 0
	while upper > lower:
		ind = lower + (upper - lower)//2
		val = n[ind]
		if target == val:
			return ind
		elif target > val:
			lower = ind
		elif target < val:
			upper = ind 
binary(A, 66)


def palindrome(n):
	if n // 10 == 0:
		return False
	temp = n
	reverseNum = 0
	while temp !=0:
		reverseNum = (reverseNum * 10) + (temp % 10)
		temp = temp // 10

	if n == reverseNum:
		return "Match", reverseNum
	else:
		return False

palindrome(1221)



memo = {}
def fib(n):
	if n in memo:
		return memo[n]
	elif n <= 2:
		return 1
	else:
		f = fib(n-1) + fib(n-2)
	print(memo[n])
	memo[n] = f
	return f

fib(10)


##############
##############
# Quick Sort

class Solution:
	def quickSort(self, num):
		upper = []
		lower = []
		equal = []
		if len(num) > 1:
			for i in num:
				pivot = num[0]
				if i > pivot:
					upper.append(i)
				elif i == pivot:
					equal.append(i)
				elif i < pivot:
					lower.append(i)
			return self.quickSort(lower) + equal + self.quickSort(upper)
		else:
			return num

p1 = Solution()
p1.quickSort([44,55,22,11,33,21,100,1])

##############
##############
# Binary search

class Solution:
	def binary_search(self, nums, target):
		lower = 0
		upper = len(nums)
		counter = len(nums)
		while counter:
			ind = lower + (upper - lower) // 2
			val = nums[ind]
			if target < val:
				upper = ind
			elif val == target:
				return ind
			elif target > val:
				lower = ind
			counter -=1

p1 = Solution()
p1.binary_search([10,20,30,40,50], 50)