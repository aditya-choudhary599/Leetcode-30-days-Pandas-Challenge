# Question Link : https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

import pandas as pd


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged_df = employees.merge(employee_uni, on='id', how='left')
    merged_df.drop(['id'], axis=1, inplace=True)
    return merged_df
