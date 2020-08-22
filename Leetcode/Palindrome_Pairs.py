# Solution 1: Save {Word: index} into hash.
# If a part of reverse of each word exists in hash and the rest part of the word is palindrome, then sum of two word is panlindrome.
# Time : O(NM^2), Space : O(N)


class Solution(object):
    def palindromePairs(self, words):
        a, ans = {word: i for i, word in enumerate(words)}, []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                word_l, word_r = word[:j], word[j:]
                word_l_rev, word_r_rev = word_l[::-1], word_r[::-1]
                val_l, val_r = a.get(word_l_rev), a.get(word_r_rev)
                if val_l is not None and val_l != i and word_r == word_r_rev:
                    ans.append([i, val_l])
                if (
                    val_r is not None
                    and val_r != i
                    and word_l == word_l_rev
                    and j != 0
                ):
                    ans.append([val_r, i])
        return ans
