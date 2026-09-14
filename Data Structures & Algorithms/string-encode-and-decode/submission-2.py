class Solution:

    def encode(self, strs: List[str]) -> str:
        output = self.digits(len(strs))
        for string in strs:
            output += self.digits(len(string))
        for string in strs:
            output += string
        return output
    def decode(self, s: str) -> List[str]:
        length = int(s[:3])
        strs = []
        lengths = []
        ptr = 3
        for i in range(length):
            lengths.append(int(s[ptr:ptr+3]))
            ptr += 3
        for length in lengths:
            strs.append(s[ptr:ptr+length])
            ptr += length
        return strs
            

    def digits(self, num: int):
        if num // 100 >= 1:
            return str(num)
        if num // 10 >= 1:
            return '0' + str(num)
        return '0' + '0' + str(num)