class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        hor, ver = ord(coordinates[0]) - ord('a'), int(coordinates[1])

        if (hor % 2 == 0 and ver % 2 == 0) or (hor % 2 != 0 and ver % 2 != 0):
            return True
        
        return False