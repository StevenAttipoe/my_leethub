class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        count = 0
        popped = None
        element = ''

        for c in formula + '#':
            if c.isupper() or c in '()#':
                if element:
                    stack[-1][element] += count if count else 1
                    element = ''
                elif count or popped:
                    for subElement, subCount in (popped or stack.pop()).items():
                        stack[-1][subElement] += subCount * max(count, 1)
                    popped = 0
                count = 0

            if c == '(':
                stack.append(defaultdict(int))
            elif c == ')':
                popped = stack.pop()
            elif c.isdigit():
                count = count * 10 + int(c)
            else:
                element += c


        return ''.join([f'{e}{c}' if c > 1 else e for e,c in sorted(stack.pop().items())])
