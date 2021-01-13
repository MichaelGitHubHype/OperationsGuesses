def eval_expression(s1: str, s2: str) -> bool:
    """
    Evaluates the result of s1 and s2, and returns if they are equal.
    Precondition: s1 and s2 are string representations of a 
    mathematical expression
    Postcondition: returns True if both mathematical expressions are 
    equal to each other
    """
    return eval(s1.split('=')[0]) == eval(s2.split('=')[0])
