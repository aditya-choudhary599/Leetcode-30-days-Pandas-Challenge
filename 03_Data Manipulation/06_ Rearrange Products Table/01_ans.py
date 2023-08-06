# Question Link : https://leetcode.com/problems/rearrange-products-table/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    new_dict = {'product_id': [], 'store': [], 'price': []}
    for i in range(products.shape[0]):
        if pd.notna(products.loc[i, 'store1']):
            new_dict['product_id'].append(products.loc[i, 'product_id'])
            new_dict['store'].append('store1')
            new_dict['price'].append(products.loc[i, 'store1'])

        if pd.notna(products.loc[i, 'store2']):
            new_dict['product_id'].append(products.loc[i, 'product_id'])
            new_dict['store'].append('store2')
            new_dict['price'].append(products.loc[i, 'store2'])

        if pd.notna(products.loc[i, 'store3']):
            new_dict['product_id'].append(products.loc[i, 'product_id'])
            new_dict['store'].append('store3')
            new_dict['price'].append(products.loc[i, 'store3'])

    return pd.DataFrame(new_dict)
