class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        start, end = set(), set()

        for path in paths:
            start.add(path[0])
            end.add(path[1])
        
        for city in end:
            if city not in start:
                return city
        
        return "" # Never reached