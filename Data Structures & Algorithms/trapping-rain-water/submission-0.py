class Solution:
    def trap(self, height: List[int]) -> int:
        p_max = [0]
        s_max = []

        for i in range(1, len(height)):
            p_max.append(max(p_max[i-1], height[i-1]))
        
        rev_height = height[::-1]

        s_max.append(0)

        for j in range(1, len(rev_height)):
            s_max.append(max(s_max[j-1], rev_height[j-1]))

        s_max = s_max[::-1]

        ans = 0
        for k in range(len(height)):
            level = min(p_max[k], s_max[k]) - height[k]
            if level > 0:
                ans += level
        
        return ans

        