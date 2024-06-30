## Challenge Description
Can you break into this super secure portal? 

https://jupiter.challenges.picoctf.org/problem/6353/

## Writeup
The link directs to a verification portal, but the site is not of much interest to us, So I checked the source code of of the page. It contains a script which is written in a single line. I added appropriate spaces to it and this is what it looks like.

```java
var _0x5a46=['0a029}','_again_5','this','Password\x20Verified','Incorrect\x20password','getElementById','value','substring','picoCTF{','not_this'];
(function(_0x4bd822,_0x2bd6f7){
  var _0xb4bdb3=function(_0x1d68f6){
    while(--_0x1d68f6){
      _0x4bd822['push'](_0x4bd822['shift']());
    }
  };
  _0xb4bdb3(++_0x2bd6f7);
}
(_0x5a46,0x1b3));
var _0x4b5b=function(_0x2d8f05,_0x4b81bb){
  _0x2d8f05=_0x2d8f05-0x0;
  var _0x4d74cb=_0x5a46[_0x2d8f05];
  return _0x4d74cb;
};
function verify(){
  checkpass=document[_0x4b5b('0x0')]('pass')[_0x4b5b('0x1')];
  split=0x4;
  if(checkpass[_0x4b5b('0x2')](0x0,split*0x2)==_0x4b5b('0x3')){
    if(checkpass[_0x4b5b('0x2')](0x7,0x9)=='{n'){
      if(checkpass[_0x4b5b('0x2')](split*0x2,split*0x2*0x2)==_0x4b5b('0x4')){
        if(checkpass[_0x4b5b('0x2')](0x3,0x6)=='oCT'){
          if(checkpass[_0x4b5b('0x2')](split*0x3*0x2,split*0x4*0x2)==_0x4b5b('0x5')){
            if(checkpass['substring'](0x6,0xb)=='F{not'){
              if(checkpass[_0x4b5b('0x2')](split*0x2*0x2,split*0x3*0x2)==_0x4b5b('0x6')){
                if(checkpass[_0x4b5b('0x2')](0xc,0x10)==_0x4b5b('0x7')){
                  alert(_0x4b5b('0x8'));
                }
              }
            }
          }
        }
      }
    }
  }
  else{
    alert(_0x4b5b('0x9'));
  }
}

```

This still isn't very easy to understand so I changed the variables to those that I understand and simplified the functions a little bit.
```Java
var variables_array=['0a029}','_again_5','this','Password\x20Verified','Incorrect\x20password','getElementById','value','substring','picoCTF{','not_this'];

(function(a,b){
    var func1=function(c){
        while(--c){
        a.push(a.shift());
        };
        func1(++b);
    }
}(variables_array,435));

var func2=function(a){
  return variables_array[a];
};

function verify(){
  checkpass=document[func2(0)]('pass')[func2(1)];
  if(checkpass[func2(2)](0,8)==func2(3)){
    if(checkpass[func2(2)](8,16)==func2(4)){
      if(checkpass[func2(2)](24,36)==func2(5)){
        if(checkpass[func2(2)](16,24)==func2(6)){
          alert(func2(8));
        }
      }
    }
  }
}
else{
  alert(func2(9));
}

```

Here is an analysis of the code: 
- `func1` : Shifts the array `455` times. The number of elements in the array is `10`, so effectively the the array is shifted `5` times.
- `func2` : Passes elements of the array as another function. `func2(i)` is just `variables_array[i]`
- `verify` : A series of if statements checks the `pass` provided to actual parts of the `pass` from the `variables_array`.

I have made the code much more readable. by replacing `func1` and `func2` with the actual values from array and changing the array

Now the new variables array is:
```Java
var variables_array=['getElementById','value','substring','picoCTF{','not_this','0a029}','_again_5','this','Password\x20Verified','Incorrect\x20password'];
```

From this code we can see:
```Java
checkpass[func2(2)](0,8)==func2(3)
checkpass[func2(2)](8,16)==func2(4)
checkpass[func2(2)](16,24)==func2(6)
checkpass[func2(2)](24,36)==func2(5)
```


So the `pass` is effectively:

`picoCTF{`+`not_this`+`_again_5`+`0a029}`

We can thus see our flag.

## Flag
picoCTF{not_this_again_50a029}
