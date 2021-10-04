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
    """
    straightforward DFS solution
    time O(n)
    space O(D) D: max depth of input

    """
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        depth = 1
        res = 0
        for n in nestedList:
            if n.isInteger():
                res += n.getInteger()
            else:
                res += self.helper(depth, n.getList(), 0)
        return res

    def helper(self, depth, nestedList, res):
        depth += 1
        for n in nestedList:
            if n.isInteger():
                res += depth * n.getInteger()
            else:
                res = self.helper(depth, n.getList(), res)
        return res
