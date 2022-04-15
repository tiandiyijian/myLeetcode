# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:

    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        n = len(s)
        if n <= 2:
            return None
        stack = deque([])
        # 弹出栈顶的同时把它加入新的栈顶元素中
        num = 0
        negative = 1
        for i, c in enumerate(s):
            if c == '[':
                stack.append(NestedInteger())
            elif c == ',' or c == ']':
                if s[i - 1].isdigit():
                    num = negative * num
                    stack[-1].add(NestedInteger(num))
                    num, negative = 0, 1
                if c == ']' and len(stack) > 1:
                    stack[-2].add(stack.pop())
            elif c == '-':
                negative = -1
            else:
                num = num * 10 + int(c)
        return stack.pop()
