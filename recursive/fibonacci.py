def fibonacci(num):
    '''Fibonacci number is like 0,1,2,3,5,8,13,21.....
    For calculating fibonacci we have to follow this 5 = 3 + 2
    so f(5) = f(n-1) + f(n-2)'''
    assert num >= 0 and int(num) == num, "Number should be positive integer"
    if num in (0, 1):
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)


print(fibonacci(8))
