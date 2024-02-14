# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        visited = set()  # Track visited numbers
        longest = 0

        for num in num_set:
            # Skip numbers already visited
            if num in visited:
                continue

            length = 1
            right = num + 1
            while right in num_set:
                length += 1
                right += 1
                visited.add(right)  
            longest = max(longest, length)

        return longest

#Dumbest but works(Need to work on Improvement)