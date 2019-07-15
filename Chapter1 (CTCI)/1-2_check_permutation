#1-2
import unittest

def function(str_a, str_b):
  if len(str_a) != len(str_b):
    return False

  str_cnt = [0 for _ in range(128)]
  
  for char in str_a:
    idx = ord(char)
    str_cnt[idx] += 1
  
  for char in str_b:
    idx = ord(char)
    str_cnt[idx] -= 1
    if str_cnt[idx] < 0:
      return False

  return True

class Test(unittest.TestCase):
    dataT = [("asbd","basd"), ("abcdefg", "gabdcef")]
    dataF = [("asbd","bas"), ("abcdefg", "gabcef")]

    def test_function(self):
        # true check
        for data in self.dataT:
            actual = function(data[0], data[1])
            self.assertTrue(actual)
        # false check
        for data in self.dataF:
            actual = function(data[0], data[1])
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()