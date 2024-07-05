# Description
This level introduces the concept that memory can be accessed outside of its allocated region,
how the stack variables are laid out, and that modifying outside of the allocated memory can modify program execution.


This level is at `/opt/protostar/bin/stack0`

## Source Code
```C
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];

  modified = 0;
  gets(buffer);

  if(modified != 0) {
      printf("you have changed the 'modified' variable\n");
  } else {
      printf("Try again?\n");
  }
}
```

# Writeup
I started by running the porgram `stack0` and this is what it looked like

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/6eda5a32-f9c6-414a-a3c7-d42e54a5353a)

Looking at the source code, program first declares a variable `modified` and sets its value to `0`.It then inputs a `buffer` string of size `64` bytes.

Now if I give a buffer that is more than `64` bytes long, we might be able to change the value of the `modified` variable. I will be doing just that

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/09512f3c-3f8a-4f38-9c8e-2ec1af5df578)

We have thus completed this challenge.
