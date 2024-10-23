def main(S, d):
    '''create a babylonian function.

    Args:
        S (int): number
        d (int): numnber
        
    Returns:
        float: result
    '''
    p = pow(d,2)
    a = S - p / 2 * d

    b = a + d

    p2 = pow (a,2)
    x = b - (p2 / 2 * b)
    
    return (x)
r = main(122, 4)
print (r)