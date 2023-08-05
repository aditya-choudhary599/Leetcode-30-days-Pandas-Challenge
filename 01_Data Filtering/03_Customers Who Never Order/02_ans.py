# Question Link : https://leetcode.com/problems/customers-who-never-order/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Select the rows which `id` is not present in orders['customerId'].
    df = customers[~customers['id'].isin(orders['customerId'])]

    # Build a dataframe that only contains the column `name`
    # and rename the column `name` as `Customers`.
    df = df[['name']].rename(columns={'name': 'Customers'})
    return df
