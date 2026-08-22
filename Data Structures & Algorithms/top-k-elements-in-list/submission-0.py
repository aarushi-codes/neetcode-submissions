class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for item in nums:
            d[item] = d.get(item, 0) + 1
        
        d2 = {}
        for item in d:
            d2.setdefault(d[item], []).append(item)
        
        ans = []
        while len(ans) != k:
            ans += d2[max(d2)]
            d2.pop(max(d2))

        return ans


        

        