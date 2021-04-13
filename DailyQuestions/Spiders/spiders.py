from collections import deque
    
input = open('input.txt', 'r')
n = int(input.readline())
    
def bfs(graph, beads):
    length = 0
    for bead in range(1,beads+1):
        que = deque([(bead,0)])
        visited = set()
        while que:
            node, depth = que.popleft()
            length = max(length, depth)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited: que.append((neighbor, depth+1))
        
    return length   
    
maxLength = 0
for line in range(n):
    graph = {}
    spider = input.readline().split()
    beads = int(spider[0])
    for i in range(1, beads+1): graph[i] = []
    for i in range(1, len(spider), 2): 
        graph[int(spider[i])].append(int(spider[i+1]))
        graph[int(spider[i+1])].append(int(spider[i]))
    maxLength += bfs(graph, beads)
    
output = open('output.txt','w')
output.writelines(f'{maxLength}')