"""
给定一个二叉树，找出其最大深度
二叉树的深度为根结点到最圆叶子节点的最长路径上的节点数

二叉树题目的递归解法可以分两类思路
    第一类是遍历一遍二叉树得出答案
    第二类是通过分解问题计算出答案
    这两类思路分别对应着 回溯算法核心框架 和 动态规划核心框架。


综上，遇到一道二叉树的题目时的通用思考过程是：
    1、是否可以通过遍历一遍二叉树得到答案？如果可以，用一个 traverse 函数配合外部变量来实现。
    2、是否可以定义一个递归函数，通过子问题（子树）的答案推导出原问题的答案？如果可以，
       写出这个递归函数的定义，并充分利用这个函数的返回值。
    3、无论使用哪一种思维模式，你都要明白二叉树的每一个节点需要做什么，需要在什么时候（前中后序）做。
"""

from binary_tree import TreeNode

res = 0
depth = 0


def max_depth_1(node):
    """
    这个解法应该很好理解，但为什么需要在前序位置增加 depth，在后序位置减小 depth？
    因为前面说了，前序位置是进入一个节点的时候，后序位置是离开一个节点的时候，depth 记录当前递归到的节点深度，
    你把 traverse 理解成在二叉树上游走的一个指针，所以当然要这样维护。
    至于对 res 的更新，你放到前中后序位置都可以，只要保证在进入节点之后，离开节点之前（即 depth 自增之后，自减之前）就行了
    """
    traverse(node)
    return res


def traverse(node):
    global res
    global depth
    if node is None:
        return
    # 前序位置
    depth += 1
    if node.left is None and node.right is None:
        # 到达叶子节点，到达最大深度
        res = max(res, depth)

    traverse(node.left)
    traverse(node.right)
    # 后序位置
    depth -= 1


def max_depth(node):
    """
    只要明确递归函数的定义，这个解法也不难理解，但为什么主要的代码逻辑集中在后序位置？
    因为这个思路正确的核心在于，你确实可以通过子树的最大深度推导出原树的深度，
    所以当然要首先利用递归函数的定义算出左右子树的最大深度，然后推出原树的最大深度，主要逻辑自然放在后序位置。
    """
    if node is None:
        return 0
    left_max = max_depth(node.left)
    right_max = max_depth(node.right)
    return max(left_max, right_max) + 1


