
# Raft

## Introduction
This is my analysis for *Raft*. I started by using linux but very soon I understood that wont be of any help to me here. So I looked up on the internet for ways to view and edit save files of games. This is my writeup for the same.

## Writeup

I started a new world and as you can see I have nothing much in this world and my thirst level is going down very fast...Now I save it as it is. This is my game save. 

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/61b928e3-7cd2-4eb3-ada8-a7233b022178)

I located the game save in the hidden AppData folder. To get here open you search bar and type %AppData%. This will direct you to a hidden folder. This is where all the games store their save files. Raft's save file is in the following location `\AppData\LocalLow\Raft\Raft\SavedGames`. Now from some research I found out this amazing tool called [Save Editor](https://www.saveeditonline.com). So I uploaded my save file here and this is what I got.

![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/185db93d-a97d-44f9-a553-55f04cd4eeed)

This is part of the save file...it shows all the player charecteristics like inventory items and their amount and even thirst and hunger.

I will start by increasing my hunger and thirst to 100. 
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/75e00833-9940-40c3-8e56-e693689eba6a)

Now saving this file and going into the game my thirst and hunger has indeed increased to 100.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/cadc562f-7a32-4f44-97d1-56a188aff2ef)

I did the same for inventory items and game it the max number that is 10. And it worked as well.
![image](https://github.com/AKripper/COPS-CSOC/assets/167231621/d402b7bf-db59-453a-9d00-3f41b0caaff7)

## Results
- I was able to locate the save file of the game.
- I was able to read the save file.
- I was able to modify the save file.
- The modifications caused in game changes as well.
- [Here](mygame.rgd) is my final save file.


