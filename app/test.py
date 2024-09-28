import unittest
from app import Point

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

if __name__ == "__main__":
  unittest.main()

