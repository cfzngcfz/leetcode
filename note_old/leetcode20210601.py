# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:14:50 2021

@author: CC-i7-8750H
"""
# # 1074. 元素和为目标值的子矩阵数量

# matrix = [[0,1,0],[1,1,1],[0,1,0]]
# target = 0
# matrix = [[1,-1],[-1,1]]
# target = 0
# matrix = [[904]]
# target = 0

# # 思路：枚举子矩阵的上下边界，并计算出该边界内每列的元素和，则原问题转换成了一维的“560. 和为K的子数组”问题


# count = 0
# for i_start in range(len(matrix)):
#     temp = [0]*len(matrix[0])
#     for i_end in range(i_start,len(matrix)):
#         pre = []
#         dict_mp = {0:1}
#         for jj in range(len(matrix[0])):
#             temp[jj] += matrix[i_end][jj]
#             if jj == 0:
#                 pre.append(temp[0])
#             else:
#                 pre.append(temp[jj]+pre[-1])
#             if pre[jj]-target in dict_mp:
#                 count += dict_mp[pre[jj]-target]
#             if pre[jj] not in dict_mp:
#                 dict_mp[pre[jj]] = 1
#             else:
#                 dict_mp[pre[jj]] += 1
# print(count)


# # 523. 连续的子数组和
# nums = [23,2,4,6,7]
# k = 6
# # nums = [23,2,6,4,7]
# # k = 6

# # 思路:来源560. 和为K的子数组，但不同
# # pre[i] = nums[0~i]
# # nums[j~i] = pre[i] - pre[j-1]
# # if nums[j~i] % k = 0 => (pre[i] - pre[j-1]) % k = 0:
# #                      => pre[i] % k = pre[j-1] % k 
# # 由于 0 <= j < i, 所以只要查看 pre[i]%k 是否在 pre[-1]%k,pre[0]%,...,pre[i-2]%k 中出现过
# # 如果出现过返回True，否则返回False
# label = False
# pre = [nums[0]]
# set1 = set()
# for ii in range(1,len(nums)):
#     if ii == 1:
#         set1.add(0)
#     else:
#         set1.add(pre[ii-2]%k)
#     if (nums[ii]+pre[-1])%k not in set1:
#         pre.append(nums[ii]+pre[-1])
#     else:
#         label = True
#         break
# print(label)
        
        
# # 超时
# label = False
# for ii in range(len(nums)-1):
#     temp = nums[ii]
#     for jj in range(ii+1,len(nums)):
#         temp += nums[jj]
#         # print(ii,temp)
#         if temp%k == 0:
#             label = True
#             break
#     if label == True:
#         break
# print(label)

# # 525. 连续数组
# nums = [0,1,0]
# nums = [0,1,1,0,1,1,1,0]
# nums = [1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1]
# nums = [0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,1,1,0,0,1,1,0,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,0,1,1,0,1,1,1,0,0,1]
# nums = [1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,0]

# # 官方思路：将数组中的 0 视作 −1，则原问题转换成「求最长的连续子数组，其元素和为 0」
# # 转化后的思路与思路2类似，理解上更直观
# nums2 = []
# for num in nums:
#     if num == 0:
#         nums2.append(-1)
#     else:
#         nums2.append(1)
# pre = []
# dict_mp = {0:-1}
# max_len = 0
# for ii in range(len(nums2)):
#     if ii == 0:
#         pre.append(nums2[0])
#     else:
#         pre.append(nums2[ii]+pre[-1])
#     if pre[ii] in dict_mp:
#         max_len = max(max_len, ii - dict_mp[pre[ii]])
#     if pre[ii] not in dict_mp:
#         dict_mp[pre[ii]] = ii
# print(max_len)

# # 思路2：来源560. 和为K的子数组（求数量），本题目的不同之处在于，求子数组的最大长度
# # let pre[i] = sum(nums[0:i+1])
# # sum(nums[j:i+1]) = pre[i] - pre[j-1]
# # if sum(nums[j:i+1])*2 = i-j+1 (i.e., [j,i]区间内nums之和等于该区间长度一半)
# #     => 2*pre[i] - 2*pre[j-1] = i - (j-1)
# #     => 2*pre[i] - i = 2*pre[j-1] - (j-1)
# # 由于 0 <= j < i, 所以只要查找 2*pre[i]-i 是否等于
# # 2*pre[-1]+1,2*pre[0],...,2*pre[i`]-i`,...,2*pre[i-1]-(i-1)
# # 因为要找满足要求的子区间最大长度，且i`越小，区间长度i-i`(这里的i`指代推导过程中的j-1)越大
# # 所以在构建哈希表时，只需要记录2*pre[i`]-i`最早出现的索引i`，即dict_mp[2*pre[i`]-i`] = i`
# dict_mp = {1:-1} # 初始条件为 2*pre[-1]-(-1)
# pre = []
# count = 0
# max_len = 0
# for ii in range(len(nums)):
#     if ii == 0:
#         pre.append(nums[ii])
#     else:
#         pre.append(nums[ii] + pre[-1])
#     if 2*pre[ii] - ii in dict_mp:
#         jj = dict_mp[2*pre[ii] - ii]
#         max_len = max(max_len, ii-jj)
#     if 2*pre[ii] - ii not in dict_mp:
#         dict_mp[2*pre[ii] - ii] = ii
# print(max_len)

# # 动态规划在特定的一种情况下还需要枚举，超时
# dp = [0]*len(nums)
# dp[0] = 0
# for ii in range(1,len(nums)):
#     if nums[ii] != nums[ii-1]:
#         if ii-2 >= 0:
#             dp[ii] = dp[ii-2] + 2
#         else:
#             dp[ii] = 2
#     else:
#         if ii-dp[ii-1]-1 >= 0 and nums[ii] != nums[ii-dp[ii-1]-1]:
#             if ii-dp[ii-1]-2 >= 0:
#                 dp[ii] = dp[ii-1] + 2 + dp[ii-dp[ii-1]-2]
#             else:
#                 dp[ii] = dp[ii-1] + 2
#         else:
#             if nums[ii] == nums[max(ii-dp[ii-1], 0)]:
#                 dp[ii] = dp[ii-1]
#             else: #这种情况下，还需要循环，所以超时
#                 temp = 0
#                 len1 = 0
#                 for jj in range(ii,0,-2):
#                     temp += nums[jj]+nums[jj-1]
#                     if temp*2 == ii-jj+2:
#                         len1 = ii-jj+2
#                 dp[ii] = len1
# print(max(dp))

# # 超时，全枚举做验证
# dp2 = [0]*len(nums)
# dp2[0] = 0
# for ii in range(1,len(nums)):
#     for jj in range(ii-1,-1,-1):
#         if float(sum(nums[jj:ii])+nums[ii]) == float(ii-jj+1)/2:
#             dp2[ii] = ii-jj+1
# print(max(dp2))
#-----------------------------------------------------------------------------#
# # 1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？
# candiesCount = [7,4,5,3,8]
# queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
# candiesCount = [5,2,6,4,1]
# queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
# candiesCount = [16,38,8,41,30,31,14,45,3,2,24,23,38,30,31,17,35,4,9,42,28,18,37,18,14,46,11,13,19,3,5,39,24,48,20,29,4,19,36,11,28,49,38,16,23,24,4,22,29,35,45,38,37,40,2,37,8,41,33,8,40,27,13,4,33,5,8,14,19,35,31,8,8]
# queries = [[35,669,5],[72,822,74],[47,933,94],[62,942,85],[42,596,11],[56,1066,18],[54,571,45],[39,890,100],[3,175,26],[48,1489,37],[40,447,52],[30,584,7],[26,1486,38],[21,1142,21],[9,494,96],[56,759,81],[13,319,16],[20,1406,57],[11,1092,19],[24,670,67],[38,1702,33],[5,676,32],[50,1386,77],[36,1551,87],[29,1445,13],[58,977,13],[7,887,64],[37,1396,23],[0,765,69],[40,1083,86],[43,1054,49],[48,690,92],[28,1201,56],[47,948,43],[57,233,25],[32,1293,65],[0,1646,34],[43,1467,39],[39,484,23],[21,1576,69],[12,1222,68],[9,457,83],[32,65,9],[10,1424,42],[35,534,3],[23,83,22],[33,501,33],[25,679,51],[2,321,42],[1,240,68],[7,1297,42],[45,480,72],[26,1472,9],[6,649,90],[26,361,57],[49,1592,7],[11,158,95],[35,448,24],[41,1654,10],[61,510,43],[31,1230,95],[11,1471,12],[37,43,84],[56,1147,48],[69,1368,65],[22,170,24],[56,192,80],[34,1207,69],[1,1226,22],[37,1633,50],[11,98,58],[17,125,13],[0,1490,5],[37,1732,43],[45,793,14],[16,578,72],[50,241,78]]


# # 改进
# type_start = []
# type_end = []
# for ii in range(len(candiesCount)):
#     if ii == 0:
#         type_start.append(0)
#     else:
#         type_start.append(candiesCount[ii-1]+type_start[-1])
#     type_end.append(type_start[ii]+candiesCount[ii]-1)
# output = []
# for favoriteType, favoriteDay, dailyCap in queries:
#     if favoriteDay <= type_end[favoriteType] and type_start[favoriteType] <= min(type_end[-1], (favoriteDay+1)*dailyCap-1):
#         output.append(True)
#     else:
#         output.append(False)
# print(output)

# # 超时
# candies = []
# for ii in range(len(candiesCount)):
#     candies += [ii]*candiesCount[ii]
# output2 = []
# for jj in range(len(queries)):
#     if ((queries[jj][1]+1)*queries[jj][2] <= len(candies)
#         and candies[queries[jj][1]] <= queries[jj][0] <= candies[(queries[jj][1]+1)*queries[jj][2]-1]):
#         output2.append(True)
#     elif (queries[jj][1] < len(candies) < (queries[jj][1]+1)*queries[jj][2]
#         and candies[queries[jj][1]] <= queries[jj][0] <= candies[-1]):
#         output2.append(True)
#     elif queries[jj][1] == len(candies) and queries[jj][0] == candies[-1]:
#         output2.append(True)
#     else:
#         output2.append(False)
# print(output2)
# print(output == output2)
#-----------------------------------------------------------------------------#









