class Solution:
    def recurseComboSum(self, curr_index, candidates, previous, target, combinations):
        if sum(previous) == target:
            combinations.append(previous)
            return
        if sum(previous) > target:
            return
        if curr_index > len(candidates) - 1:
            return
        self.recurseComboSum(curr_index + 1, candidates, previous + [candidates[curr_index]], target, combinations)
        next_index = curr_index + 1
        while next_index < len(candidates) and candidates[next_index] == candidates[curr_index]:
            next_index += 1
        self.recurseComboSum(next_index, candidates, previous, target, combinations)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []
        self.recurseComboSum(0, candidates, [], target, combinations)
        return combinations