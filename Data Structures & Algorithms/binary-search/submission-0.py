class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            count = 0
            for i in range(len(nums)):
                if nums[i] != target:
                    count+=1
                else:
                    break
            return count
        return -1


        