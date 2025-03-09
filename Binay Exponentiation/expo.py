x = int(input("Enter the base: "))
n = int(input("Enter the exponent: "))

# def power(x, n):
#     if n == 0:
#         return 1
#     if n % 2 == 0:
#         return power(x*x, n//2)
#     return x*power(x*x, n//2)

def power(x,n):
    if n == 0:
        return 1
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == -1:
        if n % 2 == 0:
            return 1
        else:
            return -1
    if n < 0:
        x = 1/x
        n = -n
        
    binary_form = n
    ans = 1
    mod = 10**9 + 7


    while binary_form > 0:
        if binary_form % 2 == 1:
            ans = (ans*x) % mod
        x = (x*x) % mod
        binary_form //= 2
        
    return ans



