class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Initialize visited set to keep track of visited states
        visited = set(deadends)
        if "0000" in visited:
            return -1
        
        # Initialize queue for BFS
        queue = deque([('0000', 0)])
        
        # Perform BFS
        while queue:
            current, steps = queue.popleft()
            
            if current == target:
                return steps
            
            # Generate next states by rotating each wheel
            for i in range(4):
                for increment in (-1, 1):
                    next_state = current[:i] + str((int(current[i]) + increment) % 10) + current[i+1:]
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, steps + 1))
        
        # If target state cannot be reached
        return -1

        
