import unittest
from app import Point
from app import LifeCell
from app import LifeBoard

class TestPoint(unittest.TestCase):
  def test_get_around(self):
    point = Point(0,0)
    around_points = point.get_around()
    self.assertEqual(around_points, [
      { "x": -1, "y": -1 },
      { "x": 0, "y": -1 },
      { "x": 1, "y": -1 },
      { "x": -1, "y": 0 },
      { "x": 1, "y": 0 },
      { "x": -1, "y": 1 },
      { "x": 0, "y": 1 },
      { "x": 1, "y": 1 },
    ])
  def test_to_string(self):
    point = Point(1,2)
    self.assertEqual(point.to_string(), "1_2")

class TestLifeBoard(unittest.TestCase):
  def test_get_around_state(self):
    board = LifeBoard(4,4)
    for x in range(board.width):
      for y in range(board.height):
        board.cells[Point(x,y).to_string()] = LifeCell(x,y,True)

    self.assertEqual(board.get_around_state(0,0), 3)
    self.assertEqual(board.get_around_state(1,0), 5)
    self.assertEqual(board.get_around_state(2,0), 5)
    self.assertEqual(board.get_around_state(3,0), 3)
    self.assertEqual(board.get_around_state(0,1), 5)
    self.assertEqual(board.get_around_state(1,1), 8)
    self.assertEqual(board.get_around_state(2,1), 8)
    self.assertEqual(board.get_around_state(3,1), 5)
    self.assertEqual(board.get_around_state(0,2), 5)
    self.assertEqual(board.get_around_state(1,2), 8)
    self.assertEqual(board.get_around_state(2,2), 8)
    self.assertEqual(board.get_around_state(3,2), 5)
    self.assertEqual(board.get_around_state(0,3), 3)
    self.assertEqual(board.get_around_state(1,3), 5)
    self.assertEqual(board.get_around_state(2,3), 5)
    self.assertEqual(board.get_around_state(3,3), 3)

    for x in range(board.width):
      for y in range(board.height):
        board.cells[Point(x,y).to_string()] = LifeCell(x,y,False)

    self.assertEqual(board.get_around_state(0,0), 0)
    self.assertEqual(board.get_around_state(1,0), 0)
    self.assertEqual(board.get_around_state(2,0), 0)
    self.assertEqual(board.get_around_state(3,0), 0)
    self.assertEqual(board.get_around_state(0,1), 0)
    self.assertEqual(board.get_around_state(1,1), 0)
    self.assertEqual(board.get_around_state(2,1), 0)
    self.assertEqual(board.get_around_state(3,1), 0)
    self.assertEqual(board.get_around_state(0,2), 0)
    self.assertEqual(board.get_around_state(1,2), 0)
    self.assertEqual(board.get_around_state(2,2), 0)
    self.assertEqual(board.get_around_state(3,2), 0)
    self.assertEqual(board.get_around_state(0,3), 0)
    self.assertEqual(board.get_around_state(1,3), 0)
    self.assertEqual(board.get_around_state(2,3), 0)
    self.assertEqual(board.get_around_state(3,3), 0)

    expected = 0
    for x in [0,1,2]:
      for y in [0,1,2]:
        board.cells[Point(x,y).to_string()] = LifeCell(x,y,True)
        if x != 1 or y != 1:
          expected += 1
        self.assertEqual(board.get_around_state(1,1), expected)

  def test_get_next_state(self):
    self.assertEqual(LifeBoard.get_next_state(True, 0), False)
    self.assertEqual(LifeBoard.get_next_state(True, 1), False)
    self.assertEqual(LifeBoard.get_next_state(True, 2), True)
    self.assertEqual(LifeBoard.get_next_state(True, 3), True)
    self.assertEqual(LifeBoard.get_next_state(True, 4), False)
    self.assertEqual(LifeBoard.get_next_state(True, 5), False)
    self.assertEqual(LifeBoard.get_next_state(True, 6), False)
    self.assertEqual(LifeBoard.get_next_state(True, 7), False)
    self.assertEqual(LifeBoard.get_next_state(True, 8), False)

    self.assertEqual(LifeBoard.get_next_state(False, 0), False)
    self.assertEqual(LifeBoard.get_next_state(False, 1), False)
    self.assertEqual(LifeBoard.get_next_state(False, 2), False)
    self.assertEqual(LifeBoard.get_next_state(False, 3), True)
    self.assertEqual(LifeBoard.get_next_state(False, 4), False)
    self.assertEqual(LifeBoard.get_next_state(False, 5), False)
    self.assertEqual(LifeBoard.get_next_state(False, 6), False)
    self.assertEqual(LifeBoard.get_next_state(False, 7), False)
    self.assertEqual(LifeBoard.get_next_state(False, 8), False)

if __name__ == "__main__":
  unittest.main()

