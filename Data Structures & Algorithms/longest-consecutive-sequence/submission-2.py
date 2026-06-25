class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        nums = sorted(set(nums))
        last= []

        count = 1
        for i in range(len(nums)-1):
            first = nums[i]
            second = nums[i+1]
            if second - first == 1:
                count +=1
                # print(count)
            elif second - first != 1:
                last.append(count)
                count = 1
                # print(last,count)
            else:
                pass
        last.append(count)
            
        last = sorted(last)
        lenght = len(last)
        # print(last,lenght,last[lenght-1])
        return (last[lenght-1])
