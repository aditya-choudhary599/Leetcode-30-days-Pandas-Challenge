# Question Link : https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd


def find_managers(df: pd.DataFrame) -> pd.DataFrame:
    temp = df['managerId'].value_counts()
    ls = temp[temp >= 5].index.tolist()

    filtered_df = df[df['id'].isin(ls)][['name']]

    return filtered_df
