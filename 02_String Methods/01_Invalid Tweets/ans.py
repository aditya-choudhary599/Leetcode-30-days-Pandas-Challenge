# Question Link : https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    ans = tweets[tweets['content'].apply(lambda x: len(x) > 15)]
    return ans[['tweet_id']]
