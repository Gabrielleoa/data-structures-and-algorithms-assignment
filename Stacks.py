def is_balanced(expression):
    stack = []
    brackets = {')', '(', '}','{',']','['}
    for char in expression:
        if char in brackets.values() : 
            stack.append(char)
        elif char in brackets.keys():
            if not stack != brackets[char]:
                return False
            return False
    return not stack
    
expression1= "([])"
expression2 = "([{"
print(is_balanced(expression1))
print(is_balanced(expression2))
