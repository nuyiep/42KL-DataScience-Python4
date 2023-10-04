

def square(x: int | float) -> int | float:
    '''Square
        E.g. 4 * 4 = 16'''
    x = x ** 2
    return (x)


def pow(x: int | float) -> int | float:
    '''Power of x
        E.g. 4 ^ 4 = 256'''
    x = x ** x
    return (x)


def outer(x: int | float, function) -> object:
    count = 0
    '''Outer function
        Remembering the count, to loop again
        eveyr time, not remembering the output'''
    def inner() -> float:
        '''Inner function'''
        nonlocal count
        count += 1
        result = x
        for i in range(count):
            result = function(result)
        return (result)
    return inner
