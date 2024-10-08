import random
import os
import time

class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def get_around(self):
    return [
      { "x": self.x - 1, "y": self.y - 1 },
      { "x": self.x, "y": self.y - 1 },
      { "x": self.x + 1, "y": self.y - 1 },
      { "x": self.x - 1, "y": self.y },
      { "x": self.x + 1, "y": self.y },
      { "x": self.x - 1, "y": self.y + 1 },
      { "x": self.x, "y": self.y + 1 },
      { "x": self.x + 1, "y": self.y + 1 },
    ]
  def to_string(self):
    return "{}_{}".format(self.x,self.y)

class LifeCell:
  def __init__(self, x, y, alive):
    self.x = x
    self.y = y
    self.alive = alive

class LifeBoard:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.cells = {}
    for x in range(width):
      for y in range(height):
        self.cells[Point(x,y).to_string()] = LifeCell(x, y, random.randint(0,1) == 1)

  def get_around_state(self,x,y):
    lives = 0
    for point in Point(x,y).get_around():
      xy = Point(point["x"], point["y"]).to_string()
      try:
        cell = self.cells[xy]
      except:
        cell = None
      if cell is not None and cell.alive:
        lives += 1
    return lives

  @staticmethod
  def get_next_state(current_alive_state, score):
    return score == 3 or score == 2 and current_alive_state

  def go_to_next_state(self):
    changed = False
    next_cells = {}
    for x in range(self.width):
      for y in range(self.height):
        cell = self.cells[Point(x,y).to_string()]
        lives = self.get_around_state(x,y)
        next_cell_alive = LifeBoard.get_next_state(cell.alive, lives)
        next_cells[Point(x,y).to_string()] = LifeCell(x,y,next_cell_alive)
        changed = changed or cell.alive != next_cell_alive
    self.cells = next_cells
    return changed

  def print_state(self):
    for y in range(self.height):
      for x in range(self.width):
        cell = self.cells["{}_{}".format(x,y)]
        state = " "
        if cell.alive:
          state = "*"
        print(state, end=" ")
      print()

if __name__ == "__main__":
  board = LifeBoard(20,10)
  while True:
    os.system("clear")
    board.print_state();
    changed = board.go_to_next_state()
    if changed == False:
      break
    time.sleep(0.3)

