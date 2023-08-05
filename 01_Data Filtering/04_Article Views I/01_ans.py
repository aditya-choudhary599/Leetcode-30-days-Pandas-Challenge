# Question Link : https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    helper = {'id': set()}
    for i in range(0, views.shape[0], 1):
        if views.loc[i, 'viewer_id'] == views.loc[i, 'author_id']:
            helper['id'].add(views.loc[i, 'author_id'])

    temp = list(helper['id'])
    temp.sort()
    helper['id'] = temp

    return pd.DataFrame(helper)
