# Question Link : https://leetcode.com/problems/classes-more-than-5-students/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    temp = courses.groupby(['class'], as_index=False).nunique()
    temp = temp.query("`student` >= 5")
    temp.drop(['student'], axis=1, inplace=True)
    return temp
