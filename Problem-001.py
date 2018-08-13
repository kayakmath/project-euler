N=1000

def tri(n):
  return int(n*(n+1)/2)

def mbelow(n,k):
  nn = int(n/k)
  return k*tri(nn)

print(mbelow(N-1,3)+mbelow(N-1,5)-mbelow(N-1,15))
