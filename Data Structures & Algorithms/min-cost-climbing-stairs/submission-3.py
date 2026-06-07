class Solution:
    def dp(self, cost, step, prev):
        if step == len(cost):
            return 0
        elif step == len(cost) - 1:
            return cost[step]
        elif step in prev:
            return prev[step]
        else:
            take_one = self.dp(cost, step+1, prev)
            take_two = self.dp(cost, step+2, prev)
            prev[step] = cost[step] + min(take_one, take_two)
            return prev[step]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.dp(cost, 0, {}), self.dp(cost, 1, {}))