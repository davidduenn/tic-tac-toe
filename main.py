import winning

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

    winner = winning.get_winner(board)
    if winner:
      winning.print_winner(winner)
      return 0
  

main()
