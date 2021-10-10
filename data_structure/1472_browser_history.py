class BrowserHistory:
    """
    https://leetcode.com/problems/design-browser-history
    clear about pointers and array operation
    back and fwd can be improved to O(1) by calculating pointer

    """
    def __init__(self, homepage: str):
        self.his = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.pos += 1
        self.his.insert(self.pos, url)
        del self.his[self.pos + 1:]

    def back(self, steps: int) -> str:
        l = self.pos
        while steps > 0 and l > 0:
            steps -= 1
            l -= 1
        self.pos = l
        return self.his[l]

    def forward(self, steps: int) -> str:
        l = self.pos
        while l < len(self.his) - 1 and steps > 0:
            steps -= 1
            l += 1
        self.pos = l
        return self.his[l]
