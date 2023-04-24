class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        
        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0):
            sign = -1 
 
        dividend, divisor = abs(dividend), abs(divisor)
    
        res = len(range(divisor, dividend+1, divisor))
        
        if sign == -1:
            res = -res
            
        if res > (2 ** 31) -1:
            return (2 ** 31) -1
        elif res < (-2 ** 31):
            return (-2 ** 31)
        else:
            return res