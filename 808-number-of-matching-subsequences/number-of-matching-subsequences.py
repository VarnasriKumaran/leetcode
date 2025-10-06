class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        d=defaultdict(deque)
        count=0

        for word in words:
            d[word[0]].append((word,0))

        for i in s:
            q=d[i]
            d[i]=deque()

            while q:
                word,idx=q.popleft()
                idx+=1
                if idx==len(word):
                    count+=1
                else:
                    d[word[idx]].append((word,idx))
        return count



    





        