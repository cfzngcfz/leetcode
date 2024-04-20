# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 20:30:02 2021

@author: CC-i7-8750H
"""

# 二叉�?
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
root = TreeNode(1,2,3)
root.left = TreeNode(2,4,5)
root.right = TreeNode(3,6,7)
root.left.left = TreeNode(4,8,9)
root.left.right = TreeNode(5,10,11)
root.right.left = TreeNode(6,12,13)
root.right.right = TreeNode(7,14,15)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)

# 前序遍历
temp = []
def dfs(root):
    if not root:
        return
    temp.append(root.val)
    dfs(root.left)
    dfs(root.right)
dfs(root)
print(temp)

# 中序遍历
temp = []
def dfs(root):
    if not root:
        return
    dfs(root.left)
    temp.append(root.val)
    dfs(root.right)
dfs(root)
print(temp)

# 后序遍历
temp = []
def dfs(root):
    if not root:
        return
    dfs(root.left)
    dfs(root.right)
    temp.append(root.val)
dfs(root)
print(temp)

# 层序遍历 - 广度优先
#写法1
output = []
record = [root]
while len(record) > 0:
    temp_val = []
    for _ in range(len(record)):
        cur_node = record.pop(0)
        if cur_node:
            temp_val.append(cur_node.val)
            record.append(cur_node.left)
            record.append(cur_node.right)
        else:
            temp_val.append(None)
    output.append(temp_val)
print(output[0:-1])
#写法2
output = []
record = [root]
layer = 0
while len(record) > 0:
    if len(output) == layer:
        output.append([])
    temp_record = []
    for ii in range(len(record)):
        if record[ii]:
            output[layer].append(record[ii].val)
            temp_record.append(record[ii].left)
            temp_record.append(record[ii].right)
        else:
            output[layer].append(None)
    record = temp_record
    layer += 1
print(output[0:-1])


# 层序遍历 - 深度优先
output = []
def dfs(root, layer):
    if len(output) == layer:
        output.append([])
    if not root:
        # output[layer].append(None)
        return 
    else:
        output[layer].append(root.val)
        dfs(root.left, layer+1)
        dfs(root.right, layer+1)
dfs(root, 0)
print(output[0:-1])

# # 最大深�?
# def maxDepth(root):
#     if not root:
#         return 0
#     else:
#         return max(maxDepth(root.left), maxDepth(root.right)) + 1
# maxDepth(root)
#-----------------------------------------------------------------------------#
# # 95. 不同的二叉搜索树 II
# n = 3

"""
迭代模板三：未研究透彻
def build_Trees(list1):
    if len(list1) == 0:
        return [None]
    all_trees = []
    for ii in range(len(list1)):
        left_trees = build_Trees(list1[0:ii])
        right_trees = build_Trees(list1[ii+1:])
        for l in left_trees:
            for r in right_trees:
                cur_tree = TreeNode(list1[ii])
                cur_tree.left = l
                cur_tree.right = r
                all_trees.append(cur_tree)
    return all_trees
"""
# record = build_Trees([ii+1 for ii in range(n)])
# print(record)

# # 96. 不同的二叉搜索树
# n=4

# #用动态规划模�?95题的生成过程
# dp = [1,1]
# for ii in range(2,n+1):
#     count = 0
#     for jj in range(len(dp)):
#         count += dp[jj]*dp[len(dp)-jj-1] #左子树的种类*右子树的种类
#     dp.append(count)
# print(dp[n])
#-----------------------------------------------------------------------------#
# # question 98 验证二叉搜索�? 已完�?
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
#-----------------------------------------------------------------------------#
# # 99. 恢复二叉搜索�?
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(2)

# root = TreeNode(1)
# root.left = TreeNode(3)
# root.left.right = TreeNode(2)

# #方法一：如果节点的值均不同的情�?
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
# # question 100 相同的树 已完�?
# p = TreeNode(1)
# p.left = TreeNode(2)
# p.right = TreeNode(3)
# q = TreeNode(1)
# q.left = TreeNode(2)
# q.right = TreeNode(2)

# # 方法一:动态规�?
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
#-----------------------------------------------------------------------------#
# # question 105 从前序与中序遍历序列构造二叉树 已完�?
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]

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
# # 108. 将有序数组转换为二叉搜索�?
# nums = [-10,-3,0,5,9]
"""
迭代模板�?
def backtrack(list1):
    if len(list1) == 0:
        return
    else:
        root = TreeNode(list1[len(list1)//2])
        root.left = backtrack(list1[0:len(list1)//2])
        root.right = backtrack(list1[len(list1)//2+1:])
    return root
"""
# root = backtrack(nums)
#-----------------------------------------------------------------------------#
# # 110. 平衡二叉�?
# # root = TreeNode(3)
# # root.left = TreeNode(9)
# # root.right = TreeNode(20)
# # root.right.left = TreeNode(15)
# # root.right.right = TreeNode(7)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.left.left.right = TreeNode(4)

# # root = None

# # 官方
# def isBalanced(self, root):
#     def maxDepth(root):
#         if not root:
#             return 0
#         else:
#             return max(maxDepth(root.left), maxDepth(root.right)) + 1
#     if not root:
#         return True
#     else:        
#         return abs(maxDepth(root.left)-maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# # 方法一：自上到�?
# def maxDepth(root):
#     if not root:
#         return 0
#     else:
#         return max(maxDepth(root.left), maxDepth(root.right)) + 1

# label = True
# record = [root]
# while len(record) > 0:
#     for _ in range(len(record)):
#         cur_node = record.pop(0)
#         if cur_node:
#             if abs(maxDepth(cur_node.left)-maxDepth(cur_node.right)) <= 1:
#                 record.append(cur_node.left)
#                 record.append(cur_node.right)
#             else:
#                 label = False
#                 break
#     if label == False:
#         break
# print(label)

# # 110. 平衡二叉�?
# # root = TreeNode(3)
# # root.left = TreeNode(9)
# # root.right = TreeNode(20)
# # root.right.left = TreeNode(15)
# # root.right.right = TreeNode(7)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.left.left.right = TreeNode(4)

# # root = None

# # 官方
# def isBalanced(self, root):
#     """
#     :type root: TreeNode
#     :rtype: bool
#     """
#     def maxDepth(root):
#         if not root:
#             return 0
#         else:
#             return max(maxDepth(root.left), maxDepth(root.right)) + 1
#     if not root:
#         return True
#     else:        
#         return abs(maxDepth(root.left)-maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# # 方法一：自上到�?
# def maxDepth(root):
#     if not root:
#         return 0
#     else:
#         return max(maxDepth(root.left), maxDepth(root.right)) + 1

# label = True
# record = [root]
# while len(record) > 0:
#     for _ in range(len(record)):
#         cur_node = record.pop(0)
#         if cur_node:
#             if abs(maxDepth(cur_node.left)-maxDepth(cur_node.right)) <= 1:
#                 record.append(cur_node.left)
#                 record.append(cur_node.right)
#             else:
#                 label = False
#                 break
#     if label == False:
#         break
# print(label)
#-----------------------------------------------------------------------------#
# # 111. 二叉树的最小深�?
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
#-----------------------------------------------------------------------------#
# # 112. 路径总和
# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(8)
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.right.right.left = TreeNode(5)
# root.right.right.right = TreeNode(1)
# targetSum = 22

# 方法一：层序遍�? - 深度优先
"""
output = []
def dfs(root, count):
    if not root:
        return
    else:
        if root.left == None and root.right == None:
            output.append(count+root.val)
        else:
            dfs(root.left, count+root.val)
            dfs(root.right, count+root.val)
dfs(root, 0)
"""
# print(targetSum in output)

# # 113. 路径总和 II

# # 方法一：层序遍�? - 深度优先
# output = []
# def dfs(root, list1):
#     if not root:
#         return
#     else:
#         if root.left == None and root.right == None:
#             if targetSum == sum(list1+[root.val]):
#                 output.append(list1+[root.val])
#         else:
#             dfs(root.left, list1+[root.val])
#             dfs(root.right, list1+[root.val])
# dfs(root, [])
# print(output)

# 129. 求根节点到叶节点数字之和
#-----------------------------------------------------------------------------#
# # 114. 二叉树展开为链�?
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
#-----------------------------------------------------------------------------#
# # 116. 填充每个节点的下一个右侧节点指�?
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

# #方法一：层序遍�?
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
# # 1600. 皇位继承顺序
# # 多叉�?-前序遍历
# dict1 = {}
# input1 = [["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"]]
# for ii in range(len(input1)):
#     if input1[ii][0] not in dict1:
#         dict1[input1[ii][0]] = [input1[ii][1]]
#     else:
#         dict1[input1[ii][0]].append(input1[ii][1])

# # 前序遍历
# temp = ["king"]
# def backtrack(node):
#     if node not in dict1:
#         return
#     else:
#         for ii in range(len(dict1[node])):
#             temp.append(dict1[node][ii])
#             backtrack(dict1[node][ii])

# backtrack("king")
# print(temp)



