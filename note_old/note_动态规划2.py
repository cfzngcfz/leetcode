# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:59:23 2021

@author: CC-i7-8750H
"""
# https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92.md#0-1-%E8%83%8C%E5%8C%85

# A.组合问题：dp[i] += dp[i-num]
# 494. 目标和
# B.True、False问题：dp[i] = dp[i] or dp[i-num]
# 139. 单词拆分
# 416. 分割等和子集
# C.最大最小问题：dp[i] = min(dp[i], dp[i-num]+1)或者dp[i] = max(dp[i], dp[i-num]+1)
# 474. 一和零

# leetcode 509 号算法题：斐波那契数
# leetcode 647 号算法题：回文子串
# leetcode 131 号算法题：分割回文串
# leetcode 516 号算法题：最长回文子序列
# leetcode 1143 号算法题：最长公共子序列
# leetcode 486 号算法题：预测赢家
# leetcode 877 号算法题：石子游戏
# 0-1 背包问题
#-----------------------------------------------------------------------------#
# # question 72 编辑距离 已完成 动态规划

# # 动态规划 - 解题思路
# # word1[i-1] vs word2[j-1]            word1[i-1] vs word2[j]
# #     dp[i-1][j-1]                         dp[i-1][j]
# #                            \                  |
# #                             \                 |
# #   if word1[i] != word2[j]    \                |
# #      word1[i] 替换为word2[j]  \               |  word1 增加1
# #   if word1[i] == word2[j]      \              |
# #      不变                       \             |
# #                                  *            *
# # word1[i] vs word2[j-1]              word1[i] vs word2[j-1]
# #      dp[i][j-1]        ----------->       dp[i][j]         
# #                         word2 增加1
# #                  等价于 word1 删除1

# # word1 = "horse"
# # word2 = "ros"

# # # word1 = "intention"
# # word1 = "entzntion"
# # word2 = "execution"

# # word1 = 'z'
# # word2 = 'cda'

# # word1 = 'ad'
# # word2 = ''

# # word1 = ''
# # word2 = 'cda'

# # word1 = ''
# # word2 = ''

# word1 = "dinitrophenylhydrazine"
# word2 = "dimethylhydrazine"

# if len(word1) > 0 and len(word2) > 0:
#     dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
#     for jj in range(len(word2)+1):
#         dp[0][jj] = jj
#     for ii in range(1,len(word1)+1):
#         dp[ii][0] = ii
#     for ii in range(1,len(word1)+1):
#         for jj in range(1,len(word2)+1):
#             if word1[ii-1] == word2[jj-1]:
#                 dp[ii][jj] = min(dp[ii-1][jj]+1, dp[ii][jj-1]+1, dp[ii-1][jj-1])
#             else:
#                 dp[ii][jj] = 1 + min(dp[ii-1][jj], dp[ii][jj-1], dp[ii-1][jj-1])
#     print(dp[-1][-1])
# else:
#     print(max(len(word1), len(word2)))
#-----------------------------------------------------------------------------#
# # 87. 扰乱字符串
# s1 = "great"
# s2 = "rgeat"
# # s1 = "abcde"
# # s2 = "caebd"
# # s1 = "a"
# # s2 = "b"
# # s1 = "aaccd"
# # s2 = "acaad"
# # s1 = "aaccb"
# # s2 = "cabac"
# # s1 = "abb"
# # s2 = "bba"

# # 方法一：动态规划
# # dp[kk][ii][jj]表示s1[ii:ii+kk]与s2[jj:jj+kk]是否可以交换得到
# dp = [[[False]*len(s1) for _ in range(len(s1))] for _ in range(len(s1)+1)]
# #dp[0]无意义，随着kk的增大，有效区域缩小，呈金字塔形

# for ii in range(len(s1)):
#     for jj in range(len(s1)):
#         dp[1][ii][jj] = s1[ii] == s2[jj] #初始条件：对于长度是1的子串，相等为true，不相等为false
# for kk in range(2,len(s1)+1):
#     for ii in range(len(s1)-kk+1): #随kk的增加，而递减
#         for jj in range(len(s1)-kk+1): #随kk的增加，而递减
#             label = False
#             for ll in range(1,kk):
#                 #不交换的情况：s1[ii:ii+ll]与s2[jj:jj+ll]可交换，并且s1[ii+ll:ii+kk]与s2[jj+ll:jj+kk]可交换
#                 label = label or dp[ll][ii][jj] and dp[kk-ll][ii+ll][jj+ll]
#                 #交换的情况：s1[ii:ii+ll]与s2[jj+kk-ll:jj+kk]可交换，并且s1[ii+ll:ii+kk]与s2[jj:jj+kk-ll]可交换
#                 label = label or dp[ll][ii][jj+kk-ll] and dp[kk-ll][ii+ll][jj]
#             dp[kk][ii][jj] = label # 由dp[1]～dp[kk-1]决定
#             # 例如：dp[3][0][0] = dp[1][0][0] and dp[2][1][1]
#             #                 or dp[1][0][2] and dp[2][1][0]
#             #                 or dp[2][0][0] and dp[1][2][2]
#             #                 or dp[2][0][1] and dp[1][2][0]
# print(dp[-1][0][0])

# # 题解：动态规划
# def isScramble(self, s1, s2):
#     if s1 == s2:
#         return True
#     if sorted(s1) != sorted(s2):
#         return False
#     for i in range(1, len(s1)):
#         if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
#             return True
#         if self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
#             return True
#     return False
#-----------------------------------------------------------------------------#
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
# # 1269. 停在原地的方案数
# # steps = 3
# # arrLen = 2
# steps = 2
# arrLen = 4
# # steps = 4
# # arrLen = 5

# # dp[i][j] 表示在i步操作之后，指针位于下标j的方案数
# # dp[i][j]=dp[i−1][j−1]+dp[i−1][j]+dp[i−1][j+1]
# num_col = min(arrLen,steps+1) #缩小列的搜索范围
# dp = [[0]*num_col for _ in range(steps)]
# dp[0][0] = dp[0][1] = 1
# for ii in range(1,steps):
#     for jj in range(num_col):
#         dp[ii][jj] = dp[ii-1][jj]
#         if 0 <= jj-1 < num_col:
#             dp[ii][jj] += dp[ii-1][jj-1]
#         if 0 <= jj+1 < num_col:
#             dp[ii][jj] += dp[ii-1][jj+1]
# print(dp[-1][0]%(10**9+7))
#-----------------------------------------------------------------------------#
# # 1473. 粉刷房子 III
# # houses = [0,0,0,0,0]
# # cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
# # m = 5
# # n = 2
# # target = 3 #9
# # houses = [0,0,0,0,0]
# # cost = [[1,10],[10,1],[1,10],[10,1],[1,10]]
# # m = 5
# # n = 2
# # target = 5 #5
# # houses = [0,2,1,2,0]
# # cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
# # m = 5
# # n = 2
# # target = 3 #11
# houses = [3,1,2,3]
# cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
# m = 4
# n = 3
# target = 3 #-1

# # 动态规划思路
# # if houses[i] = 0:
# #     dp[i][j][k] = cost[i][j] + min{ dp[i-1][j*][k],   j*  = j(与前一个房子颜色一样)
# #                                   { dp[i-1][j*][k-1], j* != j(与前一个房子颜色不一样)
# # if houses[i] = j+1:
# #     dp[i][j][k] = min{ dp[i-1][j*][k],   j*  = j(与前一个房子颜色一样)
# #                      { dp[i-1][j*][k-1], j* != j(与前一个房子颜色不一样)
# # if houses[i] != 0 and houses[i] != j+1:
# #     dp[i][j][k] = inf (第i个房子已涂色,不能再涂其他颜色)

# dp = [[[float('inf')]*(target+1) for jj in range(n)] for ii in range(m)]

# for jj in range(n):
#     if houses[0] == 0:
#         dp[0][jj][1] = cost[0][jj]
#     elif houses[0] == jj+1:
#         dp[0][jj][1] = 0
#     for ii in range(1,m):
#         if houses[ii] == 0:
#             dp[ii][jj][1] = dp[ii-1][jj][1] + cost[ii][jj]
#         elif houses[ii] == jj+1:
#             dp[ii][jj][1] = dp[ii-1][jj][1]

# for kk in range(2,target+1):
#     for jj in range(n):
#         for ii in range(1,m):
#             temp = float('inf')
#             for j2 in range(n):
#                 if j2 == jj:
#                     temp = min(temp, dp[ii-1][j2][kk])
#                 else:
#                     temp = min(temp, dp[ii-1][j2][kk-1])
#             if houses[ii] == 0:
#                 dp[ii][jj][kk] = temp + cost[ii][jj]
#             elif houses[ii] == jj+1:
#                 dp[ii][jj][kk] = temp

# output = float('inf')
# for jj in range(n):
#     output = min(output, dp[-1][jj][-1])
# if output == float('inf'):
#     output = -1
# print(output)
#-----------------------------------------------------------------------------#
# # 1787. 使所有区间的异或结果为零
# nums = [1,2,0,3,0]
# k = 1 # 3
# nums = [3,4,5,2,1,7,3,4,7]
# k = 3 # 3
# nums = [1,2,4,1,2,5,1,2,6]
# k = 3 # 3
# nums = [1,2,4,3,7,5,8,9,6]
# k = 4 # 6
# # nums = [23,27,14,0,14,3,7,10,14,23,5,5]
# # k = 1 # 11
# # nums = [17,4,31,15,0,3,7,29,8,26,4,30,4,16,29,18,18,21,16,3,30,10]
# # k = 2 #19
# # nums = [31,5,17,15,0,19,1,12,4,9,0,17,1,1,24,7,28,10,23,4,8,4,14,5,23,26,27,8,20,10,18,30,2,23,1,12,21,19,1,1,27,28,25,24,20,19,2,9,17]
# # k = 20 #28

# # 下面算法的改进
# # dp[col][xor]: 前col个元素的异或值之和为xor时，要更改的最小元素数
# # 核心: dp[col][xor] = min(dp[col-1][xor^x] + count[col] - dict[col][x])
# #                       x
# #       x in [0, 2**10); count[col] 表示第col列元素总数; dict[col,x]表示x在第col列中出现的次数
# # 优化: dp[col][xor] = min(t1, t2)
# #       if x 未在第col列中出现,即dict[col][x] = 0:
# #           t2 = min(dp[col-1][xor^x] + count[col]) = min(dp[col-1]) + count[col] （因为此处的异或运算是满射的）
# #       if x 在第col列中出现,即dict[col][x] > 0:
# #           t1 = min(dp[col-1][xor^x] + count[col] - dict[col][x])
# #                 x in dict_temp
# dp = [[] for _ in range(k)]
# for ii in range(k):
#     dict_temp = {}
#     col_count = 0
#     for jj in range(ii,len(nums),k):
#         if nums[jj] not in dict_temp:
#             dict_temp[nums[jj]] = 1
#         else:
#             dict_temp[nums[jj]] += 1
#         col_count += 1
#     if ii == 0:
#         dp[0] = [col_count]*2**10
#         for key in dict_temp:
#             dp[0][key] -= dict_temp[key]
#     else:
#         dp[ii] = [min(dp[ii-1]) + col_count]*2**10  #超时的原因在此
#         #[min(dp[ii-1]) + col_count]*2**10 比 [col_count for _ in range(2**10)] 速度更快
#         for jj in range(2**10):
#             for key in dict_temp:
#                 dp[ii][jj] = min(dp[ii-1][jj^key] + col_count - dict_temp[key], dp[ii][jj])
# print(dp[k-1][0])
#-----------------------------------------------------------------------------#
# # 664. 奇怪的打印机
# s = "aaabbb"
# s = "aba"
# s = "baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa" #19
# s = "baacdddaaddaaaaccbddb" #7

# # 动态规划思路
# # dp[i][j] 表示区间[i,j]的最少打印操作数
# # dp[i][j] = { dp[i][j-1]               , if s[i]  = s[j]
# #            | min dp[i][k] + dp[k+1][j], if s[i] != s[j]
# #               k  (k from i to j-1)
# # example:
# #            a b a b
# #        /      |      \               
# # a + bab    ab + ab    aba + b
# # 1 + 2       2 + 2       2 + 1
# #   3           4           3
# dp = [[1]*len(s) for _ in range(len(s))]
# for ii in range(len(s)-1,-1,-1):
#     for jj in range(ii+1,len(s),1):
#         if s[ii] == s[jj]:
#             dp[ii][jj] = dp[ii][jj-1]
#         else:
#             temp = float('inf')
#             for kk in range(ii,jj):
#                 temp = min(temp, dp[ii][kk]+dp[kk+1][jj])
#             dp[ii][jj] = temp
# print(dp[0][-1])

#-----------------------------------------------------------------------------#
# # question 91 解码方法 完成 动态规划
# s = "301"
# s = '12'
# s = "226"
# # s = "0"
# # s = "06"
# s = "2101"

# dict2 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
# dp = [0 for _ in range(len(s))]

# if s[0] == '0':
#     dp[0] = 0
# else:
#     dp[0] = 1
# if len(s) >= 2:
#     if s[0:2] in dict2 and s[1] != '0':
#         dp[1] = 2
#     elif s[0:2] in dict2 and s[1] == '0':
#         dp[1] = 1
#     elif s[0:2] not in dict2 and s[1] != '0' and s[0] != '0':
#         dp[1] = 1
#     elif s[0:2] not in dict2 and s[1] != '0' and s[0] == '0':
#         dp[1] = 0
#     else:
#         dp[1] = 0
        
# if len(s) >= 3:
#     for ii in range(2,len(s)):
#         if s[ii-1]+s[ii] in dict2 and s[ii] != '0': 
#             dp[ii] = dp[ii-1] + dp[ii-2]
#         elif s[ii-1]+s[ii] in dict2 and s[ii] == '0': #只有10或20，与前两个状态一致
#             dp[ii] = dp[ii-2]    
#         elif s[ii-1]+s[ii] not in dict2 and s[ii] != '0' and s[ii-1] != '0': #ii-1与ii只能拆开
#             dp[ii] = dp[ii-1]
#         elif s[ii-1]+s[ii] not in dict2 and s[ii] != '0' and s[ii-1] == '0': #ii-1与ii只能拆开
#             dp[ii] = dp[ii-1]
#         elif s[ii-1]+s[ii] not in dict2 and s[ii] == '0':
#             dp[ii] = 0
# print(dp[-1])
#-----------------------------------------------------------------------------#
# # question 300 最长递增子序列  已完成 - 贪心算法 需要进一步研究
# nums = [10,9,2,5,3,7,101,18,4,8,6,12]
# # nums = [0,1,0,3,2,3]
# # nums = [7,7,7,7,7,7,7]
# # nums = [4,10,4,3,8,9]

# # 方法一：动态规划-时间复杂度 O(n^2)
# # dp[i]定义为以第i个数字结尾的最长上升子序列的长度
# dp = [1 for _ in range(len(nums))]
# for ii in range(1,len(nums)):
#     for jj in range(ii):
#         if nums[jj] < nums[ii]:
#             dp[ii] = max(dp[ii], dp[jj]+1)
# print(max(dp))

# # 方法二：基于二分查找的动态规划-时间复杂度 O(nlogn)
# record = [nums[0]]
# for ii in range(1,len(nums)):
#     # print(record) #查看更新过程
#     if record[-1] >= nums[ii]:
#         #如果nums[ii] <= record[-1]，则在record数组中二分查找，找到第一个比nums[ii]小的数record[index-1]，并跟新record[index]=nums[ii]
#         index = bisect.bisect_left(record,nums[ii])
#         record[index] = nums[ii]
#     else:
#         #如果nums[ii] > record[-1]，则直接加入到record数组末尾
#         record.append(nums[ii])
# print(len(record))

# # question 354 俄罗斯套娃信封问题 
# # envelopes =[[5,4],[6,4],[6,7],[2,3]]
# # envelopes = [[1,1],[5,10],[6,2],[7,3],[8,4]]
# # envelopes = [[46,89],[50,53],[52,68],[72,45],[77,81]]
# # envelopes = [[2,100],[3,200],[4,300],[5,400],[5,500],[5,250],[6,370],[6,360],[7,380]]
# # envelopes = [[10,8],[1,12],[6,15],[2,18]]
# envelopes = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]

# # 方法一 动态规划
# envelopes.sort()
# dp = [1 for _ in range(len(envelopes))]
# for ii in range(1,len(envelopes)):
#     for jj in range(ii):
#         if envelopes[jj][0] < envelopes[ii][0] and envelopes[jj][1] < envelopes[ii][1]:
#             dp[ii] = max(dp[ii], dp[jj]+1)
# print(max(dp))
# # 方法二：基于二分查找的动态规划
# envelopes.sort(key=lambda x: (x[0], -x[1])) #按第一个元素升序，第二个元素降序 排列
# record = [envelopes[0]]
# for ii in range(1,len(envelopes)):
#     print(record) #查看更新过程        
#     if record[-1][0] < envelopes[ii][0] and record[-1][1] < envelopes[ii][1]:
#         record.append(envelopes[ii])
#     else:
#         temp = [record[jj][1] for jj in range(len(record))]
#         index = bisect.bisect_left(temp,envelopes[ii][1])
#         record[index] = envelopes[ii]
# print(len(record))
