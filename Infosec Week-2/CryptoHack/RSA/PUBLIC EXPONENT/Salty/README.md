## Challenge Description
Smallest exponent should be fastest, right?

Challenge files:
  - [salty.py](salty_9854bdcadc3f8b8f58008a24d392c1bf.py)
  - [output.txt](output_95f558e889cc66920c24a961f1fb8181.txt)

## Writeup
We see that the value for `e` is set to be `1`. This causes the RSA encryption to be trivial and insecure. We can use this to exploit our flag.

When `e=1`:

`ct = pt mod n`


Given that `n` is a sufficiently large quantity, thus we get `ct = pt`.

So we can convert `ct` to bytes and we will get our flag.

[Here](salty.py) is the script.

## Flag
crypto{saltstack_fell_for_this!}
