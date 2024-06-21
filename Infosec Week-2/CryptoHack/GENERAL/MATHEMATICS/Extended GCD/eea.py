# Calculates extended GCD
def extended_gcd(p,q):
    if p==0:
        return q,0,1
    else:
        gcd,u1,v1=extended_gcd(q%p,p)
        u=v1-(q//p)*u1
        v=u1
        return gcd,u,v

p=26513
q=32321
gcd,u,v=extended_gcd(p,q)
print(f"GCD: {gcd}, u: {u}, v: {v}")

# Output : GCD: 1, u: 10245, v: -8404
