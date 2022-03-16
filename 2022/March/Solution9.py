# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         stack = []
#
#         for part in path.split("/"):
#             if part == "..":
#                 if stack:
#                     stack.pop()
#                 elif part == "." or not part:
#                     continue
#                 else:
#                     stack.append(part)
#
#         result = "/" + "/".join(stack)
#
#         return result

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def process(s: str, symbol1, symbol2) -> str:
            stack = []
            balance = 0
            for i in s:
                if i == symbol1:
                    balance += 1
                elif i == symbol2:
                    if balance == 0:
                        continue
                    balance -= 1
                stack.append(i)

            return "".join(stack)

        result = process(s, "(", ")")
        result = process(result[::-1], ")", "(")

        return result[::-1]



