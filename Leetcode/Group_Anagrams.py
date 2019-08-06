# Solution 1 :  Use Hash after sorting string, Time : O(NMlogM), Space : O(NM) (N : number of strings, M : Maximum length of strings)
# Solution 2 : Use Hash . Set string that represents the number of strings as a key. Time : O(NM), Space :O(NM)

class Solution(object):
    def groupAnagrams_2(self, strs):
        a = dict()
        for s in strs:
            nums = [0 for _ in range(26)] # Number of alphabets
            for c in s:
                nums[ord(c)-ord('a')] += 1
            key_a = []
            for i in range(len(nums)):
                key_a.append('#')
                key_a.append(str(nums[i]))
            key = ''.join(key_a)
            if key in a:
                a[key].append(s)
            else:
                a[key] = [s]
        return list(a.values())
                
                
    def groupAnagrams_1(self, strs):
        a = dict()
        for s in strs:
            key = ''.join(sorted(s))
            if key in a:
                a[key].append(s)
            else:
                a[key] = [s]
        return list(a.values())
                
        
        
