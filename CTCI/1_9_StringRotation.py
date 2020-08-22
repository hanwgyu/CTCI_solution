# 1-9 StringRotation
import unittest


def isSubstring(string, sub_string):
    return string.find(sub_string) != -1


# Solution:s1을 두번 연결한 문장에 s2가 속하면 rotation.
def function(s1, s2):
    if len(s1) != len(s2):
        return False
    return isSubstring(s1 + s1, s2)


class Test(unittest.TestCase):
    data = [
        ("waterbottle", "erbottlewat", True),
        ("hi", "ih", True),
        ("hihahi", "ihaihh", False),
    ]

    def test_function(self):
        for data in self.data:
            res = function(data[0], data[1])
            self.assertEqual(res, data[2])


if __name__ == "__main__":
    unittest.main()
