import redis


def generate_simple_move(board):
  # Run through the lists and return the
  # first discovered blank spot as the move
  for row, x in enumerate(board):
    try:
      column = x.index(0)
    except ValueError:
      continue
    return row,column

def generate_complex_move(board):
  pass
