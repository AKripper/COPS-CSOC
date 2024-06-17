## Challenge Description
What is the name for the best single-key attack against AES?

## Writeup
The part of the question, "It turns out that there is [an attack](https://en.wikipedia.org/wiki/Biclique_attack) on AES that's better than bruteforce, but only slightly – it lowers the security level of AES-128 down to 126.1 bits, and hasn't been improved on for over 8 years. Given the large "security margin" provided by 128 bits, and the lack of improvements despite extensive study, it's not considered a credible risk to the security of AES. But yes, in a very narrow sense, it "breaks" AES."


The biclique attack is still (as of April 2019) the best publicly known single-key attack on AES

## Flag
crypto{Biclique}
