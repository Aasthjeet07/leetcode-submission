class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open = 0
        close = 0
        ans = 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                open += 1
            else:
                close += 1
            if open == close:
                ans = max(ans, open * 2)
            elif close > open:
                open = 0
                close = 0

        open = 0
        close = 0

#right to left
        for i in range(n-1, -1, -1):
            if s[i] == '(':
                open += 1
            else:
                close += 1

            if open == close:
                ans = max(ans, open * 2)
            elif open > close:
                open = 0
                close = 0    

        return ans



        