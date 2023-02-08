"""
 * 你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。
 * 如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的 子文件夹 。
 * 文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：'/' 后跟一个或者多个小写英文字母。
 * 例如，"/leetcode" 和 "/leetcode/problems" 都是有效的路径，而空字符串和 "/" 不是。
 * 提示：
 * 1、1 <= folder.length <= 4 * 10^4
 * 2、2 <= folder[i].length <= 100
 * 3、folder[i] 只包含小写字母和 '/'
 * 4、folder[i] 总是以字符 '/' 起始
 * 5、每个文件夹名都是 唯一 的
 * 链接：https://leetcode.cn/problems/remove-sub-folders-from-the-filesystem/
"""
from typing import List


class Solution:

    def removeSubFolders(self, folder: List[str]) -> List[str]:
        ans = []
        for f in sorted(folder):
            if not ans or not f.startswith(ans[-1] + '/'):
                ans.append(f)
        return ans


if __name__ == '__main__':
    # ["/a","/c/d","/c/f"]
    print(Solution().removeSubFolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
    # ["/a"]
    print(Solution().removeSubFolders(["/a", "/a/b/c", "/a/b/d"]))
    # ["/a/b/c","/a/b/ca","/a/b/d"]
    print(Solution().removeSubFolders(["/a/b/c", "/a/b/ca", "/a/b/d"]))
