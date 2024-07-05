# Description
Stack2 looks at environment variables, and how they can be set.

This level is at /opt/protostar/bin/stack2

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
  char *variable;

  variable = getenv("GREENIE");

  if(variable == NULL) {
      errx(1, "please set the GREENIE environment variable\n");
  }

  modified = 0;

  strcpy(buffer, variable);

  if(modified == 0x0d0a0d0a) {
      printf("you have correctly modified the variable\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }

}
```

# Writeup
I ran the program but didn't know how to set the environment variable. So I searched for it and found this website called [freecodecamp](https://www.freecodecamp.org/news/how-to-set-an-environment-variable-in-linux/)

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/b1947010-9c5a-4e3e-b06d-a101f2db85c9)

Now running the program again. I notice that I have to change the environment variable `GREENIE` and overflow it such that it changes the `modified` value accordingly.


From the previous question we learnt that `0d`, `0a`, `0d`, `0a` are just hexaecimal numbers for ascii values of charecters that overflow the buffer.
So now looking at the ascii table following are the charecters:
- 0d = '\r'
- 0a = '\n'

So we have to set the variable such that the the first four variable stacked upon the overflow will be passed to the `modified` variable.
The value can be:
`aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n\r\n\r`
This when stacked it will have '\n'(0x0a) at the bottom following the other charecters.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/1ea402db-7c56-4230-8424-2d2e228fbea1)


But this does not work so now I'll be using python for this. 

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/3852bced-12e5-4665-a68d-aef86b0f54d3)

And the challenge is thus solved.
