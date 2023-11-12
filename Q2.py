class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(i,j):
            nonlocal m,n
            grid[i][j]="0"
            for r,c in dir:
                row=i+r
                col=c+j
                if row>=0 and row<m and col>=0 and col<n and grid[row][col]=="1":
                    dfs(row,col)
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(i,j)
                    cnt+=1
        return cnt
        