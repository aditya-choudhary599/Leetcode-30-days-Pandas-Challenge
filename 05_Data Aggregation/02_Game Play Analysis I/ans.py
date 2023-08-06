# Question Link : https://leetcode.com/problems/game-play-analysis-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.drop(['device_id', 'games_played'], axis=1, inplace=True)
    activity = activity.groupby(['player_id'], as_index=False).min()
    activity = activity.rename(columns={'event_date': 'first_login'})
    return activity
