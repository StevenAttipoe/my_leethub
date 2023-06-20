class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        prevUpper = 0

        for upper, percent in brackets:
            #Difference in upper bounds
            upperDiff = upper - prevUpper
            if income >= 0:
                #Check if income is less than upperDiff
                if income < upperDiff: 
                    upperDiff = income
                tax += (percent / 100) * upperDiff
                income -= upperDiff
                prevUpper = upper
            else:
                break
        return tax