## Challenge Description
Several of the challenges are dynamic and require you to talk to our challenge servers over the network. This allows you to perform man-in-the-middle attacks on people trying to communicate, or directly attack a vulnerable service. To keep things consistent, our interactive servers always send and receive JSON objects.

Such network communication can be made easy in Python with the `pwntools` module. This is not part of the Python standard library, so needs to be installed with pip using the command line `pip install pwntools`.

For this challenge, connect to `socket.cryptohack.org` on port `11112`. Send a JSON object with the key buy and value flag.

`The example script below contains the beginnings of a solution for you to modify, and you can reuse it for later challenges.`


Connect at `socket.cryptohack.org 11112`

Challenge files:
  - [pwntools_example.py](pwntools_example_72a60ff13df200692898bb14a316ee0b.py)


## Writeup
Change the the request parameter `clothes` to `flag` and run the program. We get our flag.

## Flag
crypto{sh0pp1ng_f0r_fl4g5}
