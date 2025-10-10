class Solution:
    #先定位行 → 再定位列。矩阵只保证“行优先有序”，而不是“二维整体递增”
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix[0])-1
        m=len(matrix)-1
        if matrix is None or len(matrix)==0 or len(matrix[0])==0:
            return False
        top=0
        low=m #这个说最后的 
        while top<=low: #超过他的时候low就是小的那个了
            cm= (top+low)//2
            if matrix[cm][0] == target:
                return True
            elif matrix[cm][0] > target:
                low=cm-1
            else:
                top=cm+1 
        left=0
        right=n
        while left<=right:
            rm = (left+right)//2
            if  matrix[low][rm]==target:
                return True
            elif  matrix[low][rm]>target:
                right=rm-1
            else:
                left=rm+1 #这时候rr就是最小的
        return False





        

        return False
                
                
        