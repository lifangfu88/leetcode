from typing import List


def gas_station(self, gas: List[int], cost: List[int]) -> int:
    """
    O(n^2) solution is simple to come up with;
    it needs math analysis for O(n) solution;

    as long as gas tank is >=0 along the road, there must be a solution

    https://leetcode.com/problems/gas-station/

    :param self:
    :param gas:
    :param cost:
    :return:
    """
    # it's key to get that as long as sum(gas) >= sum(cost), there must be a solution
    if not gas or not cost or not len(gas) == len(cost) or sum(gas) < sum(cost):
        return -1

    n = len(gas)
    tank = [gas[i] - cost[i] for i in range(n)]

    current = 0
    res = 0
    for i in range(n):
        current += tank[i]
        if current < 0:
            res = i + 1
            current = 0

    return res
