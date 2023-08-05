# Question Link : https://leetcode.com/problems/patients-with-a-condition/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd
import re


def satisfy(s: str) -> bool:
    temp = s.split(' ')
    pattern = r'^DIAB1[a-zA-Z0-9]*$'

    for i in temp:
        if re.match(pattern, i) is not None:
            return True

    return False


def find_patients(df: pd.DataFrame) -> pd.DataFrame:
    for i in range(0, df.shape[0], 1):
        if not satisfy(df.loc[i, 'conditions']):
            df.drop(i, inplace=True)
    return df
