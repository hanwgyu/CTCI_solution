#1-3
import unittest

def function(string, length):
  idx = len(string) - 1
  for i in reversed(range(length)):
    if string[i] == ' ':
      string[idx - 2 : idx + 1] = '%20'
      idx -= 3
    else:
      string[idx]= string[i]
      idx -= 1    

  return string

class Test(unittest.TestCase):
    dataT = [((list('as  bd    '),6), list('as%20%20bd'))]
    dataF = [((list('as bd         '),5), list('as%20%20bd'))]

    def test_function(self):
        # true check
        for data in self.dataT:
            res = function(data[0][0], data[0][1])
            self.assertEqual(res, data[1])
        # false check
        for data in self.dataF:
            res = function(data[0][0], data[0][1])
            self.assertNotEqual(res, data[1])

if __name__ == "__main__":
    unittest.main()