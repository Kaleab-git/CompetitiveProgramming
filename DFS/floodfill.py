class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int,visited = set()) -> List[List[int]]:
        startingPixel = image[sr][sc]
        if startingPixel == newColor:
            return image 
        column, row = len(image),len(image[0])
        image[sr][sc] = newColor
        self.dfs(sr, sc, image, startingPixel, newColor, column, row)
        return image

    def dfs(self, i, j, image, startingPixel, newColor, column, row):
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]

                if (0 <= next_i < column and 0 <= next_j < row) and (image[next_i][next_j] == startingPixel):
                    next_state = (next_i, next_j)
                    if next_state:                 
                        image[next_i][next_j] = newColor
                        self.dfs(next_i, next_j, image, startingPixel, newColor, column, row)
