# Question Link : https://leetcode.com/problems/find-users-with-valid-e-mails/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

import re


def helper(email):
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    return re.match(pattern, email) is not None


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    for i in range(0, users.shape[0], 1):
        if not helper(users.loc[i, 'mail']):
            users.drop(i, inplace=True)
    return users
