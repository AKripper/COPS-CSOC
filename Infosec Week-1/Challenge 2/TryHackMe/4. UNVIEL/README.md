## Background
It seems the cybercriminal is aware that we are on to them. As we were investigating into their Github account we observed indicators that the account owner had already begun editing and deleting information in order to throw us off their trail. It is likely that they were removing this information because it contained some sort of data that would add to our investigation. Perhaps there is a way to retrieve the original information that they provided? 

## Questions
1. What cryptocurrency does the attacker own a cryptocurrency wallet for?
2. What is the attacker's cryptocurrency wallet address?
3. What mining pool did the attacker receive payments from on January 23, 2021 UTC?
4. What other cryptocurrency did the attacker exchange with using their cryptocurrency wallet?

## Writeup
While browsing in Aiko Abe's github repositaries I came accross a repositary named 'ETH' that contained some information about the cryptocurrency wallet address of the attcker. The tasks 1 and 2 are thus done.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/7763e5ff-2f00-4057-a13e-d5caa4fcacf6)

The Repositary has 2 commits and the first commit probably contains an accidental leak of the attacker's crypto wallet. It is as follows:

`stratum://0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef.Aiko:pswd@eu1.ethermine.org:4444`

0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef is the wallet address.


Now I used [blockchain.com](https://www.blockchain.com/explorer/addresses/eth/0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef) to extract the transaction details of the attacker.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/be0c4c32-c852-49ea-a91d-61f9e7a87050)

We can see this transaction happening at 24th Jan 2 am IST ie it happened on 23rd Jan 8:30 pm UTC. The Mining pool is Ethermine:
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/1b914a4a-dba2-4677-b820-e7e6805f03e7)

This is the token portfolio of the account.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/75a947e1-d727-46b0-a7ef-265275d39e18)

## Answers
1. Ethereum
2. 0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef
3. Ethermine
4. Tether
