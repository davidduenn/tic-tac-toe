def get_input(x_turn):
  if x_turn:
    print("Player X,")
  else:
    print("Player O,")
  next_move = input('Give your next move, x coordinate: ')
  try:
    x = int(next_move)
  except ValueError:
    print "inccorect value"
  next_move = input('Give your next move, y coordinate: ')
  try:
    y = int(next_move)
  except ValueError:
    print "inccorect value"
  return [x,y]

def valid_move(board, x, y):
  if board[x][y] is not 0:
    print "Invalid move, try again"
    return 0
  return 1

def make_move(board, x, y, char):
  board[x][y] = char

def clean_board_for_db(board):
  my_str=''
  for i in board:
    for j in i:
      my_str = my_str + str(j)
  return my_str

def clean_move_for_db(move):
  # move: [board, player, x, y]
  board = clean_board_for_db(move[0])
  return board + str(move[1]) + str(move[2]) + str(move[3])
