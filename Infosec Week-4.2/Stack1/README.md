# Description

This level looks at the concept of modifying variables to specific values in the program, and how the variables are laid out in memory.

This level is at /opt/protostar/bin/stack1

#### Hints

- If you are unfamiliar with the hexadecimal being displayed, “man ascii” is your friend.
- Protostar is little endian

## Source code
```C
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];

  if(argc == 1) {
      errx(1, "please specify an argument\n");
  }

  modified = 0;
  strcpy(buffer, argv[1]);

  if(modified == 0x61626364) {
      printf("you have correctly got the variable to the right value\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }
}
```

# Writeup
For this challenge I have connected the VM to my local host using `ssh`.

Running the `stack1` file shows this

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/28d2d6e1-94e9-4d6b-857f-686d3fefbc75)

So I tried again and this is what I got

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/1630ddbb-a3bc-47fe-9f9f-1f37611974a5)

Now again giving input more that `64` bytes we get this

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/d49ec7de-0baa-4573-bba9-41b8cf7d6fdd)

I was able to modify the variable. So I tried different combinations and understood how it works. After the 64 bytes of the buffer, the rest of the bytes get stored in the `modified` variable and stacks upwards. These are my trials

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/1bbd13ce-bc7c-4e2c-9806-3e9566ed9623)

I was thus able to solve the challenge.
