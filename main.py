### Check for win and print
def check_top(board):
  # Check to see if the top row is solid
  if board[0][0] == board[0][1] == board[0][2]:
    return board[0][0]
  return 0

def check_diag(board):
  # Check to see if the top-let to bottom-right diag is solid
  if board[0][0] == board[1][1] == board[2][2]:
    return board[0][0]
  return 0

def rotate_90(board):
  # Better way to do this?
  new_board = [[0,0,0],[0,0,0],[0,0,0]]
  new_board[1][1] = board[1][1]  # middle space doesn't rotate

  new_board[0][0] = board[0][2]
  new_board[0][1] = board[1][2]
  new_board[0][2] = board[2][2]
  new_board[1][0] = board[0][1]
  new_board[1][2] = board[2][1]
  new_board[2][0] = board[0][0]
  new_board[2][1] = board[1][0]
  new_board[2][2] = board[2][0]
  return new_board

def get_winner(board):
  check_board = board # Don't rotate the canonical board
  # Return 0 if no winner, 1 if x, 2 if o, 3 if draw
  for i in 1,2,3,4:
    win = check_top(check_board)
    if win:
        print_board(board)
        return win
    if i is 1 or 2:
      # Only need to check the diagonals twice
      win = check_diag(check_board)
      if win:
        print_board(board)
        return win
    if i is 1 or 2 or 3:
      # Only need to rotate thrice
      check_board = rotate_90(check_board)

  # Check for draw
  draw = 1
  for row in board:
    if 0 in row:
      draw = 0
  if draw:
    print_board(board)
    return 3

  # No winner
  return 0

def print_winner(winner):
  if winner == 1:
      print "Winner: X"
  if winner == 2:
      print "Winner: O"
  if winner == 3:
      print "Game is a draw"
### /Check for win and print


### Get input and move
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
### /Get input and move


### Print
def print_board(board):
  for i in board:
    row = ""
    for j in i:
      if j is 0:
        row = row + '_'
      elif j is 1:
        row = row + 'X'
      elif j is 2:
        row = row + 'O'
    print row
### /Print

  
def main():
  board = [[0,0,0],[0,0,0],[0,0,0]]
  x_turn = 1
  while 1:
    print_board(board)
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
