def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    '''
    解题思路：
    sliding windows with two pointers
    '''
    n = len(s)
    if n == 0 or k == 0:
        return 0

    left, right = 0, 0
    hashmap = defaultdict()
    max_len = 1

    while right < n:  # add new pointer and move right pointer
        hashmap[s[right]] = right
        right += 1

        if len(hashmap) == k + 1:
            # delete the leftmost character
            del_idx = min(hashmap.values())
            del hashmap[s[del_idx]]
            # move left pointer of the slidewindow
            left = del_idx + 1
        max_len = max(max_len, right - left)
    return max_len
