class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        add = 1
        new_lst = []

        for i in range(len(nums)):

            for j in range(len(nums)):

                if i == j:
                    pass
                else:
                    add = add * nums[j]

            new_lst.append(add)
            add = 1

        return new_lst