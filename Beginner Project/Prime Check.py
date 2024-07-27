#Prime Check

def prime_check(x):
    is_prime = True #bool 已定义
    for i in range(2, x):  #遍历1到X中间的数。如果任意一个数可以整除，就不是素数
        if x % i == 0:
            is_prime = False
    if is_prime:
        print('It is a prime number.')
    else:
        print('It is not a prime number.')
