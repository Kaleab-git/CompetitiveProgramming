class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        M = []
        Rows = [0] * C
        distance = 0
        distance_list = []
        answer = []
        for i in range(R):
            M.append(Rows)
        for r in range(R):
            for c in range(C):
                distance = abs(r0 - r) + abs(c0 - c)
                distance_list.append([distance, r, c])
        distance_list.sort()
        for i in range(len(distance_list)):
            answer.append(distance_list[i][1:])
        
        return answer
     