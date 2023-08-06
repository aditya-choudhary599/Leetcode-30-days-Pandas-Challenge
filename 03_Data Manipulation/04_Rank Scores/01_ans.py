# Question Link : https://leetcode.com/problems/rank-scores/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by='score', ascending=False)
    scores.drop(columns=['id'], inplace=True)

    # Added new column
    scores['rank'] = 1

    scores = scores.reset_index(drop=True)
    for i in range(1, scores.shape[0]):
        if scores.loc[i, 'score'] < scores.loc[i - 1, 'score']:
            scores.loc[i, 'rank'] = scores.loc[i - 1, 'rank'] + 1
        else:
            scores.loc[i, 'rank'] = scores.loc[i - 1, 'rank']

    return scores
