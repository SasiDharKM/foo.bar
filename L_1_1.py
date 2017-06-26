limit=30000 #estimate from the prime number theory
prime = [True for i in range(limit)]
index=2

while(index*index < limit):
    if(prime[index-1]):
        for i in range(index*2,limit,index):
            prime[i-1] = False
    index+=1

prime_string = ""
for i in range(1,limit):
    if prime[i]:
        prime_string+=(str(i+1))

def answer(n):
    # your code here
    return prime_string[n:n+5]
print (answer(3))