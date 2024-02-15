# https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                last = stack.pop()
                ans[last] = i - last
            stack.append(i)
        return ans
# The solution came with a group of friends no sole credits  to anyone. 