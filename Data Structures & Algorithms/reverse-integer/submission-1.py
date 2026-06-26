class Solution:
    def reverse(self, x: int) -> int:
        print(type(x))

        # print(x == 0 and ( -2**31<x and x< 2**31 )) 
        num = 0 
        if x < 0 :
            num = -1
            x = x* -1
        n = str(x)
        rev = ""
        for i in n:
            rev = i+rev
        if num == -1:
            rev = int(rev) * -1
        if not (-2**31< int(rev) and int(rev)< 2**31 ):
            return 0
        print(rev)
        return int(rev)
