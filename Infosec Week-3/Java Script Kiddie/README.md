## Challenge Description
The image link appears broken... https://jupiter.challenges.picoctf.org/problem/42101

## Writeup
The link has a key submition portal that displays a broken image each time we submit a 16 digit key. The source code of the page contains the following script.
```Java
var bytes = [];
$.get("bytes", function(resp) {
    bytes = Array.from(resp.split(" "), x => Number(x));
});

function assemble_png(u_in){
    var LEN = 16;
    var key = "0000000000000000";
    var shifter;
    if(u_in.length == LEN){
        key = u_in;
    }
    var result = [];
    for(var i = 0; i < LEN; i++){
        shifter = key.charCodeAt(i) - 48;
        for(var j = 0; j < (bytes.length / LEN); j ++){
            result[(j * LEN) + i] = bytes[(((j + shifter) * LEN) % bytes.length) + i]
        }
    }
    while(result[result.length-1] == 0){
        result = result.slice(0,result.length-1);
    }
    document.getElementById("Area").src = "data:image/png;base64," + btoa(String.fromCharCode.apply(null, new Uint8Array(result)));
    return false;
}
```

The code scrambles the column of every 16th byte. For example, the bytes of at the place 0, 16, 32, 48 ... and so on will all be scrambled within themselves according to a certain shift algoritm. We can reverse engineer this algoritm and make a code that gives us the key for the image as we know what the first 16 bytes of PNG image are.

I deduced that the scramble is nothing but a simple shift. By this I mean that for each corresponding value of the key, the column moves down by that much number.

So I made a [script](script.py) that iterates through every column and identifies where the actual byte of the PNG image is by comparing it to first 16 bytes of the PNG.

This gives us the key for the image and typing the key on the portal displays the following QR code.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/2be91a57-f493-441d-936b-b06297cd7094)

Using a QR code decoder we get our flag.

## Flag
