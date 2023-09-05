# twitter-etl-pipeline

This is my first data pipeline that I have created using Airflow and AWS, following guidance from Darshil Parmar's YouTube channel.

# Packages
`pip3 install pandas`
`pip3 install tweepy` (for the Twitter API)
`pip3 install s3fs` (to store, read and write data from S3 buckets)

More details about the tweepy API can be found [here](https://docs.tweepy.org/en/stable/api.html).

# Pulling in data
## Parameters
`screen_name`: the account that you wish tor read in tweets from
`count`: how many tweets you wish to extract from the timeline
`include_rts`: boolean if you wish to include retweets
`tweet_mode`: 'extended' is standard to read in the full tweet; see [here](https://twitterdev.github.io/tweet-updates/upcoming.html).

At this point, I discovered that you are not able to read in tweets using the free version of the Twitter API, so I had to resort to user lookup instead. This is a real shame as it massively restricts the amount of data that I am able to pull in, but I'll still continue with pipeline creation.
