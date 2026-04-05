import time

class Twitter:

    def __init__(self):
        self.followMap = [[1 if i==j else 0 for i in range(101)] for j in range(101)]
        self.newFeeds = [[] for j in range(101)]
        self.userPosted = [[] for j in range(101)]
        self.numTweets = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.userPosted[userId], (-self.numTweets, userId, tweetId))
        self.numTweets += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        follows = [f for (f, v) in enumerate(self.followMap[userId]) if v == 1]
        allTweets = []
        topRecentTweets = []
        for follow in follows:
            allTweets.extend(self.userPosted[follow])
        heapq.heapify(allTweets)
        i = 0
        
        while i < min(len(allTweets), 10):
            (ts, poster, tweet) = sorted(allTweets)[i]
            topRecentTweets.append(tweet)
            i+=1
        return topRecentTweets


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId][followeeId] = 1


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId][followeeId] = 0

            
