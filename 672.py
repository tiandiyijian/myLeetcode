class Solution:
    def flipLights(self, n: int, k: int) -> int:
        if k == 0:
            return 1

        match n:
            case 1:
                return 2
            case 2:
                return 3 if k == 1 else 4
            case _:
                return 4 if k == 1 else 7 if k == 2 else 8
