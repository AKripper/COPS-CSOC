output = "43104f0c32017b48340179266203350636025f6b6e0a5f2730423f42"

for j in range(0,len(output),4):
    
    for p in range(0,128):
        for q in range(0,128):    
            flag = chr(p)+chr(q)

            s = ''.join(format(ord(i), '02x') for i in flag)
            e = ""

            for i in range(0,len(s),4):
                e += format(int(s[i:i+2],16)^int(s[i:i+4],16), '02x')
            
            
            if e == output[j:j+4]:
                print(flag,end="")
            
    
