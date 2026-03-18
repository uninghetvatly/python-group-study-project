# Valid Parentheses
class Solution(object):
    def isValid(self, s):
        check = []
        for i in range(len(s)):
            if (s[i] == '(' or s[i] == '[' or s[i] == '{'):
                check.append(s[i])
            else:
                if (len(check) == 0):
                    return False
                top = check[-1]
                if ((s[i] == ')' and top != '(') or (s[i] == ']' and top != '[') or (s[i] == '}' and top != '{')):
                    return False
                check.pop()
        return (len(check) == 0)
        