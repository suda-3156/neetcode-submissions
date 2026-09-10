class Solution:

    def encode(self, strs: List[str]) -> str:
        n :int = len(strs)
        counts :list[int] = []
        
        for s in strs:
            counts.append(len(s))

        encoded: str = str(n) + ","
        encoded += ",".join(list(map(str, counts))) + ","
        encoded += "".join(strs)

        return encoded

    def decode(self, s: str) -> List[str]:
        parts = s.split(",")
        n = int(parts[0])
        counts: list[int] = list(map(int, parts[1:n+1]))

        s = ",".join(parts[n+1:])

        decoded: list[str] = []
        for count in counts:
            new_s = s[:count]
            s = s[count:]
            decoded.append(new_s)

        return decoded