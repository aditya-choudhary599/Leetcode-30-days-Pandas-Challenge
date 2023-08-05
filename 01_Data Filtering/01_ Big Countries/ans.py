# Question Link : https://leetcode.com/problems/big-countries/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    ans = world.query("`area`>=3000000 or `population`>=25000000")
    ans = ans[['name', 'area', 'population']]
    return ans
