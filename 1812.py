class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col = ord(coordinates[0]) - ord('a')
        row = int(coordinates[1]) - 1

        return (row + col) & 1 == 1
