# Question Link : https://leetcode.com/problems/sales-person/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    id_of_red = company.loc[company['name'] == 'RED', 'com_id'].iloc[0]

    orders = orders[orders['com_id'] == id_of_red]

    temp = sales_person.merge(orders, on='sales_id', how='left')

    missing_orders = temp[temp['order_id'].isna()]

    result = missing_orders[['name']].reset_index(drop=True)

    return result
