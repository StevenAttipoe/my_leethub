class Codec:
    def __init__(self):
        self.dic = {}

    def encode(self, longUrl: str) -> str:
        hashCode = hash(longUrl)
        self.dic[hashCode] = longUrl
        return hashCode
        

    def decode(self, shortUrl: str) -> str:
        return self.dic[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))