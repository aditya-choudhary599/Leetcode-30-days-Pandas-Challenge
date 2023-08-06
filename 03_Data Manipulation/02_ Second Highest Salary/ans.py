# Question Link : https://leetcode.com/problems/second-highest-salary/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salaries = employee['salary'].unique()  # Get unique salaries
    print(sorted_salaries)
    sorted_salaries.sort()  # Sort the unique salaries

    if 2 <= len(sorted_salaries):
        nth_highest = sorted_salaries[-2]  # Get the nth highest salary

        # Filter employees with the nth highest salary
        result_df = employee[employee['salary'] == nth_highest].head(1)
        return result_df[['salary']].rename(columns={'salary': 'SecondHighestSalary'})
    else:
        # Return an empty DataFrame if n is too large
        return pd.DataFrame([None], columns=['SecondHighestSalary'])
