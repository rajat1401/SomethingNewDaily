## Twitter Design

- follow or unfollow other users
- tweet stuff
- see tweets from users I am following - timeline

### Design

1. <font color="cyan">User Table</font>: uuid and metadata for each user with # followers and followees for quick lookup (profile page)
2. Two Tables: <font color="cyan">following</font> and <font color="cyan">followed_by</font>. So, when user A starts following B, 4 rows are updated:- 
    - A's followee count ++
    - B's follower count ++
    - following table has entry A follows B
    - followed_by table has entry B followed by A
3. <font color="cyan">Tweet Table</font>: sender id, tweet id, timestamp and content. composite primary key on uid, tid and timestamp to get tweets of a user chronologically.

4. <font color="orange">Timeline</font>: Most important. For simplicity, say chronological order. Gra some tweets from users you are following and sort them. If scrolled further, get tweets of timestamp older than current oldest. Thus, table primary key on timestamp helpful. 

> For a power user followin thousands of users, we can take a sampling from followees based on weights (interactions) and generate the feed. 