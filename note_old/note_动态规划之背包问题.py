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
weights = [2,2,6,5,4]
values = [3,6,5,4,6]
Volume = 9
# weights = [2,2,3,1,5,2]
# values = [2,3,1,5,4,3]
# Volume = 10
# weights = [8,10,6,3,7,2]
# values = [4,6,2,2,5,1]
# Volume = 12
#-----------------------------------------------------------------------------#
# A. 求最大装包价值
# # 0-1背包问题
# 动态规划思路
# 设dp[ii][jj] 表示前ii件物品在重量不超过jj的前提下不重复装包的最大价格
# 不超过容量的01背包问题
dp = [[0]*(Volume+1) for _ in range(len(weights)+1)]
# # 恰好装满的01背包问题
# dp = [[-float('inf')]*(Volume+1) for _ in range(len(weights)+1)] # 恰好装满的01背包问题
# for ii in range(len(weights)+1):
#     dp[ii][0] = 0

for ii in range(1,len(weights)+1):
    for jj in range(1,Volume+1):
        if jj >= weights[ii-1]:
            dp[ii][jj] = max(dp[ii-1][jj], #第ii件物品没装入背包的情况
                              dp[ii-1][jj-weights[ii-1]] + values[ii-1]) #第ii件物品装入背包的情况
        else:
            dp[ii][jj] = dp[ii-1][jj]
print('----0-1背包问题dp----')
for ii in range(len(dp)):
    print('前',ii,'件: ',dp[ii])

# 完全背包问题
# 设dp[ii][jj] 表示前ii件物品在重量不超过jj的前提下可重复装包的最大价格
# 不超过容量的01背包问题
dp = [[0]*(Volume+1) for _ in range(len(weights)+1)]
# # 恰好装满的01背包问题
# dp = [[-float('inf')]*(Volume+1) for _ in range(len(weights)+1)] # 恰好装满的01背包问题
# for ii in range(len(weights)+1):
#     dp[ii][0] = 0
    
for ii in range(1,len(weights)+1):
    for jj in range(Volume+1):
        dp[ii][jj] = dp[ii-1][jj] #第ii件物品没装入背包的情况
        if jj >= weights[ii-1]:
            for kk in range(1,jj//weights[ii-1]+1):
                dp[ii][jj] = max(dp[ii][jj],
                                  dp[ii-1][jj-weights[ii-1]*kk]+values[ii-1]*kk) #第ii件物品装入背包kk件的情况
print('----完全背包问题dp1----')
for ii in range(len(dp)):
    print('前',ii,'件: ',dp[ii])

# 算法改进
# 不超过容量的01背包问题
dp = [[0]*(Volume+1) for _ in range(len(weights)+1)]
# # 恰好装满的01背包问题
# dp = [[-float('inf')]*(Volume+1) for _ in range(len(weights)+1)] # 恰好装满的01背包问题
# for ii in range(len(weights)+1):
#     dp[ii][0] = 0

for ii in range(1,len(weights)+1):
    for jj in range(Volume+1):
        dp[ii][jj] = dp[ii-1][jj]
        if jj >= weights[ii-1]:
            dp[ii][jj] = max(dp[ii][jj],
                              dp[ii][jj-weights[ii-1]]+values[ii-1])
print('----完全背包问题dp2----')
for ii in range(len(dp)):
    print('前',ii,'件: ',dp[ii])
#-----------------------------------------------------------------------------#
# B. 求可行装包数量
# # 0-1背包问题
# 动态规划思路
# 设dp[ii][jj] 表示前ii件物品在重量不超过jj的前提下不重复装包的最大价格
dp = [[0]*(Volume+1) for _ in range(len(weights)+1)]
dp[0][0] = 1
for ii in range(1,len(weights)+1):
    for jj in range(Volume+1): # 注意从0开始，与求最大价值不同
        if jj >= weights[ii-1]:
            dp[ii][jj] = (dp[ii-1][jj] #第ii件物品没装入背包的情况
                          + dp[ii-1][jj-weights[ii-1]]) #第ii件物品装入背包的情况
        else:
            dp[ii][jj] = dp[ii-1][jj]
print('----0-1背包问题dp----')
for ii in range(len(dp)):
    print('前',ii,'件: ',dp[ii])
print('不超过容量的01背包问题可行方案数:',sum(dp[-1]))
print('恰好装满的01背包问题可行方案数:',dp[-1][-1])
# 测试答案
# 不超过容量的01背包问题可行方案数为16，即：
# None, (2), (2), (6), (5), (4), (2,2), (2,6), (2,5), (2,4),
# (2,6), (2,5), (2,4), (5,4), (2,2,5), (2,2,4)
# 恰好装满的01背包问题可行方案数为2，即：
# (5,4), (2,2,5)

# 完全背包问题
# 设dp[ii][jj] 表示前ii件物品在重量不超过jj的前提下可重复装包的最大价格
dp = [[0]*(Volume+1) for _ in range(len(weights)+1)]
dp[0][0] = 1
for ii in range(1,len(weights)+1):
    for jj in range(Volume+1):
        dp[ii][jj] = dp[ii-1][jj] #第ii件物品没装入背包的情况
        if jj >= weights[ii-1]:
            for kk in range(1,jj//weights[ii-1]+1):
                dp[ii][jj] += dp[ii-1][jj-weights[ii-1]*kk] #第ii件物品装入背包kk件的情况
print('----完全背包问题dp1----')
for ii in range(len(dp)):
    print('前',ii,'件: ',dp[ii])
print('不超过容量的01背包问题可行方案数:',sum(dp[-1]))
print('恰好装满的01背包问题可行方案数:',dp[-1][-1])

# 算法改进
dp = [[0]*(Volume+1) for _ in range(len(weights)+1)]
dp[0][0] = 1
for ii in range(1,len(weights)+1):
    for jj in range(Volume+1):
        dp[ii][jj] = dp[ii-1][jj]
        if jj >= weights[ii-1]:
            dp[ii][jj] = (dp[ii][jj]
                          + dp[ii][jj-weights[ii-1]])
print('----完全背包问题dp2----')
for ii in range(len(dp)):
    print('前',ii,'件: ',dp[ii])
print('不超过容量的01背包问题可行方案数:',sum(dp[-1]))
print('恰好装满的01背包问题可行方案数:',dp[-1][-1])


# 求最优方案还没写
print('--------------实例----------------------------')
#-----------------------------------------------------------------------------#
# # 416. 分割等和子集
# # 一维01背包问题，求最大装包价值
# nums = [1,5,11,5]
# # nums = [1,2,3,5]

# if sum(nums)%2 == 0:
#     Volume = sum(nums)//2
#     dp = [[0]*(Volume+1) for _ in range(len(nums)+1)]
#     for ii in range(1,len(nums)+1):
#         for jj in range(1,Volume+1):
#             if jj >= nums[ii-1]:
#                 dp[ii][jj] = max(dp[ii-1][jj], #第ii件物品没装入背包的情况
#                                   dp[ii-1][jj-nums[ii-1]] + nums[ii-1]) #第ii件物品装入背包的情况
#             else:
#                 dp[ii][jj] = dp[ii-1][jj]
#     print(dp[-1][-1] == Volume)
# else:
#     print(False)


# # 1049. 最后一块石头的重量 II
# stones = [2,7,4,1,8,1] #1
# stones = [31,26,33,21,40] #5
# stones = [1,2] #1
# stones = [1,2,4,8,16,32,64,12,25,51] #1
# stones = [53,54,3,61,67] #2

# # 思路：原问题 <=> 将stones分成两组，一组元素和从正的方向趋近sum(stones)/2，另外一个组元素和从负的方向趋近于sum(stones)/2
# #             <=> 从stones中选择选择若干元素，凑成总和不超过sum(stones)/2
# #             <=> 一维01背包问题，求最大装包价值
# dp = [[0]*(sum(stones)//2+1) for _ in range(len(stones)+1)]
# for ii in range(1,len(stones)+1):
#     for jj in range(sum(stones)//2+1):
#         if jj >= stones[ii-1]:
#             dp[ii][jj] = max(dp[ii-1][jj], dp[ii-1][jj-stones[ii-1]]+stones[ii-1])
#         else:
#             dp[ii][jj] = dp[ii-1][jj]
# print(sum(stones)-dp[-1][-1]*2)

# # 平行机算法超时
# upper_bound = sum(stones) #上界
# def backtrack(stones,record):
#     global upper_bound
#     if len(stones) == 0:
#         if max(record) < upper_bound:
#             upper_bound = max(record) 
#         return
#     else:
#         cur_job = stones[0]
#         temp_set = set()
#         for ii in range(2):
#             if record[ii] not in temp_set: #再分配新工件前，如果两个工人的完工时间一样，新工件分配给任意工人的最小完工时间一致，只需遍历一个工人即可，可将另外一个工人的分枝裁剪
#                 temp_set.add(record[ii])
#                 record[ii] += cur_job
#                 if max(record) < upper_bound: #如果当前工件分配给第ii个工人导致目标函数超过上界，则剪枝
#                     backtrack(stones[1:],record)
#                 record[ii] -= cur_job
# backtrack(stones,[0 for _ in range(2)])
# print(abs(sum(stones)-upper_bound*2))

# # 494. 目标和
# # 思路1：原问题 <=> 从nums中找若干元素，使得它们的和等于(sum(nums)-target)//2
# # 一维01背包问题，求可行解数量
# nums = [1,1,1,1,1]
# target = 3
# nums = [1]
# target = 1
# nums = [2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53]
# target = 1000

# if (sum(nums)-target)%2 == 0 and sum(nums)-target >= 0:
#     Volume = (sum(nums)-target)//2
#     dp = [[0]*(Volume+1) for _ in range(len(nums)+1)]
#     dp[0][0] = 1
#     for ii in range(1,len(nums)+1):
#         for jj in range(Volume+1): # 注意从0开始，与求最大价值不同
#             if jj >= nums[ii-1]:
#                 dp[ii][jj] = (dp[ii-1][jj] #第ii件物品没装入背包的情况
#                             + dp[ii-1][jj-nums[ii-1]]) #第ii件物品装入背包的情况
#             else:
#                 dp[ii][jj] = dp[ii-1][jj]
#     print(dp[-1][-1])
# else:
#     print(0)

# # 思路2: 将区间分为左右两部分
# right_start = len(nums)//2 + len(nums)%2
# # 回溯求左区间元素取'+'或'-'之后所有元素之和，及其对应的数量，构建哈希表
# dict_left = {}
# def backtrack_left(nums, temp):
#     if len(nums) == 0:
#         if temp not in dict_left:
#             dict_left[temp] = 1
#         else:
#             dict_left[temp] += 1
#         return
#     else:
#         backtrack_left(nums[1:], temp+nums[0])
#         backtrack_left(nums[1:], temp-nums[0])
# backtrack_left(nums[0:right_start],0)
# # 回溯求右区间每个元素分别取'+'或'-'之后所有元素之和，判断其是否等于target - 左区间的元素之和
# # 如果是，通过哈希表累计统计
# global count
# count = 0
# def backtrack_right(nums, temp):
#     global count
#     if len(nums) == 0:
#         if target - temp in dict_left:
#             count += dict_left[target - temp]
#         return
#     else:
#         backtrack_right(nums[1:], temp+nums[0])
#         backtrack_right(nums[1:], temp-nums[0])
# backtrack_right(nums[right_start:],0)

# print(count)

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