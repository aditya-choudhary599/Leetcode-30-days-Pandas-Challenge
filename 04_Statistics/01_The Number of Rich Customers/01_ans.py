# Question Link : https://leetcode.com/problems/the-number-of-rich-customers/

import pandas as pd


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    temp = store.query("`amount` > 500")
    rich_count = len(temp['customer_id'].unique())
    helper = {'rich_count': rich_count}
    # Wrap the helper dictionary in a list to create a DataFrame
    return pd.DataFrame([helper])
