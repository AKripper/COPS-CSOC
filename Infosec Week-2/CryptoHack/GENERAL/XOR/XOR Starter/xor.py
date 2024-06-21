str="label"
n=13

print("crypto{",end="")

# XORS "label" with 13
for i in str:
    print(chr(ord(i)^n),end="")
    
print("}")

# Output : crypto{aloha}
