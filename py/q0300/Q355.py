"""
 * 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近 10 条推文。
 * 实现 Twitter 类：
 * 1、Twitter() 初始化简易版推特对象
 * 2、void postTweet(int userId, int tweetId) 根据给定的 tweetId 和 userId 创建一条新推文。
 *     每次调用此函数都会使用一个不同的 tweetId 。
 * 3、List<Integer> getNewsFeed(int userId) 检索当前用户新闻推送中最近  10 条推文的 ID 。
 *     新闻推送中的每一项都必须是由用户关注的人或者是用户自己发布的推文。推文必须 按照时间顺序由最近到最远排序 。
 * 4、void follow(int followerId, int followId) ID 为 followerId 的用户开始关注 ID 为 followId 的用户。
 * 5、void unfollow(int followerId, int followId) ID 为 followerId 的用户不再关注 ID 为 followId 的用户。
 * 提示：
 * 1 <= userId, followerId, followId <= 500
 * 0 <= tweetId <= 10^4
 * 所有推特的 ID 都互不相同
 * postTweet、getNewsFeed、follow 和 unfollow 方法最多调用 3 * 10^4 次
 * 链接：https://leetcode.cn/problems/design-twitter/
"""

from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import Deque, List

#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#


# @lc code=start
class Twitter:

    def __init__(self):
        self.d_post = defaultdict(Deque)
        self.d_followers = defaultdict(set)
        self.tick = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        lst = self.d_post[userId]
        lst.appendleft([-self.tick, tweetId])
        self.tick += 1
        if len(lst) > 10:
            lst.pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        i = 0
        data = [[self.d_post[fi][0][0], self.d_post[fi][0][1], fi, 1] for fi in self.d_followers[userId]
                if self.d_post[fi]]
        heapify(data)
        if self.d_post[userId]:
            heappush(data, [self.d_post[userId][0][0], self.d_post[userId][0][1], userId, 1])
        while i < 10 and data:
            tick, tweet_id, follower_id, idx = heappop(data)
            ans.append(tweet_id)
            if idx < len(self.d_post[follower_id]):
                heappush(data,
                         [self.d_post[follower_id][idx][0], self.d_post[follower_id][idx][1], follower_id, idx + 1])
            i += 1
        return ans

    def follow(self, followerId: int, followId: int) -> None:
        self.d_followers[followerId].add(followId)

    def unfollow(self, followerId: int, followId: int) -> None:
        self.d_followers[followerId].discard(followId)


# @lc code=end

if __name__ == '__main__':
    twitter = Twitter()
    # 用户 1 发送了一条新推文 (用户 id = 1, 推文 id = 5)
    twitter.postTweet(1, 5)
    # 用户 1 的获取推文应当返回一个列表，其中包含一个 id 为 5 的推文
    # [5]
    print(twitter.getNewsFeed(1))
    # 用户 1 关注了用户 2
    twitter.follow(1, 2)
    # 用户 2 发送了一个新推文 (推文 id = 6)
    twitter.postTweet(2, 6)
    # 用户 1 的获取推文应当返回一个列表，其中包含两个推文，id 分别为 -> [6, 5] 。推文 id 6 应当在推文 id 5 之前，因为它是在 5 之后发送的
    # [6, 5]
    print(twitter.getNewsFeed(1))
    # 用户 1 取消关注了用户 2
    twitter.unfollow(1, 2)
    # 用户 1 获取推文应当返回一个列表，其中包含一个 id 为 5 的推文。因为用户 1 已经不再关注用户 2
    # [5]
    print(twitter.getNewsFeed(1))
