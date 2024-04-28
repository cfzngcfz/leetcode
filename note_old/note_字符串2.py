# -*- coding: utf-8 -*-

# # question 132 分割回文串 II 已完成
# s = 'aab'
# s = "eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj"

# # 两次动态规划：第一次DP用于判断并记录子串是否为回文串
# huiwen = [[True]*len(s) for _ in range(len(s))]
# for ii in range(len(s)-1,-1,-1):
#     for jj in range(ii+1,len(s)):
#         huiwen[ii][jj] = huiwen[ii+1][jj-1] and s[ii] == s[jj]
# # 第二次DP用于寻找最少分割，使得分割后的子串均为回文串
# dp = [0]
# index = 1
# while index < len(s):
#     if huiwen[0][index]: #如果前n个字符子串为回文串
#         dp.append(0)
#     else:
#         temp = []
#         for ii in range(index):
#             if huiwen[ii+1][index]: 如果第ii个字符后，直到第index个字符组成的子串为回文串
#                 temp.append(dp[ii]+1)
#         dp.append(min(temp))
#     index += 1
# print(dp[-1])

# # 官方代码
# n = len(s)
# g = [[True] * n for _ in range(n)]

# for i in range(n - 1, -1, -1):
#     for j in range(i + 1, n):
#         print(i,j)
#         g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

# f = [float("inf")] * n
# for i in range(n):
#     if g[0][i]:
#         f[i] = 0
#     else:
#         for j in range(i):
#             if g[j + 1][i]:
#                 f[i] = min(f[i], f[j] + 1)

# print(f[n - 1])
#-----------------------------------------------------------------------------#
# # 1143. 最长公共子序列
# text1 = "abcde"
# text2 = "ace"

# dp = [[0]*len(text2) for _ in range(len(text1))]
# if text1[0] == text2[0]:
#     dp[0][0] = 1
#     # print(text1[0])
# for jj in range(1,len(text2)):
#     if text1[0] == text2[jj]:
#         dp[0][jj] = 1
#     else:
#         dp[0][jj] = dp[0][jj-1]
# for ii in range(1,len(text1)):
#     if text1[ii] == text2[0]:
#         dp[ii][0] = 1
#         # print(text1[ii])
#     else:
#         dp[ii][0] = dp[ii-1][0]        
# for ii in range(1,len(text1)):
#     for jj in range(1,len(text2)):
#         if text1[ii] == text2[jj]:
#             dp[ii][jj] = dp[ii-1][jj-1] + 1 # 核心
#             # print(text1[ii])
#         else:
#             dp[ii][jj] = max(dp[ii-1][jj],dp[ii][jj-1]) # 核心
# print(dp[-1][-1])
#-----------------------------------------------------------------------------#
# # 97. 交错字符串
# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"
# s1 = ""
# s2 = ""
# s3 = ""

# # 动态规划
# # dp[ii][jj]表示s1的前ii个元素和s2的前jj个元素能否交错组成s3的第ii+jj个元素

# # 如果s1的第ii个元素（即s1[ii-1]）和s3的第ii+jj个元素（即s3[ii+jj-1]）相等
# # 那么s1的前ii个元素和s2的前jj个元素能否交错组成s3的前ii+jj个元素取决于s1的前ii−1个元素和s2的前jj个元素是否能交错组成s3的前ii+jj-1个元素
# # 即dp[ii][jj]取决于dp[ii−1,jj]

# if len(s1) + len(s2) == len(s3):
#     dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
#     dp[0][0] = True
#     for ii in range(1,len(s1)+1):
#         dp[ii][0] = s1[0:ii] == s3[0:ii]
#     for jj in range(1,len(s2)+1):
#         dp[0][jj] = s2[0:jj] == s3[0:jj]
#     for ii in range(1,len(s1)+1):
#         for jj in range(1,len(s2)+1):
#             dp[ii][jj] = (dp[ii-1][jj] and s1[ii-1] == s3[ii+jj-1]) or (dp[ii][jj-1] and s2[jj-1] == s3[ii+jj-1])
#     print(dp[-1][-1])
# else:
#     print(False)
#-----------------------------------------------------------------------------#