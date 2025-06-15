# your code goes here
import math
num = input(int())
arrAy = list(map(int, input().split()))
def add_elements(arr,n):
    total = 0
    n=int(n)
    for i in range(0,n):
        total += arr[i]
    return str(total)
print(int(add_elements(arrAy,num)))
