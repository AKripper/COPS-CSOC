# Description
Stack4 takes a look at overwriting saved EIP and standard buffer overflows.

This level is at /opt/protostar/bin/stack4

### Hints

- A variety of introductory papers into buffer overflows may help.
- gdb lets you do “run < input”
- EIP is not directly after the end of buffer, compiler padding can also increase the size.
## Source code
```C
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void win()
{
  printf("code flow successfully changed\n");
}

int main(int argc, char **argv)
{
  char buffer[64];

  gets(buffer);
}
```

# Writeup
For this challenge our goal is to overwrite the address of return function with the address of win fuction. The address of win function is `0x80483f4`.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/34aa5ee5-e8b0-45a2-a06d-0f3701140523)

Now we need to check where the return function is present in our stack. I ran the program in gdb for this purpose with the input as `aaaa`

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/4b23ea0b-eab3-4beb-b14f-f96d38d68c9b)

Now we know the address of the return function and how long the padding must be. The padding starts from `0xbffffc70` till `0xbffffcb0 + 12` which means it is `76` bytes long.
So we must add our win fucntion after a padding of `76` bytes.


I will be doing this using a python script.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/1bcdadd9-ca8b-4e16-a28d-1dbf3dfce500)

Now running this script we get this

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/ebfcd265-c24b-4522-a1af-e630f92b1180)

The challenge is thus completed.
