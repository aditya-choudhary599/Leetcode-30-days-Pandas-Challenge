# Question Link : https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/

import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher.drop('dept_id', axis=1, inplace=True)
    ans = teacher.groupby(['teacher_id'], as_index=False).nunique()
    return ans.rename(columns={'subject_id': 'cnt'})
