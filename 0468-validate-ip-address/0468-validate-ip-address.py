class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.isV4(queryIP):
            return "IPv4"

        elif self.isV6(queryIP):
            return "IPv6"

        else:
            return "Neither"

    def isV4(self, queryIP):
        octets = queryIP.split(".")

        if len(octets) != 4: 
            return False

        for octet in octets:
            if not octet.isdigit() or (len(octet) > 1 and octet[0] == '0') or int(octet) > 255:
                return False
        return True

    def isV6(self, queryIP):
        octets = queryIP.split(":")

        if len(octets) != 8: 
            return False

        for octet in octets:
            if not 1 <= len(octet) <= 4:
                return False
            
            for c in octet:
                if c.isalpha() and not ('a' <= c <= 'f' or  'A' <= c <= 'F'):
                    return False
        return True