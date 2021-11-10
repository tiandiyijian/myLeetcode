class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        root = pow(area, 0.5)
        w = int(root)
        while True:
            if area % w == 0:
                return [int(area / w), w]
            w -= 1
