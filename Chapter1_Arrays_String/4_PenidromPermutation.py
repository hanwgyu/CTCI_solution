#1-4
import unittest

#Solution 1 : a-z 알파벳들의 갯수를 셈. 총길이가 홀수일때는 갯수가 홀수인 알파벳이 하나존재가능. 총 길이가 짝수이면 갯수가 모두 짝수여야함. O(len(str)), O(알파벳갯수 26)

def is_odd(integer):
  return True if integer % 2 == 1 else False 

def function(string):
  alpha_cnt = [0 for _ in range(ord('z')-ord('a')+1)]
  str_lower = string.lower()
  str_len = len(string)

  for alpha in str_lower:
    idx = ord(alpha)-ord('a')
    alpha_cnt[idx] += 1

  max_odd_cnt = 0
  if is_odd(str_len):
    max_odd_cnt = 1
  
  for cnt in alpha_cnt:  
    if is_odd(cnt):
      max_odd_cnt -= 1
      if max_odd_cnt < 0:
        return False 

  return True

class Test(unittest.TestCase):
    data = [('TactCoa', True), ('sbdavw', False),('dbfabaf', True), ('abababababab', True)]

    def test_function(self):
        # true check
        for data in self.data:
            res = function(data[0])
            self.assertEqual(res, data[1])


if __name__ == "__main__":
    unittest.main()