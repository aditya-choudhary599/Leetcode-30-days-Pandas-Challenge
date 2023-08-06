# Question Link : https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/submissions/

import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    output = orders['customer_number'].value_counts().reset_index()
    print(output)
    return output[['customer_number']].head(1)
