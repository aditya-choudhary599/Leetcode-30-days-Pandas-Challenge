# Question Link : https://leetcode.com/problems/immediate-food-delivery-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    temp = delivery.query(
        "`order_date`==`customer_pref_delivery_date`").shape[0]/delivery.shape[0]
    return pd.DataFrame([{'immediate_percentage': round(temp*100, 2)}])
