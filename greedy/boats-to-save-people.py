class Solution:  #想到对zhang指针，不需要
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res=0
        if people is None or len(people)==0:
            return False
        people.sort( )
        l=0
        r=len(people)-1
        while l<=r:
            if people[r]+people[l] <= limit:
                l+=1
            r-=1
            res+=1
        return res
        