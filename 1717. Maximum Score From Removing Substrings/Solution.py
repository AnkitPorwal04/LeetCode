class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_and_score(s, first, second, points_value):
            stack = []
            points = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    points += points_value
                else:
                    stack.append(char)
            remaining = ''.join(stack)
            return remaining, points
        
        # Determine the order based on the points
        if x >= y:
            s, points = remove_and_score(s, 'a', 'b', x)
            s, additional_points = remove_and_score(s, 'b', 'a', y)
            points += additional_points
        else:
            s, points = remove_and_score(s, 'b', 'a', y)
            s, additional_points = remove_and_score(s, 'a', 'b', x)
            points += additional_points
        
        return points
