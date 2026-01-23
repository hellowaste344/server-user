# without DP (inefficient)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
#####
# with DP (far efficient)
k = 10
dp = [0]*(k+1) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
dp[1] = 1
for i in range(2, k+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[k])
#####
def tail_fact(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_fact(n-1, acc * n)

print(tail_fact(5))
####
def nontail_factorial(n):
    if n == 0:
        return 1    
    else:
        return n * nontail_factorial(n-1)
print(nontail_factorial(5))