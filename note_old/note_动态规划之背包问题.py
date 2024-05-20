# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 21:51:52 2021

@author: CC-i7-8750H
"""
# 背包问题(Knapsack problem): NP complete
# 给定一组物品，每种物品都有自己的重量weights和价格values，在限定的总重量Volume内，如何选择才能使得物品的总价格最高。
# 参考：
# https://zhuanlan.zhihu.com/p/93857890
# https://github.com/tianyicui/pack/blob/master/V2.pdf
# https://leetcode-cn.com/problems/coin-change-2/solution/gong-shui-san-xie-xiang-jie-wan-quan-bei-6hxv/
#-----------------------------------------------------------------------------#
# # 279. 完全平方数
# 一维01背包问题，求可行解的最短长度
# # 改进 从 O((n+1)*(n^0.5+1)) 降低至 O(n*n^0.5)
# n = 13
# dp = [ii+1 for ii in range(n)]
# for ii in range(1,int(n**0.5)):
#     for jj in range((ii+1)**2-1,n):
#         if (jj+1)%(ii+1)**2 == 0:
#             dp[jj] = min(dp[jj], (jj+1)//((ii+1)**2))
#         else:
#             dp[jj] = min(dp[jj], (jj+1)//((ii+1)**2) + dp[(jj+1)%(ii+1)**2-1]) #改进2
# print(dp[-1])

# # 超时
# # 原问题 <=> 从 [1,2^2,3^2,..., int(sqrt(n))^2] 中选择若干元素恰好装满 n
# # 与经典01背包问题不同之处在于，不是求装包的最大价值，也不是求可行解的数量，而且是求可行解的最短长度
# # 因此，dp[ii][jj] 表示从前ii个正整数(1,...,ii)找若干完全平方和，使得它们等于jj
# dp = [[0]*(n+1) for _ in range(int(n**0.5)+1)]
# for jj in range(1,n+1):
#     dp[0][jj] = float('inf')
# for ii in range(1,int(n**0.5)+1):
#     for jj in range(1,n+1):
#         if jj >= ii**2:
#             dp[ii][jj] = min(dp[ii-1][jj], dp[ii-1][jj-ii**2*(jj//(ii**2))]+jj//(ii**2))
#         else:
#             dp[ii][jj] = dp[ii-1][jj]
# print(dp[-1][-1])


# # 322. 零钱兑换
# # 一维01背包问题，求可行解的最短长度
# coins = [1, 2, 5]
# amount = 11
# coins = [2]
# amount = 3
# coins = [1]
# amount = 0
# # coins = [1]
# # amount = 1
# # coins = [1]
# # amount = 2
# # coins = [186,419,83,408]
# # amount = 6249

# # 降维
# dp = []
# for jj in range(amount):
#     if (jj+1)%coins[0] == 0:
#         dp.append((jj+1)//coins[0])
#     else:
#         dp.append(float('inf'))
# for ii in range(1,len(coins)):
#     for jj in range(amount):
#         if jj+1 >= coins[ii]:
#             if jj-coins[ii] == -1:
#                 dp[jj] = min(dp[jj], 1)
#             else:
#                 dp[jj] = min(dp[jj], dp[jj-coins[ii]]+1)
# if len(dp) > 0:
#     if dp[-1] != float('inf'):
#         print(dp[-1])
#     else:
#         print(-1)
# else:
#     print(0)

# # 超时
# dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
# for jj in range(1,amount+1):
#     dp[0][jj] = float('inf')
# for ii in range(1,len(coins)+1):
#     for jj in range(amount+1):
#         dp[ii][jj] = dp[ii-1][jj] #第ii件物品没装入背包的情况
#         if jj >= coins[ii-1]:
#             for kk in range(1,jj//coins[ii-1]+1):
#                 dp[ii][jj] = min(dp[ii-1][jj-coins[ii-1]*kk]+kk, dp[ii][jj]) #第ii件物品装入背包kk件的情况
# if dp[-1][-1] != float('inf'):
#     print(dp[-1][-1])
# else:
#     print(-1)


# # 518. 零钱兑换 II
# # 一维完全背包问题，求可行解数量
# amount = 5
# coins = [1, 2, 5]
# # amount = 3
# # coins = [2]
# amount = 10
# coins = [10]

# # 完全背包问题
# dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
# dp[0][0] = 1
# for ii in range(1,len(coins)+1):
#     for jj in range(amount+1):
#         dp[ii][jj] = dp[ii-1][jj]
#         if jj >= coins[ii-1]:
#             for kk in range(1,jj//coins[ii-1]+1):
#                 dp[ii][jj] += dp[ii-1][jj-coins[ii-1]*kk]
# print(dp[-1][-1])


# # 1449. 数位成本和为目标值的最大数字
# # 一维完全背包问题，目标函数变化
# cost = [4,3,2,5,6,7,2,5,5]
# target = 9
# cost = [7,6,5,5,5,6,8,7,8]
# target = 12
# # cost = [2,4,6,2,4,6,4,4,4]
# # target = 5
# # cost = [6,10,15,40,40,40,40,40,40]
# # target = 47

# # 改进：ii从 len(cost)+1 降维至len(cost)，jj从target+1降维至target，kk降维至1
# dp = [-float('inf')]*(target)
# for ii in range(len(cost)):
#     for jj in range(target):
#         if jj+1 >= cost[ii]:
#             if jj-cost[ii] >= 0 and dp[jj-cost[ii]] != -float('inf'):
#                 temp2 = int(str(ii+1) + str(dp[jj-cost[ii]]))
#                 dp[jj] = max(temp2, dp[jj])
#             elif jj-cost[ii] == -1:
#                 temp2 = int(str(ii+1))
#                 dp[jj] = max(temp2, dp[jj])
# print(str(dp[-1]))
                
# # 超时
# dp = [[None]*(target+1) for _ in range(len(cost)+1)]
# for ii in range(len(cost)+1):
#     dp[ii][0] = ''
# for ii in range(1,len(cost)+1):
#     for jj in range(1,target+1):
#         dp[ii][jj] = dp[ii-1][jj] #第ii件物品没装入背包的情况
#         if jj >= cost[ii-1]:
#             for kk in range(1,jj//cost[ii-1]+1):
#                 if dp[ii-1][jj-cost[ii-1]*kk] != None: #第ii件物品装入背包kk件的情况
#                     temp2 = str(ii)*kk + dp[ii-1][jj-cost[ii-1]*kk]
#                     # 因为ii是递增的，将其排在前面等到的数字是最大的
#                     if dp[ii][jj] == None:
#                         dp[ii][jj] = temp2
#                     else:
#                         dp[ii][jj] = str(max(int(temp2), int(dp[ii][jj])))
# if dp[-1][-1] != None:
#     print(dp[-1][-1])
# else:
#     print('0')
                

# 474. 一和零
# 二维01背包问题，求可行解的最大长度
# strs = ["10", "0001", "111001", "1", "0"]
# m = 5
# n = 3
# strs = ["10", "0", "1"]
# m = 1
# n = 1

# dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]
# for ii in range(1,len(strs)+1):
#     count0 = count1 = 0
#     for ss in strs[ii-1]:
#         if ss == '0':
#             count0 += 1
#         else:
#             count1 += 1
#     for jj in range(m+1):
#         for kk in range(n+1):
#             dp[ii][jj][kk] = dp[ii-1][jj][kk]
#             if jj >= count0 and kk >= count1:
#                 dp[ii][jj][kk] = max(dp[ii][jj][kk],
#                                      dp[ii-1][jj-count0][kk-count1]+1)
# print(dp[-1][-1][-1])

# # 879. 盈利计划
# 二维01背包问题变形，求可行解数量，
# n = 5
# minProfit = 3
# group = [2,2]
# profit = [2,3]
# n = 10
# minProfit = 5
# group = [2,3,5]
# profit = [6,7,8]

# # dp[ii][jj][kk] 表示前ii个工作，选择jj个员工（背包问题的资源限制），获得kk个利润的计划数量
# # 当0 <= kk < minProfit时，表示获得kk个利润的计划数量，当kk = minProfits时，表示>=minProfit的计划数量
# # dp[ii][jj][kk] = dp[ii-1][jj][kk] #不选择第ii个工作时的计划数量
# #                + dp[ii-1][jj-group[ii-1]][max(kk-profit[ii-1],0)] #选择第ii个工作时的计划数量
# dp = [[[0]*(minProfit+1) for _ in range(n+1)] for _ in range(len(profit)+1)]
# dp[0][0][0] = 1
# for ii in range(1,len(profit)+1):
#     for jj in range(n+1):
#         for kk in range(minProfit+1):
#             if jj >= group[ii-1]:
#                 dp[ii][jj][kk] = dp[ii-1][jj][kk]+dp[ii-1][jj-group[ii-1]][max(kk-profit[ii-1],0)]
#             else:
#                 dp[ii][jj][kk] = dp[ii-1][jj][kk]
# count = 0
# for jj in range(n+1):
#     count += dp[-1][jj][-1]
# print(count)

# ------------------------------


# 377. 组合总和 Ⅳ
# 本题与「完全背包求方案数」问题的差别在于：选择方案中的不同的物品顺序代表不同方案