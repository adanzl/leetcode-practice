"""
 * 给你一个字符串化学式 formula ，返回 每种原子的数量 。
 * 原子总是以一个大写字母开始，接着跟随 0 个或任意个小写字母，表示原子的名字。
 * 如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。
 *  例如，"H2O" 和 "H2O2" 是可行的，但 "H1O2" 这个表达是不可行的。
 * 两个化学式连在一起可以构成新的化学式。
 *  例如 "H2O2He3Mg4" 也是化学式。
 * 由括号括起的化学式并佐以数字（可选择性添加）也是化学式。
 *  例如 "(H2O2)" 和 "(H2O2)3" 是化学式。
 * 返回所有原子的数量，格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），
 * 然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。
 * 提示：
 * 1、1 <= formula.length <= 1000
 * 2、formula 由英文字母、数字、'(' 和 ')' 组成
 * 3、formula 总是有效的化学式
 * 链接：https://leetcode.cn/problems/number-of-atoms/
"""

#
# @lc app=leetcode.cn id=726 lang=python3
#
# [726] 原子的数量
#


# @lc code=start
class Solution:

    def countOfAtoms(self, formula: str) -> str:

        def dfs(formula, idx):
            wd = {}
            while idx < len(formula):
                if formula[idx] == '(':
                    sub_wd, idx = dfs(formula, idx + 1)
                    for k, v in sub_wd.items():
                        wd[k] = wd.get(k, 0) + v
                elif formula[idx] == ')':
                    idx += 1
                    c = 0
                    while idx < len(formula) and formula[idx].isdigit():
                        c = c * 10 + int(formula[idx])
                        idx += 1
                    c = max(c, 1)
                    for k, v in wd.items():
                        wd[k] = v * c
                    break
                else:
                    s = idx
                    idx += 1
                    while idx < len(formula) and formula[idx].islower():
                        idx += 1
                    k = formula[s:idx]
                    c = 0
                    while idx < len(formula) and formula[idx].isdigit():
                        c = c * 10 + int(formula[idx])
                        idx += 1
                    c = max(c, 1)
                    wd[k] = wd.get(k, 0) + c
            return wd, idx

        wd, _ = dfs(formula, 0)
        return ''.join([k + (str(v) if v > 1 else '') for k, v in sorted(wd.items(), key=lambda x: x[0])])


# @lc code=end

if __name__ == '__main__':
    # "H2O"
    print(Solution().countOfAtoms("H2O"))
    # "H2MgO2"
    print(Solution().countOfAtoms("Mg(OH)2"))
    # "K4N2O14S4"
    print(Solution().countOfAtoms("K4(ON(SO3)2)2"))