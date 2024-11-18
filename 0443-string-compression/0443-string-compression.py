class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        n = 0
        
        while i < len(chars):
            cur = chars[i]
            count = 0

            while i < len(chars) and cur == chars[i]:
                count += 1
                i += 1
            
            chars[n] = cur
            n += 1
            if count > 1:
                for num in str(count):
                    chars[n] = num
                    n += 1

        return n

        