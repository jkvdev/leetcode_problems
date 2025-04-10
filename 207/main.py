
from typing import List

# Time: O(V + E)
# Space: O(V + E)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency list to track prerequisites
        adj = {course: [] for course in range(numCourses)}
        
        # Fill the adjacency list
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        # Try to detect cycles starting from each course
        for course in range(numCourses):
            stack = [(course, set())]  # Use DFS with a stack
            
            while stack:
                curr_course, visited = stack.pop()
                
                # If the current course is already in the visited set, there's a cycle
                if curr_course in visited:
                    return False
                
                visited.add(curr_course)
                
                # Add prerequisites to stack, pass a copy of visited set to avoid mutation
                for pre in adj[curr_course]:
                    stack.append((pre, visited.copy()))
            
            # Clear course prerequisites after checking to avoid redundant work
            adj[course] = []
        
        return True
    
    
    
# Example usage:
solution = Solution()
numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]  # No cycle
print(solution.canFinish(numCourses, prerequisites))  # Output: True

prerequisites_with_cycle = [[1, 0], [0, 1]]  # Has a cycle
print(solution.canFinish(2, prerequisites_with_cycle))  # Output: False