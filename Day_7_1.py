# https://leetcode.com/problems/generate-parentheses/submissions/1176215484/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, path, result):
            if left == 0 and right == 0:
                result.append(path)
                return
            if left > 0:
                dfs(left - 1, right, path + '(', result)
            if right > left:
                dfs(left, right - 1, path + ')', result)

        result = []
        dfs(n, n, '', result)
        return result