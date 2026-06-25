class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        concat = ""
        for i in digits:
            concat = concat + str(i) 
        result = int(concat)+1
        return list(str(result))     
        