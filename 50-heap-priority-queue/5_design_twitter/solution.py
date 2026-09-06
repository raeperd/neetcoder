from typing import List


class Twitter:
    def __init__(self):
        raise NotImplementedError("Implement Twitter.__init__")

    def postTweet(self, userId: int, tweetId: int) -> None:
        raise NotImplementedError("Implement Twitter.postTweet")

    def getNewsFeed(self, userId: int) -> List[int]:
        raise NotImplementedError("Implement Twitter.getNewsFeed")

    def follow(self, followerId: int, followeeId: int) -> None:
        raise NotImplementedError("Implement Twitter.follow")

    def unfollow(self, followerId: int, followeeId: int) -> None:
        raise NotImplementedError("Implement Twitter.unfollow")
