class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        names_heights = []
        for index, name in enumerate(names):
            names_heights.append((heights[index], name))
        names_heights.sort(key=lambda x: x[0], reverse = True)
        return list(map(lambda x: x[1], names_heights))