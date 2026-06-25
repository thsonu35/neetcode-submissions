class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[0] != 0 :
            return 0
        count = 0
        lens= len(nums)+1
        print(lens)
        for i in range(lens):
            count = count + i
            print(i,count)
        return count - sum(nums)
        # print(len(nums))
        # print(nums[-1])
        # count = 1
        # for i in range(nums[-1]):
        #     print(i)
        #     count = count+i
        #     print(count)
        # print(sum(nums),count)