## Background
Just as we thought, the cybercriminal is fully aware that we are gathering information about them after their attack. They were even so brazen as to message the OSINT Dojo on Twitter and taunt us for our efforts. The Twitter account which they used appears to use a different username than what we were previously tracking, maybe there is some additional information we can locate to get an idea of where they are heading to next?


We've taken a screenshot of the message sent to us by the attacker, you can view it in your browser [here](https://raw.githubusercontent.com/OsintDojo/public/main/taunt.png).

## Questions
1. What is the attacker's current Twitter handle?
2. What is the URL for the location where the attacker saved their WiFi  SSIDs and passwords?
3. What is the BSSID for the attacker's Home WiFi?

## Writeup
The social media handle of the attacker is given in the image. It is '@AikoAbe3'.I searched it on google and found something.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/8f96b0ed-03d0-4260-be7f-3575aeb5f9e6)

Here clearly the new twiter handle is '@SakuraLoverAiko'.

Going to her twitter page we see she has 9 posts and some of them are very suspicious. 

One of her posts says:
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/b334e2a3-804d-41fa-8da9-bf6767fd1922)

And there is an update for this post
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/a65c4f10-baa2-40f5-a79d-17ba31fa9c9d)

This hints us to go to the dark web and search for deep paste. So I did exactly that. I downloaded the tor browser, learnt some basics for browsing the dark web and managed to find the link for 'deep paste':
`http://deepv2w7p33xa4pwxzwi2ps4j62gfxpyp44ezjbmpttxz3owlsp4ljid.onion`

Now I searched the paste using the md5 hash provided in the [image](![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/a65c4f10-baa2-40f5-a79d-17ba31fa9c9d)
).

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/64822320-4e02-48d5-a62f-7f0020f89bdc)

This was the paste.

Now clearly the SSID for the home wifi is DK1F-G, so we can use [wigle.net](https://wigle.net/mapsearch?maplat=37.49422556604922&maplon=-220.0755481935037&mapzoom=8&n=g2%20%2Fmapsearch) to get the BSSID of the network.

## Answers
1. SakuraLoverAiko
2. http://deepv2w7p33xa4pwxzwi2ps4j62gfxpyp44ezjbmpttxz3owlsp4ljid.onion
3. 
