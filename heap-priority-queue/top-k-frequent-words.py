class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapping={}
        for w in words:
            mapping[w]= mapping.get(w,0)+1
        
        heap=[]
        for key, value in mapping.items():
            heapq.heappush(heap, (-value,key))
           
        res = [heapq.heappop(heap)[1] for _ in range(k)]  #频率越大 → -value 越小 → 越早被 pop 出

        return res
        