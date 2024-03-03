class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)

        if N < 4: return []

        validIPs = []

        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N - 1):
                    if i < 3 and j - i < 4 and k - j < 4 and 0 < N - k <= 4:
                        a, b, c, d = s[:i + 1], s[i + 1:j + 1], s[j + 1:k + 1], s[k + 1: N]
                        if (
                            (len(a) > 1 and a[0] == '0' or int(a) > 255) or 
                            (len(b) > 1 and b[0] == '0' or int(b) > 255) or
                            (len(c) > 1 and c[0] == '0' or int(c) > 255) or
                            (len(d) > 1 and d[0] == '0' or int(d) > 255) 
                        ): continue

                        IP = a + '.' + b + '.' + c + '.' + d
                        validIPs.append(IP)

        return validIPs

        