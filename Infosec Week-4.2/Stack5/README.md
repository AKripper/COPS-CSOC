# Description 
Stack5 is a standard buffer overflow, this time introducing shellcode.

This level is at /opt/protostar/bin/stack5

### Hints

- At this point in time, it might be easier to use someone elses shellcode
- If debugging the shellcode, use \xcc (int3) to stop the program executing and return to the debugger
- remove the int3s once your shellcode is done.

## Source code
```C
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  char buffer[64];

  gets(buffer);
}
```
# Writeup
I will start by running the challenge file on gdb, to check the offset of return function just like we did in the previous challenge.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/2fd898fe-4027-4ea3-8564-f2db14cbe87c)

Now doing the required padding:

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/7338162c-ea7b-4f79-ad5d-02270d70f05e)

We need to continue the padding with the `esp` address inorder to give the next instruction.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/a0c9cc8f-7f57-40c6-afa2-db74f3ada9a3)

I will be adding `\xcc` inorder to stop the program execution, this will help us identify that we have reached the required point where we can add our own shellcode.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/93919a71-de1d-425c-a769-516be25d327d)

We can see that it gives this error which means our code is working:

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/13cefa06-114f-42ec-abaa-e532a916d04d)

---
Now we need to get the shellcode from [shell-storm](https://shell-storm.org/shellcode/index.html). I will be using [this](https://shell-storm.org/shellcode/files/shellcode-811.html) shellcode

I added it to my script.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/d5f4c85f-0a0a-4028-9dc7-e12dde9b9c11)

Having done that we are ready to run the shell. We will be using `cat` command for this purpose because running it directly causes error.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/2b4b0da0-c6bb-48e3-bfee-1ec6f0e0b0c8)

We thus get the shell and challenge si completed.
