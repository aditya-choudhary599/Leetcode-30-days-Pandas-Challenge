# Question Link : https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

import pandas as pd


def actors_and_directors(df: pd.DataFrame) -> pd.DataFrame:
    temp = df.groupby(['actor_id', 'director_id'], as_index=False).nunique()
    ans = temp.query("`timestamp`>=3")
    ans.drop(['timestamp'], axis=1, inplace=True)
    return ans
