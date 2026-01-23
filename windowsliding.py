import sys
import random

def maxSum(arr, n, k):
    # initialize result
    max_sum = -sys.maxsize

    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i+j]

        max_sum = max(current_sum, max_sum)
    
    return max_sum

if __name__ == "__main__":
    k = 3
    arr = random.sample(range(-100,100), k=10)
    print(arr, end=' ')
    n = len(arr)
    print(maxSum(arr, n, k))

