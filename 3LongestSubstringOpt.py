# Complexity O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = [-1] * 128
        max_dist = 0
        last_repeat = [-1, -1]

        for i, c in enumerate(s):
            last_i = last_index[ord(c)]
            if last_i < last_repeat[0]:
                candidate = i - last_repeat[0]
            else:
                candidate = i - last_i
            max_dist = max(max_dist, candidate)
            last_index[ord(c)] = i
            if last_i != -1:
                last_repeat[0] = max(last_repeat[0], last_i)
                last_repeat[1] = i - 1
        return max_dist