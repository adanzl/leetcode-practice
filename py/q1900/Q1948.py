"""
 * 由于一个漏洞，文件系统中存在许多重复文件夹。
 * 给你一个二维数组 paths，其中 paths[i] 是一个表示文件系统中第 i 个文件夹的绝对路径的数组。
 * 例如，["one", "two", "three"] 表示路径 "/one/two/three" 。
 * 如果两个文件夹（不需要在同一层级）包含 非空且相同的 子文件夹 集合 并具有相同的子文件夹结构，则认为这两个文件夹是相同文件夹。
 * 相同文件夹的根层级 不 需要相同。如果存在两个（或两个以上）相同 文件夹，则需要将这些文件夹和所有它们的子文件夹 标记 为待删除。
 * 1、例如，下面文件结构中的文件夹 "/a" 和 "/b" 相同。它们（以及它们的子文件夹）应该被 全部 标记为待删除：
 *      /a
 *      /a/x
 *      /a/x/y
 *      /a/z
 *      /b
 *      /b/x
 *      /b/x/y
 *      /b/z
 * 2、然而，如果文件结构中还包含路径 "/b/w" ，那么文件夹 "/a" 和 "/b" 就不相同。
 *     注意，即便添加了新的文件夹 "/b/w" ，仍然认为 "/a/x" 和 "/b/x" 相同。
 * 一旦所有的相同文件夹和它们的子文件夹都被标记为待删除，文件系统将会 删除 所有上述文件夹。
 * 文件系统只会执行一次删除操作。执行完这一次删除操作后，不会删除新出现的相同文件夹。
 * 返回二维数组 ans ，该数组包含删除所有标记文件夹之后剩余文件夹的路径。路径可以按 任意顺序 返回。
 * 提示：
 * 1、1 <= paths.length <= 2 * 10^4
 * 2、1 <= paths[i].length <= 500
 * 3、1 <= paths[i][j].length <= 10
 * 4、1 <= sum(paths[i][j].length) <= 2 * 10^5
 * 5、path[i][j] 由小写英文字母组成
 * 6、不会存在两个路径都指向同一个文件夹的情况
 * 7、对于不在根层级的任意文件夹，其父文件夹也会包含在输入中
 * 链接：https://leetcode.cn/problems/delete-duplicate-folders-in-system/
"""

from collections import defaultdict
from typing import List

#
# @lc app=leetcode.cn id=1948 lang=python3
#
# [1948] 删除系统中的重复文件夹
#


# @lc code=start
class Solution:

    class Node:

        def __init__(self, val) -> None:
            self.layer = 0
            self.children = {}
            self.val = val
            self.sub = []
            self.sub_str = ''
            self.valid = True

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:

        root = Solution.Node("")
        for path in paths:
            cur = root
            for i, p in enumerate(path):
                if p not in cur.children:
                    cur.children[p] = Solution.Node(p)
                cur = cur.children[p]
                cur.layer = min(cur.layer, i - len(path))
        path_dic = defaultdict(set)

        def dfs(node):
            ss = []
            for child in node.children.values():
                dfs(child)
                ss.append(child.val + '_' + str(child.layer) + child.sub_str)
            node.sub = sorted(ss)
            node.sub_str = "".join(node.sub)
            path_dic[node.sub_str].add(node)

        dfs(root)
        for k, v in path_dic.items():
            if k == '': continue
            if len(v) > 1:
                for p in v:
                    p.valid = False
        ans = []

        def build_ans(node, path):
            if not node.valid:
                return
            if node.val != '':
                pp = path + [node.val]
                ans.append(pp)
            else:
                pp = path
            for sub in node.children.values():
                build_ans(sub, pp)

        build_ans(root, [])
        return ans


# @lc code=end

if __name__ == '__main__':
    #
    print(Solution().deleteDuplicateFolder([["e"], ["e", "e"], ["c"], ["c", "a"], ["c", "a", "e"], ["c", "a", "e", "b"],
                                            ["d"], ["d", "d"], ["d", "d", "c"], ["d", "d", "e"], ["d", "d", "e", "e"],
                                            ["d", "b"], ["d", "b", "a"], ["d", "b", "a", "e"],
                                            ["d", "b", "a", "e", "c"], ["d", "b", "a", "e", "e"], ["d", "b", "b"],
                                            ["d", "b", "c"], ["a"], ["b"]]))
    #
    print(Solution().deleteDuplicateFolder([["a"], ["a", "c"], ["a", "d"], ["a", "d", "e"], ["b"], ["b", "e"],
                                            ["b", "c"], ["b", "c", "d"], ["f"], ["f", "h"], ["f", "h", "i"], ["f", "j"],
                                            ["g"], ["g", "j"], ["g", "h"], ["g", "h", "i"]]))
    # [["b"],["f"],["l"],["c"],["h"],["f","r"],["f","o"],["l","q"],["h","t"],["f","r","g"],["f","o","l"],["f","r","g","c"],["f","r","g","c","r"]]
    print(Solution().deleteDuplicateFolder([["b"], ["f"], ["f", "r"], ["f", "r", "g"], ["f", "r", "g", "c"],
                                            ["f", "r", "g", "c", "r"], ["f", "o"], ["f", "o", "x"],
                                            ["f", "o", "x", "t"], ["f", "o", "x", "d"], ["f", "o", "l"], ["l"],
                                            ["l", "q"], ["c"], ["h"], ["h", "t"], ["h", "o"], ["h", "o", "d"],
                                            ["h", "o", "t"]]))
    # [["d"],["d","a"]]
    print(Solution().deleteDuplicateFolder([["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]))
    # [["c"],["c","b"],["a"],["a","b"]]
    print(Solution().deleteDuplicateFolder([["a"], ["c"], ["a", "b"], ["c", "b"], ["a", "b", "x"], ["a", "b", "x", "y"],
                                            ["w"], ["w", "y"]]))
    # [["c"],["c","d"],["a"],["a","b"]]
    print(Solution().deleteDuplicateFolder([["a", "b"], ["c", "d"], ["c"], ["a"]]))
    # []
    print(Solution().deleteDuplicateFolder([["a"], ["a", "x"], ["a", "x", "y"], ["a", "z"], ["b"], ["b", "x"],
                                            ["b", "x", "y"], ["b", "z"]]))
    # [["b"],["b","w"],["b","z"],["a"],["a","z"]]
    print(Solution().deleteDuplicateFolder([["a"], ["a", "x"], ["a", "x", "y"], ["a", "z"], ["b"], ["b", "x"],
                                            ["b", "x", "y"], ["b", "z"], ["b", "w"]]))
