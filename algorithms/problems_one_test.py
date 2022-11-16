
import unittest

import problems_one


# TODO: 
  # deep-learning model that takes in any code and outputs relevant test cases?
    # same thing with documentation as well


class TestStringMethods(unittest.TestCase):

  def test_reverse_trivial(self):
    rv = problems_one.reverse_string_trivial('abcd')
    self.assertEqual(rv, 'dcba')
    rv = problems_one.reverse_string_trivial('')
    self.assertEqual(rv, '')
    rv = problems_one.reverse_string_trivial(-4)
    self.assertEqual(rv, 'Incorrect Type')



if __name__ == '__main__':
    unittest.main()





