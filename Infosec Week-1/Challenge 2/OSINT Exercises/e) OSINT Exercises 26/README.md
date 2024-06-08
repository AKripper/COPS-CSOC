## Task briefing
The image below shows the contents of a [zip file](osintexercise026.zip). Inside you will find a 31-second video recorded during a train ride, and four photos of undisclosed locations. They were all taken by the same individual in February 2024. Despite having no useful metadata, they still contain enough information to track down this person’s movements.

Your task is to determine:


a) At which train stations did the person board and alight?

### Bonus Challenges

- Identify the mode of transportation in each image.
- Determine the type of train they rode.
- Estimate the speed at which the train was travelling when the footage was recorded.
- Calculate approximately how far did the person travel overall.

## Writeup 
The zip file contains the following pics and videos. I arranged them in the order they were taken as we must assume that the person was travelling and was taking pictures along his way.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/f400a147-f0eb-4547-be8b-f3acb55d1eb1)

1. The First image is from the *Chorsu Bazaar* in Tashkent, Uzbekistan.
2. The Second image is form *Anhor Lokomotiv*, which is less than 5 km from *Chorsu Bazaar*.
3. Now for the third image, searching on google search does not result in anything. After looking at the image for some time I noticed a shop named 'RENT A CAR' at the bottom left of the image.
   ![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/114a4ffd-de7c-455b-a41f-0aa33491057a)

   I used this to search around the map and found an exact match i.e, 'ORIENT RENT A CAR'.
   ![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/0955dac1-9958-4c40-9ba5-174b937345d9)
   ![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/ea2369b9-387e-4f90-85dd-0463cc71953b)

   We are thus at the exact location which is *Afrosiab Street*.
4. Now for the video, we can see the person is in a train that is moving in a somewhat out of city area. I tried finding it on maps by looking at nearby stations but wasn't able to    achieve much. So I looked up the official writeup of the question. They figured out that the time the person was traveling at was around afternoon and through the shadows they
   concluded that the person was travelling either west to east or east to west. Now looking at the [railway maps](https://railway.uz/upload/iblock/b73/b736cc5a0ba5a820a2e91a6941a9b52d.jpg) of Uzbekistan we can narrow down to this one stretch.

   ![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/4ba595ec-57b4-4ace-b574-3c53c4839c62)

   We can see the stretch is 1.19 km long so the speed of the train is approximately is 140 kmph. This is the *Jizzakh District* of Uzbekistan.
5. We can see that the train taken by the person goes till Samarkand. Now all we have to do is look at the bridges in Samarkand. We find one bridge that matches the one we were        finding.
   
   ![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/eff53381-edb0-4084-baa0-5ebf20633e62)

   It is *Shah-i-Zinda St*, Samrakand, Uzbekistan.


   
