class Solution:
    def reverseBits(self, n: int) -> int:
        number = str(bin(n)[2:].zfill(32))
        binar = number[::-1]        
        return int(binar, 2)