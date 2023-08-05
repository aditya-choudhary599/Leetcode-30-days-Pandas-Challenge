# Question Link : https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    ans = products.query("`low_fats`=='Y' and `recyclable`=='Y'")
    return ans[['product_id']]
