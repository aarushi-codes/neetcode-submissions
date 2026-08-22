class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[i-1] * nums[i-1])

        suffix = []
        r_nums = list(reversed(nums))
        for i in range(len(r_nums)):
            if i == 0:
                suffix.append(1)
            else:
                suffix.append(suffix[i-1] * r_nums[i-1])
        
        suffix.reverse()
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i])
        
        return ans



         
        