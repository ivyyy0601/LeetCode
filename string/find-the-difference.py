class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a={}
        b={}
        string=""
        for n1 in s:
            a[n1]=a.get(n1,0)+1
        for n2 in t:
            b[n2]=b.get(n2,0)+1
        for k,v in a.items():
            if k in b:
                b[k]=b[k]-v
        for k,v in b.items():
            if b[k]>=1:
                string+=k
        return string

              

        