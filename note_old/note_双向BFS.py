# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 19:04:43 2021

@author: CC-i7-8750H
"""
# 双向广度优先
# # 126. 单词接龙 II
# # 127. 单词接龙
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

beginWord = "cat"
endWord = "fin"
wordList = ["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"]

# 双向BFS改进，基于待访问的顶点集合 往下层遍历，并记录边，最后对记录的边集合进行DFS遍历生成所有可行路径
def bfs_next(word):
    #查询下一层单词
    set1 = set()
    for mm in range(len(word)):
        for nn in range(26):
            temp = word[0:mm] + chr(97+nn)+ word[mm+1:]
            #如果新生成的单词 不在已访问的顶点集合中并且在wordList中，即待访问的顶点集合，则找到下一个连通的顶点
            if temp not in set_visited and temp in set_word:
                set1.add(temp)
    return set1
def dfs(set_path, record_set):
    #深度优先遍历所有可行路径
    #如果记录中的最后一个单词与endWord相同，则终止
    if record_set[-1] == endWord:
        output.append(record_set)
    else:
        for word in set_path[record_set[-1]]:
            # 如果当前单词在可行边集合之中，或者endWord相同，则继续往下寻找
            if word in set_path or word == endWord:
                dfs(set_path, record_set+[word])
set_word = set(wordList)
if endWord in set_word:
    set_start = set([beginWord]) #用于记录左侧待访问的顶点
    set_end = set([endWord]) #用于记录右侧待访问的顶点
    set_visited = set() #用于记录已访问过的顶点
    set_path = {}                                   #记录路径（连通的路）
    # count = 0                                       #计数
    while len(set_start) > 0 and len(set_end) > 0 and len(set.intersection(set_start,set_end)) == 0:
        #选择待访问顶点数量少的一侧开始广度优先遍历
        if len(set_start) <= len(set_end):
            #将待访问的顶点 增加至已访问过的顶点集合
            set_visited.update(set_start)
            #用于记录新的待访问顶点
            set_temp = set()
            while len(set_start) > 0:
                #从待访问的顶点集合中随机选择一个
                cur = set_start.pop()
                #生成新的待访问顶点
                next_words = bfs_next(cur)
                set_temp.update(next_words)
                set_path[cur] = list(next_words)    #记录路径 当前顶点：[与其连通的待访问顶点]
            #新的待访问顶点集合替换 原先的待访问顶点集合
            set_start = set_temp
            # count += 1                              #计数
        else:
            set_visited.update(set_end)
            set_temp = set()
            while len(set_end) > 0:
                cur = set_end.pop()
                next_words = bfs_next(cur)
                set_temp.update(next_words)
                for word in list(next_words):       #记录路径
                    if word not in set_path:        #记录路径
                        set_path[word] = [cur]      #记录路径
                    else:                           #记录路径
                        set_path[word].append(cur)  #记录路径
            set_end = set_temp
            # count += 1                              #计数
    # 如果set_start和set_end都不为空，说明找到公共顶点
    if len(set_start) > 0 and len(set_end) > 0:
        # print(count+1)                              #计数
        output = []                                 #查找路径
        dfs(set_path, [beginWord])                  #查找路径
        print(output)                               #查找路径
    else: #set_start或set_end为空，说明不是连通图
        print(0)
else:
    print(0)

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

#-----------------------------------------------------------------------------#
# # 815. 公交路线
# routes = [[1,2,7],[3,6,7]]
# # routes = [[1,2,6],[3,6,7]]
# source = 1
# target = 6
# # routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
# # source = 15
# # target = 12
# # routes = [[10,13,22,28,32,35,43],[2,11,15,25,27],[6,13,18,25,42],[5,6,20,27,37,47],[7,11,19,23,35],[7,11,17,25,31,43,46,48],[1,4,10,16,25,26,46],[7,11],[3,9,19,20,21,24,32,45,46,49],[11,41]]
# # source = 37
# # target = 43

# # 双向广度优先算法
# if source == target:
#     print(0)
# else:
#     set_start = set([source])
#     set_end = set([target])
#     count_start = 0
#     count_end = 0
#     label_start = True
#     label_end = True
#     while len(set.intersection(set_start, set_end)) == 0 and (label_start or label_end):
#         cur_start = set()
#         label_start = False
#         for ii in range(len(routes)-1,-1,-1):
#             if len(set.intersection(set_start, set(routes[ii]))):
#                 cur_start.update(routes[ii])
#                 label_start = True
#                 del(routes[ii])
#         if label_start == True:
#             count_start += 1
#             set_start = cur_start
#         # print(set_start,count_start,label_start, routes)

#         if len(set.intersection(set_start, set_end)) == 0: # 注意：在从终点开始广度优先搜索之前需要增加一个判断
#             cur_end = set()
#             label_end = False
#             for ii in range(len(routes)-1,-1,-1):
#                 if len(set.intersection(set_end, set(routes[ii]))):
#                     cur_end.update(routes[ii])
#                     label_end = True
#                     del(routes[ii])
#             if label_end == True:
#                 count_end += 1
#                 set_end = cur_end
#             # print(set_end,count_end,label_end, routes)

#     if len(set.intersection(set_start, set_end)) > 0: 
#         print(count_start+count_end)
#     else:
#         print(-1)   