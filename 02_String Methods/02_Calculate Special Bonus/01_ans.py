# Question Link : https://leetcode.com/problems/calculate-special-bonus/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    helper={'employee_id':employees['employee_id'].tolist(),'bonus':[]}
    for i in range(0,employees.shape[0],1):
        if employees.loc[i,'employee_id']%2!=0 and employees.loc[i,'name'][0]!='M':
            helper['bonus'].append(employees.loc[i,'salary'])
        else:
            helper['bonus'].append(0)
    

    ans=pd.DataFrame(helper)
    ans=ans.sort_values(by=['employee_id'],ascending=True)

    return ans
            