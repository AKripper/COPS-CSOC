When we open the `data.txt` file, we see a hexdump. We see that the first 2 bytes of the file are 1f, 8b. This got me into some research where i learnt that files compressed in different methods have different magic numbers.

For this challenge I learnt that the magic number of some compressions are as follows:
1. *gzip* - 1f8b
2. *bunzip2 - 425a
And thats all there is to this challenge.
