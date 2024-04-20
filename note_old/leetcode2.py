# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 03:06:16 2021

@author: CC-i7-1065G7
"""

#-----------------------------------------------------------------------------#
# # question 4 寻找两个正序数组的中位数
# # nums1 = [1,3]
# # nums2 = [2]
# nums1 = [1,2]
# nums2 = [3,4]

# nums3 = nums1 + nums2
# nums3.sort()

# if len(nums3)%2 == 1:
#     output = nums3[len(nums3)//2]
# else:
#     output = nums3[len(nums3)//2 -1]*0.5 + nums3[len(nums3)//2]*0.5
# print(output)
#-----------------------------------------------------------------------------#
# # question 6 Z字形变换 已完成
# # s = "PAYPALISHIRING"
# # numRows = 3
# # s = "PAYPALISHIRING"
# # numRows = 4
# s = "AB"
# numRows = 1
# if numRows > 1:
#     record = [[] for _ in range(numRows)]
#     label = 0
#     for ii in range(len(s)):
#         if label == 0:
#             delta = 1
#         elif label == numRows-1:
#             delta = -1
        
#         record[label].append(s[ii])
#         label += delta
#     output = ''
#     for ii in range(len(record)):
#         for jj in range(len(record[ii])):
#             output = output + record[ii][jj]
# elif numRows == 1:
#     output = s
# print(output)
#-----------------------------------------------------------------------------#
# # question 7 整数反转 已完成
# x = 123
# # x = -123
# # x = 0
# num_str = ['1','2','3','4','5','6','7','8','9','0']
# x2_str = ''
# x_str = str(x)
# for ii in range(len(x_str)):
#     if x_str[len(x_str)-ii-1] in num_str:
#         x2_str = x2_str + x_str[len(x_str)-ii-1]
#     elif x_str[len(x_str)-ii-1] == '-':
#         x2_str = x_str[len(x_str)-ii-1] + x2_str
# x2 = int(x2_str)
# if x2 < -2**31 or x2 > 2**31-1:
#     x2 = 0
# print(x2)
#-----------------------------------------------------------------------------#
# # question 8 字符串转换整数 (atoi) 已完成
# s = "  -0012a42"
# # s = "00000-42a1234"
# # s = "4193 with words"
# # s = "words and 987"
# # s = '   -42'
# # s = '3.14d15'
# # s = "   +0 123"
# # s = "123-"
# # s = "-5-"
# # s = "+-12"
# ss = s.split(' ')
# for s2 in ss:
#     if '' == s2:
#         continue
#     elif '0' in s2 or '1' in s2 or '2' in s2 or '3' in s2 or '4' in s2 or '5' in s2 or '6' in s2 or '7' in s2 or'8' in s2 or '9' in s2:
#         s = s2
#         break
#     else:
#         s = '0'
#         break
# num = ''
# label_stop2 = 0 #遇到+-数字终止
# label_stop = 0 #用于判断数字后是否有+=
# label_zhengfu = 1
# num_str = ['1','2','3','4','5','6','7','8','9','0']
# for ii in range(len(s)):
#     if s[ii] == '-':
#         label_stop += 1
#         if label_stop <= 1:
#             label_zhengfu = -1
#     elif s[ii] == '+':
#         label_stop += 1
#     elif s[ii] in num_str:
#         num = num + s[ii]
#         label_stop = 1
#     else:
#         label_stop2 = 1
#     if label_stop > 1 or label_stop2 == 1:
#         break
# if num == '':
#     output = 0
# else: 
#     output = int(num)*label_zhengfu
#     if output < -2**31:
#         output = -2**31
#     elif output > 2**31-1:
#         output = 2**31-1    
# print(output)
#-----------------------------------------------------------------------------#
# #question 9 回文数 已完成
# x = 121
# # x = -121
# # x = 10
# # x = -101
# x_str = str(x)
# x2_str = ''
# for s in x_str:
#     x2_str = s + x2_str
# print(x_str, x2_str, x_str == x2_str)
#-----------------------------------------------------------------------------#
# # question 10 正则表达式匹配 已完成 动态规划
# s = "aab"
# p = "c*a*b"
# # s = "a"
# # p = "ab*a"

# def match(s1,p1):
#     if p1 == '.':
#         return True
#     else:
#         return s1 == p1

# dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
# dp[0][0] = True
# for jj in range(1,len(p)+1):
#     if p[jj-1] == '*':
#         dp[0][jj] = dp[0][jj-2]
        
# for ii in range(1,len(s)+1):
#     for jj in range(1,len(p)+1):
#         if p[jj-1] != '*':
#             if match(s[ii-1],p[jj-1]): # 如果s的第ii个字符与p的第jj个字符匹配
#                 dp[ii][jj] = dp[ii][jj] or dp[ii-1][jj-1]
#         else:
#             if match(s[ii-1],p[jj-2]): # 如果s的第ii个字符与p的第jj-1个字符匹配
#                 dp[ii][jj] = dp[ii][jj] or dp[ii][jj-2] or dp[ii-1][jj]
#             else: #字母+* 组合 直接删除Wa
#                 dp[ii][jj] = dp[ii][jj] or dp[ii][jj-2]
# print(dp[-1][-1])

# # 官方代码
# m, n = len(s), len(p)
# def matches(i: int, j: int) -> bool:
#     if i == 0:
#         return False
#     if p[j - 1] == '.':
#         return True
#     return s[i - 1] == p[j - 1]
# f = [[False] * (n + 1) for _ in range(m + 1)]
# f[0][0] = True
# for i in range(m + 1):
#     for j in range(1, n + 1):
#         if p[j - 1] == '*':
#             f[i][j] |= f[i][j - 2]
#             if matches(i, j - 1):
#                 f[i][j] |= f[i - 1][j]
#         else:
#             if matches(i, j):
#                 f[i][j] |= f[i - 1][j - 1]
# print(f[-1][-1])

# # question 44 通配符匹配 已完成 动态规划
# # s = "aa"
# # p = "a"
# # s = "aa"
# # p = "*"
# # s = "cb"
# # p = "?a"
# s = "adceb"
# p = "*a*b"
# # s = "acdcb"
# # p = "a*c?b"
# # s = "ab"
# # p = "?*"

# dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
# dp[0][0] = True
# for jj in range(1,len(p)+1):
#     if p[jj-1] == '*':
#         dp[0][jj] = dp[0][jj] or dp[0][jj-1]
# for ii in range(1,len(s)+1):
#     for jj in range(1,len(p)+1):
#         if p[jj-1] != '*':
#             if  p[jj-1] != '?':
#                 dp[ii][jj] = dp[ii-1][jj-1] and s[ii-1] == p[jj-1]
#             else:
#                 dp[ii][jj] = dp[ii-1][jj-1]
#         else:
#             dp[ii][jj] = dp[ii-1][jj] or dp[ii][jj-1]
# print(dp[-1][-1])
# # # 解题思路
# # if p[j] != '*':
# #     d[i][j] = d[i-1][j-1] and (s[i] and p[j] match, i.e., s[i] == p[j] or p[j] == '?')
# # if p[j] == '*':
# #     dp[i][j] = dp[i-1][j]     #假设'*'与s[i]匹配，考虑s[i-1]与p[j](即'*')的结果
# #                or dp[i][j-1]  #假设'*'不与s[i]匹配，考虑s[i]与p[j-1](即'*'前一个)的结果
#-----------------------------------------------------------------------------#
# # question 11 盛最多水的容器 窗口滑动 已完成
# height = [1454,2249,4922,5151,7349,1022,8655,8124,2157,2303,5213]
# area = 0
# index1 = 0
# index2 = len(height)-1
# while index2 - index1 >= 1:
#     area_new = min(height[index1],height[index2])*(index2-index1)
#     if area_new > area:
#         area = area_new
#     if min(height[index1],height[index2]) == height[index1]:
#         index1 += 1
#     else:
#         index2 = index2 -1
# print(area)
#-----------------------------------------------------------------------------#
# # question 12 整数转罗马数字 已完成
# # roma = [[1000,'M'],[500,'D'],[100,'C'],[50,'L'],[10,'X'],[5,'V'],[1,'I']]
# num = 1994
# roma = ''
# while num > 0:
#     if len(str(num)) == 4:
#         roma += 'M'*(num//1000)
#         num = num - num//1000*1000
#     elif len(str(num)) == 3:
#         if num//100 < 4:
#             roma += 'C'*(num//100)
#         elif num//100 == 4:
#             roma += 'CD'
#         elif num//100 > 4 and num//100 < 9:
#             roma = roma + 'D' + ((num-500)//100)*'C'
#         elif num//100 == 9:
#             roma += 'CM'
#         num = num - num//100*100
#     elif len(str(num)) == 2:
#         if num//10 < 4:
#             roma += 'X'*(num//10)
#         elif num//10 == 4:
#             roma += 'XL'
#         elif num//10 > 4 and num//10 < 9:
#             roma = roma + 'L' + ((num-50)//10)*'X'
#         elif num//10 == 9:
#             roma += 'XC'
#         num = num - num//10*10
#     elif len(str(num)) == 1:
#         if num < 4:
#             roma += 'I'*num
#         elif num == 4:
#             roma += 'IV'
#         elif num > 4 and num < 9:
#             roma = roma + 'V' + (num-5)*'I'
#         elif num == 9:
#             roma += 'IX'
#         num = num - num
# print(roma)
#-----------------------------------------------------------------------------#
# # question 13 罗马数字转整数 已完成
# # I             1
# # V             5
# # X             10
# # L             50
# # C             100
# # D             500
# # M             1000

# s = "MDLXX"
# num = 0
# index = 0
# while index <= len(s)-1:
#     if s[index] == 'M':
#         num += 1000
#         index += 1
#     elif s[index] == 'C' and index < len(s)-1:
#         if s[index+1] == 'M':
#             num += 900
#             index += 2
#         elif s[index+1] == 'D':
#             num += 400
#             index += 2
#         else:
#             num += 100
#             index += 1
#     elif s[index] == 'C' and index == len(s)-1:
#         num += 100
#         index += 1
#     elif s[index] == 'D':
#         num += 500
#         index += 1
#     elif s[index] == 'X' and index < len(s)-1:
#         if s[index+1] == 'C':
#             num += 90
#             index += 2
#         elif s[index+1] == 'L':
#             num += 40
#             index += 2
#         else:
#             num += 10
#             index += 1
#     elif s[index] == 'X' and index == len(s)-1:
#         num += 10
#         index += 1
#     elif s[index] == 'L':
#         num += 50
#         index += 1
#     elif s[index] == 'I' and index < len(s)-1:
#         if s[index+1] == 'X':
#             num += 9
#             index += 2
#         elif s[index+1] == 'V':
#             num += 4
#             index += 2
#         else:
#             num += 1
#             index += 1
#     elif s[index] == 'I' and index == len(s)-1:
#         num += 1
#         index += 1
#     elif s[index] == 'V':
#         num += 5
#         index += 1
# print(num)
#-----------------------------------------------------------------------------#
# # question 14 最长公共前缀 已完成
# strs = ["flower","flow","flight"]
# # strs = ["dog","racecar","car"]
# strs = ["ab", "a"]

# label = 1
# index = 0
# output = ''
# if len(strs) > 1:
#     maxlen = min([len(strs[ii]) for ii in range(len(strs))])
#     if maxlen > 0:
#         while label == 1 and index < maxlen:
#             ss = strs[0][index]
#             for ii in range(len(strs)-1):
#                 if strs[ii+1][index] != ss:
#                     label = 0
#                     break
#             if label == 1:
#                 output = output + ss
#                 index += 1
# elif len(strs) == 1:
#     output = strs[0]
# print(output)
#-----------------------------------------------------------------------------#
# # question 15 三数之和 已完成 双指针
# # nums = [-1,0,1,2,-1,-4]
# # nums = []
# # nums = [0]
# nums = [0,2]

# # 排序（特点避免重复） + 双指针法（特点第二个数增大，第三个数减小）
# record = []
# nums.sort()
# if len(nums) > 2:
#     for ii in range(len(nums)-2):
#         index_left = ii+1
#         index_right = len(nums)-1
#         while index_left < index_right:
#             if nums[index_left] + nums[index_right] < -nums[ii]:
#                 index_left += 1
#             elif nums[index_left] + nums[index_right] > -nums[ii]:
#                 index_right = index_right - 1
#             else:
#                 if [nums[ii],nums[index_left],nums[index_right]] not in record:
#                     record.append([nums[ii],nums[index_left],nums[index_right]])
#                 index_left += 1
#                 index_right = index_right - 1
# print(record)
# # # 超时- 三层循环
# # record = []
# # if len(nums) > 2:
# #     for ii in range(len(nums)-2):
# #         for jj in range(ii+1,len(nums)-1):
# #             for kk in range(jj+1,len(nums)):
# #                 if nums[ii]+nums[jj]+nums[kk] == 0 and [nums[ii],nums[jj],nums[kk]] not in record:
# #                     record.append([nums[ii],nums[jj],nums[kk]])
# # print(record)

# # question 18 四数之和 已完成
# nums = [1,0,-1,0,-2,2]
# nums = []
# target = 0

# nums.sort()
# record = []
# if len(nums) > 3:
#     for ii in range(len(nums)-3):
#         for jj in range(ii+1,len(nums)-2):
#             index_left = jj+1
#             index_right = len(nums)-1
#             while index_left < index_right:
#                 if nums[index_left] + nums[index_right] < target - nums[ii] - nums[jj]:
#                     index_left += 1
#                 elif nums[index_left] + nums[index_right] > target - nums[ii] - nums[jj]:
#                     index_right = index_right - 1
#                 else:
#                     if [nums[ii],nums[jj],nums[index_left],nums[index_right]] not in record:
#                         record.append([nums[ii],nums[jj],nums[index_left],nums[index_right]])
#                     index_left += 1
#                     index_right = index_right - 1
# print(record)

# # 454. 四数相加 II
# nums1 = [0,1,-1]
# nums2 = [-1,1,0]
# nums3 = [0,0,1]
# nums4 = [-1,1,1]

# # 分两组循环 + 哈希，复杂度降低至O(n**2)
# dict1 = {}
# for ii in range(len(nums1)):
#     for jj in range(len(nums2)):
#         if nums1[ii]+nums2[jj] not in dict1:
#             dict1[nums1[ii]+nums2[jj]] = 1
#         else:
#             dict1[nums1[ii]+nums2[jj]] += 1
# count = 0
# for ii in range(len(nums3)):
#     for jj in range(len(nums4)):
#         if -nums3[ii]-nums4[jj] in dict1:
#             count += dict1[-nums3[ii]-nums4[jj]]
# print(count)

# # 超时 - 无序字典
# dict1 = {}
# dict2 = {}
# dict3 = {}
# dict4 = {}
# for ii in range(len(nums1)):
#     if nums1[ii] not in dict1:
#         dict1[nums1[ii]] = 1
#     else:
#         dict1[nums1[ii]] += 1
#     if nums2[ii] not in dict2:
#         dict2[nums2[ii]] = 1
#     else:
#         dict2[nums2[ii]] += 1
#     if nums3[ii] not in dict3:
#         dict3[nums3[ii]] = 1
#     else:
#         dict3[nums3[ii]] += 1
#     if nums4[ii] not in dict4:
#         dict4[nums4[ii]] = 1
#     else:
#         dict4[nums4[ii]] += 1
# count = 0
# for num1 in dict1.keys():
#     for num2 in dict2.keys():
#         for num3 in dict3.keys():
#             if -num1-num2-num3 in dict4:
#                 count += dict1[num1]*dict2[num2]*dict3[num3]*dict4[-num1-num2-num3]
# print(count)
#-----------------------------------------------------------------------------#
# # question 16 最接近的三数之和 已完成
# nums = [-1,2,1,-4]
# target = 1
# output = 10**5
# for ii in range (len(nums)-2):
#     for jj in range(ii+1,len(nums)-1):
#         for kk in range(jj+1, len(nums)):
#             # print(ii,jj,kk)
#             output_new = abs(nums[ii]+nums[jj]+nums[kk]-target)
#             if output_new < output:
#                 output = output_new
#                 output2 = nums[ii]+nums[jj]+nums[kk]
# print(output2)
#-----------------------------------------------------------------------------#
# # question 20 有效的括号 - 已完成
# # s = "()"
# # s = "()[]{}"
# # s = "(]"
# # s = "([)]"
# # s = "{[]}"
# # s = ']['
# # s = '['
# s = "[([]])"

# record = []
# output = True
# for ss in s:
#     if ss == '(':
#         record.append(')')
#     elif ss == '[':
#         record.append(']')
#     elif ss == '{':
#         record.append('}')
#     elif ss == ')':
#         if len(record) == 0 or ss != record[-1]:
#             output = False
#             break
#         else:
#             record = record[0:-1]
#     elif ss == ']':
#         if len(record) == 0 or ss != record[-1]:
#             output = False
#             break
#         else:
#             record = record[0:-1]
#     elif ss == '}':
#         if len(record) == 0 or ss != record[-1]:
#             output = False
#             break
#         else:
#             record = record[0:-1]
# if record != []:
#     output = False
    
# print(output)

#-----------------------------------------------------------------------------#
# # question 26 删除排序数组中的重复项 已完成
# nums = [1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]

# nums2 = []
# for num in nums:
#     if num not in nums2:
#         nums2.append(num)
# for ii in range(len(nums2)):
#     nums[ii] = nums2[ii]
# print(len(nums2))
# print(nums)
#-----------------------------------------------------------------------------#
# # question 27 移除元素 已完成
# nums = [3,2,2,3]
# val = 3
# # nums = [0,1,2,2,3,0,4,2]
# # val = 2

# nums2 = []
# for num in nums:
#     if num != val:
#         nums2.append(num)
# for ii in range(len(nums2)):
#     nums[ii] = nums2[ii]
# print(len(nums2))
# print(nums)
#-----------------------------------------------------------------------------#
# # question 28 实现 strStr() 已完成
# haystack = "hello"
# needle = "ll"
# # haystack = "aaaaa"
# # needle = "bba"

# try:
#     output = haystack.index(needle)
# except ValueError:
#     output = -1
    
# print(output)            
#-----------------------------------------------------------------------------#
# # question 29 两数相除 已完成
# dividend = 10
# divisor = 3
# dividend = 7
# divisor = -3
# if dividend > 0 and divisor > 0:
#     zhengfu = 1
# elif dividend < 0 and divisor < 0:
#     zhengfu = 1
# elif dividend == 0:
#     zhengfu = 0
# else:
#     zhengfu = -1
# output = abs(dividend)//abs(divisor)*zhengfu
# if output<-2**31 or output > 2**31-1:
#     output=2**31-1
# print(output)
#-----------------------------------------------------------------------------#
# # question 30 串联所有单词的子串 已完成
# s = "barfoothefoobarman"
# words = ["foo","bar"]
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
# s = "foobarfoobar"
# words = ["foo","bar"]
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","good"]

# output = []
# len_word = len(words[0])
# for ii in range(len(s)-len(words)*len_word+1):
#     temp = [word for word in words]
#     index = ii
#     while len(temp) > 0:
#         if s[index:index+len_word] in temp:
#             del(temp[temp.index(s[index:index+len_word])])
#             index += len_word
#         else:
#             break
#     if len(temp) == 0:
#         output.append(ii)
# print(output)   
#-----------------------------------------------------------------------------#
# # question 32 最长有效括号 已完成
# s = "((()(()())()(()"
# s = "())((())"
# # s = ''
# # s = "(()())"
# # 方法一：动态规划
# # dp[ii] 表示以下标 ii 字符结尾的最长有效括号的长度
# dp = [0 for _ in range(len(s))] #以'('结尾的子串对应的dp值必定为0
# if len(s) > 0:
#     for ii in range(1,len(s)): #如果第一个字符为')'，其dp值也为0
#         if s[ii] == ')' and s[ii-1] == '(':
#             dp[ii] = dp[ii-2] + 2
#         elif s[ii] == ')' and s[ii-1] == ')':
#             # s[ii-dp[ii-1]] 与 s[ii-1]对应
#             # s[ii-dp[ii-1]-1] 与 s[ii]对应
#             if ii-dp[ii-1]-1 >= 0  and s[ii-dp[ii-1]-1] == '(':
#                 dp[ii] = dp[ii-dp[ii-1]-2] + dp[ii-1] + 2
#                 # dp[ii-dp[ii-1]-2] 为外层括号之前的最长有效括号长度
#                 # dp[ii-1] 为内从括号的最长有效括号长度
#     print(max(dp))
# else:
#     print(0)


# #方法三：从内层往外找，然后将连续的区间合并
# record = []
# for ii in range(len(s)-1):
#     if s[ii] == '(' and s[ii+1] == ')':
#         record.append([ii,ii+1])
# label = True
# while label == True:
#     print(record)
#     for ii in range(len(record)-1,0,-1):
#         print(ii)
#         if record[ii][0] == record[ii-1][1] + 1:
#             record[ii-1][1] = record[ii][1]
#             del(record[ii])
#     label = False
#     for ii in range(len(record)):
#         if record[ii][0]-1 >= 0 and record[ii][1]+1 < len(s) and s[record[ii][0]-1] == '(' and s[record[ii][1]+1] == ')':
#             record[ii][0] = record[ii][0] - 1
#             record[ii][1] = record[ii][1] + 1
#             label = label or True
#         else:
#             label = label or False
# print(record)
# longest = 0
# for ii in range(len(record)):
#     if record[ii][1] - record[ii][0] + 1 > longest:
#         longest = record[ii][1] - record[ii][0] + 1
# print(longest)
#-----------------------------------------------------------------------------#
# # question 33 搜索旋转排序数组 已完成
# nums = [4,5,6,7,0,1,2]
# target = 3

# try:
#     output = nums.index(target)
# except ValueError:
#     output = -1
# print(output)
#-----------------------------------------------------------------------------#
# # question 34 在排序数组中查找元素的第一个和最后一个位置 已完成
# nums = [2,2,3]
# nums = [2]
# nums = [2,2,2]
# target = 2

# try:
#     index = nums.index(target)
# except ValueError:
#     index = -1
# output = []
# output.append(index)
# if index == -1:
#     output.append(index)
# else:
#     while nums[index] == target and index < len(nums)-1:
#         index += 1
#     if nums[index] == target:
#         output.append(index)
#     else:
#         output.append(index-1)
# print(output)
#-----------------------------------------------------------------------------#
# # question 35 搜索插入位置 已完成
# nums = [1,3,5,6]
# target = 0

# try:
#     index = nums.index(target)
# except ValueError:
#     nums.append(target)
#     nums.sort()
#     index = nums.index(target)
# print(index)
#-----------------------------------------------------------------------------#
# # question 36 有效的数独 已完成
# # board = [
# #   ["5","3",".",".","7",".",".",".","."],
# #   ["6",".",".","1","9","5",".",".","."],
# #   [".","9","8",".",".",".",".","6","."],
# #   ["8",".",".",".","6",".",".",".","3"],
# #   ["4",".",".","8",".","3",".",".","1"],
# #   ["7",".",".",".","2",".",".",".","6"],
# #   [".","6",".",".",".",".","2","8","."],
# #   [".",".",".","4","1","9",".",".","5"],
# #   [".",".",".",".","8",".",".","7","9"]
# # ]

# board = [["8","3",".",".","7",".",".",".","."],
#          ["6",".",".","1","9","5",".",".","."],
#          [".","9","8",".",".",".",".","6","."],
#          ["8",".",".",".","6",".",".",".","3"],
#          ["4",".",".","8",".","3",".",".","1"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".","6",".",".",".",".","2","8","."],
#          [".",".",".","4","1","9",".",".","5"],
#          [".",".",".",".","8",".",".","7","9"]]

# def check(list1):
#     list2 = []
#     output = True
#     for ss in list1:
#         if ss != '.' and ss not in list2:
#             list2.append(ss)
#         elif ss != '.' and ss in list2:
#             output = False
#             break
#     return output

# num_row = len(board)
# #九宫格构造
# matrix = [[] for _ in range(num_row)]
# for ii in range(num_row):
#     for jj in range(num_row):
#         matrix[ii//3 + (jj//3)*3].append(board[ii][jj])
# #行检查
# label = True
# for ii in range(num_row):
#     temp_row = board[ii]
#     label = True and check(temp_row)
#     if label:
#         pass
#     else:
#         break
#     temp_matrix = matrix[ii]
#     label = True and check(temp_matrix)
#     if label:
#         pass
#     else:
#         break
#     temp_col = []
#     for jj in range(num_row):
#         temp_col.append(board[jj][ii])
#     label = True and check(temp_col)
#     if label:
#         pass
#     else:
#         break

# print(label)
#-----------------------------------------------------------------------------#
# question 37 解数独 已完成 回溯
# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]

# import numpy
# import copy
# board2 = numpy.array(board)
# list_empty = []
# for ii in range(board2.shape[0]):
#     for jj in range(board2.shape[0]):
#         if board2[ii,jj] == '.':
#             list_empty.append([ii,jj])
# record = [board2]

# while len(list_empty) > 0:
#     temp_record = []
#     index_row, index_col = list_empty[0]
#     for ii in range(len(record)):
#         for ss in ["1","2","3","4","5","6","7","8","9"]:
#             if ss not in record[ii][index_row,:] and ss not in record[ii][:,index_col] and ss not in record[ii][index_row//3*3:index_row//3*3+3, index_col//3*3:index_col//3*3+3]:
#                 temp_board = copy.deepcopy(record[ii])
#                 temp_board[index_row, index_col] = ss
#                 temp_record.append(temp_board)
#     del(list_empty[0])
#     record = temp_record
# print(record[0])
# for ii in range(len(board)):
#     for jj in range(len(board[0])):
#         board[ii][jj] = record[0][ii,jj]
# print(board)        
#-----------------------------------------------------------------------------#
# # question 38 外观数列 已完成
# n=5

# def next_str(str1):
#     temp_str = ' '
#     count = 1
#     output = ''
#     for ii in range(len(str1)):
#         if temp_str != str1[ii]:
#             output = output + str(count) + temp_str
#             temp_str = str1[ii]
#             count = 1
#         else:
#             count += 1
#     output = output + str(count) + temp_str
#     output = output.split(' ')[1]
#     return output
# str1 = '1'
# index = 1
# if n == 1:
#     output = '1'
# else:
#     while index < n:
#         str1 = next_str(str1)
#         index += 1
# print(str1)
#-----------------------------------------------------------------------------#
# # question 41 缺失的第一个正数 已完成
# nums = [1,2,0]
# index = 1
# label = 0
# while label == 0:
#     if index not in nums:
#         label = 1
#         break
#     else:
#         index += 1
# print(index)
#-----------------------------------------------------------------------------#
# # question 42 接雨水 已完成
# # height = [0,1,0,2,1,0,1,3,2,1,2,1]
# # height = [4,2,0,3,2,5]
# height = [4,2,3]

# list_to_right = []
# list_to_left = []
# temp_right = 0
# temp_left = 0
# for ii in range(len(height)):
#     if height[ii] > temp_right:
#         temp_right = height[ii]
#     list_to_right.append(temp_right)
#     if height[len(height)-ii-1] > temp_left:
#         temp_left = height[len(height)-ii-1]
#     list_to_left = [temp_left] + list_to_left

# area = 0
# for ii in range(len(height)):
#     area = area + min(list_to_right[ii], list_to_left[ii]) - height[ii]
# print(area)
#-----------------------------------------------------------------------------#
# # question 45 跳跃游戏 II
# # nums = [2,3,1,1,4]
# # nums = [2,3,1]
# # nums = [0]
# nums = [4,1,1,3,1,1,1]

# count = 0
# index = len(nums)-1
# while index > 0:
#     temp = index
#     for ii in range(index):
#         if index - ii <= nums[ii]:
#             temp = min(temp, ii)
#             break
#     count += 1
#     index = temp
# print(count)
#-----------------------------------------------------------------------------#
# # # question 48 旋转图像 已完成
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# # matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# # matrix = [[1]]

# num_row = len(matrix)
# num_col = len(matrix[0])

# new_cols = [[] for _ in range(num_col)]
# for jj in range(num_col):
#     for ii in range(num_row):
#         new_cols[jj].append(matrix[num_row-ii-1][jj])
# print(new_cols)
#-----------------------------------------------------------------------------#
# # question 49 字母异位词分组 已完成
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# # 方法一：对排序后字符串构建哈希表
# output_dict = {}
# for ii in range(len(strs)):
#     ss = ''.join(sorted(strs[ii]))
#     if ss not in output_dict:
#         output_dict[ss] = [ii]
#     else:
#         output_dict[ss].append(ii)

# output = []
# for ii in list(output_dict.keys()):
#     temp = [strs[jj] for jj in output_dict[ii]]
#     output.append(temp)
# print(output)

# # 方法二
# str2 = []
# str3 = []
# for str1 in strs:
#     str2.append(sorted(str1))
#     if sorted(str1) not in str3:
#         str3.append(sorted(str1))

# str4 = [[] for _ in range(len(str3))]
# for ii in range(len(str3)):
#     for jj in range(len(strs)):
#         if str3[ii] == str2[jj]:
#             str4[ii].append(strs[jj])
#-----------------------------------------------------------------------------#
# # 51. N 皇后
# n = 4

# #方法二：用set记录列、左上-右下对角线、左下-右上对角线是否占用
# # 左上-右下对角线  用横坐标和纵坐标的差表示
# # 左下-右上对角线  用横坐标和纵坐标的和表示
# import copy
# record = []
# def next_qizi(qipan, index, set_col, set_leftup2rightdown, set_left_down2rightup):
#     if index == n:
#         record.append(qipan)
#         return
#     else:
#         for ii in range(n):
#             if ii not in set_col and index-ii not in set_leftup2rightdown and index+ii not in set_left_down2rightup:
#                 qipan_new = copy.deepcopy(qipan)
#                 qipan_new[index] = qipan_new[index][0:ii]+'Q'+qipan_new[index][ii+1:]
#                 set_col.add(ii) #列
#                 set_leftup2rightdown.add(index-ii) #行-列
#                 set_left_down2rightup.add(index+ii) #行+列
#                 next_qizi(qipan_new, index+1, set_col, set_leftup2rightdown, set_left_down2rightup)
#                 set_col.remove(ii) #列
#                 set_leftup2rightdown.remove(index-ii) #行-列
#                 set_left_down2rightup.remove(index+ii) #行+列

# set_col = set()
# set_leftup2rightdown = set()
# set_left_down2rightup = set()
# next_qizi(['.'*n for _ in range(n)],0,set_col,set_leftup2rightdown,set_left_down2rightup)
# print(record)

# #方法一
# import copy
# record = []
# def next_qizi(qipan, index):
#     if index == n:
#         record.append(qipan)
#         return
#     elif index == 0:
#         for ii in range(n):
#             qipan_new = copy.deepcopy(qipan)
#             qipan_new[index] = qipan_new[index][0:ii]+'Q'+qipan_new[index][ii+1:]
#             next_qizi(qipan_new, index+1)
#     else:
#         for ii in range(n):
#             # 判断当前行的第ii列是否可以放置皇后
#             label = True
#             for jj in range(index):
#                 if 0 <= ii-(index-jj) and qipan[jj][ii-(index-jj)] == 'Q': #左上方检查
#                     label = False
#                 if ii+(index-jj) < n and qipan[jj][ii+(index-jj)] == 'Q': #右上方检查
#                     label = False
#                 if qipan[jj][ii] == 'Q': #列检查
#                     label = False
#             # 如果不冲突，则放置新皇后
#             if label == True:
#                 qipan_new = copy.deepcopy(qipan)
#                 qipan_new[index] = qipan_new[index][0:ii]+'Q'+qipan_new[index][ii+1:]
#                 next_qizi(qipan_new, index+1)
# next_qizi(['.'*n for _ in range(n)],0)
# print(record)

# #方法三 用list判断列是否以占用
# import copy
# record = []
# def next_qizi(qipan, index, record_col):
#     if index == n:
#         record.append(qipan)
#         return
#     elif index == 0:
#         for ii in range(n):
#             qipan_new = copy.deepcopy(qipan)
#             record_col_new = copy.deepcopy(record_col)
#             qipan_new[index] = qipan_new[index][0:ii]+'Q'+qipan_new[index][ii+1:]
#             record_col_new[ii] = False
#             next_qizi(qipan_new, index+1, record_col_new)
#     else:
#         for ii in range(n):
#             if record_col[ii]:
#                 label = True
#                 for jj in range(index):
#                     if 0 <= ii-(index-jj) and qipan[jj][ii-(index-jj)] == 'Q':
#                         label = False
#                     if ii+(index-jj) < n and qipan[jj][ii+(index-jj)] == 'Q':
#                         label = False
#                 if label == True:
#                     qipan_new = copy.deepcopy(qipan)
#                     record_col_new = copy.deepcopy(record_col)
#                     qipan_new[index] = qipan_new[index][0:ii]+'Q'+qipan_new[index][ii+1:]
#                     record_col_new[ii] = False
#                     # print(qipan_new)
#                     next_qizi(qipan_new, index+1, record_col_new)
# next_qizi(['.'*n for _ in range(n)],0,[True for _ in range(n)])
# print(record)
#-----------------------------------------------------------------------------#
# # question 54 螺旋矩阵 已完成
# matrix = [[1,2,3],[5,6,7],[9,10,11],[13,14,15]]
# # matrix = [[1,2,3],[4,5,6],[7,8,9]]
# # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# # matrix = [[6,9,7]]

# row_start = 0
# row_end = len(matrix)-1
# col_start = 0
# col_end = len(matrix[0])-1
# output = []
# while len(output) < len(matrix)*len(matrix[0]):
#     if row_start == row_end and col_start == col_end:
#         output += [matrix[row_start][col_start]]
#     elif row_start == row_end and col_start != col_end:
#         output += [matrix[row_start][ii] for ii in range(col_start, col_end+1)]
#     elif row_start != row_end and col_start == col_end:
#         output += [matrix[ii][col_start] for ii in range(row_start, row_end+1)]
#     else:
#         output += [matrix[row_start][ii] for ii in range(col_start,col_end)]
#         output += [matrix[ii][col_end] for ii in range(row_start,row_end)]
#         output += [matrix[row_end][ii] for ii in range(col_end,col_start,-1)]
#         output += [matrix[ii][col_start] for ii in range(row_end,row_start,-1)]
#     row_start += 1
#     row_end = row_end -1
#     col_start += 1
#     col_end = col_end -1
# print(output)

# # question 59 螺旋矩阵 II 已完成
# n = 3

# row_start = 0
# row_end = n-1
# col_start = 0
# col_end = n-1
# index = 1
# matrix = [ [0 for _ in range(n)] for _ in range(n)]
# while index <= n**2:
#     if row_start == row_end and col_start == col_end:
#         matrix[row_start][col_start] = index
#         index += 1
#     else:
#         for ii in range(col_start,col_end):
#             matrix[row_start][ii] = index
#             index += 1
#         for ii in range(row_start,row_end):
#             matrix[ii][col_end] = index
#             index += 1
#         for ii in range(col_end,col_start,-1):
#             matrix[row_end][ii] = index
#             index += 1
#         for ii in range(row_end,row_start,-1):
#             matrix[ii][col_start] = index
#             index += 1
            
#     row_start += 1
#     col_start += 1
#     row_end = row_end - 1
#     col_end = col_end - 1
# print(matrix)
#-----------------------------------------------------------------------------#
# # question 55 跳跃游戏 已完成
# # nums = [2,3,1,1,4]
# # nums = [3,2,1,0,4]
# nums = [0]

# index = 0
# current_max_step = 0
# for ii in range(len(nums)):
#     current_max_step = max(nums[ii], current_max_step)
#     if current_max_step == 0:
#         break
#     else:
#         current_max_step = current_max_step - 1

# if ii == len(nums)-1:
#     output = True
# else:
#     output = False
# print(output)
#-----------------------------------------------------------------------------#
# # question 57 插入区间 已完成
# # intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# # newInterval = [4,8]
# # intervals = [[1,3],[6,9]]
# # newInterval = [2,5]
# # intervals = []
# # newInterval = [5,7]
# intervals = [[1,5]]
# newInterval = [2,3]
# intervals = [[1,5]]
# newInterval = [2,7]

# intervals.append(newInterval)
# intervals2 = sorted(intervals)

# index = 0
# count = 1
# while count < len(intervals):
#     if intervals2[index][1] < intervals2[index+1][0]:
#         index += 1
#     else:
#         intervals2[index][1] = max(intervals2[index][1],intervals2[index+1][1])
#         del(intervals2[index+1])
#     count += 1
# print(intervals2)
#-----------------------------------------------------------------------------#
# # question 58 最后一个单词的长度 已完成
# s = "Hello World"
# # s = " "
# # s = ""
# # s = 'a'
# # s = ' a '
# # s = "b   a    "
       
# s = s.rstrip()
# temp = s.split(" ")
# if len(temp) > 1:
#         output = len(temp[-1])
# else:
#     output = len(s)
# print(output)

#-----------------------------------------------------------------------------#
# # question60 排列序列 已完成
# n = 4
# k = 9

# # 方法二
# def next_permutation(nums):
#     label = False
#     for ii in range(len(nums)-2,-1,-1):
#         if nums[ii] < nums[ii+1]:
#             label = True
#             break
#     if label == True:
#         for jj in range(len(nums)-1,-1,-1):
#             if nums[jj] > nums[ii]:
#                 break
#         nums[ii], nums[jj] = nums[jj], nums[ii]
#         nums[ii+1:] = sorted(nums[ii+1:])
#     else:
#         nums.sort()
#     return nums

# output = [str(ii) for ii in range(1,n+1)]
# if k > 1:
#     for ii in range(2,k+1):
#         output = next_permutation(output)
# print(''.join(output))

# # 方法一
# from itertools import permutations
# ss = ''
# for ii in range(1,n+1):
#     ss += str(ii)
# temp = list(permutations(ss,n))
# output = ''
# for ii in temp[k-1]:
#     print(ii)
#     output += ii
# print(output)
#-----------------------------------------------------------------------------#
# # question 65 有效数字 已完成
# s = '+3.14e-2'
# # s = "inf"
# # s = "Infinity"
# # s = "-inf"

# label = True
# for ii in range(len(s)):
#     if s[ii] not in ['+','-','e','E','.','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#         label = False
#         break
# if label == True:
#     try:
#         float(s)
#     except ValueError:
#         label = False
#     else:
#         label = True
# print(label)
#-----------------------------------------------------------------------------#
# # question 67 二进制求和 已完成
# # a = "11"
# # b = "1"
# a = "1010"
# b = "1011"

# #方法一
# print(bin(int(a,2)+int(b,2))[2:])

# #方法二
# a1 = []
# b1 = []
# for ii in range(max(len(a),len(b))):
#     a1.append('0')
#     b1.append('0')
# for ii in range(len(a)):
#     a1[ii] = a[len(a)-1-ii]
# for ii in range(len(b)):
#     b1[ii] = b[len(b)-1-ii]
    
# label = False
# num_sum = []
# for ii in range(max(len(a),len(b))):
#     if a1[ii] == '1' and b1[ii] == '1' and label == True:
#         num_sum.append('1')
#         label = True
#     elif a1[ii] == '1' and b1[ii] == '1' and label == False:
#         num_sum.append('0')
#         label = True
#     elif a1[ii] == '1' and b1[ii] == '0' and label == True:
#         num_sum.append('0')
#         label = True
#     elif a1[ii] == '1' and b1[ii] == '0' and label == False:
#         num_sum.append('1')
#         label = False
#     elif a1[ii] == '0' and b1[ii] == '1' and label == True:
#         num_sum.append('0')
#         label = True
#     elif a1[ii] == '0' and b1[ii] == '1' and label == False:
#         num_sum.append('1')
#         label = False
#     elif a1[ii] == '0' and b1[ii] == '0' and label == True:
#         num_sum.append('1')
#         label = False
#     else:
#         num_sum.append('0')
#         label = False
# if label == True:
#     num_sum.append('1')
# num_sum2 = ''    
# for ii in range(len(num_sum)):
#     num_sum2 = num_sum[ii] + num_sum2
    
# print(num_sum2)
#-----------------------------------------------------------------------------#
# # question 68 文本左右对齐 已完成
# # words = ["This", "is", "an", "example", "of", "text", "justification."]
# # maxWidth = 16
# # words = ["What","must","be","acknowledgment","shall","be"]
# # maxWidth = 16
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20

# def kongge(ss):
#     # 补空格 以实现两端对齐
#     temp_ss = ss.split(' ')
#     if len(temp_ss) > 1:
#         num_kongge = maxWidth - (len(ss) - len(temp_ss) + 1)
#         temp_kongge = ['' for _ in range(len(temp_ss)-1)]
#         index = 0
#         while num_kongge > 0:
#             if index < len(temp_ss)-1:
#                 temp_kongge[index] += ' '
#                 index += 1
#             else:
#                 index = 0
#                 temp_kongge[index] += ' '
#                 index += 1
#             num_kongge = num_kongge - 1
#         output = ''
#         for ii in range(len(temp_ss)-1):
#             output = output + temp_ss[ii] + temp_kongge[ii]
#         output += temp_ss[-1]
#     else:
#         num_kongge = maxWidth - len(temp_ss[0])
#         output = temp_ss[0]
#         for ii in range(num_kongge):
#             output += ' '
#     return output

# # 分行
# output2 = []
# line = words[0]
# label = False
# for ii in range(1, len(words)):
#     if len(line) + 1 + len(words[ii]) <= maxWidth:
#         line = line + ' ' + words[ii]
#         label = False
#     else:
#         output2.append(line)
#         line = words[ii]
#         label = True
# output2.append(line)
# # 补充空格
# for ii in range(len(output2)-1):
#     output2[ii] = kongge(output2[ii])
# # 最后一行补空格
# num_kongge = maxWidth - len(output2[-1])
# for ii in range(num_kongge):
#     output2[-1] += ' '
# print(output2)
#-----------------------------------------------------------------------------#
# # question 71 简化路径 - 栈
# path = "/a//./b/../../c/"
# # path = "/home//foo/"
# # path = "/../"
# # path = "/home/"
# # path = "/a/../../b/../c//.//"
# # path = "/a//b////c/d//././/.."

# # new
# path = path.split('/')
# list1 = []
# for ss in path:
#     if ss == '..' and len(list1) > 0:
#         list1.pop()
#     elif ss != '..' and ss != '.' and ss != '':
#         list1.append(ss)
# print('/' + '/'.join(list1))

# #old
# while '//' in path:
#     path = path.replace('//', '/')
# path2 = path.split('/')
# del(path2[0])
# if path2[-1] == '':
#     del(path2[-1])
# record = []
# for ii in range(len(path2)):
#     if path2[ii] == '.':
#         pass
#     elif path2[ii] == '..':
#         if len(record) > 0:
#             del(record[-1])
#     else:
#         record.append(path2[ii])
# output = ''
# if len(record) > 0:
#     for ii in range(len(record)):
#         output = output + '/' + record[ii]
# else:
#     output = '/'

# print(output)
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
# # question 73 矩阵置零 已完成
# # matrix = [[1,1,1],[1,0,1],[1,1,1]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# index_row = []
# index_col = []
# for ii in range(len(matrix)):
#     for jj in range(len(matrix[0])):
#         if matrix[ii][jj] == 0:
#             index_row.append(ii)
#             index_col.append(jj)
# for ii in range(len(matrix)):
#     for jj in range(len(matrix[0])):
#         if ii in index_row or jj in index_col:
#             matrix[ii][jj] = 0
# print(matrix)
#-----------------------------------------------------------------------------#
# # question 74 搜索二维矩阵 已完成
# # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# # target = 3
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13
# row = []
# for ii in range(len(matrix)):
#     row = row + matrix[ii]
# print(target in row)
#-----------------------------------------------------------------------------#
# # question 76 最小覆盖子串 已完成 
# # s = "ADOBECODEBANCZ"
# # t = "ABC"
# # s = "dacbeaf"
# # t = "aab"
# # s = "bba"
# # t = "ab"
# # s = 'abz'
# # t = 'aba'
# # s = 'a'
# # t = 'aa'
# # s = "fb"
# # t = "a"
# # s = "a"
# # t = "a"
# # s = "z"
# # t = "a"
# s = "az"
# t = "a"

# # 用哈希表（Python中的字典应用了哈希表的原理）检验是否覆盖
# def fugai(dict_s, dict_t):
#     label = True
#     for ss in unique_t:
#         if dict_s[ss] < dict_t[ss]:
#         #     label = label and True
#         # else:
#             label = label and False
#     return label

# dict_s = {ss: 0 for ss in t}
# dict_t = {ss: 0 for ss in t}
# unique_t = []
# for ss in t:
#     dict_t[ss] += 1
#     if ss not in unique_t:
#         unique_t.append(ss)
# index_left = 0
# index_right = 0
# min_len = len(s)
# output = s
# label = False
# while index_right < len(s):
#     if s[index_right] in unique_t:
#         dict_s[s[index_right]] += 1
#         if fugai(dict_s, dict_t):
#             label = True
#             while fugai(dict_s, dict_t):
#                 if s[index_left] in unique_t:
#                     dict_s[s[index_left]] = dict_s[s[index_left]] - 1
#                 index_left += 1
#             print(s[index_left-1:index_right]+s[index_right])
#             if len(s[index_left-1:index_right]+s[index_right]) < min_len:
#                 min_len = len(s[index_left-1:index_right]+s[index_right])
#                 output = s[index_left-1:index_right]+s[index_right]
#             index_right += 1
#         else:
#             index_right += 1
#     else:
#         index_right += 1
# if label == True:
#     print(output)
# else:
#     print('无法覆盖')

# # 超时
# def fugai(ss,t):
#     t2 = list(t)
#     for ii in range(len(ss)):
#         if ss[ii] in t2:
#             del(t2[t2.index(ss[ii])])
#     if len(t2) == 0:
#         return True
#     else:
#         return False

# if len(t) > 1:
#     for s_start in range(len(s)):
#         if s[s_start] in t:
#             break
#     index_left = s_start
#     index_right = s_start
#     min_len = len(s[s_start:])
#     output = s[s_start:]
#     label_unchange = False
#     label = False
#     target = list(t)
#     while index_right < len(s):
#         if s[index_right] in target and not label_unchange:
#             del(target[target.index(s[index_right])])
#             if len(target) == 0:
#                 label = True
                
#                 label_unchange = True
#                 while fugai(s[index_left:index_right]+s[index_right],t):
#                     index_left += 1
#                 target.append(s[index_left-1])
#                 print(s[index_left-1:index_right]+s[index_right])
#                 if min_len > len(s[index_left-1:index_right]+s[index_right]):
#                     min_len = len(s[index_left-1:index_right]+s[index_right])
#                     output = s[index_left-1:index_right]+s[index_right]
#                 while s[index_left] not in t:
#                     index_left += 1
#             else:
#                 index_right += 1
#                 label_unchange = False
#         else:
#             index_right += 1
#             label_unchange = False
#     if label == True:
#         print(output)
#     else:
#         print('无法涵盖')
# elif len(t) == 1:
#     if t in s:
#         print(t)
#     else:
#         print('无法涵盖')

# # 超时
# def fugai(ss,t):
#     t2 = list(t)
#     for ii in range(len(ss)):
#         if ss[ii] in t2:
#             del(t2[t2.index(ss[ii])])
#     if len(t2) == 0:
#         return True
#     else:
#         return False

# min_len = len(s)
# output = s
# if fugai(s,t):
#     if len(t) > 1:
#         index_left = 0
#         index_right = 0
#         while index_right < len(s):
#             ss2 = s[index_left:index_right]+s[index_right]
#             if ss2[-1] in t and fugai(ss2, t):
#                 if min_len > len(ss2):
#                     min_len = len(ss2)
#                     output = ss2
#                 index_left += 1
#                 while s[index_left] not in t:
#                     index_left += 1
#             else:
#                 index_right += 1
#     elif len(t) == 1:
#         output = t
#     print(output)
# else:
#     print('无法涵盖')
#-----------------------------------------------------------------------------#
# # question 79 单词搜索 -未完成

# board = [['A','B','C','E'],
#           ['S','F','C','S'],
#           ['A','D','E','E']]
# word = "ABCCED"
# word = "SEE"
# word = "ABCB"

# board = [["a"]]
# word = 'b'
# board = [['a','b', 'c']]
# word = 'aba'
# board = [['a'],['b'],['c']]
# word = 'bcb'
# board = [["a","b"]]
# word = "ba"
# board = [["C","A","A"],["A","A","A"],["B","C","D"]]
# word = "AAB"
# board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
# word = "AAAAAAAAAAAAAAB"
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"

# import copy
# output = []
# def backtrack(location, matrix, index):
#     if index == len(word):
#         output.append(matrix)
#         return
#     else:
#         if 0 <= location[0]+1 < len(matrix) and 0 <= location[1] < len(matrix[0]) and matrix[location[0]+1][location[1]] == word[index]:
#             matrix2 = copy.deepcopy(matrix)
#             matrix2[location[0]+1][location[1]] = False
#             backtrack([location[0]+1, location[1]], matrix2, index+1)
#         if 0 <= location[0]-1 < len(matrix) and 0 <= location[1] < len(matrix[0]) and matrix[location[0]-1][location[1]] == word[index]:
#             matrix2 = copy.deepcopy(matrix)
#             matrix2[location[0]-1][location[1]] = False
#             backtrack([location[0]-1, location[1]], matrix2, index+1)
#         if 0 <= location[0] < len(matrix) and 0 <= location[1]+1 < len(matrix[0]) and matrix[location[0]][location[1]+1] == word[index]:
#             matrix2 = copy.deepcopy(matrix)
#             matrix2[location[0]][location[1]+1] = False
#             backtrack([location[0], location[1]+1], matrix2, index+1)
#         if 0 <= location[0] < len(matrix) and 0 <= location[1]-1 < len(matrix[0]) and matrix[location[0]][location[1]-1] == word[index]:
#             matrix2 = copy.deepcopy(matrix)
#             matrix2[location[0]][location[1]-1] = False
#             backtrack([location[0], location[1]-1], matrix2, index+1)

# word_set = set()
# for ss in word:
#     word_set.add(ss)
# locations = [] #寻找word第一个字母的起始位置
# temp = [] #记录矩阵所有元素
# for ii in range(len(board)):
#     for jj in range(len(board[0])):
#         if board[ii][jj] == word[0]:
#             locations.append([ii,jj])
#     temp += board[ii]
# # 判断word中所有字符是否在矩阵中出现过
# label = True            
# for ss in word_set:
#     if ss not in temp:
#         label = False
# if label == True:
#     for location in locations:
#         matrix2 = copy.deepcopy(board)
#         matrix2[location[0]][location[1]] = False
#         backtrack(location, matrix2, 1)
#     print(len(output) >= 1)
# else:
#     print(label)


# # 212. 单词搜索 II
# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]

# import copy
# def check(word):
#     output = []
#     def backtrack(location, matrix, index):
#         if index == len(word):
#             output.append(matrix)
#             return
#         else:
#             if 0 <= location[0]+1 < len(matrix) and 0 <= location[1] < len(matrix[0]) and matrix[location[0]+1][location[1]] == word[index]:
#                 matrix2 = copy.deepcopy(matrix)
#                 matrix2[location[0]+1][location[1]] = False
#                 backtrack([location[0]+1, location[1]], matrix2, index+1)
#             if 0 <= location[0]-1 < len(matrix) and 0 <= location[1] < len(matrix[0]) and matrix[location[0]-1][location[1]] == word[index]:
#                 matrix2 = copy.deepcopy(matrix)
#                 matrix2[location[0]-1][location[1]] = False
#                 backtrack([location[0]-1, location[1]], matrix2, index+1)
#             if 0 <= location[0] < len(matrix) and 0 <= location[1]+1 < len(matrix[0]) and matrix[location[0]][location[1]+1] == word[index]:
#                 matrix2 = copy.deepcopy(matrix)
#                 matrix2[location[0]][location[1]+1] = False
#                 backtrack([location[0], location[1]+1], matrix2, index+1)
#             if 0 <= location[0] < len(matrix) and 0 <= location[1]-1 < len(matrix[0]) and matrix[location[0]][location[1]-1] == word[index]:
#                 matrix2 = copy.deepcopy(matrix)
#                 matrix2[location[0]][location[1]-1] = False
#                 backtrack([location[0], location[1]-1], matrix2, index+1)
    
#     word_set = set()
#     for ss in word:
#         word_set.add(ss)
#     locations = [] #寻找word第一个字母的起始位置
#     temp = [] #记录矩阵所有元素
#     for ii in range(len(board)):
#         for jj in range(len(board[0])):
#             if board[ii][jj] == word[0]:
#                 locations.append([ii,jj])
#         temp += board[ii]
#     # 判断word中所有字符是否在矩阵中出现过
#     label = True            
#     for ss in word_set:
#         if ss not in temp:
#             label = False
#     if label == True:
#         for location in locations:
#             matrix2 = copy.deepcopy(board)
#             matrix2[location[0]][location[1]] = False
#             backtrack(location, matrix2, 1)
#         return len(output) >= 1
#     else:
#         return label

# output2 = []
# for word in words:
#     if check(word):
#         output2.append(word)
# print(output2)
#-----------------------------------------------------------------------------#
# # question 80 删除排序数组中的重复项II 已完成
# # nums = [1,1,1,2,2,3]
# nums = [0,0,1,1,1,1,2,3,3]

# record = []
# temp = 1
# len_nums = len(nums)
# for ii in range(len_nums):
#     if nums[len_nums-1-ii] not in record:
#         record.append(nums[len_nums-1-ii])
#         temp = 1
#     else:
#         temp += 1
#         if temp > 2:
#             del(nums[len_nums-1-ii])
# print(len(nums))
# print(nums)
#-----------------------------------------------------------------------------#
# # question 84 柱状图中最大的矩形 已完成
# # heights = [2,1,5,6,2,3]
# # heights = [0,0,0,0,0]
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
#     print(list_heights)
# print(area)    

# ##超时算法
# # area = 0
# # for ii in range(len(heights)):
# #     for jj in range(ii,len(heights)):
# #         area_new = (jj-ii+1)*min(heights[ii:jj]+[heights[jj]])
# #         if area_new > area:
# #             area = area_new
# # print(area)

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

# # 超时
# matrix2 = [[0]*len(matrix[0]) for _ in range(len(matrix))]
# for ii in range(len(matrix)):
#     for jj in range(len(matrix[0])):
#         if matrix[ii][jj] == '1':
#             matrix2[ii][jj] = 1

# def area(index_row1,index_col1,index_row2,index_col2):
#     temp = 0
#     for ii in range(index_row1,index_row2+1):
#         temp += sum(matrix2[ii][index_col1:index_col2+1])
#         # print(matrix2[ii][index_col1:index_col2+1])
#         # print(temp)
#         # print((index_row2-index_row1+1)*(index_col2-index_col1+1))
#     if temp == (index_row2-index_row1+1)*(index_col2-index_col1+1):
#         return temp
#     else:
#         return 0
# output = 0
# for index_row1 in range(len(matrix)):
#     for index_row2 in range(index_row1, len(matrix)):
#         for index_col1 in range(len(matrix[0])):
#             for index_col2 in range(index_col1,len(matrix[0])):
#                 output_new = area(index_row1,index_col1,index_row2,index_col2)
#                 if output_new > output:
#                     output = output_new
# print(output)
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
# # question 88 合并两个有序数组 已完成
# # nums1 = [1,2,3,0,0,0]
# # m = 3
# # nums2 = [2,5,6]
# # n = 3
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# for ii in range(n):
#     nums1[m+ii] = nums2[ii]
# nums1.sort()
# print(nums1)
#-----------------------------------------------------------------------------#
# # question 89 格雷编码 已完成
# n = 4

# def gelei(list1):
#     add = len(list1)
#     list2 = []
#     for num in list1:
#         list2 = [num+add] + list2
#     list3 = list1 + list2
#     return list3

# if n > 0:
#     index = 1
#     output = [0,1]
#     while index > 0 and index < n:
#         output = gelei(output)
#         index += 1
# else:
#     output = [0]
# print(output)
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
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# root = TreeNode(1,2,3)
# root.left = TreeNode(2,4,5)
# root.right = TreeNode(3,6,7)
# root.left.left = TreeNode(4,8,9)
# root.left.right = TreeNode(5,10,11)
# root.right.left = TreeNode(6,12,13)
# root.right.right = TreeNode(7,14,15)
# root.left.left.left = TreeNode(8)
# root.left.left.right = TreeNode(9)
# root.left.right.left = TreeNode(10)
# root.left.right.right = TreeNode(11)
# root.right.left.left = TreeNode(12)
# root.right.left.right = TreeNode(13)
# root.right.right.left = TreeNode(14)
# root.right.right.right = TreeNode(15)

# # question 94 二叉树的中序遍历 已完成        

# # 递归法
# temp = []
# def dfs(root):
#     if not root:
#         return
#     dfs(root.left)
#     temp.append(root.val)
#     dfs(root.right)
# dfs(root)
# print(temp)

# # 方法二
# if root == None:
#     list_tree = []
# else:
#     list_tree = [root]
#     label = True
#     while label == True:
#         temp_label = True 
#         temp_list = []
#         for ii in range(len(list_tree)):
#             if type(list_tree[ii]) == TreeNode: #如果当前元素是TreeNode类型
#                 temp_label = temp_label and False
#                 if list_tree[ii].left != None: #如果当前元素的左子树不为空
#                     temp_list.append(list_tree[ii].left)
                    
#                 temp_list.append(list_tree[ii].val)
                
#                 if list_tree[ii].right != None: #如果当前元素的右子树不为空
#                     temp_list.append(list_tree[ii].right)
#             elif type(list_tree[ii]) == int: #如果当前元素是整数
#                 temp_list.append(list_tree[ii])
#         list_tree = temp_list
#         if temp_label == True: #如果list_tree中的元素全部不是TreeNode，则停止循环
#             label = False
# print(list_tree)
#-----------------------------------------------------------------------------#
# # 95. 不同的二叉搜索树 II
# n = 3

# # 方法二：方法一的改进
# def build_Trees(list1):
#     if len(list1) == 0:
#         return [None]
#     all_trees = []
#     for ii in range(len(list1)):
#         left_trees = build_Trees(list1[0:ii])
#         right_trees = build_Trees(list1[ii+1:])
#         for l in left_trees:
#             for r in right_trees:
#                 cur_tree = TreeNode(list1[ii])
#                 cur_tree.left = l
#                 cur_tree.right = r
#                 all_trees.append(cur_tree)
#     return all_trees
# record = build_Trees([ii+1 for ii in range(n)])
# print(record)

# #方法一：官方
# def build_Trees(start, end):
#     # start>end，说明为空树，返回[None]
#     if start > end:
#         return [None]
#     # 初始化所有可能的二叉搜索树列表all_trees=[]
#     all_trees = []
#     # 遍历每一种可能的节点ii，遍历区间[start,end+1)
#     for ii in range(start, end+1):
#         # 所有可能的左子树列表
#         left_trees = build_Trees(start, ii-1)
#         # 所有可能的右子树列表
#         right_trees = build_Trees(ii+1, end)
#         # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
#         for l in left_trees:
#             for r in right_trees:
#                 cur_tree = TreeNode(ii) #建立当前树节点cur_tree=TreeNode(ii)
#                 cur_tree.left = l #将cur_tree左子树置为l
#                 cur_tree.right = r #将cur_tree右子树置为r
#                 all_trees.append(cur_tree) #将cur_tree加入树列表中
#     # 返回树列表all_trees
#     return all_trees
# record = build_Trees(1,n)
# print(record)


# # 96. 不同的二叉搜索树
# n=4

# #用动态规划模拟95题的生成过程
# dp = [1,1]
# for ii in range(2,n+1):
#     count = 0
#     for jj in range(len(dp)):
#         count += dp[jj]*dp[len(dp)-jj-1] #左子树的种类*右子树的种类
#     dp.append(count)
# print(dp[n])
#-----------------------------------------------------------------------------#
# # question 98 验证二叉搜索树 已完成
# root = TreeNode(5,None,None)
# root.left = TreeNode(1,None,None)
# root.right = TreeNode(4,None,None)
# root.right.left = TreeNode(3,None,None)
# root.right.right = TreeNode(6,None,None)


# root = TreeNode(5,None,None)
# root.left = TreeNode(1,None,None)
# root.right = TreeNode(6,None,None)

# # 方法一
# temp = []
# def dfs(root):
#     if not root:
#         return 
#     dfs(root.left)
#     temp.append(root.val)
#     dfs(root.right)
# dfs(root)
# label = True
# for ii in range(len(temp)-1):
#     if temp[ii] >= temp[ii+1]:
#         label = False
#         break
# print(label)

# # 方法二
# list_tree = [root]
# label = True
# while label == True:
#     temp_label = True
#     temp_list = []
#     for ii in range(len(list_tree)):
#         if type(list_tree[ii]) != int:
#             if list_tree[ii].left != None:
#                 temp_list.append(list_tree[ii].left)
#             temp_list.append(list_tree[ii].val)
#             if list_tree[ii].right != None:
#                 temp_list.append(list_tree[ii].right)
#             temp_label = temp_label and False
#         else:
#             temp_list.append(list_tree[ii])
#             temp_label = temp_label and True
#     list_tree = temp_list
#     if temp_label == True:
#         label = False
# print(list_tree)

# label = True
# for ii in range(len(list_tree)-1):
#     if list_tree[ii] < list_tree[ii+1]:
#         label = label and True
#     else:
#         label = label and False
# print(label)
#-----------------------------------------------------------------------------#
# # 99. 恢复二叉搜索树
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(2)

# root = TreeNode(1)
# root.left = TreeNode(3)
# root.left.right = TreeNode(2)

# #方法一：如果节点的值均不同的情况
# temp = []
# def dfs(root):
#     if not root:
#         return
#     dfs(root.left)
#     temp.append(root.val)
#     dfs(root.right)
# dfs(root)

# temp2 = sorted(temp)
# need_change = []
# for ii in range(len(temp)):
#     if temp[ii] != temp2[ii]:
#         need_change.append(temp[ii])

# def dfs2(root):
#     if not root:
#         return
#     dfs2(root.left)
#     if root.val == need_change[0]:
#         root.val = need_change[1]
#     elif root.val == need_change[1]:
#         root.val = need_change[0]
#     dfs2(root.right)
# dfs2(root)

# #方法二：如果节点的值存在相同的情况
# temp = []
# def dfs(root):
#     if not root:
#         return
#     dfs(root.left)
#     temp.append(root)
#     dfs(root.right)
# dfs(root)
# for ii in range(len(temp)):
#     for jj in range(ii+1,len(temp)):
#         if temp[ii].val > temp[jj].val:
#             temp_num = temp[jj].val
#             temp[jj].val = temp[ii].val
#             temp[ii].val = temp_num
#-----------------------------------------------------------------------------#
# # question 100 相同的树 已完成
# p = TreeNode(1,None,3)
# p.right = TreeNode(3,4,5)
# p.right.left = TreeNode(4)
# p.right.right = TreeNode(5)
# q = TreeNode(1,None,3)
# q.right = TreeNode(3,4,5)
# q.right.left = TreeNode(4)
# q.right.right = TreeNode(5)

# # p = TreeNode(1)
# # p.left = TreeNode(2)
# # p.right = TreeNode(3)
# # q = TreeNode(1)
# # q.left = TreeNode(2)
# # q.right = TreeNode(2)

# # 方法一:动态规划
# def dfs(p,q):
#     if p == None and q == None:
#         return True
#     elif p != None and q != None:
#         if p.val != q.val:
#             return False
#         else:
#             return dfs(p.left,q.left) and dfs(p.right,q.right)
#     else:
#         return False
# print(dfs(p,q))

# # 方法二
# if type(p) == TreeNode and type(q) == TreeNode:
#     label = True
#     list_p = [p]
#     list_q = [q]
#     while len(list_p) == len(list_q) and len(list_p) > 0 and len(list_q) > 0 and label == True:
#         temp_p = []
#         temp_q = []
#         for ii in range(len(list_p)):
#             if list_p[ii].val == list_q[ii].val:
#                 label = label and True
#             else:
#                 label = label and False
#                 break
#             if type(list_p[ii].left) == TreeNode and type(list_q[ii].left) == TreeNode:
#                 temp_p.append(list_p[ii].left)
#                 temp_q.append(list_q[ii].left)
#             else:
#                 if list_p[ii].left == list_q[ii].left:
#                     label = label and True
#                 else:
#                     label = label and False
#                     break
#             if type(list_p[ii].right) == TreeNode and type(list_q[ii].right) == TreeNode:
#                 temp_p.append(list_p[ii].right)
#                 temp_q.append(list_q[ii].right)
#             else:
#                 if list_p[ii].right == list_q[ii].right:
#                     label = label and True
#                 else:
#                     label = label and False
#                     break
#         list_p = temp_p
#         list_q = temp_q
#     if len(list_p) == 0 and len(list_q) == 0:
#         label = label and True
#     else:
#         label = label and False
# elif p == None and q == None:
#     label = True
# else:
#     label = False
# print(label)
#-----------------------------------------------------------------------------#
# # question 103 二叉树的锯齿形层序遍历
# output = []
# record = [root]
# layer = 0
# while len(record) > 0:
#     if len(output) == layer:
#         output.append([])
#     temp_record = []
#     if layer%2 == 0:
#         for ii in range(len(record)):
#             if record[ii]:
#                 output[layer].append(record[ii].val)
#                 temp_record.append(record[ii].left)
#                 temp_record.append(record[ii].right)
#     else:
#         for ii in range(len(record)):
#             if record[ii]:
#                 output[layer] = [record[ii].val] + output[layer]
#                 temp_record.append(record[ii].left)
#                 temp_record.append(record[ii].right)
#     record = temp_record
#     layer += 1
# print(output[0:-1])
#-----------------------------------------------------------------------------#
# # question 105 从前序与中序遍历序列构造二叉树 已完成
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# # preorder = [1,2,3]
# # inorder = [3,2,1]

# # 方法一
# def backtrack(list_pre,list_in):
#     if len(list_pre) == 0:
#         return
#     else:
#         index = list_in.index(list_pre[0])
#         root = TreeNode(list_pre[0])
#         root.left = backtrack(list_pre[1:index+1],list_in[0:index])
#         root.right = backtrack(list_pre[index+1:],list_in[index+1:])
#     return root

# root = backtrack(preorder,inorder)

# # 方法二
# def next_layer(preorder, inorder):
#     index_val_in_inorder = inorder.index(preorder[0])
#     left_inorder = inorder[0:index_val_in_inorder]
#     right_inorder = inorder[index_val_in_inorder+1:]
#     left_preorder = preorder[1:1+len(left_inorder)]
#     right_preorder = preorder[1+len(left_inorder):]
#     return left_preorder, left_inorder, right_preorder, right_inorder

# tree = TreeNode()
# list_tree = [tree]
# list_preorder = [preorder]
# list_inorder = [inorder]
# while len(list_preorder) > 0:
#     temp_tree = []
#     temp_preorder = []
#     temp_inorder = []
#     for ii in range(len(list_preorder)):
#         list_tree[ii].val = list_preorder[ii][0]
#         left_preorder, left_inorder, right_preorder, right_inorder = next_layer(list_preorder[ii], list_inorder[ii])
#         if left_preorder != []:
#             temp_preorder.append(left_preorder)
#             temp_inorder.append(left_inorder)
#             list_tree[ii].left = TreeNode()
#             temp_tree.append(list_tree[ii].left)
#         if right_preorder != []:
#             temp_preorder.append(right_preorder)
#             temp_inorder.append(right_inorder)
#             list_tree[ii].right = TreeNode()
#             temp_tree.append(list_tree[ii].right)
#     list_tree = temp_tree
#     list_preorder = temp_preorder
#     list_inorder = temp_inorder
#-----------------------------------------------------------------------------#
# # 106. 从中序与后序遍历序列构造二叉树
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]

# def backtrack(list_in,list_post):
#     if len(list_in) == 0:
#         return
#     else:
#         index = list_in.index(list_post[-1])
#         root = TreeNode(list_post[-1])
#         root.left = backtrack(list_in[0:index],list_post[0:index])
#         root.right = backtrack(list_in[index+1:],list_post[index:-1])
#     return root

# root = backtrack(inorder,postorder)
#-----------------------------------------------------------------------------#
# # 107. 二叉树的层序遍历 II
# root = TreeNode(3,None,None)
# root.left = TreeNode(9,None,None)
# root.right = TreeNode(20,None,None)
# root.right.left = TreeNode(15,None,None)
# root.right.right = TreeNode(7,None,None)

# output = []
# record = [root]
# layer = 0
# while len(record) > 0:
#     if len(output) == layer:
#         output = [[]] + output
#     temp_record = []
#     for ii in range(len(record)):
#         if record[ii]:
#             output[-(layer+1)].append(record[ii].val)
#             temp_record.append(record[ii].left)
#             temp_record.append(record[ii].right)
#     record = temp_record
#     layer += 1
# print(output[1:])
#-----------------------------------------------------------------------------#
# # 108. 将有序数组转换为二叉搜索树
# nums = [-10,-3,0,5,9]

# def backtrack(list1):
#     if len(list1) == 0:
#         return
#     else:
#         root = TreeNode(list1[len(list1)//2])
#         root.left = backtrack(list1[0:len(list1)//2])
#         root.right = backtrack(list1[len(list1)//2+1:])
#     return root
# root = backtrack(nums)

#-----------------------------------------------------------------------------#
# # 111. 二叉树的最小深度
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# root = TreeNode(2)
# root.right = TreeNode(3)
# root.right.right = TreeNode(4)
# root.right.right.right = TreeNode(5)
# root.right.right.right.right = TreeNode(6)

# #方法一：递归
# def maxDepth(root):
#     if not root:
#         return 0
#     else:
#         # if root.left == None and root.right == None:
#         #     return 1
#         # elif root.left == None and root.right != None:
#         if root.left == None and root.right != None:
#             return maxDepth(root.right) + 1
#         elif root.left != None and root.right == None:
#             return maxDepth(root.left) + 1
#         else:
#             return min(maxDepth(root.left), maxDepth(root.right)) + 1
# print(maxDepth(root))

# #方法二：层序遍历
# if root:
#     record = [root]
#     layer = 0
#     label = True
#     while len(record) > 0:
#         layer += 1
#         for _ in range(len(record)):
#             cur_node = record.pop(0)
#             if cur_node:
#                 if cur_node.left == None and cur_node.right == None:
#                     label = False
#                     print(layer)
#                     break
#                 record.append(cur_node.left)
#                 record.append(cur_node.right)
#         if label == False:
#             break
# else:
#     print(0)
    
# # 方法二旧版本
# if root:
#     layer = 1
#     record = [root]
#     while len(record) > 0:
#         temp_record = []
#         for ii in range(len(record)):
#             if record[ii]:
#                 if record[ii].left == None and record[ii].right == None:
#                     print(layer)
#                 else:
#                     temp_record.append(record[ii].left)
#                     temp_record.append(record[ii].right)
#         record = temp_record
#         layer += 1
# else:
#     print(0)
#-----------------------------------------------------------------------------#
# # 114. 二叉树展开为链表
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(5)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.right = TreeNode(6)

# # 方法一:前序遍历
# temp = []
# def dfs(root):
#     if not root:
#         return
#     temp.append(root)
#     dfs(root.left)
#     dfs(root.right)
# dfs(root)
# print(temp)
# for ii in range(len(temp)-1):
#     temp[ii].left = None
#     temp[ii].right = output[ii+1]

# 方法二：层序遍历－深度优先
# output = []
# def dfs(root):
#     if not root:
#         return 
#     else:
#         if root not in output:
#             output.append(root)
#         dfs(root.left)
#         dfs(root.right)
# dfs(root)
# # list1 = []
# # for node in output:
# #     list1.append(node.val)
# # print(list1)
# for ii in range(len(output)-1):
#     output[ii].left = None
#     output[ii].right = output[ii+1]
# #-----------------------------------------------------------------------------#
# # 115. 不同的子序列 动态规划 and 字符串
# s = "rabbbit"
# t = "rabbit"
# # s = "babgbag"
# # t = "bag"
# # s = "dbaaadcddccdddcadacbadbadbabbbcad"
# # t = "dadcccbaab"
# t = ""
# s = "a"

# if len(s) > 0 and len(t) > 0:
#     dp = [[0]*len(s) for _ in range(len(t))]
#     if s[0] == t[0]:
#         dp[0][0] = 1
#     else:
#         dp[0][0] = 0
#     for jj in range(1,len(s)):
#         if t[0] == s[jj]:
#             dp[0][jj] = dp[0][jj-1] + 1
#         else:
#             dp[0][jj] = dp[0][jj-1]
#     for ii in range(1,len(t)):
#         for jj in range(1,len(s)):
#             if s[jj] == t[ii]:
#                 dp[ii][jj] = dp[ii-1][jj-1] + dp[ii][jj-1]
#             else:
#                 dp[ii][jj] = dp[ii][jj-1]
#     print(dp[-1][-1])
# elif len(s) == 0 and len(t) > 0:
#     print(0)
# else:
#     print(1)
# # 超时
# from itertools import combinations
# comb = list(combinations(s,len(t)))
# count = 0
# for ii in range(len(comb)):
#     if list(comb[ii]) == list(t):
#         count += 1
# print(count)
#-----------------------------------------------------------------------------#
# # 116. 填充每个节点的下一个右侧节点指针
# class Node(object):
#     def __init__(self, val=0, left=None, right=None, next=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

# #方法一：层序遍历
# if root:
#     record = [root]
#     while len(record) > 0:
#         temp_record = []
#         for ii in range(len(record)):
#             if ii < len(record)-1:
#                 record[ii].next = record[ii+1]
#             else:
#                 record[ii].next = None
#             if record[ii].left:
#                 temp_record.append(record[ii].left)
#             if record[ii].right:
#                 temp_record.append(record[ii].right)
#         record = temp_record
#     return root
# else:
#     return None
#-----------------------------------------------------------------------------#
# # question 118 杨辉三角 已完成
# output = []
# if numRows >= 1:
#     output.append([1])
# if numRows >= 2:
#     output.append([1,1])
# if numRows >= 3:
#     for ii in range(2,numRows):
#         temp = []
#         for jj in range(len(output[ii-1])-1):
#             temp.append(output[ii-1][jj]+output[ii-1][jj+1])
#         output.append([1]+temp+[1])
#-----------------------------------------------------------------------------#
# # question 119 杨辉三角 II 已完成
# output = []
# if rowIndex >= 0:
#     output.append([1])
# if rowIndex >= 1:
#     output.append([1,1])
# if rowIndex >= 2:
#     for ii in range(2,rowIndex+1):
#         temp = []
#         for jj in range(len(output[ii-1])-1):
#             temp.append(output[ii-1][jj]+output[ii-1][jj+1])
#         output.append([1]+temp+[1])
# return output[rowIndex]
#-----------------------------------------------------------------------------#
# # question 121 买卖股票的最佳时机 已完成
# prices=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# # prices = [7,1,5,3,6,4]
# # prices = [7,6,4,3,1]

# #动态规划
# buy1 = -prices[0]
# sell1 = 0
# for ii in range(1,len(prices)):
#     buy1  = max(buy1,  -prices[ii])
#     sell1 = max(sell1, buy1+prices[ii])
# print(sell1)

# #旧版本
# output = 0
# if len(prices) > 1:
#     temp = max(prices)
#     for ii in range(len(prices)-1):
#         if prices[ii] < temp and prices[ii] < prices[ii+1]:
#             temp = prices[ii]
#             max_delta = max(prices[ii+1:]) - prices[ii]
#             if max_delta > output:
#                 output = max_delta
# print(output)

# # 123. 买卖股票的最佳时机 III
# prices = [3,3,5,0,0,3,1,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
# prices = [1]
# prices = [1,1,1,1,1,1,1,1]
# prices = [2,1,2,0,1]
# prices = [1,4,1,4,3,1]

# #动态规划
# dp = [[0]*len(prices) for _ in range(4)]
# dp[0][0] = dp[2][0] = -prices[0]
# dp[1][0] = dp[3][0] = 0
# for jj in range(1,len(prices)):
#     dp[0][jj] = max(dp[0][jj-1], -prices[jj]) #只进行过一次买操作
#     dp[1][jj] = max(dp[1][jj-1], dp[0][jj-1]+prices[jj]) #进行了一次买操作和一次卖操作，即完成了一笔交易
#     dp[2][jj] = max(dp[2][jj-1], dp[1][jj-1]-prices[jj]) #在完成了一笔交易的前提下，进行了第二次买操作
#     dp[3][jj] = max(dp[3][jj-1], dp[2][jj-1]+prices[jj]) #完成了全部两笔交易
# print(max(dp[-1]))

# #官方
# buy1 = -prices[0]
# sell1 = 0
# buy2 = -prices[0]
# sell2 = 0
# for ii in range(1,len(prices)):
#     buy1  = max(buy1,  -prices[ii])
#     sell1 = max(sell1, buy1+prices[ii])
#     buy2  = max(buy2,  sell1-prices[ii])
#     sell2 = max(sell2, buy2+prices[ii])
# print(sell2)

# # 188. 买卖股票的最佳时机 IV
# k = 2
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

# # 122. 买卖股票的最佳时机 II
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
#     dp[0][ii] = max(dp[0][ii-1], dp[1][ii-1]-prices[ii]) #持有
#     dp[1][ii] = max(dp[1][ii-1], dp[0][ii-1]+prices[ii]) #空仓
# print(dp[1][-1])

# # 714. 买卖股票的最佳时机含手续费
# prices = [1, 3, 2, 8, 4, 9]
# fee = 2

# dp = [[0]*len(prices) for _ in range(2)]
# dp[0][0] = -prices[0]-fee
# for ii in range(1,len(prices)):
#     dp[0][ii] = max(dp[0][ii-1], dp[1][ii-1]-prices[ii]-fee) #持有
#     dp[1][ii] = max(dp[1][ii-1], dp[0][ii-1]+prices[ii]) #空仓

# print(dp[1][-1])

# # 309. 最佳买卖股票时机含冷冻期
# prices = [1,2,3,0,2]

# dp = [[0]*len(prices) for _ in range(2)]
# dp[0][0] = -prices[0]
# dp[1][0] = 0
# dp[0][1] = max(dp[0][0], dp[1][0]-prices[1])
# dp[1][1] = max(dp[1][0], dp[0][0]+prices[1])
# for ii in range(2,len(prices)):
#     dp[0][ii] = max(dp[0][ii-1], dp[1][ii-2]-prices[ii]) #持有
#     dp[1][ii] = max(dp[1][ii-1], dp[0][ii-1]+prices[ii]) #空仓
# print(dp[1][-1])
#-----------------------------------------------------------------------------#
# # 124. 二叉树中的最大路径和 未完成
# root = TreeNode(-10)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# root = TreeNode(-1)
# root.left = TreeNode(5)
# root.left.left = TreeNode(4)
# root.left.left.right = TreeNode(2)
# root.left.left.right.left = TreeNode(-4)

# # 超时
# def pathSum(root):
#     output = []
#     def dfs(root, count):
#         if not root:
#             return
#         else:
#             output.append(count+root.val)
#             dfs(root.left, count+root.val)
#             dfs(root.right, count+root.val)
#     dfs(root, 0)
#     return max(output)
    
# temp = []
# def dfs(root):
#     if not root:
#         return
#     else:
#         if root.left == None and root.right == None:
#             temp.append(root.val)
#         elif root.left != None and root.right == None:
#             temp.append(max(root.val, pathSum(root.left), root.val+pathSum(root.left)))
#         elif root.left == None and root.right != None:
#             temp.append(max(root.val, pathSum(root.right), root.val+pathSum(root.right)))
#         else:
#             temp.append(max(root.val, pathSum(root.left), pathSum(root.right),
#                             root.val+pathSum(root.left)+pathSum(root.right),
#                             root.val+pathSum(root.left), root.val+pathSum(root.right)))
#     dfs(root.left)
#     dfs(root.right)
# dfs(root)
# print(max(temp))
#-----------------------------------------------------------------------------#
# # # question 125 验证回文串 已完成
# s = "A man, a plan, a canal: Panama"
# # s = "race a car"

# s = s.lower()
# s_keep = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'])

# #改进
# index_left = 0
# index_right = len(s)-1
# label = True
# while index_left < index_right:
#     if s[index_left] not in s_keep:
#         index_left += 1
#     elif s[index_right] not in s_keep:
#         index_right -= 1
#     elif s[index_left] in s_keep and s[index_right] in s_keep and s[index_left] == s[index_right]:
#         index_left += 1
#         index_right -= 1
#     else:
#         label = False
#         break
# print(label)

# #旧版本
# ss = ''
# for s1 in s:
#     if s1 in s_keep:
#         ss += s1
# index_left = 0
# index_right = len(ss)-1
# label = True
# while index_left < index_right:
#     if ss[index_left] == ss[index_right]:
#         index_left += 1
#         index_right -= 1
#     else:
#         label = label and False
#         break
# print(label)
#-----------------------------------------------------------------------------#
# # 126. 单词接龙 II
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"] #5

# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot","dog"] #0

# beginWord = "red"
# endWord = "tax"
# wordList = ["ted","tex","red","tax","tad","den","rex","pee"] #4

# beginWord = "a"
# endWord = "c"
# wordList = ["a","b","c"] #2

# beginWord = "qa"
# endWord = "sq"
# wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

# beginWord = "cat"
# endWord = "fin"
# wordList = ["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"]

# # 双向BFS改进，基于待访问的顶点集合 往下层遍历，并记录边，最后对记录的边集合进行DFS遍历生成所有可行路径
# def bfs_next(word):
#     #查询下一层单词
#     set1 = set()
#     for mm in range(len(word)):
#         for nn in range(26):
#             temp = word[0:mm] + chr(97+nn)+ word[mm+1:]
#             #如果新生成的单词 不在已访问的顶点集合中并且在wordList中，即待访问的顶点集合，则找到下一个连通的顶点
#             if temp not in set_visited and temp in set_word:
#                 set1.add(temp)
#     return set1
# def dfs(set_path, record_set):
#     #深度优先遍历所有可行路径
#     #如果记录中的最后一个单词与endWord相同，则终止
#     if record_set[-1] == endWord:
#         output.append(record_set)
#     else:
#         for word in set_path[record_set[-1]]:
#             # 如果当前单词在可行边集合之中，或者endWord相同，则继续往下寻找
#             if word in set_path or word == endWord:
#                 dfs(set_path, record_set+[word])
# set_word = set(wordList)
# if endWord in set_word:
#     set_start = set([beginWord]) #用于记录左侧待访问的顶点
#     set_end = set([endWord]) #用于记录右侧待访问的顶点
#     set_visited = set() #用于记录已访问过的顶点
#     set_path = {}                                   #记录路径（连通的路）
#     # count = 0                                       #计数
#     while len(set_start) > 0 and len(set_end) > 0 and len(set.intersection(set_start,set_end)) == 0:
#         #选择待访问顶点数量少的一侧开始广度优先遍历
#         if len(set_start) <= len(set_end):
#             #将待访问的顶点 增加至已访问过的顶点集合
#             set_visited.update(set_start)
#             #用于记录新的待访问顶点
#             set_temp = set()
#             while len(set_start) > 0:
#                 #从待访问的顶点集合中随机选择一个
#                 cur = set_start.pop()
#                 #生成新的待访问顶点
#                 next_words = bfs_next(cur)
#                 set_temp.update(next_words)
#                 set_path[cur] = list(next_words)    #记录路径 当前顶点：[与其连通的待访问顶点]
#             #新的待访问顶点集合替换 原先的待访问顶点集合
#             set_start = set_temp
#             # count += 1                              #计数
#         else:
#             set_visited.update(set_end)
#             set_temp = set()
#             while len(set_end) > 0:
#                 cur = set_end.pop()
#                 next_words = bfs_next(cur)
#                 set_temp.update(next_words)
#                 for word in list(next_words):       #记录路径
#                     if word not in set_path:        #记录路径
#                         set_path[word] = [cur]      #记录路径
#                     else:                           #记录路径
#                         set_path[word].append(cur)  #记录路径
#             set_end = set_temp
#             # count += 1                              #计数
#     # 如果set_start和set_end都不为空，说明找到公共顶点
#     if len(set_start) > 0 and len(set_end) > 0:
#         # print(count+1)                              #计数
#         output = []                                 #查找路径
#         dfs(set_path, [beginWord])                  #查找路径
#         print(output)                               #查找路径
#     else: #set_start或set_end为空，说明不是连通图
#         print(0)
# else:
#     print(0)

# # 超时 双向BFS，基于已遍历的连通路径 往下一层寻找，比基于待访问的顶点集合遍历的计算量多
# # 因为多条已遍历的连通路径 对应一个待访问的顶点
# import copy
# def bfs_next(record):
#     #广度优先遍历下一层所有连通的路径
#     output = []
#     set1 = set()
#     for ii in range(len(record)):
#         cur = record[ii][0][-1]
#         for mm in range(len(cur)):
#             for nn in range(26):
#                 temp = cur[0:mm] + chr(97+nn)+ cur[mm+1:]
#                 if temp not in record[ii][0] and temp in record[ii][1]:
#                     set1.add(temp)
#                     visited = copy.deepcopy(record[ii][0])
#                     visited.append(temp)
#                     waiting = copy.deepcopy(record[ii][1])
#                     waiting.remove(temp)
#                     output.append([visited, waiting])
#     return output, set1
# set_word = set(wordList)
# if endWord in set_word:
#     record_start = [[[beginWord],set_word]] # 记录 左侧已访问过的路径 + 未访问的顶点集合
#     record_end = [[[endWord],set_word]] # 记录 右侧已访问过的路径 + 未访问的顶点集合
#     set_start = set([beginWord]) # 用于记录 左侧待访问的顶点集合
#     set_end = set([endWord]) # 用于记录 右侧待访问的顶点集合
#     while len(record_start) > 0 and len(record_end) > 0 and len(set.intersection(set_start,set_end)) == 0:
#         # 选择已遍历的连通路径数量少的一侧开始往下找
#         if len(record_start) <= len(record_end):
#             # 更新已遍历的连通路径 及 待访问的顶点集合
#             record_start, set_start = bfs_next(record_start)
#         else:
#             record_end, set_end = bfs_next(record_end)
#     if len(record_start) > 0 and len(record_end) > 0:
#         # 根据公共顶点，生成最短连通路径
#         output2 = []
#         for ii in range(len(record_start)):
#             for jj in range(len(record_end)):
#                 if record_start[ii][0][-1] == record_end[jj][0][-1]:
#                     temp_end = []
#                     for word_in_end in record_end[jj][0]:
#                         temp_end = [word_in_end] + temp_end
#                     output2.append(record_start[ii][0]+temp_end[1:])
#         print(output2)
#     else:
#         print(0)
# else:
#     print(0)
    
# #题解
# import collections
# if not endWord in wordList:
#     print([])
# else:
#     hash=collections.defaultdict(list)
#     for word in wordList:
#         for ii in range(len(word)):
#             hash[word[0:ii]+"*"+word[ii+1:]].append(word)
#     def edges(word):
#         for ii in range(len(word)):
#             for newWord in hash[word[0:ii]+'*'+word[ii+1:]]:
#                 if not newWord in marked:
#                     yield newWord
#     def findPath(end):
#         res=[]
#         for curr in end:
#             for parent in path[curr[0]]:
#                 res.append([parent]+curr)
#         return res
#     marked=set()
#     path=collections.defaultdict(set)
#     begin=set([beginWord])
#     end=set([endWord])
#     forward=True
#     while begin and end:
#         if len(begin)>len(end):
#             begin,end=end,begin
#             forward=not forward
#         temp=set()
#         for word in begin:
#             marked.add(word)
#         for word in begin:
#             for w in edges(word):
#                 temp.add(w)
#                 if forward:
#                     path[w].add(word)
#                 else:
#                     path[word].add(w)
#         print(path)
#         begin=temp
        
#         if begin&end:
#             res=[[endWord]]
#             while res[0][0]!=beginWord:
#                 res=findPath(res)
#             print(res)
#-----------------------------------------------------------------------------#
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
#-----------------------------------------------------------------------------#
# # 130. 被围绕的区域 
# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","O","X"]]


#-----------------------------------------------------------------------------#
# # question 131 分割回文串 已完成
# from itertools import combinations
# def huiwen(ss):
#     if len(ss) == 1:
#         return True
#     else:
#         index_left = 0
#         index_right = len(ss)-1
#         label = True
#         while index_left < index_right:
#             if ss[index_left] == ss[index_right]:
#                 pass
#             else:
#                 label = False
#                 break
#             index_left += 1
#             index_right = index_right - 1
#         return label

# # s = 'aab'
# s = 'bb'
# # s = 'a'

# if len(s) > 1:
#     num = len(s)-1
#     output = []
#     for jj in range(num+1):
#         comb = list(combinations([hh+1 for hh in range(num)],jj))
#         for ii in range(len(comb)):
#             label = True
#             print(comb[ii])
#             index = 0
#             temp_s = []
#             for kk in range(len(comb[ii])):
#                 label = label and huiwen(s[index:comb[ii][kk]])
#                 if label:
#                     temp_s.append(s[index:comb[ii][kk]])
#                 else:
#                     break
#                 index = comb[ii][kk]
#             label = label and huiwen(s[index:])
#             if label:
#                 temp_s.append(s[index:])
#             if label == True:
#                 output.append(temp_s)
# else:
#     output = [[s]]
# print(output)
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

# # 超时，仅使用第二次DP
# def huiwen(ss):
#     if len(ss) == 1:
#         return True
#     else:
#         index_left = 0
#         index_right = len(ss)-1
#         label = True
#         while index_left < index_right:
#             if ss[index_left] == ss[index_right]:
#                 pass
#             else:
#                 label = False
#                 break
#             index_left += 1
#             index_right = index_right - 1
#         return label

# dp = [0]
# index = 1
# while index < len(s):
#     if huiwen(s[0:index] + s[index]):
#         dp.append(0)
#     else:
#         temp = []
#         for ii in range(index):
#             if huiwen(s[ii+1:index]+s[index]):
#                 temp.append(dp[ii]+1)
#         dp.append(min(temp))
#     index += 1
# print(dp[-1])

# # #超时
# # from itertools import combinations
# # def huiwen(ss):
# #     if len(ss) == 1:
# #         return True
# #     else:
# #         index_left = 0
# #         index_right = len(ss)-1
# #         label = True
# #         while index_left < index_right:
# #             if ss[index_left] == ss[index_right]:
# #                 pass
# #             else:
# #                 label = False
# #                 break
# #             index_left += 1
# #             index_right = index_right - 1
# #         return label
# # num = len(s)
# # for ii in range(num):
# #     label2 = False
# #     # print(ii)
# #     comb = list(combinations([hh+1 for hh in range(num-1)],ii))
# #     for jj in range(len(comb)):
# #         label = True
# #         # temp = []
# #         index = 0
# #         for kk in range(len(comb[jj])):
# #             if huiwen(s[index:comb[jj][kk]]):
# #                 label = label and True
# #             else:
# #                 label = label and False
# #             # temp.append(s[index:comb[jj][kk]])
# #             index = comb[jj][kk]
# #         if huiwen(s[index:]):
# #             label = label and True
# #         else:
# #             label = label and False
# #         # temp.append(s[index:])
# #         # print(temp)
        
# #         if label == True:
# #             label2 = True
# #             break
# #     if label2 == True:
# #         break
# # print(ii)
#-----------------------------------------------------------------------------#
# # 133. 克隆图
# class Node(object):
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
        
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node1.neighbors = [node2,node4]
# node2.neighbors = [node1,node3]
# node3.neighbors = [node2,node4]
# node4.neighbors = [node1,node3]
# node = node1

# list_node = []
# def dfs(node):
#     if not node:
#         return
#     if node not in list_node:
#         list_node.append(node)
#     print(node.val)
#     for ii in range(len(node.neighbors)):
#         if node.neighbors[ii] not in list_node:
#             dfs(node.neighbors[ii])
# dfs(node)

# list_node_new = []
# for ii in range(len(list_node)):
#     list_node_new.append(Node(list_node[ii].val))

# for ii in range(len(list_node_new)):
#     list_node_new[ii].neighbors = []
#     for jj in range(len(list_node[ii].neighbors)):
#         index = list_node.index(list_node[ii].neighbors[jj])
#         list_node_new[ii].neighbors.append(list_node_new[index])
# node_new = list_node_new[0]
#-----------------------------------------------------------------------------#
# # 134. 加油站
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# gas  = [2,3,4]
# cost = [3,4,3]
# gas = [5,1,2,3,4]
# cost = [4,4,1,5,1]
# gas = [5,8,2,8]
# cost = [6,5,6,6]

# label2 = False
# for ii in range(len(gas)):
#     count = 0
#     label = True
#     for jj in range(len(gas)):
#         count += gas[(ii+jj)%len(gas)] - cost[(ii+jj)%len(gas)]
#         if count < 0:
#             label = False
#             break
#     if label == True:
#         label2 = True
#         break
# if label2 == True:
#     print(ii)
# else:
#     print(-1)
#-----------------------------------------------------------------------------#
# # 135. 分发糖果
# ratings = [1,2,5,5,5,3,2,4,6,2,9,8,1]
# ratings = [1,2,4,5,5,3,2,1,6,9,9,8,1]
# ratings = [1,0,2]
# ratings = [1,2,2]
# ratings = [1,2,4]
# ratings = [3,2,1]
# ratings = [3]
# ratings = [1,3,4,5,2]

# dp = [1 for _ in range(len(ratings))]
# for ii in range(1,len(ratings)):
#     if ratings[ii-1] < ratings[ii]:
#         dp[ii] = max(dp[ii-1] + 1, dp[ii])
#     else:
#         break
# for jj in range(len(ratings)-2,-1,-1):
#     if ratings[jj] > ratings[jj+1]:
#         dp[jj] = max(dp[jj+1] + 1, dp[jj])
#     else:
#         break
# for local_min in range(1,len(ratings)-1):
#     if ratings[local_min-1] >= ratings[local_min] and ratings[local_min] <= ratings[local_min+1]:
#         # print(local_min)
#         index = 0
#         while local_min+index+1 < len(ratings) and ratings[local_min+index] < ratings[local_min+index+1]:
#             dp[local_min+index+1] = max(dp[local_min+index]+1,dp[local_min+index+1])
#             index += 1
#         index = 0
#         while local_min-index-1 > -1 and ratings[local_min-index] < ratings[local_min-index-1]:
#             dp[local_min-index-1] = max(dp[local_min-index]+1,dp[local_min-index-1])
#             index += 1
# print(dp)
# print(sum(dp))
#-----------------------------------------------------------------------------#
# # 139. 单词拆分
# s = "leetcode"
# wordDict = ["leet", "code"] #True
# s = "applepenapple"
# wordDict = ["apple", "pen"] #True
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"] #False
# s = "a"
# wordDict = ["b"] #False
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"] #True
# s = "aaaaaaa"
# wordDict = ["aaaa","aaa"] #True

# # 动态规划
# word_len = []
# for word in wordDict:
#     if len(word) not in word_len:
#         word_len.append(len(word))
# word_len.sort()

# dp = [False for _ in range(len(s))]
# for ii in range(len(s)):
#     if ii+1 >= word_len[0]:
#         label = False
#         for len1 in word_len:
#             if ii-len1+1 == 0:
#                 if s[ii-len1+1:ii]+s[ii] in wordDict:
#                     label = True
#                     break
#             elif ii-len1+1 > 0:
#                 if s[ii-len1+1:ii]+s[ii] in wordDict and dp[ii-len1]:
#                     label = True
#                     break
#         dp[ii] = label
# print(dp[-1])

# # 递归超时
# set_words = set()
# word_len = []
# for word in wordDict:
#     for ss in word:
#         set_words.add(ss)
#     if len(word) not in word_len:
#         word_len.append(len(word))
# word_len.sort(reverse=True)

# label2 = True
# for ss in s:
#     if ss not in set_words:
#         label2 = False
#         break
# if label2 == True:
#     def backtrack(ss):
#         if len(ss) == 0:
#             return True
#         else:
#             label = False
#             for ii in word_len:
#                 if len(ss) >= ii and ss[0:ii] in wordDict:
#                     label = label or backtrack(ss[ii:])
#                     if label == True:
#                         break
#             return label
#     print(backtrack(s))
# else:
#     print(False)

# # 140. 单词拆分 II
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# # s = "pineapplepenapple"
# # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# # s = "catsandog"
# # wordDict = ["cats", "dog", "sand", "and", "cat"]

# word_len = []
# for word in wordDict:
#     if len(word) not in word_len:
#         word_len.append(len(word))
# word_len.sort()

# record = []
# def backtrack(ss,list1):
#     if len(ss) == 0:
#         record.append(' '.join(list1))
#         return
#     else:
#         for ii in word_len:
#             if len(ss) >= ii and ss[0:ii] in wordDict:
#                 backtrack(ss[ii:], list1+[ss[0:ii]])
# backtrack(s, [])
# print(record)
#-----------------------------------------------------------------------------#
# # 152. 乘积最大子数组
# nums = [2,3,-2,4]
# nums = [-2,0,-1]
# nums = [-2,3,-4]
# nums = [-5,2,4,1,-2,2,-6,3,-1,-1,-1,-2,-3,5,1,-3,-4,2,-4,6,-1,5,-6,1,-1,
#         -1,1,1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,1,-1,1,1,
#         -1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,1,-1,-1,-1,-1]
# # nums = [-3,0,1,-2]
# # nums = [0,-3,1,1]

# dp1 = [1 for _ in range(len(nums))]
# dp2 = [1 for _ in range(len(nums))]
# dp1[0] = nums[0] # 最大
# dp2[0] = nums[0] # 最小

# for ii in range(1,len(nums)):
#     if nums[ii] == 0:
#         dp1[ii] = 0
#         dp2[ii] = 0
#     elif nums[ii] > 0:
#         dp1[ii] = max(nums[ii]*dp1[ii-1], nums[ii])
#         dp2[ii] = min(nums[ii]*dp2[ii-1], nums[ii])
#     else:
#         dp1[ii] = max(nums[ii]*dp2[ii-1], nums[ii])
#         dp2[ii] = min(nums[ii]*dp1[ii-1], nums[ii])
# print(dp1)
# print(dp2)
# print(max(dp1))
#-----------------------------------------------------------------------------#
# # question 165 比较版本号 已完成
# version1 = "1.01"
# version2 = "1.001"
# # version1 = "1.0"
# # version2 = "1.0.0"
# # version1 = "0.1"
# # version2 = "1.1"
# # version1 = "1.0.1"
# # version2 = "1"
# # version1 = "7.5.2.4"
# # version2 = "7.5.3"

# v1 = version1.split('.')
# v2 = version2.split('.')
# v11 = [0 for _ in range(max(len(v1),len(v2)))]
# v12 = [0 for _ in range(max(len(v1),len(v2)))]
# for ii in range(len(v1)):
#     v11[ii] = int(v1[ii])
# for jj in range(len(v2)):
#     v12[jj] = int(v2[jj])
# label = True
# for ii in range(len(v11)):
#     if v11[ii] > v12[ii]:
#         print(1)
#         label = label and False
#         break
#     elif v11[ii] < v12[ii]:
#         print(-1)
#         label = label and False
#         break
#     # else:
#     #     label = label and True
# if label == True:
#     print(0)
#-----------------------------------------------------------------------------#
# # question 167 两数之和II - 输入有序数组
# numbers = [1,2,7,11,15]
# target = 9
# # numbers = [0,0,0,0,0,0,0,2,3,9,9,9,9,9,9,9,9,9,9]
# # target = 5

# index_left = 0
# index_right = len(numbers)-1
# while index_left < index_right:
#     if numbers[index_left] + numbers[index_right] > target:
#         index_right -= 1
#     elif numbers[index_left] + numbers[index_right] < target:
#         index_left += 1
#     else:
#         break
# print(numbers[index_left],numbers[index_right])
# print([index_left+1, index_right+1])
#-----------------------------------------------------------------------------#
# # question 168 Excel表列名称 已完成
# columnNumber = 26*26**2 + 26*26**1 + 25*26**0
# columnNumber = 1
# columnNumber = 28
# columnNumber = 701
# columnNumber = 702
# columnNumber = 703

# import math
# dict1 = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',
#          8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',
#          15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',
#          21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
# list_index = []
# for ii in range(int(math.log(columnNumber,26)), -1,-1):
#     list_index.append(columnNumber//26**ii)
#     columnNumber -= columnNumber//26**ii*26**ii
# print(list_index)

# columnStr = ''
# label_borrow = False
# index = len(list_index)-1
# while index > -1:
#     if label_borrow == True:
#         if list_index[index] != 0:
#             list_index[index] -= 1
#             label_borrow = False
#         else:
#             list_index[index] = 25
#             label_borrow = True
#     if list_index[index] == 0 and index == 0:
#         break
#     elif list_index[index] == 0 and index != 0:
#         columnStr = dict1[26] + columnStr
#         label_borrow = True
#         index -= 1
#     else:
#         columnStr = dict1[list_index[index]] + columnStr
#         index -= 1
# print(columnStr)

# # question 171 Excel表列序号
# columnTitle = "A"
# # columnTitle = "AB"
# # columnTitle = "ZY"

# dict2 = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,
#           'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
#           'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,
#           'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
# count = 0
# for ii in range(len(columnTitle)):
#     count += dict2[columnTitle[ii]]*26**(len(columnTitle)-1-ii)
# print(count)

# # question 405 数字转换为十六进制数
# num = 15*16**7 + 15*16**6 + 15*16**5 + 15*16**4 + 15*16**3 + 15*16**2 + 15*16**1 + 15*16**0
# num = 26
# num = -2
# import math
# dict1 = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',
#          8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}

# if num != 0:
#     if num < 0:
#         num = 4294967295 + 1 + num
#     num_str = ''
#     for ii in range(int(math.log(num,len(dict1))), -1,-1):
#         num_str += dict1[num//len(dict1)**ii]
#         num -= num//len(dict1)**ii*len(dict1)**ii
# else:
#     num_str = '0'
# print(num_str)

# # question 504 七进制数
# num = 6*7**8 + 6*7**7 + 6*7**6 + 6*7**5 + 6*7**4 + 6*7**3 + 6*7**2 + 6*7**1 + 6*7**0
# # num = 100
# # num = -7
# import math
# dict1 = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6'}

# if num != 0:
#     if num > 0:
#         num_str = ''
#     else:
#         num_str = '-'
#         num = -num
#     for ii in range(int(math.log(num,len(dict1))), -1,-1):
#         num_str += dict1[num//len(dict1)**ii]
#         num -= num//len(dict1)**ii*len(dict1)**ii
# else:
#     num_str = '0'
# print(num_str)
#-----------------------------------------------------------------------------#
# # 174. 地下城游戏
# dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]

# #超时
# ops = ['down']*(len(dungeon)-1) + ['right']*(len(dungeon[0])-1)
# output = []
# def backtrack(record, coordinate, ops):
#     if len(ops) == 0:
#         output.append(record)
#     else:
#         for ii in range(len(ops)):
#             if ops[ii] == 'down':
#                 backtrack(record+[record[-1]+dungeon[coordinate[0]+1][coordinate[1]]], [coordinate[0]+1,coordinate[1]], ops[0:ii]+ops[ii+1:])
#             elif  ops[ii] == 'right':
#                 backtrack(record+[record[-1]+dungeon[coordinate[0]][coordinate[1]+1]], [coordinate[0],coordinate[1]+1], ops[0:ii]+ops[ii+1:])
# backtrack([dungeon[0][0]],[0,0],ops)

# blood = -float('inf')
# for ii in range(len(output)):
#     # print(min(output[ii]))
#     blood = max(min(output[ii]),blood)
# if blood <= 0:
#     print(-blood+1)
# else:
#     print(blood)
#-----------------------------------------------------------------------------#
# # 187. 重复的DNA序列
# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# # s = "AAAAAAAAA" # 9
# # s = "AAAAAAAAAA" #10
# # s = "AAAAAAAAAAA" #11
# # s = "AAAAAAAAAAAAA" #13

# dict1 = {}
# output = []
# for ii in range(len(s)-9):
#     if s[ii:ii+10] not in dict1:
#         dict1[s[ii:ii+10]] = 1
#     else:
#         dict1[s[ii:ii+10]] += 1
#         if dict1[s[ii:ii+10]] == 2:
#             output.append(s[ii:ii+10])
# print(output)

# # #超时
# # record = []
# # for ii in range(len(s)-10):
# #     if s[ii:ii+10] in s[ii+1:] and s[ii:ii+10] not in record:
# #         record.append(s[ii:ii+10])
# # print(record)
#-----------------------------------------------------------------------------#
# # 201. 数字范围按位与
# left = 5
# right = 7
# # left = 0
# # right = 0
# # left = 1
# # right = 2147483647

# b_left = bin(left).split('b')[-1]
# b_right = bin(right).split('b')[-1]
# b_left = '0'*(len(b_right)-len(b_left)) + b_left

# count = 0
# for ii in range(len(b_right)):
#     if b_left[ii] == b_right[ii]:
#         count += int(b_left[ii])*2**(len(b_right)-1-ii)
#     else:
#         break
# print(count)

# # 898. 子数组按位或操作
# # arr = [0]
# arr = [1,1,2]
# # arr = [1,2,4]

# #超时
# output = []
# for ii in range(len(arr)):
#     for len1 in range(1,len(arr)+1-ii):
#         # print(arr[ii:ii+len1])
#         if len1 == 1:
#             count = arr[ii]
#         else:
#             count = count | arr[ii+len1-1]
#         if count not in output:
#             output.append(count)
# print(len(output))

# # 超时
# def anweihuo(list1):
#     count = list1[0]
#     for ii in range(1,len(list1)):
#         count = count | list1[ii]
#     return count
# output = []
# for ii in range(len(arr)):
#     if arr[ii] not in output:
#         output.append(arr[ii])
# if len(arr) > 1:
#     for len1 in range(2,len(arr)+1):
#         for ii in range(len(arr)-len1+1):
#             temp = anweihuo(arr[ii:ii+len1])
#             if temp not in output:
#                 output.append(temp)
# print(len(output))

# # 982. 按位与为零的三元组
# A = [0,2,1,0,3,2,3,1] #392

# # 超时
# count = 0
# for ii in range(len(A)):
#     if A[ii] == 0:
#         count += len(A)**2
#     else:
#         temp = A[ii]-
#         for jj in range(len(A)):
#             if temp & A[jj] == 0:
#                 count += len(A)
#             else:
#                 temp2 = temp & A[jj]
#                 for kk in range(len(A)):
#                     if temp2 & A[kk] == 0:
#                         count += 1
# print(count)
# # 超时
# from itertools import combinations
# count = 0
# combs = list(combinations(A, 2))
# for comb in combs:
#     #print(list(comb))
#     if list(comb)[0] & list(comb)[1] == 0:
#         count += 6
# combs = list(combinations(A, 3))
# for comb in combs:
#     #print(list(comb))
#     if list(comb)[0] & list(comb)[1] & list(comb)[2] == 0:
#         count += 6
# print(count + A.count(0))
#-----------------------------------------------------------------------------#
# # question 202 快乐数 已完成
# n = 123
# record = [n]
# label = True
# while record[-1] != 1:
#     temp = 0
#     for ss in str(record[-1]):
#         temp += int(ss)**2
#     if temp not in record:
#         record.append(temp)
#     else:
#         label = False
#         break
# print(label)
#-----------------------------------------------------------------------------#
# # 207. 课程表
# numCourses = 2
# prerequisites = [[1,0]]
# prerequisites = [[1,0],[0,1]]

#-----------------------------------------------------------------------------#
# # question 214 最短回文串 已完成 - 找前N个连续字符是回文串，且N最大化
# s = "aabadabaaa"
# # s = "aabadabaa"
# # s = "aabadaba"
# # s = "aabaadabaaa"
# # s = "aabcdeaaa"
# # s = "aabcdea"
# # s = "abcd"
# # s = "abbacd"

# s2 = ''
# for ss in s:
#     s2 = ss + s2

# index = 1
# for ii in range(len(s)-1):
#     if s[0:len(s)-ii] == s2[ii:]:
#         index = len(s)-ii
#         break
        
# temp = ''
# for ii in range(index,len(s)):
#     temp = s[ii] + temp
# output = temp + s
# print(output)

# # 超时
# huiwen = [[True]*len(s) for _ in range(len(s))]
# for ii in range(len(s)-1,-1,-1):
#     for jj in range(ii+1,len(s)):
#         huiwen[ii][jj] = huiwen[ii+1][jj-1] and s[ii] == s[jj]

# index_right = 0
# index_max = 0
# while index_right < len(s):
#     if huiwen[0][index_right] == True:
#         if index_right > index_max:
#             index_max = index_right
#     index_right += 1
    
# temp = ''
# for ii in range(index_max+1,len(s)):
#     temp = s[ii] + temp
# output = temp + s
# print(output)
#-----------------------------------------------------------------------------#
# # question 219 存在重复元素 II 已完成
# nums = [1,2,3,1]
# k = 3
# nums = [1,0,1,1]
# k = 1
# # nums = [1,2,3,1,2,3]
# # k = 2

# label = False
# dict1 = {}
# for ii in range(len(nums)):
#     if nums[ii] not in dict1:
#         dict1[nums[ii]] = ii
#     else:
#         if ii - dict1[nums[ii]] > k:
#             dict1[nums[ii]] = ii
#         else:
#             label = True
#             break
# print(label)
#-----------------------------------------------------------------------------#
# # 220. 存在重复元素 III  桶排序
# nums = [1,2,3,1]
# k = 3
# t = 0
# # nums = [1,0,1,1]
# # k = 1
# # t = 2
# nums = [1,5,9,1,5,9]
# k = 2
# t = 3

# def index_bucket(num):
#     if num >= 0:
#         return num//(t+1)
#     else:
#         return -((-num-1)//(t+1)+1)

# bucket = {} #桶队列
# label = False
# for ii in range(len(nums)):
#     temp_index = index_bucket(nums[ii])
#     if temp_index in bucket: #如果当前num的桶编号在队列之中，则满足终止条件
#         label = True
#         break
#     else:
#         # 如果当前num的桶左邻编号在队列之中，并且该桶内的元素与当前num的距离小于t
#         if temp_index-1 in bucket and abs(bucket[temp_index-1] - nums[ii]) <= t:
#             label = True
#             break
#         # 如果当前num的桶右邻编号在队列之中，并且该桶内的元素与当前num的距离小于t
#         elif temp_index+1 in bucket and abs(bucket[temp_index+1] - nums[ii]) <= t:
#             label = True
#             break
#         else:
#             #队列增加新的桶
#             bucket[temp_index] = nums[ii]
#             #维护桶队列的数量，将ii-k对应的桶移除，使得桶队列的长度始终小于k
#             if ii >= k:
#                 del(bucket[index_bucket(nums[ii-k])])
# print(label)
#-----------------------------------------------------------------------------#
# # 223. 矩形面积
# A = -2
# B = -2
# C = 2
# D = 2
# E = -2
# F = 2
# G = 2
# H = 4

# if E <= A < G <= C:
#     len_x = G - A
# elif E <= A < C < G:
#     len_x = C - A
# elif A < E < G <= C:
#     len_x = G - E
# elif A < E < C < G:
#     len_x = C - E
# else:
#     len_x = 0
# if F <= B < H <= D:
#     len_y = H - B
# elif F <= B < D < H:
#     len_y = D - B
# elif B < F < H <= D:
#     len_y = H - F
# elif B < F < D < H:
#     len_y = D - F
# else:
#     len_y = 0
# print((C-A)*(D-B) + (G-E)*(H-F) - len_x*len_y)
#-----------------------------------------------------------------------------#
# # question 224 基本计算器
# # s = "(1+(4+5+2)-3)+(6+8)"
# # s = "1 + 1"
# # s = " 2-1 + 2 "
# # s = "-2+ 1"
# s = "- (3 + (14 + 5)) + ( 9 - 1)"
# # s = "2-(5-6)"

# # 用栈记录括号前的+-
# s = s+' '
# count = 0
# temp = ''
# fuhao = [1]
# for ii in range(len(s)):
#     if s[ii] not in [' ','+','-','(',')']:
#         temp += s[ii]
#         # print(temp)
#     else:
#         if temp != '':
#             # print(temp)
#             temp = int(temp)
#             for jj in range(len(fuhao)):
#                 temp = temp*fuhao[jj]
#             count += temp
#         temp = ''
#         if s[ii] == '+':
#             fuhao[-1] = 1
#         elif s[ii] == '-':
#             fuhao[-1] = -1
#         elif s[ii] == '(':
#             fuhao.append(1)
#         elif s[ii] == ')':
#             del(fuhao[-1])
# print(count)

# # # 超时 - 从内层括号向外，逐层求解
# # s = s.replace(' ','')
# # index2 = len(s)-1
# # while index2 > 0:
# #     if s[index2] == ')':
# #         label = True
# #         break
# #     else:
# #         index2 = index2 - 1
# # if index2 == 0:
# #     label = False
# # while label == True:
# #     index = 0
# #     while index < len(s):
# #         if s[index] == '(':
# #             index_left = index
# #             index += 1
# #         elif s[index] == ')':
# #             index_right = index
# #             break
# #         else:
# #             index += 1
# #     temp = s[index_left+1:index_right]
# #     # temp = temp.replace('-','+-')
# #     temp = temp.replace('-','+-')
# #     temp2 = temp.split('+')
# #     count = 0
# #     for ii in range(len(temp2)):
# #         if temp2[ii] != '':
# #             count += int(temp2[ii])
# #     s3 = s[0:index_left] + str(count)
# #     s = s3.replace('--','+') + s[index_right+1:]
# #     print(s)
# #     index2 = len(s)-1
# #     while index2 > 0:
# #         if s[index2] == ')':
# #             label = True
# #             break
# #         else:
# #             index2 = index2 - 1
# #     if index2 == 0:
# #         label = False

# # s = s.replace('-','+-')
# # s2 = s.split('+')
# # count = 0
# # for ii in range(len(s2)):
# #     if s2[ii] != '':
# #         count += int(s2[ii])
# # print(count)

# # 227. 基本计算器 II 已完成
# s = " 3+5 / 2 -3+2*2"
# s = "3+2*2"
# s = " 3/2 "
# s = " 3+5 / 2 "
# def chengchu(ss):
#     count2 = 1
#     label_chengchu = 1
#     temp2 = ''
#     for ii in range(len(ss)):
#         if ss[ii] not in ['*','/']:
#             temp2 += ss[ii]
#         else:
#             # print(temp2)
#             if label_chengchu == 1:
#                 count2 = count2*int(temp2)
#             else:
#                 count2 = count2//int(temp2)
#             if ss[ii] == '*':
#                 label_chengchu = 1
#             elif ss[ii] == '/':
#                 label_chengchu = -1
#             temp2 = ''
#     if label_chengchu == 1:
#         count2 = count2*int(temp2)
#     else:
#         count2 = count2//int(temp2)
#     return count2

# count = 0
# temp = ''
# label_fuhao = 1
# # print(label_fuhao)
# for ii in range(len(s)):
#     if s[ii] not in ['+', '-']:
#         temp += s[ii]
#     else:
#         if '/' not in temp and '*' not in temp:
#             count += int(temp)*label_fuhao
#         else:
#             count += chengchu(temp)*label_fuhao
#         # print(temp)
#         if s[ii] == '-':
#             label_fuhao = -1
#         else:
#             label_fuhao = 1
#         temp = ''
# if '/' not in temp and '*' not in temp:
#     count += int(temp)*label_fuhao
# else:
#     count += chengchu(temp)*label_fuhao
# print(count)
#-----------------------------------------------------------------------------#
# # question 228 汇总区间 已完成
# # nums = [0,1,2,4,5,7]
# # nums = [0,2,3,4,6,8,9]
# # nums = []
# # nums = [-1]
# nums = [0]

# output = []
# if len(nums) > 0:
#     record = [nums[0]]
#     for ii in range(1,len(nums)):
#         if nums[ii] == nums[ii-1] + 1:
#             record.append(nums[ii])
#         else:
#             # print(record)
#             if len(record) == 1:
#                 output.append(str(record[0]))
#             else:
#                 output.append(str(record[0])+'->'+str(record[-1]))
#             record = [nums[ii]]
#     # print(record)
#     if len(record) == 1:
#         output.append(str(record[0]))
#     else:
#         output.append(str(record[0])+'->'+str(record[-1]))
# print(output)
#-----------------------------------------------------------------------------#
# # 235. 二叉搜索树的最近公共祖先
# root = TreeNode(6)
# root.left = TreeNode(2)
# root.right = TreeNode(8)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(4)
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)
# root.right.left = TreeNode(7)
# root.right.right = TreeNode(9)

# p = root.left
# q = root.left.right 

# while root:
#     if min(p.val,q.val) <= root.val <= max(p.val,q.val):
#         break
#     elif max(p.val,q.val) < root.val:
#         root = root.left
#     else:
#         root = root.right
# print(root.val)
#-----------------------------------------------------------------------------#
# # 238. 除自身以外数组的乘积
# nums = [1,2,3,4]
# if 0 in nums:
#     if nums.count(0) > 1:
#         output = [0 for _ in range(len(nums))]
#     else:
#         output = [0 for _ in range(len(nums))]
#         count = 1
#         for ii in range(len(nums)):
#             if nums[ii] != 0:
#                 count = count * nums[ii]
#         output[nums.index(0)] = count
# else:
#     output = []
#     count = 1
#     for ii in range(len(nums)):
#         count = count * nums[ii]
#     for ii in range(len(nums)):
#         output.append(int(count/nums[ii]))
# print(output)
#-----------------------------------------------------------------------------#
# # question 263 丑数
# n = 0
# if n == 0:
#     print(False)
# else:
#     while n % 5 == 0:
#         n = n // 5
#     while n % 3 == 0:
#         n = n // 3
#     while n % 2 == 0:
#         n = n // 2
#     if n == 1:
#         print(True)    
#     else:
#         print(False)
#-----------------------------------------------------------------------------#
# # 264. 丑数 II
# n = 1690

# # 方法一：每次从堆中取出最小的丑数x，如果2x, 3x, 5x不在堆中则加入堆 
# record = [1]
# for _ in range(n):
#     record.sort()
#     temp = record.pop(0)
#     if temp*2 not in record:
#         record.append(temp*2)
#     if temp*3 not in record:
#         record.append(temp*3)
#     if temp*5 not in record:
#         record.append(temp*5)
# print(temp)
#-----------------------------------------------------------------------------#
# # question 273 整数转换英文表示 已完成
# # num = 1234567891
# # num = 20
# num = 1000000000
# output_target = "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

# num_en1 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
#            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 
#            'Seventeen', 'Eighteen', 'Nineteen']
# num_en2 = ['','','Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
# # Hundred
# num_en3 = ['', 'Thousand', 'Million', 'Billion']

# num_str = str(num)
# num_str2 = ''
# for ss in num_str:
#     num_str2 = ss + num_str2
# output = ''
# index = 0
# while index <= len(num_str)-1:
#     if index%3 == 0:
#         if output[0:len('Zero')+1] == ' Zero':
#             output = output[len('Zero')+1:]
#         if output[0:len('Thousand')+1] == ' Thousand':
#             output = output[len('Thousand')+1:]
#         if output[0:len('Million')+1] == ' Million':
#             output = output[len('Million')+1:]
#         output = ' ' + num_en3[index//3] + output
#     if index%3 != 2 and index != len(num_str2)-1 and (int(num_str2[index+1]) == 0 or int(num_str2[index+1])) == 1:
#         # 十分位为0或1
#         temp = num_str2[index+1]+num_str2[index]
#         output = ' ' + num_en1[int(temp)] + output
#         index = index + 2
#     elif index%3 != 2 and index != len(num_str2)-1 and int(num_str2[index+1]) != 0 and int(num_str2[index+1]) != 1:
#         # 十分位为2-9
#         if int(num_str2[index]) == 0:
#             output = ' ' + num_en2[int(num_str2[index+1])] + output
#         else:
#             output = ' ' + num_en2[int(num_str2[index+1])] + ' ' + num_en1[int(num_str2[index])] + output
#         index = index + 2
#     elif index%3 != 2 and index == len(num_str2)-1:
#         # 个位
#         output = ' ' + num_en1[int(num_str2[index])] + output
#         index = index + 1
#     elif index%3 == 2 and int(num_str2[index]) == 0:
#         # 百分位为0
#         index = index + 1
#     elif index%3 == 2 and int(num_str2[index]) != 0:
#         # 百分位不为0
#         if output[0:len('Zero')+1] == ' Zero':
#             output = output[len('Zero')+1:]
#         output = ' ' + num_en1[int(num_str2[index])] + ' ' +'Hundred' + output
#         index = index + 1
            
# output = output.strip()    
# print(output)
#-----------------------------------------------------------------------------#
# # 274. H 指数 已完成
# citations = [3,0,6,1,5]
# # citations = [100,99]
# citations = [0,1,0]

# citations.sort()
# label = False
# for ii in range(len(citations),0,-1):
#     if citations[len(citations)-ii] >= ii:
#         label = True
#         print(ii)
#         break
# if label == False:
#     print(0)
#-----------------------------------------------------------------------------#
# # question 278 第一个错误的版本
# def isBadVersion(version):
#     if version >= 558565:
#         return True
#     else:
#         return False
# n = 48465515
# index = [1, n]
# while isBadVersion(index[-1]) == True:
#     if isBadVersion((index[-1]-index[0])//2+index[0]) == True:
#         index[-1] = (index[-1]-index[0])//2+index[0]-1
#     else:
#         index[-1] -= 1
#         index[0] = (index[-1]-index[0])//2+index[0]
#     print(index)
# print(index[-1]+1)

# # question 374 猜数字大小
# n = 1
# pick = 1
# n = 20
# pick = 20

# def guess(num):
#     if pick < num:
#         return -1
#     elif pick > num:
#         return 1
#     else:
#         return 0

# if guess(n) == 0:
#     print(n)
# else:
#     index = [1,n]
#     while guess((index[1]-index[0])//2+index[0]) != 0:
#         if guess((index[1]-index[0])//2+index[0]) == 1:
#             index[0] = (index[1]-index[0])//2+index[0]
#         else:
#             index[1] = (index[1]-index[0])//2+index[0]
#         # print(index)
#     print((index[1]-index[0])//2+index[0])
#-----------------------------------------------------------------------------#
# # 289. 生命游戏
# board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# board = [[1,1],[1,0]]

# import copy
# board2 = copy.deepcopy(board)

# def check(ii,jj,target):
#     count = 0
#     if 0 <= ii-1 < len(board) and 0 <= jj-1 < len(board[0]) and board2[ii-1][jj-1] == target:
#         count += 1
#     if 0 <= ii-1 < len(board) and 0 <= jj < len(board[0]) and board2[ii-1][jj] == target:
#         count += 1
#     if 0 <= ii-1 < len(board) and 0 <= jj+1 < len(board[0]) and board2[ii-1][jj+1] == target:
#         count += 1
#     if 0 <= ii < len(board) and 0 <= jj-1 < len(board[0]) and board2[ii][jj-1] == target:
#         count += 1
#     if 0 <= ii < len(board) and 0 <= jj+1 < len(board[0]) and board2[ii][jj+1] == target:
#         count += 1
#     if 0 <= ii+1 < len(board) and 0 <= jj-1 < len(board[0]) and board2[ii+1][jj-1] == target:
#         count += 1
#     if 0 <= ii+1 < len(board) and 0 <= jj < len(board[0]) and board2[ii+1][jj] == target:
#         count += 1
#     if 0 <= ii+1 < len(board) and 0 <= jj+1 < len(board[0]) and board2[ii+1][jj+1] == target:
#         count += 1
#     return count

# for ii in range(len(board)):
#     for jj in range(len(board[0])):
#         if board2[ii][jj] == 1:
#             if check(ii,jj,1) < 2 or check(ii,jj,1) > 3:
#                 board[ii][jj] = 1 - board2[ii][jj]
#         if board2[ii][jj] == 0:
#             if check(ii,jj,1) == 3:
#                 board[ii][jj] = 1 - board2[ii][jj]
# print(board)
#-----------------------------------------------------------------------------#
# # question 290 单词规律 已完成
# pattern = "abba"
# s = "dog cat cat dog"
# # pattern = "abba"
# # s = "dog cat cat fish"
# # pattern = "aaaa"
# # s = "dog cat cat dog"
# # pattern = "abba"
# # s = "dog dog dog dog"
# # pattern = "abc"
# # s = "b c a"
# # pattern = "aaa"
# # s = "aa aa aa aa"

# words = s.split(' ')
# label = True

# if len(words) != len(pattern):
#     label = False
# else:
#     record_p = []
#     record_s = []
#     for ii in range(len(words)):
#         if pattern[ii] not in record_p and words[ii] not in record_s:
#             record_p.append(pattern[ii])
#             record_s.append(words[ii])
#         elif pattern[ii] in record_p and words[ii] in record_s and record_p.index(pattern[ii]) == record_s.index(words[ii]):
#             continue
#         else:
#             label = False
#             break

# print(label)
#-----------------------------------------------------------------------------#
# # question 292 Nim游戏 已完成
# n = 5

# if n%4 == 0:
#     output = False
# else:
#     output = True
# print(output)


# # record = [[1, True],[2, True],[3, True],[4, False]]

# # if n <= 4:
# #     output = record[n-1][1]
# # else:
# #     index = 5
# #     while index <= n:
# #         label = False
# #         for ii in range(3):
# #             # print(not record[-1-ii][1])
# #             label = label or (not record[-1-ii][1])
# #         record.append([index, label])
# #         index += 1

# #     output = record[-1][1]
# # print(output)
#-----------------------------------------------------------------------------#
# # question 295 数据流的中位数 已完成
# class MedianFinder(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.list1 = []
#         self.output = 0.0

#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: None
#         """
#         self.list1  = self.list1 + [num]
#         self.list1.sort()

#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         n = len(self.list1)
#         if n%2 == 1:
#             self.output = self.list1[n//2]
#         else:
#             self.output = self.list1[n//2-1]*0.5 + self.list1[n//2]*0.5
#         print(self.output)
#         return self.output


# input1 = [[6],[10],[2],[6],[5],[0],[6],[3],[1],[0],[0]]
# x = MedianFinder()
# for ii in range(len(input1)):
#     x.addNum(input1[ii][0])
#     x.findMedian()
#-----------------------------------------------------------------------------#
# # # question 300 最长递增子序列  已完成 - 贪心算法 需要进一步研究
# # 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# # 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

# # nums = [10,9,2,5,3,7,101,18,4,8,6,12]
# # nums = [0,1,0,3,2,3]
# # nums = [7,7,7,7,7,7,7]
# nums = [4,10,4,3,8,9]

# record = [nums[0]]
# for ii in range(1,len(nums)):
#     if record[-1] >= nums[ii]:
#         for jj in range(len(record)):
#             if record[jj] >= nums[ii]:
#                 record[jj] = nums[ii]
#                 break
#     else:
#         record.append(nums[ii])
#     # print(record)
# print(len(record))
#-----------------------------------------------------------------------------#
# # question 303 区域和检索 - 数组不可变 已完成
# # list1 = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# list1 = [[[3]],[0,0]]

# class NumArray(object):

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.num_list = nums
        
#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         return sum(self.num_list[i:j]+[self.num_list[j]])
        
# obj = NumArray(list1[0][0])
# for ii in range(1,len(list1)):
#     print(obj.sumRange(list1[ii][0],list1[ii][1]))
#-----------------------------------------------------------------------------#
# # question 306 累加数 - 待完成
# num = "199100199"
# # num = "11112"
# # num = "999108117"
# # num = "999108207"
# # num = "112358"
# # num = "120300500"
# # num = "001023"


# len_num1 = 1
# len_num2 = 1
# len_num3 = 1

# def len_to_int(len_left, len_num1, len_num2, len_num3):
#     output_num = [int(num[len_left:len_left+len_num1]), int(num[len_left+len_num1:len_left+len_num1+len_num2]), int(num[len_left+len_num1+len_num2:len_left+len_num1+len_num2+len_num3])]
#     return output_num

# label_stop = 0
# start_3num = []
# for ii in range(len(num)//3+1):
#     for jj in range(len(num)//3+1):
#         len_num1 = ii+1
#         len_num2 = jj+1
#         len_num3 = 1
#         while len_num1 + len_num2 + len_num3 <= len(num) and len_num3 <= len(num)//3+1:
#             output_num = len_to_int(0, len_num1, len_num2, len_num3)
#             if output_num[0] + output_num[1] == output_num[2]:
#                 start_3num.append([len_num1,len_num2,len_num3])
#             len_num3 += 1
# print(start_3num)

# label_all = False
# for ii in range(len(start_3num)):
#     len_num1 = start_3num[ii][0]
#     len_num2 = start_3num[ii][1]
#     len_num3 = start_3num[ii][2]
#     len_left = 0
#     label = True
#     while len_left + len_num1 + len_num2 + len_num3 <= len(num):
#         output_num = len_to_int(len_left, len_num1, len_num2, len_num3)
#         if output_num[2] == 0:
#             len_num3 += 1
#         else:
#             if output_num[0] + output_num[1] == output_num[2]:
#                 print(output_num)
#                 len_left += len_num1
#                 len_num1 = len_num2
#                 len_num2 = len_num3
#                 len_num3 = max(len_num1, len_num2)
#                 label = label and True
#                 break
#                 len_num3 += 1
#             else:
#                 label = label and False
#                 len_num3 += 1
#                 break
#     label_all = label_all or label
    
# print(label_all)
#-----------------------------------------------------------------------------#
# # 312. 戳气球
# nums = [1,9,1]
# nums = [7,9,8,0,7,1,3,5,5,2,3]

# # 超时
# output = []
# def backtrack(nums, count):
#     if len(nums) == 2:
#         output.append(count+nums[0]*nums[1]+max(nums))
#         return
#     # elif len(nums) == 3 and nums[1] <= nums[0] and nums[1] <= nums[2]:
#     #     output.append(count+nums[0]*nums[1]*nums[2]+nums[0]*nums[2]+max(nums[0],nums[2]))
#     #     return
#     else:
#         for ii in range(len(nums)):
#             if 0 < ii < len(nums)-1:
#                 # count += nums[ii-1]*nums[ii]*nums[ii+1]
#                 backtrack(nums[0:ii]+nums[ii+1:], count+nums[ii-1]*nums[ii]*nums[ii+1])
#             elif ii == 0:
#                 # count += nums[ii]*nums[ii+1]
#                 backtrack(nums[ii+1:], count+nums[ii]*nums[ii+1])
#             else:
#                 # count += nums[ii-1]*nums[ii]
#                 backtrack(nums[0:ii], count+nums[ii-1]*nums[ii])
# backtrack(nums, 0)
# print(max(output))
#-----------------------------------------------------------------------------#
# # question 318 吉单词长度乘积
        
# words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# # words = ["a","ab","abc","d","cd","bcd","abcd"]
# # words = ["a","aa","aaa","aaaa"]
# # words = ["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]
# def word_area(worda, wordb):
#     label = True
#     for ii in range(len(worda)):
#         for jj in range(len(wordb)):
#             if worda[ii] == wordb[jj]:
#                 label = False
#                 break
#         if label == False:
#             break
#     return label

# words2 = []
# for word in words:
#     temp = []
#     for jj in range(len(word)):
#         if word[jj] not in temp:
#             temp.append(word[jj])
#     # word = list(word)
#     temp.sort()
#     words2.append(temp)

# output2 = 0
# for ii in range(len(words2)):
#     for jj in range(ii+1, len(words2)):
#         label = word_area(words2[ii], words2[jj])
#         if label == True:
#             output_new = len(words[ii])*len(words[jj])
#             if output_new > output2:
#                 output2 = output_new
# print(output2)
#-----------------------------------------------------------------------------#
# # question 319 灯泡开关 已完成
# # 归纳找规律，平方数一定为1
# n =9
# import math
# print(int(math.sqrt(n)))

# deng = [0 for _ in range(n)]
# for step in range(1,n+1):
#     index = 0
#     while index < n -step+1:
#         deng[index+step-1] = 1 - deng[index+step-1]
#         index += step
# print(sum(deng))
#-----------------------------------------------------------------------------#
# # question 326 3的幂 已完成
# n = 3**5+1

# import math
# if n > 0:
#     if 3**round(math.log(n,3), 0) == n: #如果整除
#         output = True
#     else:
#         output = False
# else:
#     output = False
# print(output)
#-----------------------------------------------------------------------------#
# # question 331 验证二叉树的前序序列化 已完成
# preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# # preorder = "1,#"
# # preorder = "9,#,#,1"

# # 方法一：构建曹位的栈，当遇到空节点时，仅将栈顶元素减 1；当遇到非空节点时，将栈顶元素减 1后，再向栈中压入一个 2。无论何时，如果栈顶元素变为 0，就立刻将栈顶弹出。
# preorder = preorder.split(',')
# caowei = 1
# for ii in range(len(preorder)):
#     if preorder[ii] != '#':
#         caowei += 1
#     else:
#         caowei = caowei - 1
#     if caowei == 0:
#         break
# print(ii == len(preorder) -1 and caowei == 0)

# # 方法二：num + # + # -> #
# preorder = preorder.split(',')

# label = True
# preorder2 = [elem for elem in preorder]
# while label == True:
#     index = 0
#     for index in range(len(preorder)-2):
#         if preorder[index] != "#" and preorder[index+1] == "#" and preorder[index+2] =="#":
#             preorder2 = preorder[0:index] + ["#"] + preorder[index+3:]
#             break
#     if preorder2 == preorder:
#         label = False
#     else:
#         preorder = preorder2
# print(preorder == ['#'])
#-----------------------------------------------------------------------------#
# # 332. 重新安排行程
# # tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# # tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# # tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]

# dict1 = {}
# for ii in range(len(tickets)):
#     if tickets[ii][0] not in dict1:
#         dict1[tickets[ii][0]] = [tickets[ii][1]]
#     else:
#         dict1[tickets[ii][0]].append(tickets[ii][1])
# print(dict1)
# output = ["JFK"]
# while output[-1] in dict1 and len(dict1[output[-1]]) > 0:
#     # if len(dict1[output[-1]]) == 1:
#     #     temp = dict1[output[-1]][0]
#     #     del(dict1[output[-1]][0])
#     # else:
#     if output[-1] == 'TIA':
#         break
#     dict1[output[-1]].sort()
#     #循环问题没解决
#     label = False
#     for ii in range(len(dict1[output[-1]])): 
#         if dict1[output[-1]][ii] in dict1:
#             label = True
#             temp = dict1[output[-1]][ii]
#             del(dict1[output[-1]][ii])
#             break
#     if label == False:
#         temp = dict1[output[-1]][0]
#         del(dict1[output[-1]][0])
#     output.append(temp)
# print(output)

# import copy
# dict1 = {}
# for ii in range(len(tickets)):
#     if tickets[ii][0] not in dict1:
#         dict1[tickets[ii][0]] = [tickets[ii][1]]
#     else:
#         dict1[tickets[ii][0]].append(tickets[ii][1])
# # print(dict1)
# # record = ["JFK"]
# output = []
# def backtrack(dict1, record):
#     if len(record) == len(tickets)+1:
#         output.append(record)
#         return
#     else:
#         if record[-1] in dict1:
#             for ii in range(len(dict1[record[-1]])):
#                 dict1_new = copy.deepcopy(dict1)
#                 del(dict1_new[record[-1]][ii])
#                 record_new = copy.deepcopy(record)
#                 record_new.append(dict1[record[-1]][ii])
#                 backtrack(dict1_new, record_new)
# backtrack(dict1, ["JFK"])
# print(output)

#-----------------------------------------------------------------------------#
# # question 336 回文对 - 未完成

# words = ["abcd","dcba","lls","s","sssll"]
# words = ["bat","tab","cat"]
# words = ["a",""]

# # 超时
# def huiwen(ss):
#     if len(ss) == 1:
#         return True
#     else:
#         index_left = 0
#         index_right = len(ss)-1
#         label = True
#         while index_left < index_right:
#             if ss[index_left] == ss[index_right]:
#                 pass
#             else:
#                 label = False
#                 break
#             index_left += 1
#             index_right = index_right - 1
#         return label

# output = []
# for ii in range(len(words)):
#     for jj in range(len(words)):
#         if ii != jj and huiwen(words[ii] + words[jj]):
#             output.append([ii,jj])
# print(output)
#-----------------------------------------------------------------------------#
# # question 338 比特位计数
# num = 5
# output = []
# for ii in range(num+1):
#     # print(ii)
#     temp = bin(ii).split('b')[-1]
#     count = 0
#     for ss in temp:
#         if ss == '1':
#             count += 1
#     output.append(count)
# print(output)
#-----------------------------------------------------------------------------#
# # 341. 扁平化嵌套列表迭代器 已完成
# class NestedIterator(object):
#     def __init__(self, nestedList):
#         """
#         Initialize your data structure here.
#         :type nestedList: List[NestedInteger]
#         """
#         self.nestedList = []
#         def next_layer(nestedList):
#             for ii in range(len(nestedList)):
#                 if type(nestedList[ii]) == int:
#                     self.nestedList.append(nestedList[ii])
#                 elif type(nestedList[ii]) == list:
#                     next_layer(nestedList[ii])
#         next_layer(nestedList)
        
#     def next(self):
#         """
#         :rtype: int
#         """
#         temp2 = self.nestedList[0]
#         del(self.nestedList[0])
#         return temp2

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return len(self.nestedList) > 0
        
# nestedList = [1,[4,[6]]]
# i = NestedIterator(nestedList)
# print(i.nestedList)
# v = []
# while i.hasNext():
#     v.append(i.next())
# print(v)
#-----------------------------------------------------------------------------#
# # question 345 反转字符串中的元音字母 未完成
# s = "leetcode"
# # s = "hello"
# s = "Live on evasions? No, I save no evil."
# target = "Live on evasIons? No, i save no evil."
# s2 = list(s)
# yuanyin = ['a','e','i','o','u', 'A', 'E', 'i', 'O', 'U']
# index_yuanyin = []
# record_yuanyin = []
# for ii in range(len(s2)):
#     if s2[ii] in yuanyin:
#         index_yuanyin.append(ii)
#         record_yuanyin = [s2[ii]] + record_yuanyin
        
# for ii in range(len(index_yuanyin)):
#     s2[index_yuanyin[ii]] = record_yuanyin[ii]
# s_out = ''
# for s1 in s2:
#     s_out += s1
# print(s_out)
# print(target)
#-----------------------------------------------------------------------------#
# # # question 354 俄罗斯套娃信封问题 已完成 - 同300
# # envelopes = [[5,4],[6,8],[6,7],[2,3]]
# # envelopes = [[1,1],[1,1],[1,1]]
# # envelopes =[[5,4],[6,4],[6,7],[2,3]]
# # envelopes = [[1,1],[5,10],[6,2],[7,3],[8,4]]
# # envelopes = [[46,89],[50,53],[52,68],[72,45],[77,81]]
# # envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
# # envelopes = [[2,1],[4,1],[6,2],[8,3],[10,5],[12,8],[14,13],[16,21],[18,34],[20,55]]# print(envelopes)
# envelopes = [[10,8],[1,12],[6,15],[2,18]]

# envelopes.sort()
# print(envelopes)
# dp = [1 for ii in range(len(envelopes))]

# for ii in range(1,len(envelopes)):
#     for jj in range(ii):
#         if envelopes[jj][0] < envelopes[ii][0] and envelopes[jj][1] < envelopes[ii][1]:
#             dp[ii] = max(dp[ii], dp[jj]+1)
# print(max(dp))
#-----------------------------------------------------------------------------#
# # 363. 矩形区域不超过 K 的最大数值和
# matrix = [[1,0,1],[0,-2,3]]
# k = 2
# matrix = [[2,2,-1]]
# k = 3
# matrix = [[2,2,-1]]
# k = 0
# matrix = [[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]]
# k = 10

# record = -float('inf')
# for ii_start in range(len(matrix)):
#     col_sum = [0 for _ in range(len(matrix[0]))]
#     for ii_end in range(ii_start,len(matrix)):
#         for jj in range(len(matrix[0])):
#             col_sum[jj] += matrix[ii_end][jj]
#         # print(ii_start,ii_end,col_sum)
#         for jj_start in range(len(matrix[0])):
#             temp = 0
#             for jj_end in range(jj_start,len(matrix[0])):
#                 temp += col_sum[jj_end]
#                 # print(temp)
#                 if record < temp < k:
#                     record = max(record, temp)
#                 elif temp == k:
#                     record = k
# print(record)

# # 超时
# dp = []
# for jj in range(len(matrix[0])):
#     for kk in range(jj+1,len(matrix[0])+1):
#         temp = []
#         for ii in range(len(matrix)):
#             temp.append(sum(matrix[ii][jj:kk]))
#         dp.append(temp)
# record = -float('inf')
# for ii in range(len(dp)):
#     for jj in range(len(dp[0])):
#         for kk in range(1,len(dp[0])+1):
#             if record < sum(dp[ii][jj:kk]) < k:
#                 record = max(record, sum(dp[ii][jj:kk]))
#             elif sum(dp[ii][jj:kk]) == k:
#                 record = k
# print(record)
#-----------------------------------------------------------------------------#
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
#-----------------------------------------------------------------------------#
# # 372. 超级次方
# a = 78267
# b = [1,7,7,4,3,1,7,0,1,4,4,9,2,8,5,0,0,9,3,1,2,5,9,6,0,9,9,0,9,6,0,5,3,7,9,8,8,9,8,2,5,4,1,9,3,8,0,5,9,5,6,1,1,8,9,3,7,8,5,8,5,5,3,0,4,3,1,5,4,1,7,9,6,8,8,9,8,0,6,7,8,3,1,1,1,0,6,8,1,1,6,6,9,1,8,5,6,9,0,0,1,7,1,7,7,2,8,5,4,4,5,2,9,6,5,0,8,1,0,9,5,8,7,6,0,6,1,8,7,2,9,8,1,0,7,9,4,7,6,9,2,3,1,3,9,9,6,8,0,8,9,7,7,7,3,9,5,5,7,4,9,8,3,0,1,2,1,5,0,8,4,4,3,8,9,3,7,5,3,9,4,4,9,3,3,2,4,8,9,3,3,8,2,8,1,3,2,2,8,4,2,5,0,6,3,0,9,0,5,4,1,1,8,0,4,2,5,8,2,4,2,7,5,4,7,6,9,0,8,9,6,1,4,7,7,9,7,8,1,4,4,3,6,4,5,2,6,0,1,1,5,3,8,0,9,8,8,0,0,6,1,6,9,6,5,8,7,4,8,9,9,2,4,7,7,9,9,5,2,2,6,9,7,7,9,8,5,9,8,5,5,0,3,5,8,9,5,7,3,4,6,4,6,2,3,5,2,3,1,4,5,9,3,3,6,4,1,3,3,2,0,0,4,4,7,2,3,3,9,8,7,8,5,5,0,8,3,4,1,4,0,9,5,5,4,4,9,7,7,4,1,8,7,5,2,4,9,7,9,1,7,8,9,2,4,1,1,7,6,4,3,6,5,0,2,1,4,3,9,2,0,0,2,9,8,4,5,7,3,5,8,2,3,9,5,9,1,8,8,9,2,3,7,0,4,1,1,8,7,0,2,7,3,4,6,1,0,3,8,5,8,9,8,4,8,3,5,1,1,4,2,5,9,0,5,3,1,7,4,8,9,6,7,2,3,5,5,3,9,6,9,9,5,7,3,5,2,9,9,5,5,1,0,6,3,8,0,5,5,6,5,6,4,5,1,7,0,6,3,9,4,4,9,1,3,4,7,7,5,8,2,0,9,2,7,3,0,9,0,7,7,7,4,1,2,5,1,3,3,6,4,8,2,5,9,5,0,8,2,5,6,4,8,8,8,7,3,1,8,5,0,5,2,4,8,5,1,1,0,7,9,6,5,1,2,6,6,4,7,0,9,5,6,9,3,7,8,8,8,6,5,8,3,8,5,4,5,8,5,7,5,7,3,2,8,7,1,7,1,8,7,3,3,6,2,9,3,3,9,3,1,5,1,5,5,8,1,2,7,8,9,2,5,4,5,4,2,6,1,3,6,0,6,9,6,1,0,1,4,0,4,5,5,8,2,2,6,3,4,3,4,3,8,9,7,5,5,9,1,8,5,9,9,1,8,7,2,1,1,8,1,5,6,8,5,8,0,2,4,4,7,8,9,5,9,8,0,5,0,3,5,5,2,6,8,3,4,1,4,7,1,7,2,7,5,8,8,7,2,2,3,9,2,2,7,3,2,9,0,2,3,6,9,7,2,8,0,8,1,6,5,2,3,0,2,0,0,0,9,2,2,2,3,6,6,0,9,1,0,0,3,5,8,3,2,0,3,5,1,4,1,6,8,7,6,0,9,8,0,1,0,4,5,6,0,2,8,2,5,0,2,8,5,2,3,0,2,6,7,3,0,0,2,1,9,0,1,9,9,2,0,1,6,7,7,9,9,6,1,4,8,5,5,6,7,0,6,1,7,3,5,9,3,9,0,5,9,2,4,8,6,6,2,2,3,9,3,5,7,4,1,6,9,8,2,6,9,0,0,8,5,7,7,0,6,0,5,7,4,9,6,0,7,8,4,3,9,8,8,7,4,1,5,6,0,9,4,1,9,4,9,4,1,8,6,7,8,2,5,2,3,3,4,3,3,1,6,4,1,6,1,5,7,8,1,9,7,6,0,8,0,1,4,4,0,1,1,8,3,8,3,8,3,9,1,6,0,7,1,3,3,4,9,3,5,2,4,2,0,7,3,3,8,7,7,8,8,0,9,3,1,2,2,4,3,3,3,6,1,6,9,6,2,0,1,7,5,6,2,5,3,5,0,3,2,7,2,3,0,3,6,1,7,8,7,0,4,0,6,7,6,6,3,9,8,5,8,3,3,0,9,6,7,1,9,2,1,3,5,1,6,3,4,3,4,1,6,8,4,2,5]

# # 超时
# ss = ''
# for ii in range(len(b)):
#     ss += str(b[ii])
# print( (a**int(ss))%1337 ) # ss太大，计算超时
#-----------------------------------------------------------------------------#
# # question 383 赎金信 已完成
# ransomNote = "a"
# magazine = "b"

# dict_r = {}
# dict_s = {}
# for ss in ransomNote:
#     if ss not in dict_r:
#         dict_r[ss] = 1
#         dict_s[ss] = 0
#     else:
#         dict_r[ss] += 1
# for ss in magazine:
#     if ss not in dict_s:
#         dict_s[ss] = 1
#     else:
#         dict_s[ss] += 1
# label = True        
# for s2 in list(dict_r.keys()):
#     if dict_r[s2] > dict_s[s2]:
#         label = False
#         break
# print(label)

# # question 389 找不同
# s = "abcd"
# t = "abcde"
# s = ""
# t = "y"
# s = "a"
# t = "aa"
# s = "ae"
# t = "aea"

# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# dict_s = {}
# dict_t = {}
# for ss in alphabet:
#     dict_s[ss] = 0
#     dict_t[ss] = 0
# for ss in s:
#     dict_s[ss] += 1
# for ss in t:
#     dict_t[ss] += 1

# for ss in alphabet:
#     if dict_s[ss] + 1 == dict_t[ss]:
#         print(ss)
#         break
#-----------------------------------------------------------------------------#
# # question 392 判断子序列 已完成
# # s = "abc"
# # t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
# s = "b"
# t = "abc"
# if len(s) > 0:
#     index = 0
#     count = 0
#     label = False
#     while index < len(t):
#         if t[index] == s[count]:
#             index += 1
#             count += 1
#         else:
#             index += 1
#         if count == len(s):
#             label = True
#             break
#     print(label)
# else:
#     print(True)
#-----------------------------------------------------------------------------#
# # 393. UTF-8 编码验证
# data = [197, 130, 1] # True
# # data = [235, 140, 4] # False
# # data = [249,130,130,130,130,1] # False
# data = [237] # False

# def func(num):
#     temp = bin(num)[2:]
#     if len(temp) >= 8:
#         temp = temp[-8:]
#     else:
#         temp = '0'*(8-len(temp))+temp
#     return temp

# index = 0
# label = True
# while index < len(data):
#     temp = func(data[index])
    
#     if temp[0] == '0':
#         index += 1
#     elif temp[0:3] == '110':
#         if index+1 < len(data) and func(data[index+1])[0:2] == '10':
#             index += 2
#         else:
#             label = False
#             break
#     elif temp[0:4] == '1110':
#         if index+2 < len(data) and func(data[index+1])[0:2] == '10' and func(data[index+2])[0:2] == '10':
#             index += 3
#         else:
#             label = False
#             break
#     elif temp[0:5] == '11110':
#         if index+3 < len(data) and func(data[index+1])[0:2] == '10' and func(data[index+2])[0:2] == '10' and func(data[index+3])[0:2] == '10':
#             index += 4
#         else:
#             label = False
#             break
#     else:
#         label = False
#         break
# print(label)
#-----------------------------------------------------------------------------#
# # question 395 至少有K个重复字符的最长子串
# s = "aaacbbab"
# k = 3
# # s = "aaabb"
# # k = 3
# # s = "ababbc"
# # k = 2
# # s = "caaabbbe"
# # k = 3
# # s = "weitong"
# # k = 2
# # s = 'aa'
# # k = 3

# def fenduan(s):
#     s_unique = []
#     output_left = ''
#     output_right = ''
#     index_end = 0
#     index_start = 0
#     while index_end < len(s):
#         if s[index_end] not in s_unique and s.count(s[index_end]) >= k:
#             s_unique.append(s[index_end])
#             index_end += 1
#         elif s[index_end] in s_unique:
#             index_end += 1
#         else:
#             if index_start < index_end:
#                 output_left = s[index_start:index_end]
#             break
#     output_right = s[index_end+1:]
#     return [output_left, output_right]

# output = 0
# list_s = []
# if len(s) >= k:
#     list_s += fenduan(s)
#     if len(list_s[0]) == 0 and len(list_s[1]) == 0:
#         max_k = len(s)
#         if max_k > output:
#             output = max_k
#             # print(output)
#     elif len(list_s[0]) > 0 and len(list_s[1]) == 0:
#         del(list_s[1])
#     elif len(list_s[1]) > 0 and len(list_s[0]) == 0:
#         del(list_s[0])
#     # print(list_s)

# while len(list_s) > 0:
#     if len(list_s[0]) >= k:
#         temp = fenduan(list_s[0])
#         if len(temp[0]) == 0 and len(temp[1]) == 0:
#             max_k = len(list_s[0])
#             if max_k > output:
#                 output = max_k
#                 # print(output)
#         elif len(temp[0]) > 0 and len(temp[1]) == 0:
#             list_s.append(temp[0])
#         elif len(temp[1]) > 0 and len(temp[0]) == 0:
#             list_s.append(temp[1])
#         else:
#             list_s.append(temp[0])
#             list_s.append(temp[1])
#     del(list_s[0])
#     # print(list_s)
        
# print(output)
#-----------------------------------------------------------------------------#
# # question 401 二进制手表 已完成
# num = 7
# from itertools import combinations
# output = []
# for kk in range(num+1): 
#     if kk <= 4 and num-kk <= 6: #小时只有4个灯，分钟只有6个灯
#         #小时
#         hours = []
#         combs = list(combinations([0,1,2,3], kk))
#         for comb in combs:
#             # print(list(comb))
#             temp = list(comb)
#             count = 0
#             for ii in range(len(temp)):
#                 count += 2**temp[ii]
#             hours.append(count) 
#         #分钟
#         minutes = []
#         combs = list(combinations([0,1,2,3,4,5], num-kk))
#         for comb in combs:
#             # print(list(comb)
#             temp = list(comb)
#             count = 0
#             for ii in range(len(temp)):
#                 count += 2**temp[ii]
#             minutes.append(count)
        
#         comb2 = []
#         if len(hours) == 0:
#             hours = [0]
#         if len(minutes) == 0:
#             minutes = [0]
#         for ii in range(len(hours)):
#             for jj in range(len(minutes)):
#                 temp_str = ''
#                 if hours[ii] <= 11 and minutes[jj] <= 59:
#                     temp_str = temp_str + str(hours[ii]) + ':'
#                     if 0 <= minutes[jj] and minutes[jj] <= 9:
#                         temp_str = temp_str + '0' + str(minutes[jj])
#                     elif 10 <= minutes[jj] and minutes[jj] <= 59:
#                         temp_str = temp_str + str(minutes[jj])
#                 if temp_str != '':
#                     # print(temp_str)
#                     output.append(temp_str)
# print(output)
#-----------------------------------------------------------------------------#
# # 403. 青蛙过河
# stones = [0,1,3,5,6,8,12,17]
# # stones = [0,1,2,3,4,8,9,11]
# stones = [0,1,3,6,10,15,16,21]

# # 类似动态规划
# dict1 = {}
# dict1[stones[0]] = [0]
# for ii in range(1,len(stones)):
#     for jj in range(ii):
#         jump = stones[ii] - stones[jj]
#         if stones[jj] in dict1:
#             for num in dict1[stones[jj]]:
#                 if abs(jump-num) <= 1: #可以从stones[jj]跳到stones[ii]
#                     if stones[ii] not in dict1:
#                         dict1[stones[ii]] = [jump]
#                     else:
#                         dict1[stones[ii]].append(jump)
#                     break
# print(stones[-1] in dict1)
#-----------------------------------------------------------------------------#
# # 421. 数组中两个数的最大异或值
# nums = [3,10,5,25,2,8]
# # nums = [2,4]
# # nums = [8,10,2]
# # nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# # nums = [4,6,7]

# # 官方，没搞懂
# # 最高位的二进制位编号为 30
# HIGH_BIT = 30

# x = 0
# for k in range(HIGH_BIT, -1, -1):
#     seen = set()
#     # 将所有的 pre^k(a_j) 放入哈希表中
#     for num in nums:
#         # 如果只想保留从最高位开始到第 k 个二进制位为止的部分
#         # 只需将其右移 k 位
#         seen.add(num >> k)

#     # 目前 x 包含从最高位开始到第 k+1 个二进制位为止的部分
#     # 我们将 x 的第 k 个二进制位置为 1，即为 x = x*2+1
#     x_next = x * 2 + 1
#     found = False
    
#     # 枚举 i
#     for num in nums:
#         if x_next ^ (num >> k) in seen:
#             found = True
#             break

#     if found:
#         x = x_next
#     else:
#         # 如果没有找到满足等式的 a_i 和 a_j，那么 x 的第 k 个二进制位只能为 0
#         # 即为 x = x*2
#         x = x_next - 1

# print(x)


# # 超时
# if len(nums) <= 1:
#     print(0)
# else:
#     import bisect
#     nums.sort()
#     critical = int('1'*(len(bin(nums[-1])[2:])-1),2)
#     index = bisect.bisect_right(nums,critical)
#     if index != 0:
#         temp = 0
#         for ii in range(0,index):
#             for jj in range(index,len(nums)):
#                 temp = max(temp, nums[ii]^nums[jj])
#     else:
#         temp = 0
#         for ii in range(len(nums)):
#             for jj in range(ii+1,len(nums)):
#                 temp = max(temp, nums[ii]^nums[jj])
#     print(temp)
#-----------------------------------------------------------------------------#
# # 453. 最小操作次数使数组元素相等
# nums = [1,2,3,1,0]

# #超时
# count = 0
# while True:
#     num_max = max(nums)
#     index = nums.index(num_max)
#     label = True
#     for ii in range(len(nums)):
#         if ii != index:
#             if nums[ii] < num_max:
#                 label = False
#     if label == True:
#         break
#     else:
#         for ii in range(len(nums)):
#             if ii != index:
#                 nums[ii] += 1
#         count += 1
# print(count)
#-----------------------------------------------------------------------------#
# # question 456 132模式 已完成

# nums = [3,2,1,4,2]
# nums = [1,0,1,-4,-3]
# nums = [4,3,2,1,0]
# nums = [1,2,3,4,5]
# nums = [1,2,3,3,3,4,5,3]
# nums = [10,12,6,8,3,11]

# if len(nums) >= 3:
#     record = []
#     temp = [nums[0]]
#     for ii in range(1,len(nums)):
#         if nums[ii] >= nums[ii-1]:
#             temp.append(nums[ii])
#         else:
#             record.append(temp)
#             temp = [nums[ii]]
#     record.append(temp)
#     print(record)
#     label = False
#     if 1 < len(record) < len(nums):
#         for ii in range(1,len(record)):
#             for jj in range(len(record[ii])):
#                 for kk in range(ii):
#                     if record[kk][0] < record[ii][jj] < record[kk][-1]:
#                         label = True
#                         break
#     print(label)
# else:
#     print(False)
#-----------------------------------------------------------------------------#
# # 459. 重复的子字符串
# s = "abcabcabc"
# s = "abaababaab"
# s = 'aaaaa'
# s = 'a'
# s = 'ab'
# s = 'aba'
# s = 'aabb'
# s = "babbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbb"

# def gcd(x,y):
#     # 辗转相除
#     while y != 0:
#         temp = x % y
#         x = y
#         y = temp
#     return x

# list_s = []
# list_count = []
# for ii in range(len(s)):
#     if s[ii] not in list_s:
#         list_s.append(s[ii])
#         list_count.append(s.count(s[ii]))
# if len(list_s) == 1:
#     max_repeat = list_count[0]
# else:
#     max_repeat = gcd(list_count[0],list_count[1])
#     for ii in range(2,len(list_count)):
#         max_repeat = gcd(list_count[ii], max_repeat)

# if max_repeat > 1:
#     label2 = False
#     for num_repeat in range(2,max_repeat+1):
#         if max_repeat%num_repeat == 0:
#             print(num_repeat)
#             label = True
#             min_str = s[0:0+len(s)//num_repeat]
#             if label == True:
#                 for ii in range(1,num_repeat):
#                     temp_str = s[ii*len(s)//num_repeat:ii*len(s)//num_repeat+len(s)//num_repeat]
#                     # print(temp_str)
#                     if temp_str != min_str:
#                         label = False
#             label2 = label2 or label
# else:
#     label2 = False
# print(label2)
#-----------------------------------------------------------------------------#
# 474. 一和零
strs = ["10", "0001", "111001", "1", "0"]
m = 3
n = 4
# strs = ["10", "0", "1"]
# m = 1
# n = 1

def count01(str1):
    count0 = 0
    count1 = 0
    for ss in str1:
        if ss == '0':
            count0 += 1
        else:
            count1 += 1
    return count0, count1

dp = [[0,0,0] for ii in range(len(strs))]
for ii in range(len(strs)):
    count0, count1 = count01(strs[ii])
    if count0 <= m and count1 <= n:
        dp[ii][0] = 1
        dp[ii][1] = count0
        dp[ii][2] = count1
        for jj in range(ii-1,-1,-1):
            if dp[jj][0] + 1 > dp[ii][0]:
                if dp[jj][1] + count0 <= m and dp[jj][2] + count1 <= n:
                    dp[ii][0] = dp[jj][0] + 1
                    dp[ii][1] = dp[jj][1] + count0
                    dp[ii][2] = dp[jj][2] + count1
output = 0
for ii in range(len(dp)):
    output = max(output, dp[ii][0])
print(output)
#-----------------------------------------------------------------------------#
# 477. 汉明距离总和
# nums = [4,14,2]

# num_str = []
# len_str = len(bin(max(nums))[2:])
# for ii in range(len(nums)):
#     cur_str = bin(nums[ii])[2:]
#     num_str.append('0'*(len_str-len(cur_str)) + cur_str)
# count2 = 0
# for ii in range(len_str):
#     count = 0
#     for jj in range(len(nums)):
#         if num_str[jj][ii] == '1':
#             count += 1
#     count2 += (len(nums)-count)*count
# print(count2)
# # 超时
# count = 0
# for ii in range(len(nums)):
#     for jj in range(ii+1,len(nums)):
#         for s in bin(nums[ii]^nums[jj])[2:]:
#             if s == '1':
#                 count += 1
# print(count)
#-----------------------------------------------------------------------------#
# # 492. 构造矩形 已完成
# area = 8

# for ii in range(int(area**0.5),-1,-1):
#     if area%ii == 0:
#         print([area//ii,ii])
#         break
#-----------------------------------------------------------------------------#
# # 494. 目标和
# nums = [1,1,1,1,1]
# target = 3
# # nums = [1]
# # target = 1

# right_start = len(nums)//2 + len(nums)%2
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
# # global count
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
#-----------------------------------------------------------------------------#
# # 496. 下一个更大元素 I
# nums1 = [4,1,2]
# nums2 = [1,3,4,2]
# nums1 = [2,4]
# nums2 = [1,2,3,4]

# def next_larger(num):
#     index = nums2.index(num)
#     label = False
#     for ii in range(index+1,len(nums2)):
#         if nums2[ii] > num:
#             label = True
#             break
#     if label == False:
#         return -1
#     else:
#         return nums2[ii]
# output = []
# for num in nums1:
#     output.append(next_larger(num))
# print(output)
#-----------------------------------------------------------------------------#
# # question 500 键盘行 已完成
# words = ["Hello","Alaska","Dad","Peace"]
# dict1 = {}
# for ss in "qwertyuiop":
#     dict1[ss] = 1
# for ss in "asdfghjkl":
#     dict1[ss] = 2
# for ss in "zxcvbnm":
#     dict1[ss] = 3
# print(dict1)

# record = []
# for word in words:
#     temp = []
#     for ii in range(len(word)):
#         if dict1[word[ii].lower()] not in temp:
#             temp.append(dict1[word[ii].lower()])
#     if len(temp) == 1:
#         record.append(word)
# print(record)
#-----------------------------------------------------------------------------#
# # 501. 二叉搜索树中的众数
# temp = [1,2]
# freq = 0
# zhongshu = []
# unique = set()
# for ii in range(len(temp)):
#     if temp[ii] not in unique:
#         unique.add(temp[ii])
#         if temp.count(temp[ii]) > freq:
#             zhongshu = [temp[ii]]
#             freq = max(freq,temp.count(temp[ii]))
#         elif temp.count(temp[ii]) == freq:
#             zhongshu.append(temp[ii])
# print(zhongshu)
#-----------------------------------------------------------------------------#
# # question 503 下一个更大元素 II 已完成
# nums = [1,2,3,4,3]
# # nums = [1]
# # nums = []

# output2 = []
# if len(nums) > 2:
#     for ii in range(len(nums)):
#         label = False
#         for jj in range(ii+1,len(nums)):
#             if nums[ii] < nums[jj]:
#                 output = nums[jj]
#                 label = True
#                 break
#             else:
#                 output = -1
#         if label == False:
#             for jj in range(ii):
#                 if nums[ii] < nums[jj]:
#                     output = nums[jj]
#                     label = True
#                     break
#                 else:
#                     output = -1
#         output2.append(output)
# elif len(nums) == 1:
#     output2 = [-1]
# print(output2)
#-----------------------------------------------------------------------------#
# # 506. 相对名次 已完成
# score = [5, 4, 3, 2, 1]

# sort_down = sorted(score, reverse=True)
# output = []
# for ii in score:
#     index = sort_down.index(ii)
#     if index == 0:
#         output.append("Gold Medal")
#     elif index == 1:
#         output.append("Silver Medal")
#     elif index == 2:
#         output.append("Bronze Medal")
#     else:
#         output.append(str(index+1))
# print(output)
#-----------------------------------------------------------------------------#
# # 507. 完美数 已完成
# num = 28

# if num > 1:
#     yinzi = [1]
#     for ii in range(2,int(num**0.5)+1):
#         if num%ii == 0:
#             yinzi += [ii, num//ii]
#     print(yinzi)
#     print(sum(yinzi) == num)
# else:
#     print(False)
#-----------------------------------------------------------------------------#
# # 541. 反转字符串 II 已完成
# s = "abcdefg"
# k = 2

# def str_reverse(ss):
#     output = ''
#     for s in ss:
#         output = s + output
#     return output

# output2 = ''
# for ii in range(len(s)//k+1):
#     if ii%2 == 0:
#         output2 += str_reverse(s[ii*k+0:ii*k+k])
#     else:
#         output2 += s[ii*k+0:ii*k+k]
# print(output2)
#-----------------------------------------------------------------------------#
# # 551. 学生出勤记录 I 已完成
# s = "ALL"

# count_A = 0
# label = True
# for ii in range(len(s)):
#     if s[ii] == 'A':
#         count_A += 1
#         if count_A > 1:
#             label = False
#             break
#     if ii < len(s)-2 and s[ii] == 'L' and s[ii+1] =='L' and s[ii+2] == 'L':
#         label = False
#         break
# print(label)
#-----------------------------------------------------------------------------#
# # 554. 砖墙 与官方思路一致
# wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# # wall = [[1],[1],[1]]
# # wall = [[1,1],[2],[1,1]]
# # wall = [[100000000],[100000000],[100000000]]

# weight = sum(wall[0])
# dict1 = {}
# for ii in range(len(wall)):
#     temp = 0
#     for jj in range(len(wall[ii])-1):
#         temp += wall[ii][jj]
#         if temp not in dict1:
#             dict1[temp] = 1
#         else:
#             dict1[temp] += 1  #线从砖块的边缘经过的次数
# # print(dict1)            
# temp2 = 0
# for num in dict1.keys():
#     temp2 = max(temp2,dict1[num])
# print(len(wall)-temp2) #穿过砖块的最小数量

# # 超时
# list_set = []
# for row in wall:
#     dp = [0 for _ in range(len(row))]
#     dp[0] = row[0]
#     for jj in range(1,len(row)):
#         dp[jj] = dp[jj-1] + row[jj]
#     list_set.append(set(dp))
# temp = len(wall)
# for jj in range(1,weight):
#     count = 0
#     for ii in range(len(list_set)):
#         if jj in list_set[ii]:
#             count += 1
#     temp = min(temp,len(wall)-count)
# print(temp)
#-----------------------------------------------------------------------------#
# # 557. 反转字符串中的单词 III 已完成
# s = "Let's take LeetCode contest"
# def str_reverse(ss):
#     output = ''
#     for s in ss:
#         output = s + output
#     return output

# ss2 = s.split(' ')
# output = ''
# for ss1 in ss2:
#     output += str_reverse(ss1) + ' '
# print(output[0:-1])
#-----------------------------------------------------------------------------#
# 560. 和为K的子数组
nums = [1,1,1]
k = 2
nums = [1]
k = 0

# 思路：前缀和+哈希表优化
# 「力扣」第 1248 题： 统计「优美子数组」 - 待解决
# 前缀和pre[ii] = pre[ii−1] + nums[ii]
# [i_start,ii]闭区间内nums元素之和为k，可以表示为pre[ii]-pre[i_start-1] = k
# 如果查找 以ii结尾的前缀和 等于k的数量，
# 由于 i_start 的取值范围为[0, ii]
# 则只需要查找前缀和pre[-1],pre[0],...,pre[ii-1]等于pre[ii]-k的数量
# 利用dict_mp记录前缀和及出现的次数，因此dict_map[pre[ii]-k]即为要查找的数量
pre = [] # 记录包含第ii个元素的前缀和，即[0:ii]闭区间内nums元素之和
dict_mp = {0:1} #记录前缀和pre[ii](key)，以及pre[ii]出现的次数(value)
# 初始条件为pre[-1] = 0,即nums为空时，区间和 0 出现了1次，所以dict_mp = {0:1}
count = 0 
for ii in range(len(nums)):
    if ii == 0:
        pre.append(nums[0])
    else:
        pre.append(nums[ii]+pre[-1])
    if pre[ii]-k in dict_mp:
        count += dict_mp[pre[ii]-k]
    # 先查找前缀和pre[-1],pre[0],...,pre[ii-1]等于pre[ii]-k的数量
    # 由于查找时不包含当前的前缀和pre[ii]，因此在dict_mp中添加前缀和pre[ii]的操作，需要再查找之后执行
    if pre[ii] not in dict_mp:
        dict_mp[pre[ii]] = 1
    else:
        dict_mp[pre[ii]] += 1
print(count)

# # 枚举区间的起点和重点，超时
# count = 0
# for ii in range(len(nums)):
#     temp = 0
#     for jj in range(ii,len(nums)):
#         temp += nums[jj]
#         if temp == k:
#             count += 1
# print(count)

# 1074. 元素和为目标值的子矩阵数量





#-----------------------------------------------------------------------------#
# # 594. 最长和谐子序列
# nums = [1,3,2,2,5,2,3,7]
# # nums = [1,2,3,4]
# # nums = [1,1,1,1]

# nums.sort()
# index = 0
# count = 0
# while index < len(nums)-1:
#     delta = nums.count(nums[index])
#     if index+delta < len(nums) and nums[index+delta] == nums[index] + 1:
#         count = max(count, nums.count(nums[index+delta])+delta)
#     index += delta
# print(count)
#-----------------------------------------------------------------------------#
# # 605. 种花问题
# flowerbed = [1,0,0,0,0,1]
# n = 2
# # flowerbed = [1,0,0,0,1,0,0]
# # n = 2

# index = 0
# count = 0
# while index < len(flowerbed):
#     if flowerbed[index] == 1:
#         index += 2
#     elif flowerbed[index] == 0 and index < len(flowerbed)-1 and flowerbed[index+1] == 0:
#         index += 2
#         count += 1
#     elif flowerbed[index] == 0 and index < len(flowerbed)-1 and flowerbed[index+1] == 1:
#         index += 3
#     elif flowerbed[index] == 0 and index == len(flowerbed)-1:
#         index += 2
#         count += 1
# print(count >= n)
#-----------------------------------------------------------------------------#
# # question647 回文子串 已完成
# s = "aaa"

# huiwen = [[True]*len(s) for _ in range(len(s))]
# for ii in range(len(s),-1,-1):
#     for jj in range(ii+1,len(s)):
#         huiwen[ii][jj] = s[ii] == s[jj] and huiwen[ii+1][jj-1]
# print(huiwen)
# count = 0
# for ii in range(len(huiwen)):
#     for jj in range(len(huiwen)):
#         if ii <= jj and huiwen[ii][jj] == True:
#             count += 1
# print(count)
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

# # 超时，根据官方思路改进
# import copy
# if len(nums) % k == 0:
#     init = len(nums) // k
# else:
#     init = len(nums) // k + 1
# dp = [[init]*2**10 for _ in range(k)]
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
#         for key in dict_temp:
#             dp[0][key] -= dict_temp[key]
#     else:
#         temp = min(dp[ii-1]) + col_count
#         for jj in range(2**10):
#             t2 = copy.deepcopy(temp)
#             for key in dict_temp:
#                 t2 = min(dp[ii-1][jj^key] + col_count - dict_temp[key], t2)
#             dp[ii][jj] = t2
# print(dp[k-1][0])

# # 超时
# if k == 1:
#     count = 0
#     for ii in range(len(nums)):
#         if nums[ii] == 0:
#             count += 1
#     print(len(nums)-count)
# elif k == 2:
#     dict_temp = {}
#     for jj in range(len(nums)):
#         if nums[jj] not in dict_temp:
#             dict_temp[nums[jj]] = 1
#         else:
#             dict_temp[nums[jj]] += 1
#     num_freq = 0
#     for key in dict_temp.keys():
#         if dict_temp[key] > num_freq:
#             num_freq = dict_temp[key]
#     print(len(nums)-num_freq)
# else:
#     list_freq = []
#     list_most = []
#     for ii in range(k):
#         dict_temp = {}
#         for jj in range(ii,len(nums),k):
#             if nums[jj] not in dict_temp:
#                 dict_temp[nums[jj]] = 1
#             else:
#                 dict_temp[nums[jj]] += 1
    
#         num_freq = 0
#         num_most = []
#         for key in dict_temp.keys():
#             if dict_temp[key] > num_freq:
#                 num_freq = dict_temp[key]
#                 num_most = [key]
#             elif dict_temp[key] == num_freq:
#                 num_most.append(key)
#         list_freq.append(num_freq)
#         list_most.append(num_most)
        
#     output = set()
#     def backtrack(list_most, record):
#         if len(list_most) == 0:
#             temp = record[0]
#             for jj in range(1,len(record)):
#                 temp = temp ^ record[jj]
#             output.add(temp)
#         else:
#             for num in list_most[0]:
#                 backtrack(list_most[1:], record+[num])
#     backtrack(list_most, [])

#     if 0 in output:
#         print(len(nums)-sum(list_freq))
#     else:
#         print(len(nums)-sum(list_freq)+sorted(list_freq)[0])
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
# # 665. 非递减数列
# nums = [4,2,3]
# # nums = [4,2,1]
# # nums = [3,4,2,3]

# dp = [0 for _ in range(len(nums))]
# dp[-1] = nums[-1]
# for ii in range(len(nums)-2,-1,-1):
#     dp[ii] = min(dp[ii+1], nums[ii])
# print(dp)
# count = 0
# for ii in range(len(nums)-1):
#     if dp[ii] < nums[ii]:
#         count += 1
# print(count <= 1)
#-----------------------------------------------------------------------------#
# # 690. 员工的重要性
# class Employee(object):
#     def __init__(self, id, importance, subordinates):
#         # :type id: int
#         # :type importance: int
#         # :type subordinates: List[int]
#         self.id = id
#         self.importance = importance
#         self.subordinates = subordinates
# employees = [Employee(1,2,[2]),Employee(2,3,[])]
# id = 2
# employees = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]
# id = 1

# # 方法一改进
# dict1 = {}
# for employee in employees:
#     dict1[employee.id] = [employee.importance, employee.subordinates]
# list_id = [id]
# count = 0
# while len(list_id) > 0:
#     for ii in range(len(list_id)):
#         cur_id = list_id.pop(0)
#         count += dict1[cur_id][0]
#         list_id += dict1[cur_id][1]
# print(count)

# # 方法一
# list_id = [id]
# count = 0
# while len(list_id) > 0:
#     for ii in range(len(list_id)):
#         cur_id = list_id.pop(0)
#         for employee in employees:
#             if employee.id == cur_id:
#                 count += employee.importance
#                 list_id += employee.subordinates
# print(count)
#-----------------------------------------------------------------------------#
# # 692. 前K个高频单词
# words = ["i", "love", "leetcode", "i", "love", "coding"]
# k = 2
# words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
# k = 4

# import collections
# dict1 = collections.OrderedDict()

# for word in words:
#     if word not in dict1:
#         dict1[word] = 1
#     else:
#         dict1[word] += 1
# dict1_sort = sorted(dict1.items(), key = lambda x:(-x[1],x[0]))
# output = []
# for ii in range(k):
#     output.append(dict1_sort[ii][0])
# print(output)
#-----------------------------------------------------------------------------#
# # 696. 计数二进制子串
# s = "00110011"
# s = "10101"
# s = "00110"

# # 超时
# count = 0
# for len1 in range(1,len(s)//2+1):
#     print(len1)
#     for ii in range(len(s)-len1*2+1):
#         if s[ii:ii+len1*2] == '0'*len1+'1'*len1 or s[ii:ii+len1*2] == '1'*len1+'0'*len1:
#             count += 1
# print(count)
#-----------------------------------------------------------------------------#
# # question 697 数组的度 已完成
# nums = [1,2,2,3,1,4,2]

# num_weiyi = []
# for num in nums:
#     if num not in num_weiyi:
#         num_weiyi.append(num)
# freq = []
# for num in num_weiyi:
#     freq.append(nums.count(num))
# du = max(freq)

# target_nums = []
# for num in num_weiyi:
#     if nums.count(num) == du and num not in target_nums:
#         target_nums.append(num)

# output = len(nums)      
# for target_num in target_nums:
#     for ii in range(len(nums)):
#         if nums[ii] == target_num:
#             # print(ii)
#             break
#     for jj in range(len(nums)):
#         if nums[len(nums)-jj-1] == target_num:
#             # print(len(nums)-jj-1)
#             break
#     output_new = len(nums)-jj-1-ii+1
#     if output_new < output:
#         output = output_new
# print(output)
#-----------------------------------------------------------------------------#
# # 700. 二叉搜索树中的搜索
# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(7)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# val = 2

# while root != None:
#     if root.val == val:
#         # return root
#         break
#     elif root.val < val:
#         root = root.right
#     else:
#         root = root.left
#-----------------------------------------------------------------------------#
# # 720. 词典中最长的单词
# words = ["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]
# words = ["w","wo","wor","worl","world"]
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# words = ["rac","rs","ra","on","r","otif","o","onpdu","rsf","rs","ot","oti","racy","onpd"]

# 错误
# words.sort()
# dp = [0 for _ in range(len(words))]
# for ii in range(len(words)):
#     if len(words[ii]) == 1:
#         dp[ii] = 1
#     elif len(words[ii]) > 1 and ii > 0:
#         dp[ii-1] > 0 and words[ii-1]+words[ii][-1] == words[ii]:
#         dp[ii] = dp[ii-1] + 1
# print(words)
# print(dp)
# print(words[dp.index(max(dp))])
#-----------------------------------------------------------------------------#
# # 733. 图像渲染
# # image = [[1,1,1],[1,1,0],[1,0,1]]
# # image = [[1,1,0],[1,1,0],[1,0,1]]
# image = [[1,1,0],[0,1,1],[1,1,0]]
# sr = 1
# sc = 1
# newColor = 2

# image = [[0,0,0],[0,1,0]]
# sr = 1
# sc = 0
# newColor = 2

# import numpy,copy
# image_new = numpy.array([[None]*len(image[0]) for _ in range(len(image))])
# image_new[sr,sc] = newColor
# image_new2 = copy.deepcopy(image_new)
# # while None == numpy.unique(image_new)[0]:
# while None in image_new:
#     for ii in range(image_new.shape[0]):
#         for jj in range(image_new.shape[1]):
#             if image_new[ii,jj] == None:
#                 label2 = False
#                 label = False
#                 if 0 <= ii+1 < image_new.shape[0] and image_new2[ii+1,jj] != None:
#                     label2 = True
#                     if image[ii][jj] == image[ii+1][jj] and image_new2[ii+1,jj] == newColor:
#                         label = label or True
#                     #     image_new[ii,jj] = newColor
#                     # else:
#                     #     image_new[ii,jj] = image[ii][jj]
#                 if 0 <= ii-1 < image_new.shape[0] and image_new2[ii-1,jj] != None:
#                     label2 = True
#                     if image[ii][jj] == image[ii-1][jj] and image_new2[ii-1,jj] == newColor:
#                         label = label or True
#                     #     image_new[ii,jj] = newColor
#                     # else:
#                     #     image_new[ii,jj] = image[ii][jj]
#                 if 0 <= jj+1 < image_new.shape[1] and image_new2[ii,jj+1] != None:
#                     label2 = True
#                     if image[ii][jj] == image[ii][jj+1] and image_new2[ii,jj+1] == newColor:
#                         label = label or True
#                     #     image_new[ii,jj] = newColor
#                     # else:
#                     #     image_new[ii,jj] = image[ii][jj]
#                 if 0 <= jj-1 < image_new.shape[1] and image_new2[ii,jj-1] != None:
#                     label2 = True
#                     if image[ii][jj] == image[ii][jj-1] and image_new2[ii,jj-1] == newColor:
#                         label = label or True
#                     #     image_new[ii,jj] = newColor
#                     # else:
#                     #     image_new[ii,jj] = image[ii][jj]
#                 if label2 == True:
#                     if label == True:
#                         image_new[ii,jj] = newColor
#                     else:
#                         image_new[ii,jj] = image[ii][jj]
#     print(image_new)
#     image_new2 = copy.deepcopy(image_new)
# output = []
# for ii in range(image_new.shape[0]):
#     output.append(list(image_new[ii]))
# print(output)

#-----------------------------------------------------------------------------#
# # 748. 最短补全词
# licensePlate = "1s3 PSt"
# words = ["step", "steps", "stripe", "stepple"]

# licensePlate = licensePlate.lower()
# dict_license = {}
# alphabet = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
# for ss in licensePlate:
#     if ss in alphabet:
#         if ss not in dict_license:
#             dict_license[ss] = 1
#         else:
#             dict_license[ss] += 1
# print(dict_license)
# def check(word):
#     dict_word = {}
#     list_license = list(dict_license.keys())
#     for ss in list_license:
#         dict_word[ss] = 0
#     for ss in word:
#         if ss in dict_license:
#             dict_word[ss] += 1
#     label = True
#     for ss in list_license:
#         if dict_license[ss] > dict_word[ss]:
#             label = False
#             break
#     return label
# min_len = 16
# output = ''
# for word in words:
#     if check(word):
#         if len(word) < min_len:
#             min_len = len(word)
#             output = word
# print(output)
#-----------------------------------------------------------------------------#
# # question 766 托普利茨矩阵 - 斜对角线构造 已完成
# matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# matrix = [[1,2],[2,2]]
# matrix = [[1,2]]
# def check(list1):
#     temp_num = list1[0]
#     output = True
#     for ii in range(1,len(list1)):
#         if list1[ii] != temp_num:
#             output = False
#             break
#     return output
    
# num_row = len(matrix)
# num_col = len(matrix[0])

# label = True
# index_col = 0
# while index_col < num_col-1:
#     temp = []
#     for ii in range(min(num_row, num_col-index_col)):
#         temp.append(matrix[ii][ii+index_col])
#     index_col += 1
#     # print(temp)
#     if check(temp):
#         pass
#     else:
#         label = False
#         break
# if label == True:
#     index_row = 1
#     while index_row < num_row-1:
#         temp = []
#         for ii in range(min(num_col, num_row-index_row)):
#             temp.append(matrix[ii+index_row][ii])
#         index_row += 1
#         # print(temp)
#         if check(temp):
#             pass
#         else:
#             label = False
#             break
# print(label)
#-----------------------------------------------------------------------------#
# # 781. 森林中的兔子
# answers = [1, 1, 2]
# answers = [10, 10, 10]
# answers = [4,4,4,4,4,2]

# dict1 = {}
# for num in answers:
#     if num not in dict1:
#         dict1[num] = 1
#     else:
#         dict1[num] += 1
        
# count = 0
# for num in dict1.keys():
#     count += ((dict1[num]-1)//(num+1) + 1)*(num+1)
# print(count)
#-----------------------------------------------------------------------------#
# # 804. 唯一摩尔斯密码词
# words = ["gin", "zen", "gig", "msg"]

# alphabet = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.",
#                  "h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.",
#                  "o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-",
#                  "u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
# set1 = set()
# for word in words:
#     temp = ''
#     for ss in word:
#         temp += alphabet[ss]
#     set1.add(temp)
# print(len(set1))
#-----------------------------------------------------------------------------#
# # 810. 黑板异或游戏
# nums = [1, 1, 2]

# # 思路：当且仅当以下两个条件至少满足一个时，Alice 必胜：
# # 1)nums的全部元素的异或结果等于 00；
# # 2)nums的长度是偶数。
# if len(nums)%2 == 0:
#     print(True)
# else:
#     count = nums[0]
#     for ii in range(1,len(nums)):
#         count = count ^ nums[ii]
#     if count == 0:
#         print(True)
#     else:
#         print(False)
#-----------------------------------------------------------------------------#
# # question 832 翻转图像 已完成

# A = [[1,1,0],[1,0,1],[0,0,0]]
# A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

# B = [[] for _ in range(len(A))]
# for ii in range(len(A)):
#     for jj in range(len(A[ii])):
#         B[ii]= [1- A[ii][jj]] + B[ii]
# print(B)
#-----------------------------------------------------------------------------#
# # question 866 回文素数 已完成 - 回文根+素数
# N = 1

# def sushu(num):
#     # 检查小于math.sqrt(num)的数中有没有能整除num的
#     if num == 2:
#         return True
#     elif num == 1:
#         return False
#     else:
#         label = True
#         if num%2 == 0:
#             label = False
#         else:
#             for ii in range(3,int(num**0.5)+1,2):
#                 if num%ii == 0:
#                     label = False
#     return label

# def next_huiwen(num): #回文根
#     num_str = str(num)
#     if len(num_str)%2 == 1:
#         base_huiwen = num_str[0:len(num_str)//2] + num_str[len(num_str)//2]
#         temp = ''
#         for ii in range(len(base_huiwen)-1):
#             temp = base_huiwen[ii] + temp
#         output_str = base_huiwen + temp
#         if num > int(output_str):
#             base_huiwen = str(int(base_huiwen)+1)
#             temp = ''
#             for ii in range(len(base_huiwen)-1):
#                 temp = base_huiwen[ii] + temp
#             output_str = base_huiwen + temp
#     else:
#         base_huiwen = num_str[0:len(num_str)//2]
#         temp = ''
#         for ii in range(len(base_huiwen)):
#             temp = base_huiwen[ii] + temp
#         output_str = base_huiwen + temp
#         if num > int(output_str):
#             base_huiwen = str(int(base_huiwen)+1)
#             temp = ''
#             for ii in range(len(base_huiwen)):
#                 temp = base_huiwen[ii] + temp
#             output_str = base_huiwen + temp
#     return int(output_str)
    
# N = next_huiwen(N)
# while not sushu(N):
#     N = next_huiwen(N+1)
# print(N)

#-----------------------------------------------------------------------------#
# # question 888 公平的糖果棒交换 已完成
# # A = [1,1]
# # B = [2,2]
# # A = [1,2]
# # B = [2,3]
# A = [2]
# B = [1,3]

# label = 0
# for ii in range(len(A)):
#     if int((2*A[ii] - sum(A) + sum(B))/2) in B:
#         output = [A[ii], int((2*A[ii] - sum(A) + sum(B))/2)]
#         break
# print(output)
#-----------------------------------------------------------------------------#
# # question 896 单调数列
# # A = [1,2,2,3]
# # A = [6,5,4,4]
# # A = [1,3,2]
# # A = [1,2,4,5]
# # A = [1,1,1]
# A = [1] # -> True

# label_up = True
# label_down = True
# for ii in range(len(A)-1):
#     if A[ii] <= A[ii+1]:
#         pass
#     else:
#         label_up = False
#     if A[ii] >= A[ii+1]:
#         pass
#     else:
#         label_down = False
#     if label_up or label_down:
#         pass
#     else:
#         break
# output = label_up or label_down
# print(output)
#-----------------------------------------------------------------------------#
# # 897. 递增顺序搜索树 - 思路与官方一致
# root = TreeNode(5)
# root.left = TreeNode(3)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.left.left.left = TreeNode(1)
# root.right = TreeNode(6)
# root.right.right = TreeNode(8)
# root.right.right.left = TreeNode(7)
# root.right.right.right = TreeNode(9)

# temp = []
# def dfs(root):
#     if not root:
#         return
#     dfs(root.left)
#     temp.append(root.val)
#     dfs(root.right)
# dfs(root)
# print(temp)

# if len(temp) > 0:
#     root = TreeNode(temp[0])
#     p = root
#     for ii in range(1,len(temp)):
#         p.right = TreeNode(temp[ii])
#         p = p.right
# else:
#     root = None
#-----------------------------------------------------------------------------#
# # 901. 股票价格跨度
# nums = [100, 80, 60, 70, 60, 75, 85, 110]
# nums = [31,41,48,59,79]
# nums = [28,14,28,35,46,53,66,80,87,88]
# dp = [0 for _ in range(len(nums))]
# dp[0] = 1
# for ii in range(1,len(nums)):
#     if nums[ii-1] > nums[ii]:
#         dp[ii] = 1
#     else:
#         count = dp[ii-1]
#         index = ii-1-dp[ii-1]
#         while index >= 0 and nums[index] <= nums[ii]:
#             count += dp[index]
#             index -= dp[index]
#         dp[ii] = count + 1
# print(dp)
#-----------------------------------------------------------------------------#
# # 908. 最小差值 I
# A = [1]
# K = 0
# # A = [0,10]
# # K = 2
# # A = [1,3,6]
# # K = 2
# def hebing(intervals):
#     intervals.sort()
#     output = [intervals[0]]
#     if len(intervals) > 1:
#         for ii in range(1,len(intervals)):
#             if output[-1][1] >= intervals[ii][0]:
#                 output[-1][0] = max(output[-1][0],intervals[ii][0])
#             else:
#                 output.append(intervals[ii])
#     return output
# if len(A) > 1:
#     intervals = []
#     for ii in range(len(A)):
#         intervals.append([A[ii]-K, A[ii]+K])
#     intervals = hebing(intervals)
#     if len(intervals) == 1:
#         print(0)
#     else:
#         print(intervals[-1][0] - intervals[0][1])
# else:
#     print(0)
#-----------------------------------------------------------------------------#
# # 917. 仅仅反转字母
# S = "ab-cd"
# S = "a-bC-dEf-ghIj"
# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
#         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# list_S = list(S)
# list_new = []
# list_index = []
# for ii in range(len(list_S)):
#     if list_S[ii] in alphabet:
#         list_index.append(ii)
#         list_new = [S[ii]] + list_new
# for ii in range(len(list_index)):
#     list_S[list_index[ii]] = list_new[ii]
        
# print(''.join(list_S))
#-----------------------------------------------------------------------------#
# # 950. 按递增顺序显示卡牌
# deck = [17,13,11,2,3,5,7]
# deck.sort(reverse = True)
# output = [deck[0]]
# for ii in range(1,len(deck)):
#     output = [deck[ii]] + [output[-1]] + output[0:-1]
# print(output)
#-----------------------------------------------------------------------------#
# # 993. 二叉树的堂兄弟节点
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.right = TreeNode(5)
# x = 5
# y = 4

# record = [root]
# while len(record) > 0:
#     label = False
#     for ii in range(len(record)):
#         cur = record.pop(0)
#         if cur.left != None and cur.right != None:
#             if cur.left.val == x or cur.right.val == x:
#                 label = True
#                 continue
#             else:
#                 record.append(cur.left)
#                 record.append(cur.right)
#         elif cur.left != None and cur.right == None:
#             if cur.left.val == x:
#                 label = True
#                 continue
#             else:
#                 record.append(cur.left)
#         elif cur.left == None and cur.right != None:
#             if cur.right.val == x:
#                 label = True
#                 continue
#             else:
#                 record.append(cur.right)
#     if label == True:
#         brother = [cur.val for cur in record]
#         print(y in brother)
#         break
#-----------------------------------------------------------------------------#
# # question 995 K连续位的最小翻转次数 -超时 待完成
# A = [0,1,0]
# K = 1
# # A = [1,1,0]
# # K = 2
# # A = [0,0,0,1,0,1,1,0]
# # K = 3

# count = 0
# index = 0
# while index < len(A)-K+1:
#     if A[index] == 1:
#         index += 1
#     else:
#         for jj in range(K):
#             A[index+jj] = 1 - A[index+jj]
#         count += 1
# # 判断
# label = 0
# for jj in range(K-1):
#     if A[len(A)-1-jj] == 0:
#         label = 1
#         break
# if label == 1:
#     output = -1
# else:
#     output = count
# print(output)
#-----------------------------------------------------------------------------#
# # question 1004  窗口滑动 -待完成
# A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# K = 3
# # A = [0,0,0,1]
# # K = 4
# # A = [1,1,1,0,0,0,1,1,1,1,0]
# # K = 2

# A2 = []
# for ii in range(len(A)):
#     if A[ii] == 0:
#         A2.append(1)
#     else:
#         A2.append(0)

# # A2 = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0]
# index1 = 0
# index2 = 0
# output = 0
# while index2 <= len(A2)-1:
#     if sum(A2[index1:index2+1]) <= K:
#         output_new = index2 - index1 + 1
#         index2 += 1
#         if output_new > output:
#             output = output_new
#     elif sum(A2[index1:index2+1]) == K+1:
#         index1 += 1
#         # while A2[index1] == 0:
#         #     index1 += 1
#         # while A2[index1] == 1:
#         #     index1 += 1
#         # output_new = index2 - index1
#         # if output_new > output:
#         #     output = output_new
 
# print(output)
#-----------------------------------------------------------------------------#
# # 1006. 笨阶乘
# N = 0
# record = []
# for ii in range(N):
#     print(N-ii)
#     if ii%4 == 0:
#         temp = N-ii
#     elif ii%4 == 1:
#         temp = temp *(N-ii)
#     elif ii%4 == 2:
#         temp = temp // (N-ii)
#     else:
#         record.append(temp)
#         record.append(N-ii)
# if (N-1)%4 != 3:
#     record.append(temp)
# print(record)
# for ii in range(2,len(record),2):
#     record[ii] = - record[ii]
# print(sum(record))
#-----------------------------------------------------------------------------#
# # 1011. 在 D 天内送达包裹的能力
# 官方思路，下限为max(weights)，上限为sum(weights)，然后用二分法查找

# weights = [1,2,3,4,5,6,7,8,9,10]
# D = 5
# # weights = [3,2,2,4,1,4]
# # D = 3
# # weights = [1,2,3,1,1]
# # D = 4

# # 从下限往上找
# import math
# index = max(math.ceil(sum(weights)/D), max(weights)) #下限
# while index > 0:
#     count = 0
#     temp = 0
#     for ii in range(len(weights)):
#         if temp + weights[ii] <= index:
#             temp += weights[ii]
#         else:
#             count += 1
#             temp = weights[ii]
#     if temp > 0:
#         count += 1
#     if count <= D:
#         break
#     else:
#         index += 1
# print(index)
#-----------------------------------------------------------------------------#
# # 1035. 不相交的线
# nums1 = [1,4,2]
# nums2 = [1,2,4]
# nums1 = [2,5,1,2,5]
# nums2 = [10,5,2,1,5,2]
# nums1 = [1,3,7,1,7,5]
# nums2 = [1,9,2,5,1]

# dp = [[0]*len(nums2) for _ in range(len(nums1))]
# if nums1[0] == nums2[0]:
#     dp[0][0] = 1
# else:
#     dp[0][0] = 0
# for ii in range(1,len(nums1)):
#     if nums1[ii] == nums2[0]:
#         dp[ii][0] = max(1, dp[ii-1][0])
#     else:
#         dp[ii][0] = max(0, dp[ii-1][0])
# for jj in range(1,len(nums2)):
#     if nums1[0] == nums2[jj]:
#         dp[0][jj] = max(1, dp[0][jj-1])
#     else:
#         dp[0][jj] = max(0, dp[0][jj-1])
# for ii in range(1,len(nums1)):
#     for jj in range(1,len(nums2)):
#         if nums1[ii] == nums2[jj]:
#             dp[ii][jj] = dp[ii-1][jj-1] + 1
#         else:
#             dp[ii][jj] = max(dp[ii][jj-1], dp[ii-1][jj])
# print(dp[-1][-1])
#-----------------------------------------------------------------------------#
# # 1047 删除字符串中的所有相邻重复项 已完成
# S = "abbbacaa"

# index = 0
# while index < len(S)-1:
#     temp = ''
#     if S[index] == S[index+1]:
#         temp = S[0:index] + S[index+2:]
#         if index > 0:
#             index = index - 1
#         else:
#             index = 0
#         S = temp
#     else:
#         index += 1
# print(S)
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
# # 1042. 不邻接植花
# # n = 3
# # paths = [[1,2],[2,3],[3,1]]
# # n = 4
# # paths = [[1,2],[3,4]]
# # n = 4
# # paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# n = 5
# paths = [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]

#-----------------------------------------------------------------------------#
# # question 1052 爱生气的书店老板  - 超时
# # customers = [1,0,1,2,1,1,7,5]
# # grumpy = [0,1,0,1,0,1,0,1]
# # X = 4
# customers = [2,3]
# grumpy = [1,1]
# X = 3

# output = 0
# for ii in range(len(grumpy)-min(X,len(customers))+1):
#     if grumpy[ii] == 0 and ii+X >= len(grumpy):
#         grumpy_new = [_ for _ in grumpy]
#         grumpy_new[ii:len(grumpy)] = [0 for _ in range(len(grumpy)-ii)]
#         temp = 0
#         for jj in range(len(customers)):
#             temp += customers[jj]*(1-grumpy_new[jj])
#         if temp > output:
#             output = temp
#     elif grumpy[ii] == 1:
#         grumpy_new = [_ for _ in grumpy]
#         grumpy_new[ii:ii+X] = [0 for _ in range(X)]
#         temp = 0
#         for jj in range(len(customers)):
#             temp += customers[jj]*(1-grumpy_new[jj])
#         if temp > output:
#             output = temp
# print(output)
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
# # question 1178 猜字谜 - 超时/待完成
# words = ["aaaa","asas","able","ability","actt","actor","access"]
# puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# # words = ["apple","pleas","please"]
# # puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]

# def str_2_num(str1):
#     if str1 == 'a':
#         index = 0
#     elif str1 == 'b':
#         index = 1
#     elif str1 == 'c':
#         index = 2
#     elif str1 == 'd':
#         index = 3
#     elif str1 == 'e':
#         index = 4
#     elif str1 == 'f':
#         index = 5
#     elif str1 == 'g':
#         index = 6
#     elif str1 == 'h':
#         index = 7
#     elif str1 == 'i':
#         index = 8
#     elif str1 == 'j':
#         index = 9
#     elif str1 == 'k':
#         index = 10
#     elif str1 == 'l':
#         index = 11
#     elif str1 == 'm':
#         index = 12
#     elif str1 == 'n':
#         index = 13
#     elif str1 == 'o':
#         index = 14
#     elif str1 == 'p':
#         index = 15
#     elif str1 == 'q':
#         index = 16
#     elif str1 == 'r':
#         index = 17
#     elif str1 == 's':
#         index = 18
#     elif str1 == 't':
#         index = 19
#     elif str1 == 'u':
#         index = 20
#     elif str1 == 'v':
#         index = 21
#     elif str1 == 'w':
#         index = 22
#     elif str1 == 'x':
#         index = 23
#     elif str1 == 'y':
#         index = 24
#     elif str1 == 'z':
#         index = 25
#     return index
        
# def str_2_bool(s):
#     temp = [False for _ in range(26)]
#     for ii in range(len(s)):
#         temp[str_2_num(s[ii])] = True
#     return temp
        
# str_2_bool('az')


# record = [0 for _ in range(len(puzzles))]
# def word_in_puzzle(word, puzzle):
#     # label = True
#     str_2_bool(puzzle[0]) and 
#     if puzzle[0] in word:
#         label = True
#         index = 0
#         while index < len(word):
#             if word[index] not in puzzle:
#                 label = False
#                 break
#             index += 1
#     else:
#         label = False
#     return label
        
# output = [0 for _ in range(len(puzzles))]
# for ii in range(len(words)):
#     for jj in range(len(puzzles)):
#         if word_in_puzzle(words[ii],puzzles[jj]):
#             record[jj] += 1
# print(record)
#-----------------------------------------------------------------------------#
# # 1190. 反转每对括号间的子串
# s = "(u(love)i)"
# s = "(ed(et(oc))el)"
# s = "a(bcdefghijkl(mno)p)q"

# index_left = 0
# index_right = len(s) - 1
# while '(' in s:
#     for ii in range(len(s)):
#         if s[ii] == '(':
#             index_left = ii
#         elif s[ii] == ')':
#              index_right = ii
#              break
#     temp = ''
#     for jj in range(index_right-1, index_left, -1):
#         temp += s[jj]
#     s = s[0:index_left] + temp + s[index_right+1:]
# print(s)
#-----------------------------------------------------------------------------#
# # 1260. 二维网格迁移 已完成
# grid = [[1,2,3],[4,5,6],[7,8,9]]
# k = 1
# grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
# k = 4
# grid = [[1,2,3],[4,5,6],[7,8,9]]
# k = 9
# def qianyi(grid):
#     record = []
#     for ii in range(len(grid)):
#         record.append([grid[ii][-1]]+grid[ii][0:-1])
#     temp = record[-1][0]
#     for ii in range(len(grid)-1,0,-1):
#         record[ii][0] = record[ii-1][0]
#     record[0][0] = temp
#     return record

# index = 0
# while index < k:
#     index += 1
#     grid = qianyi(grid)
# print(grid)
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
# # 1310. 子数组异或查询
# arr = [1,3,4,8]
# queries = [[0,1],[1,2],[0,3],[3,3]]
# arr = [4,8,2,10]
# queries = [[2,3],[1,3],[0,0],[0,3]]

# dp = [0 for _ in range(len(arr))]
# dp[0] = arr[0]
# for ii in range(1,len(arr)):
#     dp[ii] = dp[ii-1] ^ arr[ii]
    
# output = []
# for ii in range(len(queries)):
#     if queries[ii][0] == 0:
#         output.append(dp[queries[ii][1]])
#     else:
#         output.append(dp[queries[ii][0]-1]^dp[queries[ii][1]])
# print(output)
#-----------------------------------------------------------------------------#
# # question 1323 6和9组成的最大数字
# # num = 9669
# # num = 9996
# num = 9999

# num_str = list(str(num))
# index = 0
# while index < len(num_str):
#     if num_str[index] == '9':
#         index += 1
#     else:
#         num_str[index] = '9'
#         break
# num_str2 = ''
# for ss in num_str:
#     num_str2 += ss
# num2 = int(num_str2)
# print(num2)
#-----------------------------------------------------------------------------#
# # question 1438 绝对差不超过限制的最长连续子数组 - 滑动窗口 -已完成
# nums = [8,2,4,7]
# limit = 4
# # nums = [10,1,2,4,7,2]
# # limit = 5
# # nums = [4,2,2,2,4,4,2,2]
# # limit = 0
# # limit = 0

# output = 0
# index_left = 0
# index_right = 0
# while index_right <= len(nums)-1:
#     temp = nums[index_left:index_right+1]
#     if max(temp) - min(temp) <= limit:
#         output_new = index_right - index_left + 1
#         if output_new > output:
#             output = output_new
#         index_right += 1
#         while index_right < len(nums)-2 and nums[index_right+1] == nums[index_right]:
#             index_right += 1
#     else:
#         index_left += 1
#         while nums[index_left] == nums[index_left-1]:
#             index_left += 1
# print(output)
#-----------------------------------------------------------------------------#
# # 1442. 形成两个异或相等数组的三元组数目
# arr = [2,3,1,6,7]
# # arr = [1,1,1,1,1]
# # arr = [2,3]
# # arr = [1,3,5,7,9]
# # arr = [7,11,12,9,5,2,7,17,22]

# # 思路
# # arr[i]^arr[i+1]^...^arr[j-1] = arr[j]^arr[j+1]^ ...^arr[k]的数量
# # <=> arr[i]^arr[i+1]^...^arr[k] = 0乘以k-i的数量

# # 改进
# dp = [0 for _ in range(len(arr))]    #dp优化累计异或
# dp[0] = arr[0]
# for ii in range(1,len(arr)):
#     dp[ii] = arr[ii]^dp[ii-1]
# print(dp)
# count = 0
# for ii in range(len(arr)-1):
#     for kk in range(ii+1,len(arr)):
#         if ii == 0:
#             if dp[kk] == 0:
#                 count += kk-ii
#         else:
#             if dp[ii-1]^dp[kk] == 0:
#                 count += kk-ii
# print(count)

# # 原始
# count = 0
# for ii in range(len(arr)-1):
#     for kk in range(ii+1,len(arr)):
#         temp = arr[ii]                #dp优化累计异或
#         for mm in range(ii+1, kk+1):  #dp优化累计异或  
#             temp = temp ^ arr[mm]     #dp优化累计异或
#         if temp == 0:
#             count += kk-ii
# print(count)
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
# # 1482. 制作 m 束花所需的最少天数
# bloomDay = [1,10,3,10,2]
# m = 3
# k = 2 # -1
# bloomDay = [7,7,7,7,12,7,7]
# m = 2
# k = 3 # 12
# bloomDay = [1000000000,1000000000]
# m = 1
# k = 1 # 1000000000
# bloomDay = [1,10,2,9,3,8,4,7,5,6]
# m = 4
# k = 2 # 9
# bloomDay = [5,37,55,92,22,52,31,62,99,64,92,53,34,84,93,50,28]
# m = 8
# k = 2 # 93

# # 二分查找
# def check(day): #超时
#     label2 = False
#     index = 0
#     count = 0
#     while index + k-1 < len(bloomDay):
#         label = True
#         ii = 0
#         while ii < k:
#         # for ii in range(k): #超时的原因在这里！！改成While就好
#             if bloomDay[index+ii] > day:
#                 label = False
#                 break
#         if label == True:
#             index += k
#             count += 1
#         else:
#             index += ii+1
#         if count == m:
#             label2 = True
#             break
#     return label2

# def check(days): #官方-不超时
#     flower = 0
#     bouquet = 0
#     for i in range(len(bloomDay)):
#         if bloomDay[i] <= days:
#             flower += 1
#             if flower == k:
#                 bouquet += 1
#                 flower = 0
#         else:
#             flower = 0
#         if bouquet == m:
#             break
#     return bouquet >= m
        
# if len(bloomDay) >= m*k:
#     left = min(bloomDay)
#     right = max(bloomDay)
#     while left < right:
#         index = int((right-left)/2)+left
#         if check(index) == True:
#             right = index
#         else:
#             left = index+1
#         print(left,right)
#     print(left)
# else:
#     print(-1)
#-----------------------------------------------------------------------------#
# 1486. 数组异或操作
# n = 5
# start = 0
# n = 4
# start = 3
# n = 1
# start = 7
# n = 10
# start = 5

# count = start
# for ii in range(start+2,start+2*n-1,2):
#     count = count^ii
# print(count)
#-----------------------------------------------------------------------------#
# # 1707. 与数组中元素的最大异或值 - 未解决
# nums = [0,1,2,3,4]
# queries = [[3,1],[1,3],[5,6]]
# nums = [5,2,4,6,6,3]
# queries = [[12,4],[8,1],[6,3]]


# import bisect
# import copy
# def bin_left(num):
#     return int('1'+'0'*(len(bin(num)[2:])-1), 2)
# def bin_right(num):
#     return int('1'*len(bin(num)[2:]), 2)

# nums.sort()
# output = []
# for ii in range(len(queries)):
#     cur_num = queries[ii][0]
#     cur_left = bin_left(cur_num)
#     cur_right = bin_right(cur_num)
#     if queries[ii][1] < nums[0]:
#         output.append(-1)
#     else:
#         index_max = bisect.bisect_right(nums, queries[ii][1])-1
#         if nums[index_max] > cur_right:
#             # index从index_max往前找，直到nums[index] >= nums[index_max]的左边界（该值必然大于cur_right）
#             temp = nums[index_max]^queries[ii][0]
#             index = copy.deepcopy(index_max)-1
#             while index > - 1 and nums[index] >= bin_left(nums[index_max]):
#                 if nums[index] < nums[index+1]:
#                     temp = max(temp, nums[index]^queries[ii][0])
#                 index -= 1
#             output.append(temp)
#         elif cur_left <= nums[0] <= nums[index_max] <= cur_right:
#             # index从左到右全找
#             temp = nums[0]^queries[ii][0]
#             index = 1
#             while index < len(nums):
#                 if nums[index-1] < nums[index]:
#                     temp = max(temp, nums[index]^queries[ii][0])
#                 index += 1
#             output.append(temp)
#         elif nums[0] < cur_left <= nums[index_max] <= cur_right:
#             # index从左往右找，直到num[index] <= nums[0]的右边界（该值必然小于cur_left）
#             temp = nums[0]^queries[ii][0]
#             index = 1
#             while index < index_max+1 and nums[index] <= cur_left:
#                 if nums[index-1] < nums[index]:
#                     temp = max(temp, nums[index]^queries[ii][0])
#                 index += 1
#             output.append(temp)
#         elif nums[0] <= nums[index_max] < cur_left <= cur_right:
#             temp = nums[0]^queries[ii][0]
#             index = 1
#             while index < index_max+1 and nums[index] <= bin_right(nums[0]):
#                 if nums[index-1] < nums[index]:
#                     temp = max(temp, nums[index]^queries[ii][0])
#                 index += 1
#             output.append(temp)
# print(output)

# # 超时
# nums.sort()
# output = []
# for ii in range(len(queries)):
#     if nums[0] <= queries[ii][1]:
#         temp = nums[0]^queries[ii][0]
#         index = 1
#         while index < len(nums) and nums[index] <= queries[ii][1]:
#             if nums[index-1] < nums[index]:
#                 temp = max(temp, nums[index]^queries[ii][0])
#             index += 1
#         output.append(temp)
#     else:
#         output.append(-1)
# print(output)

#-----------------------------------------------------------------------------#
# 1720. 解码异或后的数组
# #思路：a^b=c <=> a^c=b
# encoded = [1,2,3]
# first = 1
# encoded = [6,2,7,3]
# first = 4

# output = [first]
# for ii in range(len(encoded)):
#     output.append(output[-1]^encoded[ii])
# print(output)

# # 1734. 解码异或后的排列
# encoded = [3,1]
# encoded = [6,5,4,6]

# # 利用异或运算 1)交换律 以及 2)a^b=c <=> a^c=b 找perm[0]
# #   1       ^ 2       ^ 3       ^ 4       ^ 5      ... ^ 2k         ^ 2k+1
# # = perm[0] ^ perm[1] ^ perm[2] ^ perm[3] ^ perm[4]... ^ perm[2k-1] ^ perm [2k] = 
# # = perm[0] ^ encoded[1]        ^ encoded[3]       ... ^ encoded[2k-1]
# # let total_perm = 1 ^ 2 ^ 3 ^ 4 ^ 5 ... ^ 2k ^ 2k+1, total_encoded = encoded[1] ^ encoded[3] ... ^ encoded[2k-1]
# # then perm[0] ^ total_encoded = total_perm, => perm[0] = total_encoded ^ total_perm
# first = 1
# for ii in range(2,len(encoded)+2):
#     first = first ^ ii
# for ii in range(1,len(encoded),2):
#     first = first ^ encoded[ii]
# print(first)
# output = [first]
# for ii in range(len(encoded)):
#     output.append(output[-1]^encoded[ii])
# print(output)

# # #思路同上，找perm[-1]
# last = 1
# for ii in range(2,len(encoded)+2):
#     last = last ^ ii
# for ii in range(0,len(encoded),2):
#     last = last ^ encoded[ii]
# output_reverse = [last]
# for ii in range(len(encoded)-1,-1,-1):
#     output_reverse.append(encoded[ii]^output_reverse[-1])
# output = []
# for ii in range(len(output_reverse)-1,-1,-1):
#     output.append(output_reverse[ii])
# print(output)

# # 超时
# last = 1
# for ii in range(2,len(encoded)+2):
#     last = last ^ ii
# for ii in range(0,len(encoded),2):
#     last = last ^ encoded[ii]
# output = [last]
# for ii in range(len(encoded)-1,-1,-1):
#     output = [encoded[ii]^output[0]] + output #超时的原因在这里，output = [elem] + output 效率较差 
# print(output)

# # 超时 - 枚举perm[0],从前往后找满足条件的perm
# for ii in range(1,len(encoded)+2):
#     temp_set = set([kk+1 for kk in range(len(encoded)+1)])
#     num = ii
#     temp_set.remove(ii)
#     index = 0
#     while len(temp_set) > 0:
#         num = num^encoded[index]
#         if num in temp_set:
#             temp_set.remove(num)
#             index += 1
#         else:
#             break
#     if len(temp_set) == 0:
#         break
# print(ii)
# output = [ii]
# for ii in range(len(encoded)):
#     output.append(output[-1]^encoded[ii])
# print(output)

# # 枚举perm[0],从前往后找满足条件的perm，测试思路
# for ii in range(1,len(encoded)+2):
#     temp = [ii]
#     for jj in range(len(encoded)):
#         temp.append(temp[-1]^encoded[jj])
#     print(ii,temp)
#-----------------------------------------------------------------------------#
# # 1723. 完成所有工作的最短时间
# jobs = [3,2,3]
# k = 3
# jobs = [1,2,4,7,8]
# k = 2
# jobs = [5,5,4,4,4]
# k = 2

# # 思路：多平行机排序问题 —— 回溯+剪枝
# upper_bound = sum(jobs) #上界
# def backtrack(jobs,record):
#     global upper_bound
#     if len(jobs) == 0:
#         if max(record) < upper_bound:
#             upper_bound = max(record) 
#         return
#     else:
#         cur_job = jobs[0]
#         temp_set = set()
#         for ii in range(k):
#             if record[ii] not in temp_set: #再分配新工件前，如果两个工人的完工时间一样，新工件分配给任意工人的最小完工时间一致，只需遍历一个工人即可，可将另外一个工人的分枝裁剪
#                 temp_set.add(record[ii])
#                 record[ii] += cur_job
#                 if max(record) < upper_bound: #如果当前工件分配给第ii个工人导致目标函数超过上界，则剪枝
#                     backtrack(jobs[1:],record)
#                 record[ii] -= cur_job
# backtrack(jobs,[0 for _ in range(k)])
# print(upper_bound)
#-----------------------------------------------------------------------------#
# # 1738. 找出第 K 大的异或坐标值
# matrix = [[5,2],[1,6]]
# k = 1
# matrix = [[5,2],[1,6]]
# k = 2
# matrix = [[5,2],[1,6]]
# k = 3
# matrix = [[5,2],[1,6]]
# k = 4

# dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
# for jj in range(len(matrix[0])):
#     if jj == 0:
#         for ii in range(len(matrix)):
#             dp[ii][jj] = matrix[ii][jj]
#     else:
#         for ii in range(len(matrix)):
#             dp[ii][jj] = matrix[ii][jj] ^ dp[ii][jj-1]
# for ii in range(1,len(matrix)):
#     for jj in range(len(matrix[0])):
#         dp[ii][jj] = dp[ii][jj] ^ dp[ii-1][jj]
# list1 = []
# for ii in range(len(matrix)):
#     for jj in range(len(matrix[0])):
#         list1.append(dp[ii][jj])
# list1.sort(reverse=True)
# print(list1[k-1])
#-----------------------------------------------------------------------------#
# question 1792 最大平均通过率 - 未完成，换一天再尝试（好像服务器原因，无法执行除法）
# classes = [[1,2],[3,5],[2,2]]
# extraStudents = 2
# classes = [[2,4],[3,9],[4,5],[2,10]]
# extraStudents = 4

# # 方法一：选择增量最大的+1
# while extraStudents > 0:
#     delta = []
#     for ii in range(len(classes)):
#         delta.append((classes[ii][1]-classes[ii][0])/classes[ii][1]/(classes[ii][1]+1))
#     # delta = [(classes[ii][1] - classes[ii][0])/classes[ii][1]/(classes[ii][1]+1) for ii in range(len(classes))]
#     index_max = delta.index(max(delta))
#     classes[index_max][0] += 1
#     classes[index_max][1] += 1
#     print(classes)
#     extraStudents -= 1
# count = 0
# for ii in range(len(classes)):
#     count += classes[ii][0]/classes[ii][1]
# count = count/len(classes)
# print(count)

# # 方法二
# # def average_max(list_extra):
# #     count = 0
# #     for ii in range(len(classes)):
# #         count += (classes[ii][0] + list_extra[ii])/(classes[ii][1] + list_extra[ii])
# #     count = count/len(classes)
# #     return count

# # record = [[0 for _ in range(len(classes))]]
# # while extraStudents > 0:
# #     current_record = []
# #     for ii in range(len(record)):
# #         for jj in range(len(classes)):
# #             temp = [aa for aa in record[ii]]
# #             temp[jj] += 1
# #             if temp not in current_record:
# #                 current_record.append(temp)
                
# #     record = current_record
# #     extraStudents -= 1
# # # print(record)

# # output = 0
# # for ii in range(len(record)):
# #     temp = average_max(record[ii])
# #     if temp > output:
# #         output = temp
# #         output2 = record[ii]
# #     # output = max(output, average_max(record[ii]))
# # print(output)
# # print(output2)
#-----------------------------------------------------------------------------#
# # question 1802 有界数组中指定下标处的最大值 未完成
# # n = 4
# # index = 2
# # maxSum = 6
# # n = 6
# # index = 1
# # maxSum = 10
# # n = 1
# # index = 0
# # maxSum = 24
# # n = 4
# # index = 0
# # maxSum = 4
# # n = 9
# # index = 0
# # maxSum = 90924720
# # n = 3
# # index = 2
# # maxSum = 18
# n = 9
# index = 6
# maxSum = 27

# for ii in range(maxSum//n+maxSum%n+1,maxSum//n-1,-1):
#     record = [max(maxSum//n-1,1) for _ in range(n)]
#     record[index] = ii
#     index_left = index - 1
#     while index_left > -1:
#         # record[index_left] = record[index_left+1] - 1
#         if record[index_left+1] <= maxSum//n:
#             break
#         else:
#             record[index_left] = record[index_left+1] - 1
#         index_left -= 1
#     index_right = index + 1
#     while index_right < len(record):
#         if record[index_right-1] <= maxSum//n:
#             break
#         else:
#             record[index_right] = record[index_right-1] - 1
#         index_right += 1
#     print(record)
#     if sum(record) <= maxSum:
#         break
# print(ii)
#-----------------------------------------------------------------------------#
# # 1813. 句子相似性 III
# # sentence1 = "My name is Haley"
# # sentence2 = "My Haley"
# sentence1 = "of"
# sentence2 = "A lot of words"
# # sentence1 = "Eating right now"
# # sentence2 = "Eating"
# # sentence1 = "Luky"
# # sentence2 = "Lucccky"
# # sentence1 = "c h p Ny"
# # sentence2 ="c Gd h p Ny"
# # sentence1 = "v v i y PWG CQm"
# # sentence2 = "S cfSD GsjbETXQ"

# sentence1 = sentence1.split(' ')
# sentence2 = sentence2.split(' ')
# if len(sentence1) == len(sentence2):
#     print(sentence1 == sentence2)
# else:
#     if len(sentence1) < len(sentence2):
#         sentence_a = sentence1
#         sentence_b = sentence2
#     else:
#         sentence_a = sentence2
#         sentence_b = sentence1
        
#     index_left = -1
#     for ii in range(len(sentence_a)):
#         if sentence_a[ii] == sentence_b[ii]:
#             index_left = ii
#         else:
#             break
#     if index_left == len(sentence_a)-1:
#         print(True)
#     else:
#         index_right = 0
#         for ii in range(1,len(sentence_a)-index_left):
#             if sentence_a[-ii] == sentence_b[-ii]:
#                 index_right = ii
#             else:
#                 break
#         print( index_left+1 == len(sentence_a)-index_right )
#-----------------------------------------------------------------------------#
# # 1814. 统计一个数组中好对子的数目
# # nums = [42,11,1,97]
# nums = [13,10,35,24,76]

# def rev(num):
#     num_str = str(num)
#     temp = ''
#     for s in num_str:
#         temp = s + temp
#     return int(temp)

# dict1 = {}
# for ii in range(len(nums)):
#     if nums[ii]-rev(nums[ii]) not in dict1:
#         dict1[nums[ii]-rev(nums[ii])] = 1
#     else:
#         dict1[nums[ii]-rev(nums[ii])] += 1
# count = 0
# for ii in dict1.keys():
#     # print(ii)
#     if dict1[ii] >= 2:
#         count += dict1[ii]*(dict1[ii]-1)//2
# print(count%(10**9+7))
#-----------------------------------------------------------------------------#
# # 1815. 得到新鲜甜甜圈的最多组数
# # batchSize = 3
# # groups = [1,2,3,2,2,6,2]
# # groups = [1,2,3,4,5,6]
# # batchSize = 4
# # groups = [1,3,2,5,2,2,1,6]
# # batchSize = 7
# # groups = [2,7,5,2,3,2,6,5,3,6,2,3,7,2,2,5,4,6,6,4,7,5,6,1,6,2,6,6,2,5]
# # batchSize = 8
# # groups = [8,8,4,1,6,8,6,3,7,7,2,4,1,6,7,4,1,4,2,4,4,7,6,1,5,1,3,4,1,1]
# batchSize = 3
# groups = [369821235,311690424,74641571,179819879,171396603,274036220]
# # batchSize = 7
# # groups = [145326640,622724151,591814792,827053040,111964428,344376875,42023891,436582274,78590835,408269112,930041188,846233596,158192647,889601516,134236253,366035866,123146762]

# from itertools import combinations
# import copy
# dict_groups = {}
# count = 0
# # 一个元素 = batchSize的倍数
# for ii in range(len(groups)-1,-1,-1):
#     if groups[ii]%batchSize == 0:
#         count += 1
#     else:
#         if groups[ii]%batchSize not in dict_groups:
#             dict_groups[groups[ii]%batchSize] = 1
#         else:
#             dict_groups[groups[ii]%batchSize] += 1
# # 两个元素之和 = batchSize的倍数
# for ii in range(1,batchSize//2+1):
#     if ii*2 != batchSize:
#         if ii in dict_groups and batchSize-ii in dict_groups:
#             temp_count = min(dict_groups[ii], dict_groups[batchSize-ii])
#             count += temp_count
#             dict_groups[ii] -= temp_count
#             dict_groups[batchSize-ii] -= temp_count
#     else:
#         if ii in dict_groups:
#             count += dict_groups[ii]//2
#             dict_groups[ii] = dict_groups[ii]%2

# def dict_to_list(dict_groups):
#     # 字典转升序list
#     temp_elem = list(dict_groups.keys())
#     for ii in range(len(temp_elem)-1,-1,-1):
#         if dict_groups[temp_elem[ii]] == 0:
#             del(dict_groups[temp_elem[ii]])
#     temp_elem = sorted(list(dict_groups.keys()))
#     groups = []
#     for nn in temp_elem:
#         groups += [nn for _ in range(dict_groups[nn])]    
#     return temp_elem, groups

# temp_elem, groups = dict_to_list(dict_groups)
# step = 3
# # 三个及更多元素之和 = batchSize的倍数
# while len(groups) > 0:
#     # 枚举三数之和为batchSize倍数的所有组合
#     record = []
#     combs = list(combinations(groups, step))
#     for comb in combs:
#         temp_list1 = list(comb)
#         if sum(temp_list1)%batchSize == 0:
#             if temp_list1 not in record:
#                 record.append(temp_list1)
#     print(record)
    
#     if len(record) > 0:
#         # 为所有组合分配所有可能的数量
#         num_class = len(record)
#         record2 = []
#         def backtrack(list1,num_item):
#             if sum(list1) == num_item:
#                 if list1 not in record2:
#                     record2.append(list1)
#                 return
#             else:
#                 for ii in range(num_class):
#                     list1[ii] += 1
#                     backtrack(copy.deepcopy(list1),num_item)
#                     list1[ii] -= 1
#         for ii in range(len(groups)//3,0,-1):
#             backtrack([0 for _ in range(num_class)],ii)
#         print(record2)
    
#         # 检查每个分配的数量是否可行
#         for ii in range(len(record2)):
#             temp_list2 = []
#             for jj in range(len(record2[ii])):
#                 temp_list2 += record2[ii][jj]*record[jj]
#             dict2 = {}
#             for kk in temp_elem:
#                 dict2[kk] = 0
#             for kk in temp_list2:
#                 dict2[kk] += 1
#             label = True
#             for kk in temp_elem:
#                 if dict2[kk] > dict_groups[kk]:
#                     label = False
#                     break
#             if label == True:
#                 temp_count = sum(record2[ii])
#                 count += temp_count
#                 for kk in temp_elem:
#                     dict_groups[kk] -= dict2[kk]
#                 break
#         temp_elem, groups = dict_to_list(dict_groups)
#     if len(groups) > step:
#         step += 1
#     else:
#         break

# print(groups, step)
# if 0 < len(groups) <= step:
#     print(count+1)
# elif len(groups) == 0:
#     print(count)
# else:
#     print('出现新情况')
#-----------------------------------------------------------------------------#
# # 1819. 序列中不同最大公约数的数目
# # nums = [6,10,3]
# # nums = [5,15,40,5,6]
# # nums = [1,2,1,2,4,1,5,10]
# # nums = [1]
# def gcd(x,y):
#     # 辗转相除
#     while y != 0:
#         temp = x % y
#         x = y
#         y = temp
#     return x

# # nums.sort()
# # nums.sort(reverse = True)
# set_gongyue = set()
# set_gongyue.add(nums[0])
# for ii in range(1,len(nums)):
#     # if nums[ii] not in set_gongyue:
#     temp = []
#     for jj in iter(set_gongyue):
#         if nums[ii]%jj != 0:
#             temp_gongyue = gcd(nums[ii],jj)
#             temp.append(temp_gongyue)
#     temp.append(nums[ii])
#     for kk in temp:
#         set_gongyue.add(kk)

# print(len(set_gongyue))
#-----------------------------------------------------------------------------#
# # 1824. 最少侧跳次数
# # obstacles = [0,1,2,3,0]
# # obstacles = [0,1,1,3,3,0]
# # obstacles = [0,2,1,0,3,0]
# obstacles = [0,0,3,1,0,1,0,2,3,1,0]

# set1 = {2}
# count = 0
# for ii in range(len(obstacles)-1):
#     if obstacles[ii+1] in set1 and len(set1) == 1: #如果下一步遇到唯一阻碍，则跳一次，并更新候选阻碍
#         count += 1
#         set2 = set([1,2,3])
#         set2.remove(set1.pop()) #删除下一步的阻碍
#         if obstacles[ii] in set2:
#             set2.remove(obstacles[ii]) #删除当前的阻碍
#         set1 = set2
#     elif obstacles[ii+1] in set1 and len(set1) == 2: #如果候选阻碍有两个，贪婪取较远的阻碍
#         set1.remove(obstacles[ii+1])
# print(count)

# # 超时
# count = 0
# location = 2
# for ii in range(len(obstacles)):
#     if ii < len(obstacles)-1 and obstacles[ii+1] == location:
#         count += 1
#         locations = []
#         for jj in range(1,4):
#             if jj != obstacles[ii] and jj != location:
#                 locations.append(jj)
#         if len(locations) == 1:
#             location = locations[0]
#         elif len(locations) == 2:
#             if locations[0] not in obstacles[ii+1:]:
#                 location = locations[0]
#             elif locations[1] not in obstacles[ii+1:]:
#                 location = locations[1]
#             else:
#                 if obstacles[ii+1:].index(locations[0]) < obstacles[ii+1:].index(locations[1]):
#                     location = locations[1]
#                 else:
#                     location = locations[0]
# print(count)
#-----------------------------------------------------------------------------#
# # 5720. 使字符串有序的最少操作次数
# # s = "cba"
# s = "aabaa"
# # s = "cdbea"

# #超时，该问题转成第n个全排列
# from itertools import permutations
# ss = list(s)
# ss.sort()
# perms = list(permutations(ss, len(ss)))
# temp = []
# for perm in perms:
#     cur = ''.join(list(perm))
#     if cur not in temp:
#         temp.append(cur)
# print(temp.index(s))
#-----------------------------------------------------------------------------#
# # 5736. 单线程 CPU

# tasks = [[1,2],[2,4],[3,2],[4,1]]
# # tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
# # tasks = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]

# # 超时
# for ii in range(len(tasks)):
#     tasks[ii].append(ii)
# output = []
# time = 0
# while len(tasks) > 0:
#     tasks.sort(key=lambda x: (max(time,x[0]),x[1],x[2]))
#     temp = tasks.pop(0)
#     time = max(time,temp[0]) + temp[1]
#     output.append(temp[2])
# print(output)

# # 超时
# for ii in range(len(tasks)):
#     tasks[ii].append(ii)
# output = []
# time = 0
# while len(tasks) > 0:
#     tasks.sort()
#     temp = tasks.pop(0)
#     time = temp[0] + temp[1]
#     for ii in range(len(tasks)):
#         if tasks[ii][0] < time:
#            tasks[ii][0] = time
#     output.append(temp[2])
# print(output)
#-----------------------------------------------------------------------------#
# # 剑指 Offer 48. 最长不含重复字符的子字符串
# s = "abcabcbb"
# s = "pwwkew"

# dp = [0 for _ in range(len(s))]
# dp[0] = 1
# for ii in range(1,len(s)):
#     temp_set = set([s[ii]])
#     for jj in range(ii-1,-1,-1):
#         if s[jj] not in temp_set:
#             temp_set.add(s[jj])
#         else:
#             break
#     dp[ii] = len(temp_set)
# print(max(dp))
#-----------------------------------------------------------------------------#
# 剑指 Offer 57 - II. 和为s的连续正数序列
# target = 10000

# index = 2
# output = []
# while index < target:
#     temp = []
#     if index%2 == 0:
#         if target//index-index//2+1 > 0:
#             for ii in range(target//index-index//2+1,target//index-index//2+1+index):
#                 temp.append(ii)
#         else:
#             break
#     else:
#         if target//index-index//2 > 0:
#             for ii in range(target//index-index//2, target//index-index//2+index):
#                 temp.append(ii)
#         else:
#             break
#     if sum(temp) == target:
#         output = [temp] + output
#     index += 1
# print(output)

#-----------------------------------------------------------------------------#


# # 5731. 座位预约管理系统 # 堆排序，比list+sort()快
# class SeatManager(object):
#     def __init__(self, n):
#         """
#         :type n: int
#         """
#         import heapq
#         self.list1 = [ii+1 for ii in range(n)]
#         # heapq.heapify(self.list1)
#     def reserve(self):
#         """
#         :rtype: int
#         """
#         return heapq.heappop(self.list1)
#     def unreserve(self, seatNumber):
#         """
#         :type seatNumber: int
#         :rtype: None
#         """
#         heapq.heappush(self.list1, seatNumber)

# # 5733. 最近的房间
# # rooms = [[2,2],[1,2],[3,2]]
# # queries = [[3,1],[3,3],[5,2]]
# # rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]]
# # queries = [[2,3],[2,4],[2,5]]
# rooms = [[173,397],[281,320],[415,181],[497,269],[77,285],[321,104],[385,43],[391,351],[371,287],[107,305],[247,187],[430,240],[465,321],[481,215],[1,423],[304,465],[411,176],[474,253],[219,225],[433,443],[106,365],[94,261],[135,187],[401,117],[181,276],[201,137],[461,312],[35,421],[13,307],[489,375],[69,253],[9,186],[89,164],[145,217],[331,183],[326,281],[271,429],[454,466],[153,297],[177,321],[49,381],[156,126],[117,321],[75,220],[493,71],[445,231],[263,425],[178,146],[4,131],[324,159],[5,491],[381,441],[183,73],[380,487],[192,322],[405,141],[150,301],[91,346],[100,287],[197,425],[292,391],[357,89],[486,281],[203,201],[484,429],[289,264],[17,486],[157,447],[134,67],[6,425],[237,47],[71,359],[196,467],[267,25],[265,493],[417,116],[368,191],[233,242],[207,359],[167,193],[386,306],[211,201],[22,1],[36,101],[152,171],[33,315],[351,429],[492,313],[397,267],[341,197],[161,221],[198,349],[470,405],[473,308],[301,129],[224,285],[307,137],[165,371],[337,201],[151,445]]
# queries = [[469,153],[366,66],[295,235],[73,1],[185,263],[382,127],[137,154],[321,405],[431,245],[292,166],[253,205],[24,189],[106,433],[478,361],[385,399],[259,397],[325,265],[163,129],[431,361],[316,451],[271,261],[484,236],[316,442],[5,362],[209,236],[337,289],[1,279],[249,391],[51,337],[209,18],[277,177],[117,350],[189,181],[381,307],[29,313],[251,497],[1,325],[329,321],[68,215],[446,373],[181,393],[281,116],[183,301],[362,468],[193,109],[13,189],[454,181],[400,37],[87,128],[446,497],[147,97],[273,41],[349,202],[165,105],[173,220],[233,391],[84,426],[496,441],[151,57],[295,413],[110,175],[170,215],[133,119],[445,233],[27,444],[214,53],[477,303],[353,33],[231,243],[91,417],[78,483],[145,47],[181,37],[161,29],[141,446],[231,286],[101,137],[174,309],[437,421],[211,187],[256,363],[384,211],[1,111],[451,23],[95,151],[129,213],[327,196],[30,132],[61,149],[163,11],[243,133],[33,331],[343,211],[277,1],[282,93],[251,411],[15,259],[85,149],[1,157],[169,401]]

# # 超时
# rooms.sort(key=lambda x:x[1],reverse=True)
# output = []
# for ii in range(len(queries)):
#     distance = 10**8
#     index = -1
#     for jj in range(len(rooms)):
#         if rooms[jj][1] >= queries[ii][1]:
#             if abs(rooms[jj][0]-queries[ii][0]) < distance:
#                 distance = abs(rooms[jj][0]-queries[ii][0])
#                 index = rooms[jj][0]
#             elif abs(rooms[jj][0]-queries[ii][0]) == distance:
#                 index = min(rooms[jj][0],index)
#         else:
#             break
#     output.append(index)      

# 超时
# import bisect
# dict1 = {}
# for kk in range(len(rooms)):
#     if rooms[kk][1] not in dict1:
#         dict1[rooms[kk][1]] = [rooms[kk][0]]
#     else:
#         dict1[rooms[kk][1]].append(rooms[kk][0])

# output = []
# for ii in range(len(queries)):
#     temp_list = []
#     for key in dict1.keys():
#         if key >= queries[ii][1]:
#             temp_list += dict1[key]
#     temp_list.sort()
#     # temp2 = []
#     # for ll in range(len(rooms)):
#     #     if rooms[ll][1] >= queries[ii][1]:
#     #         temp2.append(rooms[ll][0])
#     # temp2.sort()
#     # if temp2 != temp_list:
#     #     print(ll)
#     if len(temp_list) > 0:
#         if queries[ii][0] <= temp_list[0]:
#             out = temp_list[0]
#         elif queries[ii][0] >= temp_list[-1]:
#             out = temp_list[-1]
#         else:
#             index_left = bisect.bisect_left(temp_list,queries[ii][0])
#             index_right = bisect.bisect_right(temp_list,queries[ii][0])
#             if index_left != index_right:
#                 out = temp_list[index_left]
#             else:
#                 if abs(temp_list[index_left]-queries[ii][0]) < abs(temp_list[index_left-1]-queries[ii][0]):
#                     out = temp_list[index_left]
#                 else:
#                     out = temp_list[index_left-1]
#         output.append(out)
#     else:
#         output.append(-1)



# #超时
# output = []
# rooms.sort()
# for ii in range(len(queries)):
#     temp = []
#     # for jj in range(len(rooms)):
#     #     if rooms[jj][1] >= queries[ii][1]:
#     #         temp.append(rooms[jj][0])
#     # print(temp)
#     label = False
#     for jj in range(len(rooms)):
#         if rooms[jj][1] >= queries[ii][1]:
#             if rooms[jj][0] < queries[ii][0]:
#                 temp.append(rooms[jj][0])
#             elif rooms[jj][0] == queries[ii][0]:
#                 temp.append(rooms[jj][0])
#                 break
#             else:
#                 temp.append(rooms[jj][0])
#                 label = True
#                 break
#     if label == False:
#         if len(temp) == 0:
#             output.append(-1)
#         else:
#             output.append(temp[-1])
#     else:
#         if len(temp) == 0:
#             output.append(-1)
#         elif len(temp) == 1:
#             output.append(temp[-1])
#         else:
#             if abs(temp[-2]-queries[ii][0]) <= abs(temp[-1]-queries[ii][0]):
#                 output.append(temp[-2])
#             else:
#                 output.append(temp[-1])
# print(output)

# # 检验
# aa = [470,368,292,71,181,381,135,304,433,292,263,17,151,484,381,263,326,161,433,304,271,484,304,5,207,351,1,263,49,207,281,106,192,381,33,-1,1,351,69,454,173,281,177,380,192,13,454,401,89,-1,145,271,351,165,173,263,17,454,151,304,107,173,135,454,17,211,473,351,224,35,17,145,181,161,157,207,100,173,433,211,263,386,1,454,94,117,326,33,69,161,247,35,351,281,281,263,13,89,1,157]
# print(output == aa)

# for ii in range(len(aa)):
#     if aa[ii] != output[ii]:
#         print(ii)


# 5748. 包含每个查询的最小区间
# intervals = [[1,4],[2,4],[3,6],[4,4]]
# queries = [2,3,4,5]
# intervals = [[2,3],[2,5],[1,8],[20,25]]
# queries = [2,19,5,22]

# for ii in range(len(intervals)):
#     intervals[ii] = [intervals[ii][1]-intervals[ii][0]+1] + intervals[ii]
# intervals.sort(key=lambda x:x[0])
# output = []
# for jj in range(len(queries)):
#     label = False
#     for ii in range(len(intervals)):
#         if intervals[ii][1] <= queries[jj] <= intervals[ii][2]:
#             output.append(intervals[ii][0])
#             label = True
#             break
#     if label == False:
#         output.append(-1)
# print(output)

# intervals = [[1,4],[2,4],[3,6],[4,4]]
# queries = [2,3,4,5]
# # intervals = [[2,3],[2,5],[1,8],[20,25]]
# # queries = [2,19,5,22]

# dict1 = {}
# for ii in range(len(intervals)):
#     for jj in range(intervals[ii][0],intervals[ii][1]+1):
#         if jj not in dict1:
#             dict1[jj] = intervals[ii][1]-intervals[ii][0]+1
#         else:
#             dict1[jj] = min(dict1[jj], intervals[ii][1]-intervals[ii][0]+1)
# output = []
# for jj in range(len(queries)):
#     if queries[jj] not in dict1:
#         output.append(-1)
#     else:
#         output.append(dict1[queries[jj]])
# print(output)

# # 超时
# output = []
# list_set = []
# for ii in range(len(intervals)):
#     list_set.append(set([ii for ii in range(intervals[ii][0],intervals[ii][1]+1)]))
# for num in queries:
#     min_len = 10**8
#     for ii in range(len(list_set)):
#         if num in list_set[ii]:
#             min_len = min(min_len, len(list_set[ii]))
#     if min_len < 10**8:
#         output.append(min_len)
#     else:
#         output.append(-1)
# print(output)

# # 超时
# output = [float('inf') for _ in range(len(queries))]
# for ii in range(len(intervals)):
#     for jj in range(len(queries)):
#         if intervals[ii][0] <= queries[jj] <= intervals[ii][1]:
#             output[jj] = min(output[jj], intervals[ii][1]-intervals[ii][0]+1)
# for jj in range(len(output)):
#     if output[jj] == float('inf'):
#         output[jj] = -1
# print(output)

# # 超时
# output = []
# for num in queries:
#     min_len = 10**8
#     for ii in range(len(intervals)):
#         if intervals[ii][0] <= num <= intervals[ii][1]:
#             min_len = min(min_len, intervals[ii][1]-intervals[ii][0]+1)
#     if min_len < 10**8:
#         output.append(min_len)
#     else:
#         output.append(-1)
# print(output)

# 5749. 邻位交换的最小次数 已完成
# num = "5489355142"
# k = 1
# # num = "11112"
# # k = 4
# # num = "00123"
# # k = 1
# # num = "059"
# # k=5
# # num = "19813"
# # k = 37

# import copy
# def next_permutation(nums):
#     label = False
#     for ii in range(len(nums)-2,-1,-1):
#         if nums[ii] < nums[ii+1]:
#             label = True
#             break
#     if label == True:
#         for jj in range(len(nums)-1,-1,-1):
#             if nums[jj] > nums[ii]:
#                 break
#         nums[ii], nums[jj] = nums[jj], nums[ii]
#         nums[ii+1:] = sorted(nums[ii+1:])
#     else:
#         nums.sort()
#     return nums

# nums_before = []
# for ss in num:
#     nums_before.append(int(ss))
#     nums_after = copy.deepcopy(nums_before)

# for _ in range(k):
#     nums_after = next_permutation(nums_after)

# print(nums_before,'\n',nums_after)

# #计算交换次数
# count = 0
# for ii in range(len(nums_after)):
#     if nums_after[ii] != nums_before[ii]: #找到变化前后第一个不同的位置，即ii
#         for jj in range(ii+1,len(nums_after)):
#             if nums_before[jj] == nums_after[ii]:
#                 break
#         count += jj-ii
#         # 使得变化前后第ii个位置变成相同的值
#         nums_before = nums_before[0:ii] + [nums_before[jj]] + nums_before[ii:jj] + nums_before[jj+1:]
# print(count)

# # 5763. 哪种连续子字符串更长
# s = "1101"
# s = "111000"
# s = "110100010"

# max0 = 0
# max1 = 0
# count0 = 0
# count1 = 0
# if s[0] == '0':
#     count0 += 1
# else:
#     count1 += 1
# for ii in range(1,len(s)):
#     if s[ii] != s[ii-1]:
#         max0 = max(max0,count0)
#         max1 = max(max1,count1)
#         count0 = 0
#         count1 = 0
#         if s[ii] == '0':
#             count0 += 1
#         else:
#             count1 += 1
#     else:
#         if s[ii] == '0':
#             count0 += 1
#         else:
#             count1 += 1
# max0 = max(max0,count0)
# max1 = max(max1,count1)
# print(max1 > max0)

# # 5764. 准时到达的列车最小时速
# dist = [1,3,2]
# hour = 6
# # dist = [1,3,2]
# # hour = 2.7
# dist = [1,3,2]
# hour = 1.9
# # dist = [1,1,100000]
# # hour = 2.01

# import math
# def check(speed):
#     count = 0
#     for ii in range(len(dist)-1):
#         count += math.ceil(float(dist[ii])/speed)
#     count += float(dist[-1])/speed
#     return count <= hour
# min_speed = math.ceil(sum(dist)/hour)
# max_speed = 10**10
# if check(max_speed):
#     while min_speed < max_speed:
#         if check(int((max_speed-min_speed)/2+min_speed)):
#             max_speed = int((min_speed+max_speed)/2)
#         else:
#             min_speed = int((min_speed+max_speed)/2)+1
#     print(int(min_speed), int(max_speed))
# else:
#     print(-1)

# # 5765. 跳跃游戏 VII
# s = "011010"
# minJump = 2
# maxJump = 3 # True
# # s = "01101110"
# # minJump = 2
# # maxJump = 3 # False
# # s = "000110"
# # minJump = 2
# # maxJump = 3 # True

# index_0 = [0]
# for ii in range(1,len(s)):
#     if s[ii] == '0':
#         label = False
#         cur_index = len(index_0)-1
#         while cur_index > -1:
#             if minJump <= ii - index_0[cur_index] <= maxJump:
#                 index_0.append(ii)
#                 label = True
#                 break
#             elif ii - index_0[cur_index] < minJump:
#                 label = True
#             cur_index -= 1
#         if label == False:
#             break
# print(index_0[-1] == len(s)-1)

# #超时
# dp = [False for _ in range(len(s))]
# dp[0] = True
# for ii in range(1,len(s)):
#     if s[ii] == '0':
#         index = ii - minJump
#         while index >= ii-maxJump and index >= 0:
#             if dp[index] == True:
#                 dp[ii] = True
#                 break
#             index -= 1
# print(dp[-1])


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











