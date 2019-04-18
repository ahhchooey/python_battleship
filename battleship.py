from random import randint

play = True
while play:
  board = []
  for x in range(5):
    board.append(["O"] * 5)

  def print_board(board):
    for row in board:
      print(" ".join(row))

  print('You have 5 turns to hit my battleship.')
  print_board(board)

  def random_row(board):
    return randint(0, len(board) - 1)

  def random_col(board):
    return randint(0, len(board[0]) - 1)

  ship_row = random_row(board)
  ship_col = random_col(board)
  #print(ship_row, ship_col)

  turn = 0
  win = 0
  while turn < 5:
    print("Turn", turn + 1)
    guess_row = -1
    guess_col = -1
    try:
      guess_row = int(input("Guess Row: "))-1
      guess_col = int(input("Guess Col: "))-1
    except:
      print('That is not a valid input.')
    if guess_row == ship_row and guess_col == ship_col:
      print("Congratulations! You sunk my battleship!")
      board[guess_row][guess_col] = "H"
      print_board(board)
      win = 1
      turn = 5
      break
    else:
      if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print("That is not in the ocean. Please aim in the ocean. (Range 1-5)")
      elif(board[guess_row][guess_col] == "X"):
        print("You guessed that one already.")
      else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        turn +=1
      print_board(board)
  if turn == 5:
    if win == 0:
      print("Game Over. You lose.")
    again = input('Would you like to play again? (y/n) ')
    retry = 0
    while retry == 0:
      if again != 'y' and again != 'n':
        again = input('Invalid response. Please enter y or n. ')
      elif again == 'y':
        retry = 1
      elif again == 'n':
        retry = 1
        play = False
