"""
 * 给你一个目录信息列表 paths ，包括目录路径，以及该目录中的所有文件及其内容，请你按路径返回文件系统中的所有重复文件。答案可按 任意顺序 返回。
 * 一组重复的文件至少包括 两个 具有完全相同内容的文件。
 * 输入 列表中的单个目录信息字符串的格式如下：
 * "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
 * 这意味着，在目录 root/d1/d2/.../dm 下，有 n 个文件 ( f1.txt, f2.txt ... fn.txt ) 的内容分别是 ( f1_content, f2_content ... fn_content ) 。
 * 注意：n >= 1 且 m >= 0 。如果 m = 0 ，则表示该目录是根目录。
 * 输出 是由 重复文件路径组 构成的列表。其中每个组由所有具有相同内容文件的文件路径组成。文件路径是具有下列格式的字符串：
 * "directory_path/file_name.txt"
 * 提示：
 * 1、1 <= paths.length <= 2 * 10^4
 * 2、1 <= paths[i].length <= 3000
 * 3、1 <= sum(paths[i].length) <= 5 * 10^5
 * 4、paths[i] 由英文字母、数字、字符 '/'、'.'、'('、')' 和 ' ' 组成
 * 5、你可以假设在同一目录中没有任何文件或目录共享相同的名称。
 * 6、你可以假设每个给定的目录信息代表一个唯一的目录。目录路径和文件信息用单个空格分隔。
 * 进阶：
 * 1、假设您有一个真正的文件系统，您将如何搜索文件？广度搜索还是宽度搜索？
 * 2、如果文件内容非常大（GB级别），您将如何修改您的解决方案？
 * 3、如果每次只能读取 1 kb 的文件，您将如何修改解决方案？
 * 4、修改后的解决方案的时间复杂度是多少？其中最耗时的部分和消耗内存的部分是什么？如何优化？
 * 5、如何确保您发现的重复文件不是误报？
 * 链接：https://leetcode.cn/problems/find-duplicate-file-in-system/
"""

from typing import *
from collections import defaultdict


class Solution:

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for path in paths:
            data = path.split()
            p = data[0]
            for i in range(1, len(data)):
                idx = data[i].index('(')
                c = data[i][idx + 1:-1]
                dic[c].append(p + '/' + data[i][:idx])
        return [v for v in dic.values() if len(v) > 1]


if __name__ == '__main__':
    # [['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt']]
    print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
    # [['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt']]
    print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]))
