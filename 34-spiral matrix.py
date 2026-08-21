#here T=top,B=bottom,R=right,l=LEFT
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []    
        result=[] 
        T=0
        B=len(matrix)-1
        L=0
        R=len(matrix[0])-1
        while T<=B and L<=R:
            for i in range(L,R+1):
                result.append(matrix[T][i])
            T+=1
            for i in range(T,B+1):
                result.append(matrix[i][R]) 
            R-=1
            if T<=B:
                for i in range(R,L-1,-1):
                    result.append(matrix[B][i])
                B-=1
            if L<=R:
                for i in range(B,T-1,-1):
                    result.append(matrix[i][L])
                L+=1    
        return result




        
