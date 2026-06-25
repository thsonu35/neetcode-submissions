class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}      # frequency of chars in current window
        left = 0
        max_freq = 0   # highest frequency char in current window
        ans = 0

        for right in range(len(s)):

            # add current character
            count[s[right]] = count.get(s[right], 0) + 1

            # update highest frequency seen in window
            max_freq = max(max_freq, count[s[right]])

            # if window is invalid, shrink from left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # update answer
            ans = max(ans, right - left + 1)

        return ans