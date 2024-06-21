from Crypto.Util.number import *

num=11515195063862318899931685488813747395775516287289682636499965282714637259206269
flag=long_to_bytes(num)  # Converts decimal to bytes
print(flag)

# Output : b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'
