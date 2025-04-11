#4
def sum1n(n):
    if n == 1:
        return 1
    return n + sum1n(n-1)
    

    
print(sum1n(5))