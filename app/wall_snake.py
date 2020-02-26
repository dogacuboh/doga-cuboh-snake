# wall_snake.py
# This snake will only avoid walls at itself
# It isn't aware of it's health or able to actively search for food
#
# The valid moves are 'up' 'down' 'left' 'right'

import random
from app.constants import UNOCCUPIED, OCCUPIED, FOOD,HEAD, TAIL
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from app.random_snake import random_move


# wall_move()
# This function picks a move that won't result in death
#
# @parma state  - The JSON file of the game
# @parma matrix - The matrix of the current board state
# @return move  - The move to do
def wall_move(state, matrix):

    height = state["board"]["height"]
    head = state['you']["body"][0]
    head_x = head["x"]
    head_y = head["y"]
    valid_moves = []

    # Check up
    if head_y - 1 > -1 and matrix[head_y - 1][head_x] == UNOCCUPIED and (head_y - 2 == -2 or matrix[head_y - 2][head_x] != HEAD) and (head_x - 1 == -1 or matrix[head_y - 1][head_x - 1] != HEAD) and (head_x + 1 == height or matrix[head_y - 1][head_x + 1] != HEAD) :
        valid_moves.append('up')

    # Check down
    if head_y + 1 < (height) and matrix[head_y + 1][head_x] == UNOCCUPIED and (head_y + 2 == (height) or matrix[head_y + 2][head_x] != HEAD) and (head_x + 1 == (height) or matrix[head_y + 1][head_x + 1] != HEAD) and (head_x - 1 == -1 or matrix[head_y + 1][head_x - 1] != HEAD):
        valid_moves.append('down')

    # Check Left
    if head_x - 1 > -1 and matrix[head_y][head_x - 1] == UNOCCUPIED and (head_x - 2 == -2 or matrix[head_y][head_x - 2] != HEAD) and (head_y + 1 == height or matrix[head_y + 1][head_x - 1] != HEAD) and (head_y - 1 == -1 or matrix[head_y - 1][head_x - 1] != HEAD) :
        valid_moves.append('left')

    # Check right
    if head_x + 1 < (height) and matrix[head_y][head_x + 1] == UNOCCUPIED and (head_x + 2 == (height) or matrix[head_y][head_x + 2] != HEAD) and (head_y + 1 == (height) or matrix[head_y + 1][head_x + 1] != HEAD) and (head_y - 1 == -1 or matrix[head_y - 1][head_x + 1] != HEAD) :
        valid_moves.append('right')

    if len(valid_moves) == 0:
          if head_y - 1 > -1 and matrix[head_y - 1][head_x] == UNOCCUPIED:
              valid_moves.append('up')

          # Check down
          if head_y + 1 < (height) and matrix[head_y + 1][head_x] == UNOCCUPIED:
              valid_moves.append('down')

          # Check Left
          if head_x - 1 > -1 and matrix[head_y][head_x - 1] == UNOCCUPIED:
              valid_moves.append('left')

          # Check right
          if head_x + 1 < (height) and matrix[head_y][head_x + 1] == UNOCCUPIED:
              valid_moves.append('right')

          # If theres a valid move
    if len(valid_moves) > 0:
        heighest = 0
        validMove = None
        for valid in valid_moves:
          maxLenght = getMaxPath(height,head_x,head_y,matrix,valid)
          if maxLenght > heighest:
            heighest = maxLenght
            validMove = valid

        return validMove
              #random_int = random.randint(0, len(valid_moves)-1)
              #return valid_moves[random_int]
    # if theres no move
    else:
        return random_move()

def getMaxPath(height,head_x,head_y,matrix,move):
  
  count = 1
  if move == 'up':
    while head_y - count > -1 and matrix[head_y - count][head_x] == UNOCCUPIED:
      count += 1
  elif move == 'down':
    while head_y + count < (height) and matrix[head_y + count][head_x] == UNOCCUPIED:
      count += 1
  elif move == 'left':
    while head_x - count > -1 and matrix[head_y][head_x - count] == UNOCCUPIED:
      count += 1
  elif move == 'right':
    while head_x + count < (height) and matrix[head_y][head_x + count] == UNOCCUPIED:
      count += 1
  return count
