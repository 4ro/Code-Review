import unittest
from codereview import Ship 

class test_codereview(unittest.TestCase):
    def test_is_worth_it(self):
      att = Ship(30,6)
      result = att.is_worth_it()
      self.assertTrue(result)


if __name__ == "__main__":
     unittest.main()
        
