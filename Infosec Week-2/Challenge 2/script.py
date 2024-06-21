import base64

# dividing the encoded string to four different parts
enc1 = ['01000011', '01010011', '01001111', '01000011', '00110010']
enc2 = "337b6a7535375f"
enc3 = "ZDFmZjNyM243XzNuYw=="
enc4 = ['60', '144', '61', '156', '66', '65', '137', '154', '60', '154', '175']

# converts decimal values to ascii
dec1 = []
for i in enc1:
    n = int(i,2)
    dec1.append(n)

# converts given hexaecimal values to ascii
dec2 = []
for i in range(0,len(enc2),2):
    n = int(enc2[i:i+2],16)
    dec2.append(n)

# decodes base64 encoded string
dec3 = ""
bytes = enc3.encode('utf-8')
bytes = base64.b64decode(bytes)
str = bytes.decode('utf-8')
dec3 += str

# converts given octal numbers to ascii
dec4 = []
for i in enc4:
    n = int(i,8)
    dec4.append(n)


# Joins the decoded parts andd prints them
for i in dec1:
    print(chr(i),end="")
for i in dec2:
    print(chr(i),end="")
print(dec3,end="")
for i in dec4:
    print(chr(i),end="")

# Output : CSOC23{ju57_d1ff3r3n7_3nc0d1n65_l0l}
