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
