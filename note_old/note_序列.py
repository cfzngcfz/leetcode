# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:24:18 2021

@author: CC-i7-8750H
"""

#-----------------------------------------------------------------------------#
# question 11 盛最多水的容器(任意两根柱子围为的最大面积) 窗口滑动
height = [1454,2249,4922,5151,7349,1022,2787,2931,7155,2802,2041,190]
area = 0
index_left = 0
index_right = len(height)-1
while index_left < index_right:
    area_new = min(height[index_left],height[index_right])*(index_right-index_left)
    area = max(area, area_new)
    if height[index_left] <= height[index_right]:
        index_left += 1
    else:
        index_right -= 1
print(area)

#-----------------------------------------------------------------------------#
# # question 84 柱状图中最大的矩形 已完成
heights = [6,7,5,5,2,4,5,9,3] 

# 方法一：单调栈
temp = [] #单调栈，用于存储索引
dp_left = [-1 for _ in range(len(heights))] #默认哨兵位
# dp_right = [len(heights) for _ in range(len(heights))] #默认哨兵位
for ii in range(len(heights)):
    while len(temp) > 0 and heights[ii] <= heights[temp[-1]]:
        # dp_right[temp[-1]] = ii #官方方法二，有点问题，与方法一的dp_right结果不一致
        del(temp[-1])
    if len(temp) > 0:
        dp_left[ii] = temp[-1] #左侧最近的高度小于heights[ii]的柱子
    temp.append(ii)

temp = [] #单调栈，用于存储索引
dp_right = [len(heights) for _ in range(len(heights))] #默认哨兵位
for ii in range(len(heights)-1,-1,-1):
    while len(temp) > 0 and heights[ii] <= heights[temp[-1]]:
        del(temp[-1])
    if len(temp) > 0:
        dp_right[ii] = temp[-1] #右侧最近的高度小于heights[ii]的柱子
    temp.append(ii)
print(dp_right)

area = []
for ii in range(len(heights)):
    area.append(heights[ii]*(dp_right[ii]-dp_left[ii]-1))
print(max(area))

# # question 85 最大矩形 
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# matrix = []

# def bar_area(heights):
#     temp = [] #单调栈，用于存储索引
#     dp_left = [-1 for _ in range(len(heights))] #默认哨兵位
#     for ii in range(len(heights)):
#         while len(temp) > 0 and heights[ii] <= heights[temp[-1]]:
#             del(temp[-1])
#         if len(temp) > 0:
#             dp_left[ii] = temp[-1] #左侧最近的高度小于heights[ii]的柱子
#         temp.append(ii)
    
#     temp = [] #单调栈，用于存储索引
#     dp_right = [len(heights) for _ in range(len(heights))] #默认哨兵位
#     for ii in range(len(heights)-1,-1,-1):
#         while len(temp) > 0 and heights[ii] <= heights[temp[-1]]:
#             del(temp[-1])
#         if len(temp) > 0:
#             dp_right[ii] = temp[-1] #右侧最近的高度小于heights[ii]的柱子
#         temp.append(ii)
    
#     area = []
#     for ii in range(len(heights)):
#         area.append(heights[ii]*(dp_right[ii]-dp_left[ii]-1))
#     return max(area)

# record = 0
# if len(matrix) > 0:
#     dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
#     for jj in range(len(matrix[0])):
#         if matrix[0][jj] == '1':
#             dp[0][jj] = 1
#     record = max(bar_area(dp[0]), record)
#     for ii in range(1,len(matrix)):
#         for jj in range(len(matrix[0])):
#             if matrix[ii][jj] == '1':
#                 dp[ii][jj] = dp[ii-1][jj] + 1
#         record = max(bar_area(dp[ii]), record)
    
# print(record)
#-----------------------------------------------------------------------------#
# 53. 最大子序和（和最大的连续子数组）
#动态规划
# dp[i] 代表以第i个数字结尾的「连续子数组的最大和」
# dp[i] = max(dp[i-1]+num[i], num[i])
nums = [-2,1,-3,4,-1,2,1,-5,4]

dp = [0 for _ in range(len(nums))]
dp[0] = nums[0]
for ii in range(1,len(nums)):
    dp[ii] = max(dp[ii-1]+nums[ii], nums[ii])
print(max(dp))
#-----------------------------------------------------------------------------#
# question 300 最长递增子序列(递增，不连续，不改变相对顺序) #已笔记

# # question 354 俄罗斯套娃信封问题  300.最长递增子序列 的二维拓展
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

# # 368. 最大整除子集 思路同300.最长递增子序列
# nums = [1,2,3]
# # nums = [1,2,4,8]
# # nums = [2,4,8,11]
# # nums = [3,4,16,8]
# nums = [4,8,10,240]

# # 动态规划思路
# dict1 = {}
# nums.sort()
# for ii in range(len(nums)):
#     dict1[nums[ii]] = [nums[ii]]
#     count2 = 0
#     index = -1
#     for jj in range(ii-1,-1,-1):
#         if nums[ii]%nums[jj] == 0:
#             if len(dict1[nums[jj]]) > count2:
#                 index = jj
#                 count2 = len(dict1[nums[jj]])
#     if index != -1:
#         dict1[nums[ii]] = dict1[nums[index]] + dict1[nums[ii]]
# print(dict1)
# count = 0
# output = []
# for key in list(dict1.keys()):
#     if len(dict1[key]) > count:
#         output = dict1[key]
#         count = len(dict1[key])
# print(output)

# 674. 最长连续递增序列（递增，连续，不改变相对顺序）
nums = [1,3,5,4,7]

if len(nums) > 0:
    record = 0
    count = 1
    for ii in range(1,len(nums)):
        if nums[ii] > nums[ii-1]:
            count += 1
        else:
            record = max(record,count)
            count = 1
    record = max(record,count)
    print(record)
else:
    print(0)
    
# # 128. 最长连续序列（递增且步长为1，不连续，可改变相对顺序）
# nums = [100,4,200,1,3,2]
# if len(nums) > 0:
#     nums.sort()
#     output = 0
#     count = 1
#     for ii in range(1,len(nums)):
#         if nums[ii] == nums[ii-1]+1:
#             count += 1
#         elif nums[ii] == nums[ii-1]:
#             continue
#         else:
#             output = max(output, count)
#             count = 1
#     output = max(output, count)
#     print(output)
# else:
#     print(0)

# 560. 和为K的子数组
nums = [1,1,1]
k = 2
nums = [1]
k = 0

# 思路：前缀和+哈希表（560, 930, 1248）
# 前缀和 pre[ii] = pre[ii−1] + nums[ii]
# 根据前缀和定义，[i_start,ii]闭区间内元素之和（记为k），可以表示为 pre[ii] - pre[i_start-1] = k
# 目标为获取 以第ii个元素结尾的连续子数组 之和等于k的数量，
# 如果 [jj,ii]闭区间内元素之和等于k，则pre[jj]一定等于pre[ii] - k
# 由于 i_start 的取值范围为[0, ii]，只需要在前缀和pre[-1],pre[0],...,pre[ii-1]中查找pre[ii]-k出现的次数，即为所求
# 利用dict_mp记录前缀和及出现的次数，dict_map[pre[ii]-k]即为所求
pre = [] # 记录前缀和
dict_mp = {0:1} #记录前缀和pre[ii](key)，以及pre[ii]出现的次数(value)
# 初始条件为pre[-1] = 0,即nums为空时，区间和 0 出现了1次，所以dict_mp = {0:1}
count = 0 
for ii in range(len(nums)):
    if ii == 0:
        pre.append(nums[0])
    else:
        pre.append(nums[ii]+pre[-1])
        
    # 计算以第ii个元素结尾的连续子数组 之和等于k的数量，即pre[ii]-k在前缀和pre[-1],pre[0],...,pre[ii-1]中出现的次数
    if pre[ii]-k in dict_mp:
        count += dict_mp[pre[ii]-k] 
    
    # 由于上一步查找中不包含当前的前缀和pre[ii]，因此先执行查找，再往Hashmap中添加当前前缀和pre[ii]
    if pre[ii] not in dict_mp:
        dict_mp[pre[ii]] = 1
    else:
        dict_mp[pre[ii]] += 1
print(count)

# # 930. 和相同的二元子数组
# nums = [1,0,1,0,1]
# goal = 2
# # nums = [0,0,0,0,0]
# # goal = 0

# # 思路：前缀和+哈希表，思路同560
# dict1 = {}
# dp = [0 for _ in range(len(nums))]
# count = 0
# temp = nums[0]

# if temp == goal:
#     count += 1
# if temp not in dict1:
#     dict1[temp] = 1
# else:
#     dict1[temp] += 1
# for ii in range(1,len(nums)):
#     temp += nums[ii]
#     if temp >= goal:
#         if temp == goal:
#             count += 1
#         if temp - goal in dict1:
#             count += dict1[temp - goal]
#     if temp not in dict1:
#         dict1[temp] = 1
#     else:
#         dict1[temp] += 1
# print(count)

# # 1248. 统计「优美子数组」
# nums = [1,1,2,1,1]
# k = 3
# nums = [2,4,6]
# k = 1
# nums = [2,2,2,1,2,2,1,2,2,2]
# k = 2

# # 思路：预处理（奇数变成1，偶数变成0，问题转化为连续子序列之和等于k），再前缀和+哈希表
# for ii in range(len(nums)):
#     if nums[ii]%2 == 1:
#         nums[ii] = 1
#     else:
#         nums[ii] = 0

# pre = []
# dict_mp = {0:1}
# count = 0 
# for ii in range(len(nums)):
#     if ii == 0:
#         pre.append(nums[0])
#     else:
#         pre.append(nums[ii]+pre[-1])
        
#     if pre[ii]-k in dict_mp:
#         count += dict_mp[pre[ii]-k] 
    
#     if pre[ii] not in dict_mp:
#         dict_mp[pre[ii]] = 1
#     else:
#         dict_mp[pre[ii]] += 1
# print(count)
#-----------------------------------------------------------------------------#
# 双序列问题
# # 5756. 两个数组最小的异或值之和
# nums1 = [1,2]
# nums2 = [2,3] # 2
# nums1 = [1,0,3]
# nums2 = [5,3,4] # 8
# nums1 = [72,97,8,32,15]
# nums2 = [63,97,57,60,83] # 152
# nums1 = [100,26,12,62,3,49,55,77,97]
# nums2 = [98,0,89,57,34,92,29,75,13] # 200

# 思路:状态压缩动态规划
# dp[mask_int] 表示状态mask_int下的最小的异或值之和
# mask_int 与其二进制(mask_bin)是一一映射到，mask_bin中'1'的数量(记为count)由mask_int决定
# nums1[0:count]  与  mask_bin中count个'1'所在位置对应的nums2元素  组成的最小的异或值之和

# dp = [float("inf")]*2**len(nums1)
# dp[0] = 0 # 边界条件
# for mask_int in range(1, 2**len(nums1)):
#     mask = bin(mask_int)[2:]
#     count = mask.count('1')
#     for index in range(len(nums2)): # 从nums2中选取一个位置index
#         if mask_int & (1 << index) > 0: #如果mask_bin的第index个位置为1
#         # 1 << index 是第index位置为1，其他位置为0的二进制所对应的十进制数字
#         # 如果 mask_bin的第index个位置也为1，mask_int 和 1<<index 的异或与大于0
#         # 否则，mask_bin的第index个位置为0，1<<index的第index个位置为1，该位置的异或与为0
#         # mask_bin的其他位置无论为何值，1<<index的其他位置均为0，其他位置的异或与也为0
#         # 因此，mask_int 和 1<<index 的异或与 等于0
#             dp[mask_int] = min(dp[mask_int],
#                                dp[mask_int^(1<<index)] + (nums1[count-1]^nums2[index])) #核心
#             # dp[mask_int] 由 mask_bin 中某个'1'变为'0'所应对的状态mask_int`决定
#             # mask_int` ^ (1<<index) = mask_int => mask_int ^ (1<<index) = mask_int`
#             # mask_bin`中'1'的数量一定为count-1个
#             # 再加上 nums1的第count个元素 和 '1'->'0'位置所对应的nums2中的元素 的异或值
# print(dp[-1])

# # 超时
# from itertools import permutations
# # for ii in range(len(nums2)-1,-1,-1):
# #     if nums2[ii] in nums1:
# #         del(nums1[nums1.index(nums2[ii])])
# #         del(nums2[ii])
# perms = list(permutations(nums2, len(nums2)))
# temp = float('inf')
# for perm in perms:
#     count = 0
#     for ii in range(len(nums1)):
#         count += nums1[ii]^perm[ii]
#     temp = min(temp, count)
# print(temp)

# # 如果换成 两个数组最小的乘积之和？
# # 方法1
# dp = [float("inf")]*2**len(nums1)
# dp[0] = 0 # 边界条件
# for mask_int in range(1, 2**len(nums1)):
#     mask = bin(mask_int)[2:]
#     count = mask.count('1')
#     for index in range(len(nums2)): # 从nums2中选取一个位置index
#         if mask_int & (1 << index) > 0: #如果mask_bin的第index个位置为1
#             dp[mask_int] = min(dp[mask_int],
#                                dp[mask_int^(1<<index)] + (nums1[count-1]*nums2[index])) #核心
# print(dp[-1])
# #方法2，耗时长用于验证
# from itertools import permutations
# # for ii in range(len(nums2)-1,-1,-1):
# #     if nums2[ii] in nums1:
# #         del(nums1[nums1.index(nums2[ii])])
# #         del(nums2[ii])
# perms = list(permutations(nums2, len(nums2)))
# temp = float('inf')
# for perm in perms:
#     count = 0
#     for ii in range(len(nums1)):
#         count += nums1[ii]*perm[ii]
#     temp = min(temp, count)
# print(temp)

#-----------------------------------------------------------------------------#
# # 123. 买卖股票的最佳时机 III （限购买次数）
# prices = [3,3,5,0,0,3,1,4]
# prices = [1,4,1,4,3,1]

# dp = [[0]*len(prices) for _ in range(4)]
# dp[0][0] = dp[2][0] = -prices[0]
# dp[1][0] = dp[3][0] = 0
# for jj in range(1,len(prices)):
#     dp[0][jj] = max(dp[0][jj-1], -prices[jj]) #只进行过一次买操作
#     dp[1][jj] = max(dp[1][jj-1], dp[0][jj-1]+prices[jj]) #进行了一次买操作和一次卖操作，即完成了一笔交易
#     dp[2][jj] = max(dp[2][jj-1], dp[1][jj-1]-prices[jj]) #在完成了一笔交易的前提下，进行了第二次买操作
#     dp[3][jj] = max(dp[3][jj-1], dp[2][jj-1]+prices[jj]) #完成了全部两笔交易
# print(max(dp[-1]))

# # 188. 买卖股票的最佳时机 IV（限购买次数）
# prices = [3,2,6,5,0,3]

# dp = [[0]*len(prices) for _ in range(2*k)]
# for ii in range(len(dp)):
#     if ii%2 == 0:
#         dp[ii][0] = -prices[0]
#     else:
#         dp[ii][0] = 0
# for ii in range(len(dp)):
#     for jj in range(1,len(dp[0])):
#         if ii%2 == 0:
#             if ii == 0:
#                 dp[ii][jj] = max(dp[ii][jj-1], -prices[jj])
#             else:
#                 dp[ii][jj] = max(dp[ii][jj-1], dp[ii-1][jj-1]-prices[jj])
#         else:
#             dp[ii][jj] = max(dp[ii][jj-1], dp[ii-1][jj-1]+prices[jj])
# print(max(dp[-1]))
# # 同类型题目question 121 买卖股票的最佳时机

# # 122. 买卖股票的最佳时机 II（不限购买次数）
# prices = [7,1,5,3,6,4]
# # prices = [1,2,3,4,5]
# # 方法一：贪心
# temp = 0
# for ii in range(1,len(prices)):
#     if prices[ii] > prices[ii-1]:
#         temp += prices[ii] - prices[ii-1]
# print(temp)
# # 方法二：动态规划
# dp = [[0]*len(prices) for _ in range(2)]
# dp[0][0] = -prices[0]
# for ii in range(1,len(prices)):
#     dp[0][ii] = max(dp[0][ii-1], dp[1][ii-1]-prices[ii]) #持有状态
#     dp[1][ii] = max(dp[1][ii-1], dp[0][ii-1]+prices[ii]) #空仓状态
# print(dp[1][-1])

# # 714. 买卖股票的最佳时机含手续费（不限购买次数）
# prices = [1, 3, 2, 8, 4, 9]
# fee = 2

# dp = [[0]*len(prices) for _ in range(2)]
# dp[0][0] = -prices[0]-fee
# for ii in range(1,len(prices)):
#     dp[0][ii] = max(dp[0][ii-1], dp[1][ii-1]-prices[ii]-fee) #持有状态
#     dp[1][ii] = max(dp[1][ii-1], dp[0][ii-1]+prices[ii]) #空仓状态
# print(dp[1][-1])

# # 309. 最佳买卖股票时机含冷冻期（不限购买次数）
# prices = [1,2,3,0,2]

# dp = [[0]*len(prices) for _ in range(2)]
# dp[0][0] = -prices[0]
# dp[1][0] = 0
# dp[0][1] = max(dp[0][0], dp[1][0]-prices[1])
# dp[1][1] = max(dp[1][0], dp[0][0]+prices[1])
# for ii in range(2,len(prices)):
#     dp[0][ii] = max(dp[0][ii-1], dp[1][ii-2]-prices[ii]) #持有状态
#     dp[1][ii] = max(dp[1][ii-1], dp[0][ii-1]+prices[ii]) #空仓状态
# print(dp[1][-1])
#-----------------------------------------------------------------------------#
