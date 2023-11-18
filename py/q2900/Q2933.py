"""
 * 给你一个长度为 n 、下标从 0 开始的二维字符串数组 access_times 。
 * 对于每个 i（0 <= i <= n - 1 ），access_times[i][0] 表示某位员工的姓名，access_times[i][1] 表示该员工的访问时间。
 * access_times 中的所有条目都发生在同一天内。
 * 访问时间用 四位 数字表示， 符合 24 小时制 ，例如 "0800" 或 "2250" 。
 * 如果员工在 同一小时内 访问系统 三次或更多 ，则称其为 高访问 员工。
 * 时间间隔正好相差一小时的时间 不 被视为同一小时内。例如，"0815" 和 "0915" 不属于同一小时内。
 * 一天开始和结束时的访问时间不被计算为同一小时内。例如，"0005" 和 "2350" 不属于同一小时内。
 * 以列表形式，按任意顺序，返回所有 高访问 员工的姓名。
 * 提示：
 * 1、1 <= access_times.length <= 100
 * 2、access_times[i].length == 2
 * 3、1 <= access_times[i][0].length <= 10
 * 4、access_times[i][0] 仅由小写英文字母组成。
 * 5、access_times[i][1].length == 4
 * 6、access_times[i][1] 采用24小时制表示时间。
 * 7、access_times[i][1] 仅由数字 '0' 到 '9' 组成。
 * 链接：https://leetcode.cn/problems/high-access-employees/
"""
import bisect
from collections import defaultdict
from typing import List

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        a_d = defaultdict(list)
        def red(ts):
            a, r = divmod(ts, 100)
            if a == 0: return 0
            a -= 1
            return a * 100 + r
        for name, time in access_times:
            a_d[name].append(int(time))
        for ts in a_d.values():
            ts.sort()
        ans = []
        for name, ts in a_d.items():
            for i, t in enumerate(ts):
                pt = red(t)
                idx = bisect.bisect_right(ts, pt)
                if i - idx >= 2:
                    ans.append(name)
                    break
        return ans


if __name__ == '__main__':
    # ["a"]
    print(Solution().findHighAccessEmployees([["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]))
    # ["c","d"]
    print(Solution().findHighAccessEmployees( [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]))
    # ["ab","cd"]
    print(Solution().findHighAccessEmployees([["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]))
