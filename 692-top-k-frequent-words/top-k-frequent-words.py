class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=defaultdict(int)

        for i in range(len(words)):
            count[words[i]]+=1
        
        max_heap=[(-freq,word ) for word , freq in count.items()]
        heapq.heapify(max_heap)

        ans=[]

        for i in range(k):
            freq,word=heapq.heappop(max_heap)
            ans.append(word)
        return ans