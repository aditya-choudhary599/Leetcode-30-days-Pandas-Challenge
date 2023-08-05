# Question Link : https://leetcode.com/problems/fix-names-in-a-table/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def helper(row):
    return row['name'].capitalize()


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users.apply(helper, axis=1)
    users = users.sort_values(by=['user_id'])
    return users
