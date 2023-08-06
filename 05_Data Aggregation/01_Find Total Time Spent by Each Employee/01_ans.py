# Question Link : https://leetcode.com/problems/find-total-time-spent-by-each-employee/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:

    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(
        ['event_day', 'emp_id'], as_index=False).sum()
    employees = employees.rename(columns={'event_day': 'day'})
    return employees.drop(columns=['out_time', 'in_time'])
