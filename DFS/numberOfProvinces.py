class Solution:#one bfs is one city.
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        length = len(isConnected)
        if len(isConnected) == 1: return 1
        stack = []
        visited = [False]*length
        city_count = 0

        while not all(visited):
            for i in range(length):
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True
                    break
        
            while stack:
                city = stack.pop()
                for neighbor in range(length):#is a list of nieghbors and non neighbors of that city
                    if not visited[neighbor] and isConnected[city][neighbor]:
                            stack.append(neighbor)
                            visited[neighbor] = True 
            city_count += 1

        return city_count                

        