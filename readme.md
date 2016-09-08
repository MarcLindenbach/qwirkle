# Qwirkle
[Qwirkle](https://boardgamegeek.com/boardgame/25669/qwirkle) is a board game that involves
creating sets of shapes and colours. This program allows for a game of qwirkle to be played
against multiple bots & human plays. The current bots use a greedy algorithm to decide which
play to best use.
Here is the result of 4 greedy bots playing against each other:

![example](http://lindenbach.ca/media/qwirkle.png)
## To Run
Use `python play.py --players` to play followed by any number of players, the current player
types supported are:
 - human
 - greedy_body -- will always play the highest scoring combo
 - single_greedy_bot -- will only play one tile at a time, but will always play the highest scoring tile
 
For instance, to watch the two greedy bots play against each other:
`python play.py --players greedy_bot greedy_bot` and to play against a single_greedy_bot:
`python play.py --players human single_greedy_bot`
