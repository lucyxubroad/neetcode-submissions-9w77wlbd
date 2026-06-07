class Solution:

    def dp(self, i, prev):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        elif i == 2:
            return 2
        elif i in prev:
            return prev[i]
        else:
            ans = self.dp(i-1, prev) + self.dp(i-2, prev)
            prev[i] = ans
            return ans

    def climbStairs(self, n: int) -> int:
        return self.dp(n, {})
        