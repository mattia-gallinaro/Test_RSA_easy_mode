import pandas
import math
import numpy as np

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


def find_MCD(e, fi):
    divider_e = [e/2]
    divider_fi = [fi/2]
    for i in range(2, e):
        if(e%i) == 0 and i!=1:
            np.append(divider_e, i)
            print (i) 
            
    
    for j in range(1, fi):
        if(fi%j) == 0 and j != 1:
            np.append(divider_fi, j)
    
    #print (divider_fi)
    for i in range(len(divider_e)):
        for j in range(len(divider_fi)):
            if j == i and j != 1 :
                return False
    return True
    
def find_d(e, fi):
    response = False
    k = 0
    while response is not True:
        k+=1
        if(((k*fi +1) % e ) == 0):
            response = True
    return k
        
    
result = False;

while result is not True:
    print("Salve, inserisca il valore di p");
    p = int(input());
    result = is_prime(p)

result = False

while result is not True:
    print("Salve, inserisca il valore di q");
    q = int(input());
    result = is_prime(q)

n  = p * q;

print(n);

fi =  (p -1) * (q-1)

#print(fi)

e = 1
result = find_MCD(e,fi)

while result is not True:
    e+=1
    result = find_MCD(e,fi)
    
print(e)

d = find_d(e, fi)


print("Chiave pubblica" + str(e) + str(n))
print("Chiave privata " + str(d) + str(n))
