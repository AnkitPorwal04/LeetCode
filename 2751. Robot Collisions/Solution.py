from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Combine positions, healths, and directions into a list of tuples and sort by positions
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        
        stack = []  # stack to keep track of robots moving to the right
        results = [None] * len(positions)  # to store final healths of robots in original order
        
        for pos, health, direction, index in robots:
            if direction == 'R':
                stack.append((pos, health, direction, index))
            else:  # direction == 'L'
                while stack and health > 0:
                    r_pos, r_health, r_direction, r_index = stack[-1]
                    if r_health < health:
                        # Robot moving to the right is weaker, it is destroyed
                        health -= 1
                        stack.pop()
                    elif r_health > health:
                        # Robot moving to the left is weaker, it is destroyed
                        stack[-1] = (r_pos, r_health - 1, r_direction, r_index)
                        health = 0
                    else:  # r_health == health
                        # Both robots destroy each other
                        stack.pop()
                        health = 0
                
                if health > 0:
                    results[index] = health
        
        # Robots moving to the right that did not collide
        while stack:
            pos, health, direction, index = stack.pop()
            results[index] = health
        
        # Filter out the None values to get the final list of surviving robots' healths
        return [health for health in results if health is not None]
