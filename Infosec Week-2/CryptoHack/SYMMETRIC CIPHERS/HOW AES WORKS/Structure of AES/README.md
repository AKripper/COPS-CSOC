## Challenge Description
Included is a bytes2matrix function for converting our initial plaintext block into a state matrix. Write a matrix2bytes function to turn that matrix back into bytes, and submit the resulting plaintext as the flag.

Challenge files:
  - [matrix.py](matrix_e1b463dddbee6d17959618cf370ff1a5.py)

## Writeup
We have to write a code that converts a given matrix to bytes. The matrix given is basically a list of lists of size 4. So to convert it back we must simply add all the lists together and convert the ascii value back to its charecter value to display the flag. 


[Here](matrix.py) is the script.

## Flag
crypto{inmatrix}
