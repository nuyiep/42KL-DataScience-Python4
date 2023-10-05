

def check_num(args):
    '''Error checking'''
    try:
        for i in args:
            isinstance(i, int) or isinstance(i, float)
    except Exception as err:
        print("ERROR", err)


def handle_median(args, value, args_length: int):
    '''Median'''
    sorted_args = sorted(args)
    if (args_length % 2 != 0):  # odd
        pos = (args_length + 1) // 2  # //integer division
        pos = int(pos) - 1
        median = sorted_args[pos]
    else:
        pos = args_length // 2
        median = (sorted_args[pos] + sorted_args[pos - 1]) / 2
    print("median: ", median)


def handle_quartile(args, value, args_length):
    '''Quartile'''
    twenty_five = float(sorted(args)[args_length // 4])
    seventy_five = float(sorted(args)[3 * len(args) // 4])
    quartile_list = [twenty_five, seventy_five]
    print("quartile:", quartile_list)


def handle_var(args, value, args_length, count):
    '''Handle var'''
    mean = sum(args) / args_length
    difference = []
    for i in args:
        result = (i - mean) ** 2
        difference.append(result)
    outcome = 0
    for x in difference:
        outcome = outcome + x
    z = outcome / args_length
    if (count == 1):
        print("var :", z)
    return (z)


def handle_std(args, value, args_length, count):
    '''Handle std'''
    outcome = handle_var(args, value, args_length, count)
    outcome = outcome ** 0.5
    print("std :", outcome)


def ft_statistics(*args: any, **kwargs: any) -> None:
    '''Get statistics'''
    check_num(args)
    args_length = len(args)
    count = 0
    for key, value in kwargs.items():
        try:
            if value == "mean":
                mean = sum(args) / args_length
                print("mean: ", mean)
            if value == "median":
                handle_median(args, value, args_length)
            if value == "quartile":
                handle_quartile(args, value, args_length)
            if value == "var":
                count = 1
                handle_var(args, value, args_length, count)
            if value == "std":
                handle_std(args, value, args_length, count)
        except Exception:
            print("ERROR")
