class Solution:
    def hasDuplicate(self, nums) -> bool:
        count = 0
        for i in nums:
                
            element = nums.pop()
            if element in nums:
                return True
            else:
                pass
            
        return False
