class Solution:
    def isValid(self, s: str) -> bool:
        stock = []
        d = { '}' : '{',
            ')' : '(',
            ']' : '[',
        }

        for i in s:
            if i in d.values():
                stock.append(i)
            elif i in d.keys():
                if not stock or d[i] != stock.pop():
                    return False
        return not stock
