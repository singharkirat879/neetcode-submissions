class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "EMPTY"
        return "π".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY":
            return []

        return s.split("π")
