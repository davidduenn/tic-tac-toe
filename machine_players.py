import redis
import json
import math, random, time

from helpers import clean_board_for_db

random.seed(time.time())


def generate_simple_move(board):
  # Run through the lists and return the
  # first discovered blank spot as the move
  for row, x in enumerate(board):
    try:
      column = x.index(0)
    except ValueError:
      continue
    return row,column

def generate_random_move(board):
  row = int(math.floor(random.random()*3)) # give a random int (0-3)
  column = int(math.floor(random.random()*3)) # give a random int (0-3)
  return row,column

def generate_complex_move(board, r):
  best_board=[]
  best_score=0
  for board in r.keys(str(clean_board_for_db(board)+'*')):
    if int(r.get(board)) > best_score:
      best_score = r.get(board)
      best_board = board
  if best_board and best_score>0:
    print "--- complex plays from db"
    return int(best_board[10]), int(best_board[11])
  else:
    # There's no good move from the db so play a random move
    print "--- complex plays random"
    return generate_random_move(board)
