def extended_euclidean(a,b):
    if a==0:
        return b,0,1
    else:
        g,x,y = extended_euclidean(b%a,a)
        return g, y-(b//a)*x, x

def private_key(e, p, q):
    phi = (p-1)*(q-1)
    gcd,x,y = extended_euclidean(e, phi)
    return x




p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
print("d = ",private_key(e,p,q))