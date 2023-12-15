def is_balanced(expression):
    stack = []
    for char in expression:
        if expression == '()' or "{.}" or '[]' : 
            return True
        elif expression == '{' and '[' and '(' and '}' and']' and')':
            return False
    return not stack
    
expression1= "([])"
expression2 = "([{"
print(is_balanced(expression1))
print(is_balanced(expression2))
