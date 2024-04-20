# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 21:25:45 2021

@author: CC-i7-8750H
"""

# # question 56 合并区间
# intervals = [[2,6],[1,3],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals =[[1,4],[0,2],[3,5]]
intervals =[[1,4]]

intervals.sort()
output = [intervals[0]]
if len(intervals) > 1:
    for ii in range(1,len(intervals)):
        if output[-1][1] < intervals[ii][0]:
            output.append(intervals[ii])
        else:
            output[-1][1] = max(output[-1][1],intervals[ii][1])
print(output)
