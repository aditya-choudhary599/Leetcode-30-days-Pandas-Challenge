# Question Link : https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    bins = [0, 20000, 50001, float('inf')]
    labels = ['Low Salary', 'Average Salary', 'High Salary']

    accounts['category'] = pd.cut(
        accounts['income'], bins=bins, labels=labels, right=False)
    result = accounts['category'].value_counts().reindex(
        labels, fill_value=0).reset_index()
    result.columns = ['category', 'accounts_count']

    return result
