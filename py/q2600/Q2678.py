"""
 * 给你一个下标从 0 开始的字符串 details 。details 中每个元素都是一位乘客的信息，信息用长度为 15 的字符串表示，表示方式如下：
 * 1、前十个字符是乘客的手机号码。
 * 2、接下来的一个字符是乘客的性别。
 * 3、接下来两个字符是乘客的年龄。
 * 4、最后两个字符是乘客的座位号。
 * 请你返回乘客中年龄 严格大于 60 岁 的人数。
 * 提示：
 * 1、1 <= details.length <= 100
 * 2、details[i].length == 15
 * 3、details[i] 中的数字只包含 '0' 到 '9' 。
 * 4、details[i][10] 是 'M' ，'F' 或者 'O' 之一。
 * 5、所有乘客的手机号码和座位号互不相同。
 * 链接：https://leetcode.cn/problems/number-of-senior-citizens/description/
"""
from typing import List


class Solution:

    def countSeniors(self, details: List[str]) -> int:
        return len([d for d in details if int(d[11:13]) > 60])


if __name__ == '__main__':
    # 2
    print(Solution().countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
    # 0
    print(Solution().countSeniors(["1313579440F2036", "2921522980M5644"]))
