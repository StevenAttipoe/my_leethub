class Solution:
    def __init__(self):
        self.memo = {
            1 : ['0', '1'],
            2: ['01', '10', '11']
        }

    def validStrings(self, n: int) -> List[str]:
        if n in self.memo:
            return self.memo[n]

        prevValidStrings = self.validStrings(n - 1)
        validStrings = []

        for string in prevValidStrings:
            if string[-1] == '1':
                validStrings.append(string + '0')
                validStrings.append(string + '1')
            
            else:
               validStrings.append(string + '1')

        self.memo[n] = validStrings
        return validStrings

    def validStrings2(self, n: int) -> List[str]:
        def helper(i, string):
            if i == n:
                return [string]

            temp = []

            if not string or string[-1] == "1":
                temp += helper(i + 1, string + "0")
            
            return temp + helper(i + 1, string + "1")
        
        return helper(0, "")


    


        