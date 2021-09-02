# 주의) 바꾸는 순서가 중요함!

# 루프를 만들면 실패?  ㅇㅇ 루프가 없으면 거꾸로 만들면 성공하는데, 루프가 하나라도 생기면 실패한다.
##ex) abc -> bca
## 인줄알았으나 루프가 있어도 abc -> dbc-> bca로 바꾸면 됨.
## key와 value에 모든 문자가 없으면 됨.

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        converted = {} #key: character of str1, val: character of str2
        for i, c in enumerate(str1):
            if c not in converted:
                converted[c] = str2[i]
            else:
                if converted[c] != str2[i]:
                    return False
        return str1 == str2 or len(converted.keys()) != 26 or len(set(converted.values())) != 26
