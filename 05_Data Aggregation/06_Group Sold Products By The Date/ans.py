# Question Link : https://leetcode.com/problems/group-sold-products-by-the-date/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def categorize_products(df: pd.DataFrame) -> pd.DataFrame:

    def aggregate_products(group):
        num_sold = group['product'].nunique()
        products = ','.join(sorted(group['product'].unique()))
        return pd.Series({
            'num_sold': num_sold,
            'products': products
        })

    result = df.groupby('sell_date').apply(aggregate_products).reset_index()

    return result
