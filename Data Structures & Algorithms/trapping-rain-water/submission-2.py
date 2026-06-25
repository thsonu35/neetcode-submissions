class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range (len(height)):
            left = 0 
            for j in range (i,-1,-1):
                left = max(height[j],left)
            right = 0 
            for j in range (i,len(height)):
                right = max(height[j],right)
            water = water + min(left , right) - height[i]
        return water