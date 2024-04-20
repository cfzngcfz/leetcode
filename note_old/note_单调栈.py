# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 11:37:04 2021

@author: CC-i7-11700
"""
nums = [1,7,5,1,9,2,5,1]
# nums = [9,7,6,7,6,9]
print('原数组:\n',nums)

print('\n问题1.1：右侧最近更大元素问题') #待完善备注
stack_value = [] #单调栈，记录右侧下一个的更大元素
stack_index = [] #单调栈，记录其索引
output_value = [None for _ in range(len(nums))] #找不到更大值时返回的默认输出
output_index = [-1 for _ in range(len(nums))] #找不到更大值时返回的默认索引
for ii in range(len(nums)-1,-1,-1): #从右侧往栈中添加元素
    # 当前元素nums[ii]与栈中的元素进行比较
    # 依次从栈中排除所有小于或等于当前元素nums[ii]的所有元素，直到栈为空或者栈的最后一个元素大于当前元素nums[ii]
    while len(stack_value) > 0 and nums[ii] >= stack_value[-1]:
        stack_value.pop() # 移除单调栈的最后一个元素
        stack_index.pop() # 移除单调栈的最后一个元素
    # 如果栈为空，说明右侧不存在比当前元素nums[ii]更大的元素，不进行任何操作
    # 如果栈不为空，必定存在当前元素nums[ii]必然小于栈的最后一个元素，
    # 也就是说，当前元素nums[ii]的右侧必然存在大于nums[ii]，距离最近的大于nums[ii]的元素是最后加入到栈中的元素，即为栈的最后一个元素
    if len(stack_value) > 0:
        output_value[ii] = stack_value[-1]
        output_index[ii] = stack_index[-1]
    # 将当前元素nums[ii] 添加到栈中
    stack_value.append(nums[ii])
    stack_index.append(ii)
    print(ii,'栈:',stack_value,'输出:',output_value)
print('右侧最近更大的元素:\n', output_value)
print('对应索引:\n', output_index)

print('\n问题1.2：右侧最近更小元素问题')
stack_value = []
stack_index = []
output_value = [None for _ in range(len(nums))]
output_index = [-1 for _ in range(len(nums))]
for ii in range(len(nums)-1,-1,-1):
    while len(stack_value) > 0 and nums[ii] <= stack_value[-1]: #较1.1改动
        stack_value.pop()
        stack_index.pop()
    if len(stack_value) > 0:
        output_value[ii] = stack_value[-1]
        output_index[ii] = stack_index[-1]
    stack_value.append(nums[ii])
    stack_index.append(ii)
print('右侧最近更小的元素:\n', output_value)
print('对应索引:\n', output_index)


print('\n问题2.1：左侧最近更大元素问题')
stack_value = []
stack_index = []
output_value = [None for _ in range(len(nums))]
output_index = [-1 for _ in range(len(nums))]
for ii in range(len(nums)): #较1.1改动
    while len(stack_value) > 0 and nums[ii] >= stack_value[-1]:
        stack_value.pop()
        stack_index.pop()
    if len(stack_value) > 0:
        output_value[ii] = stack_value[-1]
        output_index[ii] = stack_index[-1]
    stack_value.append(nums[ii])
    stack_index.append(ii)
print('左侧最近更大的元素:\n', output_value)
print('对应索引:\n', output_index)

print('\n问题2.2：左侧最近更小元素问题')
stack_value = []
stack_index = []
output_value = [None for _ in range(len(nums))]
output_index = [-1 for _ in range(len(nums))]
for ii in range(len(nums)): #较1.1改动
    while len(stack_value) > 0 and nums[ii] <= stack_value[-1]: #较1.1改动
        stack_value.pop()
        stack_index.pop()
    if len(stack_value) > 0:
        output_value[ii] = stack_value[-1]
        output_index[ii] = stack_index[-1]
    stack_value.append(nums[ii])
    stack_index.append(ii)
print('左侧最近更小的元素:\n', output_value)
print('对应索引:\n', output_index)
#-----------------------------------------------------------------------------#
# # question 84 柱状图中最大的矩形 已完成
# heights = [2,1,5,6,2,3]
# heights = [0,0,0,0,0]
# heights = [6,7,5,5,2,4,5,9,3] 

# # 方法一：单调栈
# temp = [] #单调栈，用于存储索引
# dp_left = [-1 for _ in range(len(heights))] #默认哨兵位
# # dp_right = [len(heights) for _ in range(len(heights))] #默认哨兵位
# for ii in range(len(heights)):
#     while len(temp) > 0 and heights[ii] <= heights[temp[-1]]:
#         # dp_right[temp[-1]] = ii #官方方法二，有点问题，与方法一的dp_right结果不一致
#         del(temp[-1])
#     if len(temp) > 0:
#         dp_left[ii] = temp[-1] #左侧最近的高度小于heights[ii]的柱子
#     temp.append(ii)
# print(dp_left)

# temp = [] #单调栈，用于存储索引
# dp_right = [len(heights) for _ in range(len(heights))] #默认哨兵位
# for ii in range(len(heights)-1,-1,-1):
#     while len(temp) > 0 and heights[ii] <= heights[temp[-1]]:
#         del(temp[-1])
#     if len(temp) > 0:
#         dp_right[ii] = temp[-1] #右侧最近的高度小于heights[ii]的柱子
#     temp.append(ii)
# print(dp_right)

# area = []
# for ii in range(len(heights)):
#     area.append(heights[ii]*(dp_right[ii]-dp_left[ii]-1))
# print(max(area))

# # 方法二
# def fenduan(heights2):
#     temp = [[]]
#     current_min = min(heights2)
#     area_new = current_min * len(heights2)
    
#     for jj in range(len(heights2)):
#         if heights2[jj] == current_min:
#             temp.append([])
#         else:
#             temp[-1].append(heights2[jj])
#     len_temp = len(temp)
#     for jj in range(len_temp):
#         if temp[len_temp-1-jj] == []:
#             del(temp[len_temp-1-jj])
#     return temp,area_new

# area = 0
# list_heights = [heights]
# while len(list_heights) > 0:
#     list_temp = []
#     for ii in range(len(list_heights)):
#         output,area_new = fenduan(list_heights[ii])
#         if area_new > area:
#             area = area_new
#         list_temp += output
#     list_heights = list_temp
#     # print(list_heights)
# print(area)    


# # question 85 最大矩形
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# # matrix = []
# # matrix = [["0"]]
# # matrix = [["1"]]
# # matrix = [["0","0"]]

# #方法一：将问题转化为每层求柱状图的最大面积
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
# # 1019. 链表中的下一个更大节点
# nums = [2,1,5]
# nums = [2,7,4,3,5]
# nums = [1,7,5,1,9,2,5,1]
# nums = [9,7,6,7,6,9]

# # yuer解答，以转化为模板
# stack = []
# output = [0]*len(nums)
# for ii in range(len(nums)-1,-1,-1):
#     while stack and nums[ii] >= stack[-1]:
#         stack.pop()
#     # 此时如果右侧没有大于nums[j]的元素 则stack为空 res[j]=0 不需要改变
#     if stack:
#         output[ii] = stack[-1]
#     stack.append(nums[ii])
# print(output)

# # 自己的思路
# output = [0 for _ in range(len(nums))]
# stack = [nums[0]]
# stack_index = [0]
# for ii in range(1,len(nums)):
#     while len(stack) > 0 and nums[ii] > stack[-1]:
#         output[stack_index[-1]] = nums[ii]
#         del(stack[-1])
#         del(stack_index[-1])
#     stack.append(nums[ii])
#     stack_index.append(ii)
# print(output)









