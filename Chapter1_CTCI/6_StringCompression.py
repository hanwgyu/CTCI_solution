#1-6 String Compression
import unittest

def function(string_a):
  update_cnt = 0
  res = ''

  length = len(string_a)
  for i in range(length):
    update_cnt += 1
    #Update result
    if (i == length - 1) or string_a[i] != string_a[i+1]:
      res += string_a[i] + str(update_cnt)
      update_cnt = 0


  if length < len(res):
    return string_a
  return res

class Test(unittest.TestCase):
    data = [
      ('aabcccccaaa', 'a2b1c5a3', True),
      ('abcd', 'abcd', True),
      ('abbscd', 'a1b2s1c1d1', False),
      ('abbb', 'a1b3', True)
    ]

    def test_function(self):
        for data in self.data:
            res = function(data[0])
            self.assertEqual(res == data[1], data[2])


if __name__ == "__main__":
    unittest.main()