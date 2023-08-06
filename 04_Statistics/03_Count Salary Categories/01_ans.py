# Question Link : https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    helper = {'category': ['Low Salary', 'Average Salary',
                           'High Salary'], 'accounts_count': [0]*3}
    helper['accounts_count'][0] = accounts.query("`income`<20000").shape[0]
    helper['accounts_count'][1] = accounts.query(
        "`income`>=20000 and `income`<=50000").shape[0]
    helper['accounts_count'][2] = accounts.query("`income`>50000").shape[0]
    return pd.DataFrame(helper)
