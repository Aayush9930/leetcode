class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites == []:
            return [ i for i in range(numCourses) ]

        g = {}

        for i in range(numCourses):
            g[i] = []
        

        for x, y in prerequisites:
            g[y].append(x)
            
        num_parents = {}

        for i in range(numCourses):
            num_parents[i] = 0
        
        for node in g:
            for n in g[node]:
                num_parents[n] += 1

        ready = [ node for node in num_parents if num_parents[node] == 0 ]

        out = []
        while ready:
            node = ready.pop()
            out.append(node)

            for n in g[node]:
                num_parents[n] -= 1
                if num_parents[n] == 0:
                    ready.append(n)

        if len(set(num_parents.values())) != 1:
            return []
        
        return out
            



