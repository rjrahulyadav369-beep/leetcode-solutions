# my own solution 
class Solution(object):
    def rotate(self, matrix):
        row=len(matrix)
        col=len(matrix[0])
        result=[]
        for i in range(0,row):
            temp=[]
            for j in range(col-1,-1,-1):
                temp.append(matrix[j][i])
            result.append(temp)    
        for i in range(row):
            for j in range(col):
                matrix[i][j]=result[i][j]     
        return matrix
               
