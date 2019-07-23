#Time Complexity : O(N), Space Complexity : O(N)
class Solution(object):
    def decodeString(self, s):
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
