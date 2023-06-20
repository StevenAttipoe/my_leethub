class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        initial = 0

        for upper, percent in brackets:
            upperDiff = upper - initial
            if income >= 0:
                if income < upperDiff: 
                    upperDiff = income
                tax += (percent / 100) * upperDiff
                income -= upperDiff
                initial = upper
            else:
                break
        return tax