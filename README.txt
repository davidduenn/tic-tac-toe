A tic-tac-toe game in Python. The two players can be any of:
* human
* simple computer
* random computer
* complex computer

Moves are stored in a Redis database and are rated based on whether
they lead to wins or losses. The complex computer player checks the
database for a good move and plays it. If there's no good move, it
plays a random move.
