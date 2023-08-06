# Question Link : https://leetcode.com/problems/nth-highest-salary/

import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, n: int) -> pd.DataFrame:
    sorted_salaries = employee['salary'].unique()  # Get unique salaries
    print(sorted_salaries)
    sorted_salaries.sort()  # Sort the unique salaries

    if n <= len(sorted_salaries):
        nth_highest = sorted_salaries[-n]  # Get the nth highest salary

        # Filter employees with the nth highest salary
        result_df = employee[employee['salary'] == nth_highest].head(1)
        return result_df[['salary']]
    else:
        return pd.DataFrame()  # Return an empty DataFrame if n is too large
