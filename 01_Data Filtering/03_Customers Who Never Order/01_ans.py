# Question Link : https://leetcode.com/problems/customers-who-never-order/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ids_who_order = orders['customerId'].tolist()
    helper={'Customers':[]}

    for i in range(customers.shape[0]):
        if customers.loc[i, 'id'] not in ids_who_order:
            helper['Customers'].append(customers.loc[i,'name'])
    
    return pd.DataFrame(helper)