# Qwirkle Solver
[Qwirkle](https://boardgamegeek.com/boardgame/25669/qwirkle) is a board game that involves
creating sets of shapes and colours. Qwirkle Solver uses a greedy algorithm to decide which
play to best use.
Here is the result of 4 greedy bots playing against each other:

![example](http://lindenbach.ca/media/qwirkle.png)
## To Run
Use `python play.py --players` to play followed by any number of players, the current player
types supported are:
 - human
 - greedy_body
 - single_greedy_bot
 
For instance, to watch the two greedy bots play against each other:
`python play.py --players greedy_bot greedy_bot` and to play against a single_greedy_bot:
`python play.py --players human single_greedy_bot`