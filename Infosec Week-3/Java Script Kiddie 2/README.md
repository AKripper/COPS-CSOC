## Challenge Description
The image link appears broken... twice as badly... https://jupiter.challenges.picoctf.org/problem/38421

## Writeup
This challenge is very much similar to the previous challenge so for much detailed explanation of my thought process, you may look at my [Java Script Kiddie](https://github.com/AKripper/COPS-CSOC/tree/main/Infosec%20Week-3/Java%20Script%20Kiddie) writeup.


The key for this challenge is 32 bytes.
This is the shifter which I got from the challenge script:
```Java
shifter = Number(key.slice((i*2),(i*2)+1));
```
Clearly the key is read in chunks of 2 bytes an only the first byte is taken for furthur calculations, the other is ignored.


Rest of the Shift algorithm is the same as previous question.
Here is my [script](script.py) which gives the possible key.
I submitted this key but it didnt work, so I checked the hexdump of this broken image I got and compared it to the QR code png image of the previous question and this is what I saw.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/9c0d719c-88c0-4422-aab0-4351f56da019)

Our current key will be modified in the following way:
```
  80 10 40 90  70 80 10 10  20 30 20 80  50 30 10 50
+ 00 00 00 00  00 00 00 00  20 50 10 00  00 00 00 00
= 80 10 40 90  70 80 10 10  40 80 30 80  50 30 10 50     
```

So our modified key is `80104090708010104080308050301050`. Submitting this displayed a QR code.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/df7c31a2-5f39-4210-8442-aa14f5965e7b)


Again using [ZXing Decoder Online](https://zxing.org/w/decode.jspx) I got this

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/34e0ce26-5833-44b8-85b8-bafcf4a9657f)

We thus get our flag.

## Flag
picoCTF{14fb9aed341eac600d5322c198b64c87}
