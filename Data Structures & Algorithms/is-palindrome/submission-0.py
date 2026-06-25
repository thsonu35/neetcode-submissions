class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for ch in s:
            if ch.isalnum():
                result += ch
        string = list(result.lower())
        
        string.reverse()
        if list(result.lower()) == string:
            return True
        else:
            return False