class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        result=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        result+=1
        return result
#后缀技术
# class Solution(object):
#     def countGoodTriplets(self, arr, a, b, c):
#         MAXV = 1000
#         n = len(arr)
#         # 后缀频次：从右往左逐步填充
#         suf = [0]*(MAXV+1)
#         for v in arr:
#             suf[v] += 1

#         ans = 0
#         for i in range(n):
#             suf[arr[i]] -= 1                # i 不能再被当作 k
#             # 当前 j 的左侧固定了 i，准备一个“右侧计数”的拷贝
#             cur = suf[:]                    # 也可边走边更新，避免拷贝
#             for j in range(i+1, n):
#                 cur[arr[j]] -= 1            # j 不能再被当作 k

#                 if abs(arr[i]-arr[j]) <= a:
#                     L = max(0,  max(arr[j]-b, arr[i]-c))
#                     R = min(MAXV, min(arr[j]+b, arr[i]+c))
#                     if L <= R:
#                         # 统计 j 右边在 [L,R] 的数量
#                         ans += sum(cur[L:R+1])
#         return ans
# 时间：近似 O(n² + n·MAXV)（如果不做拷贝并改为前缀和/树状数组，可到 O(n²)）。
# 空间：O(MAXV)
# 进一步可用“前缀和数组”或“树状数组(Fenwick)”维护区间和，把 sum(cur[L:R+1]) 降到 O(log MAXV)，整体 O(n² log MAXV)。
# 结论
# 你的写法在本题约束下完全OK；
# 若追求更优复杂度或 n 变大，用“区间交+后缀计数/树状数组”方案能把复杂度降到 O(n²)（或 O(n² log V)）。
