from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def doitagain(current:str, open_left:int, close_left:int):
            #base case
            if open_left == 0 and close_left == 0:
                result.append(current)
                return
            
            # Add opening parenthesis if available
            if open_left > 0:
                doitagain(current + '(', open_left - 1, close_left)
            # Add closing parenthesis if valid (more open than close already added)
            if close_left > open_left:
                doitagain(current + ')', open_left, close_left - 1)

        doitagain("", n, n)
        return result