class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total = {}
        for item in strs: #O(n)
            freq = [0] * 26
            for ch in item: #O(m)
                freq[ord(ch) - ord('a')] += 1
            
            key = tuple(freq)
            if key not in total:
                total[key] = []
            total[key].append(item)
        
        ans = []
        for item in total:
            ans.append(total[item])
        
        return ans
