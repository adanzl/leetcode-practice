"""
 * 你有一个只支持单个标签页的 浏览器 ，最开始你浏览的网页是 homepage ，你可以访问其他的网站 url ，也可以在浏览历史中后退 steps 步或前进 steps 步。
 * 请你实现 BrowserHistory 类：
 * 1、BrowserHistory(string homepage) ，用 homepage 初始化浏览器类。
 * 2、void visit(string url) 从当前页跳转访问 url 对应的页面  。执行此操作会把浏览历史前进的记录全部删除。
 * 3、string back(int steps) 在浏览历史中后退 steps 步。如果你只能在浏览历史中后退至多 x 步且 steps > x ，那么你只后退 x 步。请返回后退 至多 steps 步以后的 url 。
 * 4、string forward(int steps) 在浏览历史中前进 steps 步。如果你只能在浏览历史中前进至多 x 步且 steps > x ，那么你只前进 x 步。请返回前进 至多 steps步以后的 url 。
 * 提示：
 * 1、1 <= homepage.length <= 20
 * 2、1 <= url.length <= 20
 * 3、1 <= steps <= 100
 * 4、homepage 和 url 都只包含 '.' 或者小写英文字母。
 * 5、最多调用 5000 次 visit， back 和 forward 函数。
 * 链接：https://leetcode.cn/problems/design-browser-history/
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.h = [homepage]
        self.idx = 1
        self.size = 1

    def visit(self, url: str) -> None:
        if self.idx == len(self.h):
            self.h.append(url)
        else:
            self.h[self.idx] = url
        self.idx += 1
        self.size = self.idx

    def back(self, steps: int) -> str:
        self.idx = max(self.idx - steps, 1)
        return self.h[self.idx - 1]

    def forward(self, steps: int) -> str:
        self.idx = min(self.idx + steps, self.size)
        return self.h[self.idx - 1]


if __name__ == '__main__':
    #
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")
    # 你原本在浏览 "leetcode.com" 。访问 "google.com"
    browserHistory.visit("facebook.com")
    # 你原本在浏览 "google.com" 。访问 "facebook.com"
    browserHistory.visit("youtube.com")
    # 你原本在浏览 "facebook.com" 。访问 "youtube.com"
    browserHistory.back(1)
    # 你原本在浏览 "youtube.com" ，后退到 "facebook.com" 并返回 "facebook.com"
    browserHistory.back(1)
    # 你原本在浏览 "facebook.com" ，后退到 "google.com" 并返回 "google.com"
    browserHistory.forward(1)
    # 你原本在浏览 "google.com" ，前进到 "facebook.com" 并返回 "facebook.com"
    browserHistory.visit("linkedin.com")
    # 你原本在浏览 "facebook.com" 。 访问 "linkedin.com"
    browserHistory.forward(2)
    # 你原本在浏览 "linkedin.com" ，你无法前进任何步数。
    browserHistory.back(2)
    # 你原本在浏览 "linkedin.com" ，后退两步依次先到 "facebook.com" ，然后到 "google.com" ，并返回 "google.com"
    browserHistory.back(7)
    # 你原本在浏览 "google.com"， 你只能后退一步到 "leetcode.com" ，并返回 "leetcode.com"
