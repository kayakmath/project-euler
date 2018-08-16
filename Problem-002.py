def fib(n):
  fibs = [1,1]
  pos = 1
  while fibs[pos]+fibs[pos-1]<n:
    fibs.append(fibs[pos]+fibs[pos-1])
    pos+=1
  return fibs

s=0
f=fib(4000000)
for x in f:
  if x%2==0:
    s+=x

print(s)
