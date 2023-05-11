"""
 * 探险家小扣的行动轨迹，都将保存在记录仪中。expeditions[i] 表示小扣第 i 次探险记录，用一个字符串数组表示。
 * 其中的每个「营地」由大小写字母组成，通过子串 -> 连接。
 * 例："Leet->code->Campsite"，表示到访了 "Leet"、"code"、"Campsite" 三个营地。
 * expeditions[0] 包含了初始小扣已知的所有营地；对于之后的第 i 次探险(即 expeditions[i] 且 i > 0)，如果记录中包含了之前均没出现的营地，则表示小扣 新发现 的营地。
 * 请你找出小扣发现新营地最多且索引最小的那次探险，并返回对应的记录索引。如果所有探险记录都没有发现新的营地，返回 -1
 * 注意：
 * 1、大小写不同的营地视为不同的营地
 * 2、营地的名称长度均大于 0。
 * 提示：
 * 1、1 <= expeditions.length <= 1000
 * 2、0 <= expeditions[i].length <= 1000
 * 3、探险记录中只包含大小写字母和子串"->"
 * 链接：https://leetcode.cn/problems/0Zeoeg/
"""
from typing import List


class Solution:

    def adventureCamp(self, expeditions: List[str]) -> int:
        mx_score, mx_idx = 0, -1
        vis = set(expeditions[0].split('->'))
        for i in range(1, len(expeditions)):
            score = 0
            for camp in expeditions[i].split('->'):
                if camp and camp not in vis:
                    score += 1
                    vis.add(camp)
            if score > mx_score:
                mx_score, mx_idx = score, i
        return mx_idx


if __name__ == '__main__':
    # -1
    print(Solution().adventureCamp(["Alice->Dex", "", "Dex"]))
    # 1
    print(Solution().adventureCamp(["leet->code", "leet->code->Campsite->Leet", "leet->code->leet->courier"]))
    # 2
    print(Solution().adventureCamp(["", "Gryffindor->Slytherin->Gryffindor", "Hogwarts->Hufflepuff->Ravenclaw"]))
