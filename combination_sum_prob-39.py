"""
Given an array of distinct integers candidates and an integer target, 
return a list of all unique combinations of candidates where the candidate numbers sums to target.

You may return the combinations in any order.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start:int, current:List[int], total:int):
            #base case
            if total == target:
                result.append(list(current))
                return
            
            #prune (also a base case)
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])
                current.pop()

        backtrack(0, [], 0)
        return result