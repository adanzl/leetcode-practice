"""
 * 网站域名 "discuss.leetcode.com" 由多个子域名组成。顶级域名为 "com" ，二级域名为 "leetcode.com" ，最低一级为 "discuss.leetcode.com" 。
 * 当访问域名 "discuss.leetcode.com" 时，同时也会隐式访问其父域名 "leetcode.com" 以及 "com" 。
 * 计数配对域名 是遵循 "rep d1.d2.d3" 或 "rep d1.d2" 格式的一个域名表示，其中 rep 表示访问域名的次数，d1.d2.d3 为域名本身。
 * 例如，"9001 discuss.leetcode.com" 就是一个 计数配对域名 ，表示 discuss.leetcode.com 被访问了 9001 次。
 * 给你一个 计数配对域名 组成的数组 cpdomains ，解析得到输入中每个子域名对应的 计数配对域名 ，并以数组形式返回。可以按 任意顺序 返回答案。
 * 提示：
 * 1、1 <= cpdomain.length <= 100
 * 2、1 <= cpdomain[i].length <= 100
 * 3、cpdomain[i] 会遵循 "repi d1i.d2i.d3i" 或 "repi d1i.d2i" 格式
 * 4、repi 是范围 [1, 104] 内的一个整数
 * 5、d1i、d2i 和 d3i 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/subdomain-visit-count/
"""
from typing import *


class Solution:

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = Counter()
        for domain in cpdomains:
            n, s = domain.split()
            idx = s.find('.')
            while idx != -1:
                cnt[s[idx + 1:]] += int(n)
                idx = s.find('.', idx + 1)
            cnt[s] += int(n)
        return [str(v) + ' ' + k for k, v in cnt.items()]


if __name__ == '__main__':
    # ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
    print(Solution().subdomainVisits(["9001 discuss.leetcode.com"]))
    # ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
    print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))