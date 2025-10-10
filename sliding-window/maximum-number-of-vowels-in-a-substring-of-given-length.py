class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #a, e, i, o, u
        # left=0
        # result=0
        # for right in range(k,len(s)+1): #right 最后一次取的是 len(s)-1，永远到不了 len(s)。
        #     count=0
        #     for element in s[left:right]: #这里又不包括 len(s)-1 就是他的真正要取的值
        #         if element=="a" or element=="e" or element=="i" or element=="o" or element=="u":
        #             count+=1
        #     result=max(result,count)
        #     left+=1
        # return result#这个不是滑动窗口
        #你用 left / right 在移动“边界”，但每次都对 s[left:right] 重新统计，所以不是 O(1) 更新；
        vowels = set("aeiou")
        left=0
        result=0
        for i in s[0:k]:
            if i in vowels:
                result+=1
        count=result
        for right in range(k,len(s)):
            if s[right] in vowels:
                count+=1
            if s[left] in vowels:
                count-=1
            left+=1
            result=max(result,count)
        return result
            
            
