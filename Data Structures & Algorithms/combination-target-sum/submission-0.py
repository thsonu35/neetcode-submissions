class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def dfs(index, curr, total):

            if total == target:
                ans.append(curr[:])
                return

            if index == len(candidates) or total > target:
                return

            # Take current number
            curr.append(candidates[index])
            dfs(index, curr, total + candidates[index])

            # Backtrack
            curr.pop()

            # Skip current number
            dfs(index + 1, curr, total)

        dfs(0, [], 0)
        return ans