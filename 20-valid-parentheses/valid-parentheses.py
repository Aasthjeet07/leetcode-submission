class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")" : "(", "{" : "}" , "]" : "["}
        st = []

        for i in s:
            if i == "(" or i == "{" or i == "[":
                st.append(i)
            else:
                if not st:
                    return False
                top = st.pop()
                
                if (i == ')' and top != '(') or (i == '}' and top != '{') or (i == ']' and top != '['):
                    return False
        
        return not st



            
        
        