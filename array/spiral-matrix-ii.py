class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startx,starty =0,0
        count=1
        for offset in range(1,n//2 +1):  #重点加一
            #n-offset是指边边值
            for i in range(starty, n-offset): #显示x不变：y动
                nums[startx][i]=count
                count+=1          #y已经到顶峰
            for j in range(startx, n-offset): #显示y(n-offset)不变 ：x动
                nums[j][n-offset]=count 
                count+=1             #x已经到顶峰
            for i in range(n-offset ,starty,-1): #x  n-offset 不变 y动 减
                nums[n-offset][i]=count
                count+=1         #y回归starty
            for j in range(n-offset ,startx,-1): #y不变，x变 减
                nums[j][starty]=count
                count+=1
            startx+=1
            starty+=1
        if n%2!=0:
            nums[n//2][n//2]=count
        return nums


            