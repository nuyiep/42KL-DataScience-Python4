

def callLimit(limit: int):
    '''Closure'''
    count = 0

    def callLimiter(function):
        '''Wrapper'''
        def limit_function(*args: any, **kwds: any):
            '''the fuction'''
            nonlocal count
            if (count < limit):
                count += 1
                return function(*args, **kwds)
                # return the result of calling function
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
