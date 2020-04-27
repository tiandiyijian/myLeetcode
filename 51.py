class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        stack = [[]]
        L = []
        while !stack.empty():
        	top = stack.pop()
        	if top.length() == 8 :
        		L.append(top)
    		else :
    			