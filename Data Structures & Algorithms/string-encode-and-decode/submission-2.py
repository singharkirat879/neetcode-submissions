class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_res = []
        for s in strs:
            encoded_res.append(f"{len(s)}#{s}")
        return "".join(encoded_res)

    def decode(self, s: str) -> list[str]:
        decoded_res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            
            start_of_str = j + 1
            end_of_str = start_of_str + length
            
            decoded_res.append(s[start_of_str:end_of_str])
            
            i = end_of_str
            
        return decoded_res

        