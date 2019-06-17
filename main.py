import redis

from copy import deepcopy # for copying the board to *_moves

from winning import get_winner, print_winner
from helpers import get_input, valid_move, make_move
from printing import print_board
from machine_players import generate_simple_move, generate_random_move, generate_complex_move


def main():
  # Initialize
  x_player_type = 3 # 0: human, 1: simple machine, 2: random machine, 3: difficult machine
  o_player_type = 2 # 0: human, 1: simple machine, 2: random machine, 3: difficult machine
  board = [[0,0,0],[0,0,0],[0,0,0]]
  x_moves=[]
  o_moves=[]
  r = redis.Redis(host="ttt_redis")
  x_turn = 1 # X goes first

  from helpers import clean_move_for_db

  # Game loop
  while 1:
    print_board(board)
    if x_turn:
      if x_player_type==0:
        [x,y] = get_input(x_turn)
        while not valid_move(board, x, y):
          [x,y] = get_input(x_turn)
      if x_player_type==1:
        [x,y] = generate_simple_move(board)
        while not valid_move(board, x, y):
          [x,y] = generate_simple_move(board)
      if x_player_type==2:
        [x,y] = generate_random_move(board)
        while not valid_move(board, x, y):
          [x,y] = generate_random_move(board)
      if x_player_type==3:
        [x,y] = generate_complex_move(board, r)
        while not valid_move(board, x, y):
          [x,y] = generate_complex_move(board, r)
      x_moves.append([deepcopy(board), 1, x, y])
      make_move(board, x, y, 1)
      x_turn=0
    else: # O's turn
      if o_player_type==0:
        [x,y] = get_input(x_turn)
        while not valid_move(board, x, y):
          [x,y] = get_input(x_turn)
      if o_player_type==1:
        [x,y] = generate_simple_move(board)
        while not valid_move(board, x, y):
          [x,y] = generate_simple_move(board)
      if o_player_type==2:
        [x,y] = generate_random_move(board)
        while not valid_move(board, x, y):
          [x,y] = generate_random_move(board)
      if o_player_type==3:
        [x,y] = generate_complex_move(board, r)
        while not valid_move(board, x, y):
          [x,y] = generate_complex_move(board, r)
      o_moves.append([deepcopy(board), 2, x, y])
      make_move(board, x, y, 2)
      x_turn=1

    # If winner: print, record moves, exit
    winner = get_winner(board)
    if winner:
      print_winner(winner)
      if winner is 1:
        for move in x_moves:
          r.incr(clean_move_for_db(move))
        for move in o_moves:
          r.decr(clean_move_for_db(move))
      else:
        for move in x_moves:
          r.decr(clean_move_for_db(move))
        for move in o_moves:
          r.incr(clean_move_for_db(move))
      return 0

main()
