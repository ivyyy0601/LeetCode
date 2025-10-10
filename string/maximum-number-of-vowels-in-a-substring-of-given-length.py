class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #a, e, i, o, u
        left=0
        result=0
        for right in range(k,len(s)):
            count=0
            for element in s[left:right]:
                if element=="a" or element=="e" or element=="i" or element=="o" or element=="u":
                    count+=1
            result=max(result,count)
            left+=1
        return result