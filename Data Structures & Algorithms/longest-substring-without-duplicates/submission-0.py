class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new = ""
        longest = 0

        for char in s:
            print(char)
            while char in new:
                new = new[1:]
                print(new)

            new = new + char
            print(new)
            longest = max(longest, len(new))
        print(longest)
        return longest
