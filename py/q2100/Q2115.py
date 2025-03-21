"""
 * 你有 n 道不同菜的信息。给你一个字符串数组 recipes 和一个二维字符串数组 ingredients 。
 * 第 i 道菜的名字为 recipes[i] ，如果你有它 所有 的原材料 ingredients[i] ，那么你可以 做出 这道菜。
 * 一份食谱也可以是 其它 食谱的原料，也就是说 ingredients[i] 可能包含 recipes 中另一个字符串。
 * 同时给你一个字符串数组 supplies ，它包含你初始时拥有的所有原材料，每一种原材料你都有无限多。
 * 请你返回你可以做出的所有菜。你可以以 任意顺序 返回它们。
 * 注意两道菜在它们的原材料中可能互相包含。
 * 提示：
 * 1、n == recipes.length == ingredients.length
 * 2、1 <= n <= 100
 * 3、1 <= ingredients[i].length, supplies.length <= 100
 * 4、1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
 * 5、recipes[i], ingredients[i][j] 和 supplies[k] 只包含小写英文字母。
 * 6、所有 recipes 和 supplies 中的值互不相同。
 * 7、ingredients[i] 中的字符串互不相同。
 * 链接：https://leetcode.cn/problems/find-all-possible-recipes-from-given-supplies
"""
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify, heapreplace, heappushpop, nlargest, nsmallest
from itertools import zip_longest, product, chain, combinations, combinations_with_replacement, permutations, \
    accumulate, pairwise, count, cycle, repeat, groupby
from functools import reduce, cmp_to_key, cache
from operator import or_, iconcat, and_, xor, mul
from math import inf, gcd, lcm, comb, factorial, isqrt, log2
from typing import List
#
# @lc app=leetcode.cn id=2115 lang=python3
# @lcpr version=30104
#
# [2115] 从给定原材料中找到所有可以做出的菜
#

INF = 0x3c3c3c3c3c3c3c3c3c


# @lc code=start
class Solution:

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []
        # 拓扑
        s_re = set(recipes)
        dep = {}  # k-依赖set
        make_set = defaultdict(set)  # k-可以制作的set 

        # 拓扑
        for r, ing in zip(recipes, ingredients):
            dep[r] = set(ing)
            for ii in ing:
                make_set[ii].add(r)
        q = deque(supplies)
        while q:
            cur = q.popleft()
            for mk in make_set[cur]:
                dep[mk].remove(cur)
                if len(dep[mk]) == 0:
                    q.append(mk)
                    if mk in s_re:
                        ans.append(mk)

        return ans


# @lc code=end

if __name__ == '__main__':
    # ["bread"]
    print(Solution().findAllRecipes(["bread"], ingredients=[["yeast", "flour"]], supplies=["yeast", "flour", "corn"]))
    # ["bread","sandwich"]
    print(Solution().findAllRecipes(["bread", "sandwich"],
                                    ingredients=[["yeast", "flour"], ["bread", "meat"]],
                                    supplies=["yeast", "flour", "meat"]))
    # ["bread","sandwich","burger"]
    print(Solution().findAllRecipes(["bread", "sandwich", "burger"],
                                    ingredients=[["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
                                    supplies=["yeast", "flour", "meat"]))
    # []
    print(Solution().findAllRecipes(["bread"], ingredients=[["yeast", "flour"]], supplies=["yeast"]))


