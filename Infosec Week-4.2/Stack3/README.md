# Description
Stack3 looks at environment variables, and how they can be set, and overwriting function pointers stored on the stack (as a prelude to overwriting the saved EIP)

### Hints

- both gdb and objdump is your friend you determining where the win() function lies in memory.
This level is at /opt/protostar/bin/stack3

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
  volatile int (*fp)();
  char buffer[64];

  fp = 0;

  gets(buffer);

  if(fp) {
      printf("calling function pointer, jumping to 0x%08x\n", fp);
      fp();
  }
}
```

# Writeup
For this challenge we are required to `objdump` exactly to an address such that the `win()` function is called. 
Now to check the address of the function I'll be using this command:
`objdump -d stack3 | grep win`

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/ddcbc037-ad83-41d4-ad93-3aaaab68da1e)

So the address is `08048424`

Since it is stacked upwards we have to provide bytes in the following way:

`\x24\x84\x04\x08`

 So I did this using python
 
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/ddd7a49c-decd-4908-9a8e-1f1eb2c82416)

The challenge is thus completed.
