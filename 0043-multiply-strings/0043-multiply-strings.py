class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        carry1 = carry2 = 1

        for i in num2[::-1]:
            carry1 = 1
            for j in num1[::-1]:
                res += int(i) * int(j) * carry1 * carry2
                carry1 *= 10
            carry2 *= 10

        return str(res)

    def multiply2(self, num1: str, num2: str) -> str:
        carry = power = 0
        res = []

        for i in range(len(num2) - 1, -1, -1):
            runningProduct = deque()
            for j in range(len(num1) - 1, -1, -1):
                product = int(num2[i]) * int(num1[j])        
                product += carry
                if product > 9:
                    if j == 0:
                        runningProduct.appendleft(str(product))
                        carry = 0
                    else:
                        runningProduct.appendleft(str(product % 10))
                        carry = product // 10
                else:
                    runningProduct.appendleft(str(product))
                    carry = 0

            res.append(int(''.join(runningProduct)) * pow(10, power))
            power += 1
        
        if carry:
            res[-1] = res[-1] + (carry * pow(10, power))

        return str(sum(res))

                
                
        