#1 my first thinking about this problem
#here time complexicity is approx n^3
rows=len(nums)
cols=len(nums[0])
for i in range(rows):
    for j in range(cols):
        if nums[i][j]==0:
            for p in range(0,rows):
                nums[i][p]=float("inf")
                nums[p][j]=float("inf")
for x in range(rows):
    for y in range(cols):
        if nums[x][y]==float("inf"):
            nums[x][y]=0
print(nums)  


#2 thinking by my tutor for brutful solution 
#may be time complexicity is n^2+n
def markinfinity(nums,row,col):
    r=len(nums)
    c=len(nums[0])   
    for i in range (r):
        if nums[i][col]!=0:
            nums[i][col]=float("inf")
    for j in range (c):
        if nums[row][j]!=0:
            nums[row][j]=float("inf")               
r=len(nums)
c=len(nums[0])
for i in range (0,r):
    for j in range (0,c):
        if nums[i][j]==0:
            markinfinity(nums,i,j) 
for i in range (r):
    for j in range(c):
        if nums[i][j]==float("inf") :
            nums[i][j]=0
print(nums)     


# here now is the best optimum solution for this problem
#time complexity=o(2*(n*m)) and space complexity=o(n+m)
class Solution(object):
    def setZeroes(self, matrix):
        r=len(matrix)
        c=len(matrix[0])
        rowtrack=[0 for _ in range(r)]
        coltrack=[0 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rowtrack[i]=-1
                    coltrack[j]=-1
        for i in range(r):
            for j in range (c):
                if rowtrack[i]==-1 or coltrack[j]==-1 :
                    matrix[i][j]=0
        return matrix                     




























