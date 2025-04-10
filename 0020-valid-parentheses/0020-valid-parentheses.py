class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        equiv = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if char in equiv.values():
                pilha.append(char)
            elif char in equiv.keys():
                if len(pilha) < 1 or equiv[char] != pilha[-1]:
                    return False
                else:
                    pilha.pop()

        if len(pilha) == 0:
            return True
        else:
            return False
            
