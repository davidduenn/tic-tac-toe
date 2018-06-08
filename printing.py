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
