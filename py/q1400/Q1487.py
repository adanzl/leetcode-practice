"""
 * 给你一个长度为 n 的字符串数组 names 。你将会在文件系统中创建 n 个文件夹：在第 i 分钟，新建名为 names[i] 的文件夹。
 * 由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 (k) 的形式为新文件夹的文件名添加后缀，其中 k 是能保证文件名唯一的 最小正整数 。
 * 返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的实际名称。
 * 提示：
 * 1、1 <= names.length <= 5 * 10^4
 * 2、1 <= names[i].length <= 20
 * 3、names[i] 由小写英文字母、数字和/或圆括号组成。
 * 链接：https://leetcode.cn/problems/making-file-names-unique/
"""
from collections import Counter
from typing import List


class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        index = {}
        for name in names:
            if name not in index:
                ans.append(name)
                index[name] = 1
            else:
                k = index[name]
                while name + '(' + str(k) + ')' in index:
                    k += 1
                t = name + '(' + str(k) + ')'
                ans.append(t)
                index[name] = k + 1
                index[t] = 1
        return ans


if __name__ == '__main__':
    # ["pes","fifa","gta","pes(2019)"]
    print(Solution().getFolderNames(["pes", "fifa", "gta", "pes(2019)"]))
    # ["gta","gta(1)","gta(2)","avalon"]
    print(Solution().getFolderNames(["gta", "gta(1)", "gta", "avalon"]))
    # ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
    print(Solution().getFolderNames(["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]))
    # ["wano","wano(1)","wano(2)","wano(3)"]
    print(Solution().getFolderNames(["wano", "wano", "wano", "wano"]))
    # ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
    print(Solution().getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)"]))
