class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings) // 2
        rods_rings = {}
        res = 0

        for i in range(0, 2*n, 2):
            color, rod = rings[i], int(rings[i+1])
            if rod not in rods_rings:
                rods_rings[rod] = [color]

            elif color not in rods_rings[rod]:
                rods_rings[rod].append(color)
        
        for _, rings in rods_rings.items():
            if len(rings) == 3:
                res += 1

        print(rods_rings)
        return res