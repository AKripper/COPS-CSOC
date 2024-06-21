import base64

hex="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
flag=bytes.fromhex(hex)        # converts hex to bytes
print(base64.b64encode(flag))  # base64 encodes the flag

# Output : b'crypto/Base+64+Encoding+is+Web+Safe/'
