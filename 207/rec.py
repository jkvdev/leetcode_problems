
from typing import List

# Time: O(V + E)
# Space: O(V + E)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list to store prerequisites for each course
        adj = {i: [] for i in range(numCourses)}

        # Fill the adjacency list from the input list of prerequisite pairs
        for course, pre in prerequisites:
            adj[course].append(pre)

        visiting = set()  # A set to keep track of nodes in the current DFS path (to detect cycles)

        def dfs(course):
            # If we're visiting a node that's already in the current DFS path, we found a cycle
            if course in visiting:
                return False

            # If the course has no prerequisites, it's safe to take
            if adj[course] == []:
                return True

            # Mark the course as being visited in the current DFS path
            visiting.add(course)

            # Recursively check all prerequisites of the course
            for pre in adj[course]:
                if not dfs(pre):
                    return False  # If a cycle is detected in any of the prerequisites, return False

            # After all prerequisites are checked and no cycle is found:
            visiting.remove(course)  # Remove from current DFS path
            adj[course] = []  # Clear prerequisites to avoid rechecking in future calls
            return True

        # Run DFS for every course
        for c in range(numCourses):
            if not dfs(c):  # If a cycle is detected, return False
                return False

        return True  # If no cycles are found, all courses can be finished
          
    
    
    
# Example usage:
solution = Solution()
numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]  # No cycle
print(solution.canFinish(numCourses, prerequisites))  # Output: True

prerequisites_with_cycle = [[1, 0], [0, 1]]  # Has a cycle
print(solution.canFinish(2, prerequisites_with_cycle))  # Output: False