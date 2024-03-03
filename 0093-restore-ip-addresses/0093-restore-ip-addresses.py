class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12: 
            return []

        N = len(s)
        validIPs = []

        for i in range(1, min(4, N - 2)):
            for j in range(i + 1, min(i + 4, N - 1)):
                for k in range(j + 1, min(j +4, N)):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if (
                        self.isNotValid(a) or 
                        self.isNotValid(b) or
                        self.isNotValid(c) or
                        self.isNotValid(d)
                    ) : continue

                    IP = a + '.' + b + '.' + c + '.' + d
                    validIPs.append(IP)

        return validIPs

    def isNotValid(self, segment):
        if len(segment) > 1 and segment[0] == '0' or int(segment) > 255:
            return True
        return False
    

        