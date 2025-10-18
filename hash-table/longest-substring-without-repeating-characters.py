class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0                      # 记录最长子串长度
        cnt = Counter()              # 用哈希表记录每个字符出现次数
        left = 0                     # 窗口左边界

        for right, c in enumerate(s):
            cnt[c] += 1              # 将当前字符加入窗口

            # 如果当前字符重复，缩小窗口直到不重复
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1

            # 更新最长长度
            ans = max(ans, right - left + 1)

        return ans
