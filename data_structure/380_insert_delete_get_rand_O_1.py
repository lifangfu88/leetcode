import random


class RandomizedSet:
    """
    key is remove, need to maintain the map while removing, thus:
    swap last element of list with the to-be-removed, update map,
    pop last element

    """

    def __init__(self):
        self.map = {} # val to i
        self.nums = []
        self.seen = set()

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        i = len(self.nums)
        self.nums.append(val)
        self.map[val] = i
        return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            i = self.map[val]

            end_val = self.nums[-1]
            self.map[end_val] = i
            del self.map[val]

            self.nums[i] = end_val
            self.nums[-1] = val
            self.nums.pop()

            return True
        return False

    def getRandom(self) -> int:
        i = len(self.nums) - 1
        r = random.randint(0, i)
        val = self.nums[r]
        return val
