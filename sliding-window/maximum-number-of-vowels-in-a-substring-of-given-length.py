class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #a, e, i, o, u
        left=0
        result=0
        for right in range(k,len(s)+1): #right 最后一次取的是 len(s)-1，永远到不了 len(s)。
            count=0
            for element in s[left:right]: #这里又不包括 len(s)-1 就是他的真正要取的值
                if element=="a" or element=="e" or element=="i" or element=="o" or element=="u":
                    count+=1
            result=max(result,count)
            left+=1
        return result