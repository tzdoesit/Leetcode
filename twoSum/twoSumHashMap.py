class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen:
                return [seen[diff], i]

            seen[n] = i


numS = [0, 1, 2, 3, 4, 5, 6, 7, 8]
targetNum = 5

s = Solution()
print(s.twoSum(numS, targetNum))