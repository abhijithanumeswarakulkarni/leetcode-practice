class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        total_steps = 0
        curr_capacity = capacity
        
        for index, value in enumerate(plants):
            if curr_capacity >= value:
                total_steps += 1
                curr_capacity -= value
            else:
                total_steps += 2 * index + 1
                curr_capacity = capacity - value

        return total_steps 