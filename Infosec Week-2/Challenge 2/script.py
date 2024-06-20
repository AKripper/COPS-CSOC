import base64

enc1 = ['01000011', '01010011', '01001111', '01000011', '00110010']
enc2 = "337b6a7535375f"
enc3 = "ZDFmZjNyM243XzNuYw=="
enc4 = [60, 144, 61, 156, 66, 65, 137, 154, 60, 154, 175]

dec1 = []
for i in enc1:
    n = int(i,2)
    dec1.append(n)
    print(chr(n),end="")

dec2 = []
for i in range(0,len(enc2),2):
    n = int(enc2[i:i+2],16)
    dec2.append(n)
    print(chr(n),end="")

dec3 = ""
bytes = enc3.encode('utf-8')
bytes = base64.b64decode(bytes)
str = bytes.decode('utf-8')
dec3 += str
print(dec3,end="")

dec4 = ""
for i in enc4:
    print(chr(i),end="")