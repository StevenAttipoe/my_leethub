class Solution:
    def reverse(self, x: int) -> int:
        reversedNum = 0
        num = x
        x = abs(x)
        
        while x != 0:
            lastNum = x % 10
            x = x // 10
            reversedNum = (reversedNum*10) + lastNum
            
        if(reversedNum.bit_length()>31): 
            return 0 
        
        return reversedNum if num >= 0 else -1 * reversedNum
            
            
        
        