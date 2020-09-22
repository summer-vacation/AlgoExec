# -*- coding: utf-8 -*-
"""

   File Name：     Twitter
   Author :       jing
   Date：          2020/4/13

   设计推特
   https://leetcode-cn.com/problems/design-twitter/
"""


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follower_followee = {}   # 存储每个人的关注者
        self.all_usefeed = {}         # 存储每个人发布的tweet
        self.time_post = []           # 列表按序存储发布的tweet

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId in self.all_usefeed.keys():
            self.all_usefeed[userId].append(tweetId)
        else:
            self.all_usefeed[userId] = [tweetId]
        self.time_post.append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        result = []
        len_time_post = len(self.time_post)
        index = len_time_post - 1
        all_f = []
        if userId in self.follower_followee.keys():
            for followee in self.follower_followee[userId]:
                if followee in self.all_usefeed.keys():
                    all_f.extend(self.all_usefeed[followee])
        if userId in self.all_usefeed.keys():
            all_f.extend(self.all_usefeed[userId])
        while index > -1 and len(result) < 10:
            cur_post = self.time_post[index]
            if cur_post in all_f:
                result.append(cur_post)
            index -= 1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follower_followee.keys():
            if followeeId in self.follower_followee[followerId]:
                return
            else:
                self.follower_followee[followerId].append(followeeId)
        else:
            self.follower_followee[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follower_followee.keys():
            if followeeId in self.follower_followee[followerId]:
                self.follower_followee[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
