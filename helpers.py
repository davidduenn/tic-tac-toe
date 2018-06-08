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
