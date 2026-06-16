from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        
        for i in range(n):
            graph[i] = []
            
        for i in range(len(edges)):
            pair = edges[i]
            
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        
        queue = [source]
        
        visited = {}
        
        visited[source] = True

        while len(queue) > 0:
            current_vertex = queue.pop()
                        
            if current_vertex == destination:
                return True
            
            for neighbor in graph[current_vertex]:
                if not neighbor in visited:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    
        return  False
                
                
"""
Teste 1

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
"""

s = Solution()
print(s.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))


"""
Teste 2

n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
"""
print(s.validPath(3, [[0,1],[1,2],[2,0]], 0, 2))

"""
Teste 3

n = 1, edges = [] source = 0, destination = 0
"""

print(s.validPath(1, [], 0, 0))
        
        