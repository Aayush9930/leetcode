class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = {}
        for i in range(numCourses):
            g[i] = []
        
        for edge in prerequisites:
            x, y = edge
            g[y].append(x)
        

        num_parents = {}

        for i in range(numCourses):
            num_parents[i] = 0

        for node in g:
            for nei in g[node]:
                num_parents[nei] = 1 + num_parents.get(nei, 0)
        print(num_parents)
        
        ready = [ node for node in num_parents if num_parents[node] == 0 ]
        out = []
        while ready:
            node = ready.pop()
            out.append(node)

            for nei in g[node]:
                num_parents[nei] -= 1
                if num_parents[nei] == 0:
                    ready.append(nei)

        for node in num_parents:
            if num_parents[node] > 0:
                return []

        return out 
            

        
