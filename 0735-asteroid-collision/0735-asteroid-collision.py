class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []            

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] + a < 0:
                    stack.pop()
                elif stack[-1] + a > 0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(a)

        return stack

    def asteroidCollision2(self, asteroids: List[int]) -> List[int]:
        stack = []            

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if abs(stack[-1]) == abs(a):
                    stack.pop()
                    break
                elif abs(stack[-1]) < abs(a):
                    stack.pop()
                else:
                    break
            else:
                stack.append(a)

        return stack