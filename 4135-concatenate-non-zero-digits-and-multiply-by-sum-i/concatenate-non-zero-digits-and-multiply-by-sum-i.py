class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sm = 0
        ans = 0
        while n > 0:
            d = n % 10
            n = n//10
            sm += d
            if d == 0:
                continue
            ans = ans * 10 + d
        
        x = 0
        while ans > 0:
            d = ans % 10
            ans = ans//10
            x = x * 10 + d
        return x * sm




                
        