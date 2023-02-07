"""
 * 力扣公司的员工都使用员工卡来开办公室的门。每当一个员工使用一次他的员工卡，安保系统会记录下员工的名字和使用时间。如果一个员工在一小时时间内使用员工卡的次数大于等于三次，这个系统会自动发布一个 警告 。
 * 给你字符串数组 keyName 和 keyTime ，其中 [keyName[i], keyTime[i]] 对应一个人的名字和他在 某一天 内使用员工卡的时间。
 * 使用时间的格式是 24小时制 ，形如 "HH:MM" ，比方说 "23:51" 和 "09:49" 。
 * 请你返回去重后的收到系统警告的员工名字，将它们按 字典序升序 排序后返回。
 * 请注意 "10:00" - "11:00" 视为一个小时时间范围内，而 "23:51" - "00:10" 不被视为一小时内，因为系统记录的是某一天内的使用情况。
 * 提示：
 * 1、1 <= keyName.length, keyTime.length <= 10^5
 * 2、keyName.length == keyTime.length
 * 3、keyTime 格式为 "HH:MM" 。
 * 4、保证 [keyName[i], keyTime[i]] 形成的二元对 互不相同 。
 * 5、1 <= keyName[i].length <= 10
 * 6、keyName[i] 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/
"""
from collections import defaultdict
from typing import List


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        timeMap = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hour, minute = int(time[:2]), int(time[3:])
            timeMap[name].append(hour * 60 + minute)

        ans = []
        for name, times in timeMap.items():
            times.sort()
            if any(t2 - t1 <= 60 for t1, t2 in zip(times, times[2:])):
                ans.append(name)
        ans.sort()
        return ans


if __name__ == '__main__':
    # ['daniel']
    print(Solution().alertNames(["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"], keyTime=["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]))
    # ['bob']
    print(Solution().alertNames(["alice", "alice", "alice", "bob", "bob", "bob", "bob"], keyTime=["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]))
    # []
    print(Solution().alertNames(["john", "john", "john"], keyTime=["23:58", "23:59", "00:01"]))
    # ['clare', 'leslie']
    print(Solution().alertNames(["leslie", "leslie", "leslie", "clare", "clare", "clare", "clare"], keyTime=["13:00", "13:20", "14:00", "18:00", "18:51", "19:30", "19:49"]))
