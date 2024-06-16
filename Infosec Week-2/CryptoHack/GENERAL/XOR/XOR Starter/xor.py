str="label"
n=13
print("crypto{",end="")
for i in str:
    print(chr(ord(i)^n),end="")
print("}")