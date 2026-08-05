class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for item in strs:
            result += str(len(item)) + "#" + item
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        p = 0 
        length = ""
        while p <= len(s) -1:
            if s[p].isdigit():
                length += s[p]
                p += 1

            if s[p] == "#":
                result.append(s[p+1:p+int(length)+1])
                p = p + int(length) + 1 
                length = ""
        return result 
