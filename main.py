import redis

from winning import get_winner, print_winner
from helpers import get_input, valid_move, make_move
from printing import print_board
from machine_players import generate_simple_move, generate_complex_move


player_type = 3
  # 0: human, 1: simple machinge, 2: difficult machine
  

def main():
  board = [[0,0,0],[0,0,0],[0,0,0]]
  x_turn = 1
  while 1:
    print_board(board)
    if player_type and not x_turn:
      # machine player will play as O
      if player_type==2:
        [x,y] = generate_simple_move(board)
      if player_type==3:
        [x,y] = generate_complex_move(board)
    else:
      [x,y] = get_input(x_turn)
      while not valid_move(board, x, y):
        [x,y] = get_input(x_turn)
    if x_turn:
      make_move(board, x, y, 1)
      x_turn=0
    else:
      make_move(board, x, y, 2)
      x_turn=1

    winner = get_winner(board)
    if winner:
      print_winner(winner)
      return 0

main()
