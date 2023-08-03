# Battleship



This is a Battleship game for one player. This is a simplified version of the classic Battleship game. The player has to guess where on a board an number of ships are hidden before they run out of turns. If they hit all the ships they win the game.

![battleship_responsive](https://github.com/ElisabethKAndersson/portfolio_project_3/assets/131455964/72314d0b-c4f3-47c4-a88a-e577f5419aa0)


[VIsit the project page on Github here.](https://github.com/ElisabethKAndersson/portfolio_project_3.git) 

[VIsit the game page on Heroku here.](https://battleship-one-player-99f1f4a0fd93.herokuapp.com/) 


---
## User Experience

The idea behind the game is for the new player to get informed, step by step what to do, without getting too much information. The game adds a personalized feel by letting the player add their name in the beginning.
The player can also change the size of the board, adjust the number of ships that they have to hit as well as adjust the number of turns they have. This makes the game more fun for returning players. They can make the game easier to beat if they want more wins, or create a big board with more ships for a greater challange.

___
## Design

The game design is very simple. It contains text and a board made from the sign ¨ to make it look like waves. Every hit is marked by the sign * and each miss is marked by the sign o.

img


### Features

The starts off with an input feature for adding the player name. The player then gets a welcome message. This message only shows once. It doesn't show if the player wants to play again, since it can be annoying to go through a lot of text every time you want to play another round.

The player then gets the option to set the size of the board, number of hidden ships on the board and number of turns.

After that the layout is cleared and the game starts for real. The player is informed of how many ships they have to find and get a visual view of the board. They have to add rows and columns. They then get to see whether they hit or missed the board followed by information on how many hits they have so far, the number of turns left, and an updated version of the board with visual signs of hits and misses. The game then continues until they have either hit all hidden ships or used all their turns.
![Battleship](https://github.com/ElisabethKAndersson/portfolio_project_3/assets/131455964/b3edc1ca-a6d3-4748-96b1-78cb9e0dd32a)


By the end of the game, the player gets the option to start over or quit. If they start over they begin with choosing the size of the board again.

### Accessibility

I have tried to keep the instructions short but clear so that the player can understand what the game is all about without having to read a lot of text.

### Future Features

- An option to have a computer opponent to compete against could be added to the game. 
- There could also be an option with different sizes on the ships.

---

## Technologies Used
The game is made with Python.

Codeanywhere - Has been used for doing the programming.

Github - Has been used for saving and storing the files.

Heroku - Has been used to launch the game.

---

## Testing

- I have run the programme through PEP8 and fixed any problems that showed up there. Current code has no error found.

- I have played the game with different sizes, number of ships and number of turns.

- I have tried all the input functions to check that there are error messages in case of invalid inputs.

- I ran through the game with my mentor when I was quite far into development.


### Bugs

- I wanted to add a play again function. But the function I called made the game only run that function and then stop.
    - I fixed it by adding a start function that contained all the code that I wanted to run when starting over. I could then call on that function if the player chose Y as reply on starting over.

- I had put input validation on a few places in case the player chose a number out of range, but I forgot to add validation in case the player pressed enter or wrote a letter instead of an integer.
    - I fixed that by adding an except ValueError.

- I had a problem that the code wasn't validated again after the error message was placed, so the wrong value god be added.
    - I instead divided some of the inputs into functions that could be called on after error message.

- In one run through I realized that I had more turns than there were possible ship locations.
    - I changed the minimum board size to number 5 instead of 4.

- In PEP8 some lines were too long.
    - I fixed that by dividing some code into two lines instead. 


### Known bugs

No remaining bugs have been detected.

---

## Deployment
The project is deployed through Code institutes mock terminal on Heroku.

### Steps for deployment:
    - Create a new Heroku app on the Heroku page.
    - Set buildbacks to Python and Node JS.
    - Link the Heroku app to Github
    - Find the Battleship repository
    - Deploy the app.


---
## Credits

I looked at a lot of different tutorials on how to make a Battleship game before starting the coding.

https://copyassignment.com/battleship-game-code-in-python/ - I used the code from this tutorial as a base to get me started. I modified it to make it more interactive.

https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/ - I wanted to add some paus between some of the text and got information on how to add delays from this page.

https://replit.com/talk/ask/How-do-I-make-my-text-in-Python-disappear-when-the-user-presses-a-key/43147 - I used information from this page to figure out how to clear old text.

https://bigmonty12.github.io/battleship - I used the board code from this page since I understood it better than other code I had seen.

---

## Acknowledgments

 - Jubril Akolade, my Code Institute mentor
    - Always giving good advice and went through the project with me and found validation errors I had missed.

 - Code institute tutor support  
    - I started off thinking a bit too big for a first python project. I got the advice that it is better to make something simpler that I understand. I changed my project and suddenly learned so much more than I had when feeling overwhelmed by the massive code I was working on.
