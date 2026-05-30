class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        topKfreq = []
        for i in range(k):
            highest_key = max(freq, key=freq.get)
            topKfreq.append(highest_key) 
            del freq[highest_key]
            
        return topKfreq