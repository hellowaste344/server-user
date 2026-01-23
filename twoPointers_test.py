import numpy as np
def two_sum(arr, target):
    n = len(arr)
    values = []
    for i in range(n):

        for j in range(i+1,n):

            if arr[i] + arr[j] == target:
                values.append(arr[i])
                values.append(arr[j])
                return values  
            
    # if no pair is found
    return False

def New_two_sum(arr, target):
    arr = sorted(arr)
    left, right = 0, len(arr)-1
    
    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return arr[left], arr[right]
        
        elif total < target:
            left += 1
        
        else:
            right -= 1


arr = np.random.randint(low=0, high=10, size=5)
target = 9

if two_sum(arr, target) is False:
    print("target missed!")
else:
    print(two_sum(arr, target))

# call second function
print(New_two_sum(arr, target))