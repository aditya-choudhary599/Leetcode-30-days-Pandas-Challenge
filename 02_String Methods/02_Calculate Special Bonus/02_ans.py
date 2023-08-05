# Question Link : https://leetcode.com/problems/calculate-special-bonus/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def calculate_bonus(row):
    if row['employee_id'] % 2 != 0 and row['name'][0] != 'M':
        return row['salary']
    else:
        return 0


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(calculate_bonus, axis=1)
    ans = employees.sort_values(by=['employee_id']).reset_index(drop=True)
    return ans[['employee_id', 'bonus']]
