class Solution:

    def maxAreaOfIsland(self, grid) -> int:
        alread_visited = set()
        max_r = 0
        for row_num, row_val in enumerate(grid):
            for col_num, col_val in enumerate(row_val):
                if (grid[row_num][col_num] == 1 and not (str(row_num) +" "+ str(col_num) in alread_visited)):
                    area = self.search(row_num, col_num, alread_visited, grid, None)
                    max_r = max(area, max_r)
        return max_r

    def search(self, row_num, col_num, alread_visited, grid, come_from):
        if (grid[row_num][col_num] == 0 or str(row_num) +" "+ str(col_num) in alread_visited):
            return 0
        else:
            num = 1
            alread_visited.add(str(row_num) +" "+ str(col_num))
            if (row_num != 0 and come_from != "above"):
                num += self.search(row_num - 1, col_num, alread_visited, grid, "below")  # up

            if (row_num != len(grid) - 1 and come_from!="below"):
                num += self.search(row_num + 1, col_num, alread_visited, grid, "above")  # down

            if (col_num != 0 and come_from!="left"):
                num += self.search(row_num, col_num - 1, alread_visited, grid, "right")  # left

            if (col_num != len(grid[0]) - 1 and come_from!="right"):
                num += self.search(row_num, col_num + 1, alread_visited, grid, "left")  # right


            return num

print(Solution().maxAreaOfIsland([
                        [0,0,1,0,0,0,0,1,0,0,0,0,0],
                       [0,0,0,0,0,0,0,1,1,1,0,0,0],
                       [0,1,1,0,1,0,0,0,0,0,0,0,0],
                       [0,1,0,0,1,1,0,0,1,0,1,0,0],
                       [0,1,0,0,1,1,0,0,1,1,1,0,0],
                       [0,0,0,0,0,0,0,0,0,0,1,0,0],
                       [0,0,0,0,0,0,0,1,1,1,0,0,0],
                       [0,0,0,0,0,0,0,1,1,0,0,0,0]]))