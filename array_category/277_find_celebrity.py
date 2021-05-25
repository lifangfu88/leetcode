"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)

https://www.lintcode.com/problem/645/

brute-force solution is O(n^2), validate each pair once.
interesting part is, one validation call can eliminate one candidate:
if True: a is not celebrity
if False: b is not celebrity

thus, call n-1 times, we will eliminate n-1 candidate,
but we will have to validate that if the single one left is real celebrity.


"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def find_celebrity(self, n):
        # Write your code here
        cel = 0
        for i in range(n):
            if Celebrity.knows(cel, i):
                cel = i
        for i in range(n):
            if cel != i and Celebrity.knows(cel, i):
                return -1
            if cel != i and not Celebrity.knows(i, cel):
                return -1
        return cel


class Celebrity:

    def knows(a:int, b:int) -> bool:
        return True
