def getPi(string):
  pi = [0 for _ in range(len(string))]

  #PI를 구할때도 DP식으로 전에 구해진 pi를 이용해 계산수를 줄임 (substring이 자기 자신인 방식)
  pivot = 0
  for i in range(1, len(string)):
    while pivot > 0 and string[i] != string[pivot]:
      pivot = pi[pivot-1]

    if string[i] == string[pivot]:
      pi[i] = ++pivot

  return pi


#KMP Algorithm
def isSubstring(main_str, sub_str):
  pi = getPi(main_str)

  pivot = 0
  for i in range(len(main_str)):
    #검사중인 길이가 전체 main_Str길이를 넘어갈경우 더이상 검사안하고 false리턴
    if (len(sub_str)-pivot) + (i-1) > len(main_str):
      return False

    #pivot을 이동. pivot을 이동한후 string match를 검사하고 안맞으면 한번더 pivot이동.
    while pivot > 0 and main_str[i] != sub_str[pivot]:
      pivot = pi[pivot-1]

    if pivot == len(sub_str) - 1:
      return True
    if main_str[i] == sub_str[pivot]:
      pivot += 1

  return False

if __name__ == "__main__":
    print(isSubstring('absbd','bsbd'))
    print(isSubstring('ab','aba'))
    print(isSubstring('aba','aaa'))
    print(isSubstring('absbd','bsd'))
