# TIC TAC TOE GAME
This is a game for player vs player or player vs computer each player get a symbol either "X" or "O" to mark their position on the game board.The game is played on a 9 square grid (3X3).Each player has to try to get 3 of their symbols in a row this can be across, down or diagonally the first to acheive this wins the game .If none get 3 in a row it is a draw.
---
![Mckups](documentation/mockup.png)

Link to App [Tic Tac Toe ](https://tic-tac-toe-pp3-3dc19c748ca1.herokuapp.com/)

# User stories
## As a player 
* I want to play a game that is clear and easy to understand for both young children and adults
* I want an easy to use menu
* I want be able to navigate easily throught options
* I want the option to quit the game 
* I want the option to play again
---
# Features


# Technologies Used
[Am I responsive](https://ui.dev/amiresponsive) to create mock up design

# Languages:
* [Python](https://www.python.org/)
* [JavaScript](https://www.javascript.com/): Code Institute Template
* [HTML](https://html.com/): Code Institute template

# Libraries and Frameworks

## Imported Libraries
* [random](https://docs.python.org/3/library/random.html) For computers turn to choose a random number.
* [os](https://docs.python.org/3/library/os.html) To Clear screen.
* [time](https://docs.python.org/3/library/time.html?highlight=time#module-time) to create a delay in clearing screen and computer answer.
* [colorama](https://pypi.org/project/colorama/) To add color to project.
* [simple_term_menu](https://pypi.org/project/simple-term-menu/) to create options menu.





---
# Flow Chart
![Flowchart](documentation/flowchart.png)
---
# Deployment
This Project was deployed through [HEROKU](https://www.heroku.com/) using these steps:

1. Create a heroku account 
2. Then select New
3. [Select Create new app](documentation/heroku-new.png)
4. Name the App, select region
5. [Select Create app](documentation/name_region.png)
6. [Then select Settings from the menu bar](documentation/setting.png)
7. [From here scroll down to Config Vars](documentation/config.png)
8. [Next add buildpacks for this project python and nodejs was used](documentation/build_pack.png)
9. [Then go to Deploy in menu bar](documentation/deploy.png)
10. [Choose github then choose connect to github](documentation/deploy-method.png)
11. [Now enter repository name in search](documentation/name.png) 
12. [Then click connect](documentation/connect.png)
13. [From here scroll down and pick either automatic Deploy or manual deploy](documentation/update-deploy.png)
14. [The app is now been built](documentation/building.png)
15. [Once this has finished click view to go to app](documentation/deployed_success.png)