# twitter-etl-pipeline

This is my first data pipeline that I have created using Airflow and AWS, following guidance from Darshil Parmar's YouTube channel. Below are the full steps that I took to get it running. Many errors were faced along the way, so it was a great learning experience. Hopefully, others will be able to learn from my mistakes :)

# Packages
`pip3 install pandas`
`pip3 install tweepy` (for the Twitter API)
`pip3 install s3fs` (to store, read and write data from S3 buckets)
`sudo pip3 install apache-airflow` (I needed `-H` after `sudo` to get this to work).

I had some issues installing airflow, but was able to get it working eventually with a virtual environment (see [here](https://www.linkedin.com/pulse/install-apache-airflow-mac-os-ranga-reddy/)).
More details about the tweepy API can be found [here](https://docs.tweepy.org/en/stable/api.html).

# Pulling in data using tweepy API
## Parameters
`screen_name`: the account that you wish tor read in tweets from
`count`: how many tweets you wish to extract from the timeline
`include_rts`: boolean if you wish to include retweets
`tweet_mode`: 'extended' is standard to read in the full tweet; see [here](https://twitterdev.github.io/tweet-updates/upcoming.html).

At this point, I discovered that you are not able to read in tweets using the free version of the Twitter API, so I had to resort to user lookup instead. This is a real shame as it massively restricts the amount of data that I am able to pull in, but I'll still continue with pipeline creation.

# Creating the pipeline

## Creating EC2 instance
![image](https://github.com/bmcd243/twitter-etl-pipeline/assets/64990696/c98f33b3-dd64-4479-99bf-056cf855c31d)

## Editing inbound rules
![image](https://github.com/bmcd243/twitter-etl-pipeline/assets/64990696/0c21c6a6-a04c-4f20-8782-e3ae5c733c68)


## Creating S3 bucket
At this point, I got the error.
```
Permissions 0644 for 'airflow_ec2_key.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "airflow_ec2_key.pem": bad permissions
ubuntu@ec2-18-130-26-83.eu-west-2.compute.amazonaws.com: Permission denied (publickey).
```
This was fixed using: `chmod 400 /path/to/my/key.pem`

## Copying files across to the EC2 instance

I then copied the py files from my local machine to Airflow.
