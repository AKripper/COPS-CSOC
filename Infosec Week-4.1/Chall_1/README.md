## Description
The challenge requires us to find the password.
Running the challenge file in linux prompts, "What is the password?" andd then according to the input tells if its 'correct' or 'incorrect'.
We need to Reverse Engineer the file to check how to code works and what the password could be.

## Writeup
I opened the file on Ghidra and directly went to the `main` function.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/5376de88-af68-45c2-b8c7-29cb0631e187)

The code outputs, "What is the password", and then stores whatever is the input in the string `local_118`. This string is then passed to the `check` function and the returned value of that function is stored in the variable `iVar1`, at the end this value decides whether the password is correct or not.

Now, looking at the `check` function.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/b9f1c4cd-e672-45be-a812-a0654e47c2ae)

The input string is stored in `param_1` and the length of the string is stored in `sVar1`. Now the conditional if statement on the password determines if the password is correct or not. According to the statement:
- Length of the string should be `10`.
- 1st charecter of the string ,i.e, `param_1[0]` should be `1`.
- `param_1[4]` should be `9`.

With these conditions we will have many passwords of the form ` 1 _ _ _ 9 _ _ _ _ _ `. So any of the password of this form will work.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/f4d9d2fb-a979-4a6f-b1f5-8131c523d4ba)

## Password
1000900000
