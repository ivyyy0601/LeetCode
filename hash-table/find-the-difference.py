class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a={}
        b={}
        string=""
        for n1 in s:
            if n1 in a:
                a[n1]+=1
            else:
                a[n1]=1
        for n2 in t:
            if n2 in b:
                b[n2]+=1
            else:
                b[n2]=1  
        for k,v in a.items():
            if k in b:
                b[k]=b[k]-v
        for k,v in b.items():
            if b[k]>=1:
                string+=k
        return string

              

        