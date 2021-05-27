# Python-Tkinter-Game-GUI
Intermediate Programming a small game and GUI using Tkinter and Python, 86%

-On pressing the start button, the code will present a small figure (rectangle/square/circle/oval, etc.), drawn in a canvas with a certain colour.
-The user must press this figure. The figure disappears after the user clicks on it.-If the user presses within two seconds the figure, it receives 1 point. 
-If the user receives 1 point, a label must update by one to reflect this change in the score.
-The figure will be redrawn at a new location on the canvas for the user to play again. 
-The same steps will be repeated until the end of the game. 


For the extra functionality that I had implemented in my assignment, I added another label located at the frame named Lives.
This signifies the chances the user has left to make a mistake.
When the start button is first pressed, the user starts with 3 lives, and if the user fails to click the figure displayed within the time frame their lives will be reduced by one.
However if the user fails to click the target object on the first time within the time frame, the game dispalys its game over page.
If the user's lives drops to 0 then a game over screen is displayed showing the user's current score and the amount of time they required.
The next thing I added was when the user clicked the start button instead of seeing a single figure drawn, two were displayed (1 square and 1 circle)
The score would increase by one if the user clicked the square within the time frame.
However, if the user clicked the circle the user receives a penalty which reduces their lives by 1 and score by 2 Ie the circle was added to distract the user. 
When any figure is clicked the objects are redrawn at a different point in the canvas.
If the user were to start the game and click the circle immediately, only the lives are reduced as the user's score cannot drop below 0.
In order to make the game more difficult, I implemented a way where if the score was greater than 5 the time to click would get smaller (to speed up the time to click) the code will randomly select a time of either 2, 1.5, or 1  seconds which is stored as the 'target' variable. Furthermore, if the score was greater than 15 target will be reduced to either 1 or 0.5 seconds. This is continued to when the score reaches 20, target will be set to 0.5.
I added some phrases which will be displayed to the user depending on their performance in the game, If their lives get reduced the game will randomly select a phrase that taunts the user to speed up. If the user's score is increased the same occurs however the phrase will be encouraging and praising the user. Another simple addition was when the objects are redrawn a new colour will be randomly selected.
Finally, if the user's score reaches over 15 they enter level 2 where 'Dark Mode' is activated.
The canvas' background is switched to black and the figure is only drawn in the white colour, and the time to click the object is reduced to 1 or 0.5 seconds.
If the user's lives have been reduced before entering level 2 their lives are restored to 3 to reward them. The second object (decoy) is not drawn in level 2 to allow the user to click as fast as they can on the target figure.

Thank you.
