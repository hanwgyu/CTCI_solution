# 1-5 One Away
import unittest

# Solution : 대문자 구분해서 52개의 배열에 갯수 입력하고, 두 벡터의 차이 벡터의 총합이 -1~1이고 제곱합이 2이하. O(n)
def function(string_a, string_b):
    lower_cnt = [0 for _ in range(26)]
    upper_cnt = [0 for _ in range(26)]
    for alpha in string_a:
        if alpha.islower():
            idx = ord(alpha) - ord("a")
            lower_cnt[idx] += 1
        else:
            idx = ord(alpha) - ord("A")
            upper_cnt[idx] += 1

    for alpha in string_b:
        if alpha.islower():
            idx = ord(alpha) - ord("a")
            lower_cnt[idx] -= 1
        else:
            idx = ord(alpha) - ord("A")
            upper_cnt[idx] -= 1

    square_sum = 0
    sum = 0
    for cnt in lower_cnt + upper_cnt:
        square_sum += pow(cnt, 2)
        sum += cnt

    if sum <= 1 and -1 <= sum and square_sum <= 2:
        return True
    return False


class Test(unittest.TestCase):
    data = [
        ("pale", "ple", True),
        ("pales", "pale", True),
        ("pale", "bale", True),
        ("paleabc", "pleabc", True),
        ("pale", "ble", False),
        ("a", "b", True),
        ("", "d", True),
        ("d", "de", True),
        ("pale", "pale", True),
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pale", "bale", True),
        ("pale", "bake", False),
        ("pale", "pse", False),
        ("ples", "pales", True),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pale", "pkle", True),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
    ]

    def test_function(self):
        # true check
        for data in self.data:
            res = function(data[0], data[1])
            self.assertEqual(res, data[2])


if __name__ == "__main__":
    unittest.main()
