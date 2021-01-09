class Solution(object):
    def findDistance(self, x,y):
        return math.sqrt((x**2) + (y**2))
    
    def kClosest(self, points, K):
        import math    
        closestPoint = []
        distance_axis_list = []
        for point in points:
            x = point[0]; y = point[1]
            d = self.findDistance(x,y)
            distance_axis_list.append([d,x,y])
        distance_axis_list.sort()
        if K == 1:
            closestPoint.append(distance_axis_list[0][1:])
            return closestPoint
        else:
            for k in range(K):
                closestPoint.append(distance_axis_list[k][1:])
        return closestPoint