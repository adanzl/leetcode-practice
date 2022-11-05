"""
 * 给你两个字符串数组 creators 和 ids ，和一个整数数组 views ，所有数组的长度都是 n 。平台上第 i 个视频者是 creator[i] ，视频分配的 id 是 ids[i] ，且播放量为 views[i] 。
 * 视频创作者的 流行度 是该创作者的 所有 视频的播放量的 总和 。请找出流行度 最高 创作者以及该创作者播放量 最大 的视频的 id 。
 * 1、如果存在多个创作者流行度都最高，则需要找出所有符合条件的创作者。
 * 2、如果某个创作者存在多个播放量最高的视频，则只需要找出字典序最小的 id 。
 * 返回一个二维字符串数组 answer ，其中 answer[i] = [creatori, idi] 表示 creatori 的流行度 最高 且其最流行的视频 id 是 idi ，可以按任何顺序返回该结果。
 * 提示：
 * 1、n == creators.length == ids.length == views.length
 * 2、1 <= n <= 10^5
 * 3、1 <= creators[i].length, ids[i].length <= 5
 * 4、creators[i] 和 ids[i] 仅由小写英文字母组成
 * 5、0 <= views[i] <= 10^5
 * 链接：https://leetcode.cn/problems/most-popular-video-creator/
"""
from collections import Counter, defaultdict
from typing import List


class Solution:

    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

        c_dict = Counter()
        i_dict = defaultdict(list)
        for c, id, v in zip(creators, ids, views):
            c_dict[c] += v
            i_dict[c].append([v, id])  # 注意 此处相同id的视屏播放量不合并~~~~~
        ans = []
        m_c = c_dict.most_common(1)[0]
        mc_list = [k for k, v in c_dict.items() if v == m_c[1]]
        for mc in mc_list:
            id_lst = sorted([[k, v] for k, v in i_dict[mc]], key=lambda x: (-x[0], x[1]))
            ans.append([mc, id_lst[0][1]])
        return ans


if __name__ == '__main__':
    # [["alice","one"],["bob","two"]]
    print(Solution().mostPopularCreator(["alice", "bob", "alice", "chris"], ids=["one", "two", "three", "four"], views=[5, 10, 5, 4]))
    # [["alice","b"]]
    print(Solution().mostPopularCreator(["alice", "alice", "alice"], ids=["a", "b", "c"], views=[1, 2, 2]))
