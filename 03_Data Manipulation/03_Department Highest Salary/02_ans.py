# Question Link : https://leetcode.com/problems/department-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge the employee and department dataframes
    merged_df = employee.merge(
        department, left_on='departmentId', right_on='id', suffixes=('', '_dep'))
    # print(merged_df)

    # Group by department and find employees with highest salary
    result_df = merged_df.groupby('name_dep').apply(
        lambda x: x[x['salary'] == x['salary'].max()])
    print(result_df)

    # Reset index and keep only relevant columns
    result_df = result_df.reset_index(
        drop=True)[['name_dep', 'name', 'salary']]
    result_df.columns = ['Department', 'Employee', 'Salary']

    return result_df
