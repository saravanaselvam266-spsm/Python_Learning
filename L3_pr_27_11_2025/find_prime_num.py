'''Sum Only Prime-Index Values

Given an array, add values only when index is prime
(prime indexes: 2,3,5,7,11…)

Input: [5,8,3,9,6,1,4,10]
Output: 3 + 9 + 1 + 10 = 23'''


def prime(n):
    fact_cnt=0
    for i in range(1,n+1):
        if n%i==0:
            fact_cnt+=1
    if fact_cnt==2:
        return True
    else:
        return False

lst=[5,8,3,9,6,1,4,10]
sum=0
for i in range(len(lst)):
    if prime(i):
        sum+=lst[i]
print(sum)