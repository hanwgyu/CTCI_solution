#Time Complexity : O(N), Space Complexity : O(N)
class Solution(object):
    #Time Complexity : O(N), Space Complexity : O(N)
    def decodeString(self, s):
    # Solution : 아래와 동일한데, String 대신 Array사용하여 복사 비용을 줄임.
    
        copy_stack, word_stack = [], []
        copy, word = 0, []
        for char in s:
            if char.isdigit():
                copy = copy * 10 + int(char)
            elif char == '[':
                copy_stack.append(copy)
                word_stack.append(word)
                copy, word = 0, []
            elif char == ']':
                word_temp = word_stack.pop()
                word_temp.extend(word * copy_stack.pop())
                word = word_temp
            else:
                word.append(char)

        return "".join(word)

    
    def decodeString_2(self, s):
    # Solution : use stack
    # 괄호 닫힐때 copy실행. 괄호 열릴때 stack에 저장.
    
        copy_stack, word_stack = [], []
        copy, word = 0, ''
        for char in s:
            if char.isdigit():
                copy = copy * 10 + int(char)
            elif char == '[':
                copy_stack.append(copy)
                word_stack.append(word)
                copy, word = 0, ''
            elif char == ']':
                word = word_stack.pop() + word * copy_stack.pop()
            else:
                word = word + char

        return word
