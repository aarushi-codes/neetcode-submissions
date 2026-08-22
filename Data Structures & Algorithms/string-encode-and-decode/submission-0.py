class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for item in strs:
            ans += item+"😃"
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        prev = 0
        for i in range(len(s)):
            if s[i] == "😃":
                ans += [s[prev:i]]
                prev = i+1

        return ans
        


