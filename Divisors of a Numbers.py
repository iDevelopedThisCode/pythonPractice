from typing import List
result = []
def printDivisors(n :int) -> List[int]:
    # Write your code here
    n=int(n)
    for i in range(1,n):
        if(n%i==0 or n==i):
            result.append(i)
    result.append(n)
    return result