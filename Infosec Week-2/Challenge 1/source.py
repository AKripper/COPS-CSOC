# Reads the flag.
with open('flag.txt', 'r') as f:
    flag = f.read()

# Converts each charecter in the flag to its ASCII value in hexadecimal.
s = ''.join(format(ord(i), '02x') for i in flag)
e = ""

for i in range(0,len(s),4):
    # XORS the first two digits with the first four digits and adds the four digit answer to the sncoded string.
    e += format(int(s[i:i+2],16)^int(s[i:i+4],16), '02x')

# Outputs the encoded string.
with open('output.txt', 'w') as f:
    f.write(e)