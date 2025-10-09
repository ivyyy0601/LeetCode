class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapping={}
        for w in words:
            mapping[w]= mapping.get(w,0)+1
        
        heap=[]
        for key, value in mapping.items():
            heapq.heappush(heap, (-value,key))
            if len(heap)>k:
                heapq.heappop(heap) #但是 Python 没有内置最大堆，只有最小堆. pop出最小的value即最大value

        res=[]
        while len(heap)>0:
            res.append(heapq.heappop(heap)[1]) 

        res.reverse()

        return res
        