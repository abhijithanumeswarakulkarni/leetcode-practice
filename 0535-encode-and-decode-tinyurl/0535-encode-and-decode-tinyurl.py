class Codec:
    storage = {}
    idx = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        Codec.storage[str(Codec.idx)] = longUrl
        tiny_url = str(Codec.idx)
        Codec.idx += 1
        return tiny_url
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return Codec.storage[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))