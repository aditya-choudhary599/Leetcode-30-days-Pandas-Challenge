# Question Link : https://leetcode.com/problems/daily-leads-and-partners/

import pandas as pd


def daily_leads_and_partners(df: pd.DataFrame) -> pd.DataFrame:
    temp = df.groupby(['date_id', 'make_name'], as_index=False).nunique()
    temp.rename(columns={'lead_id': 'unique_leads',
                'partner_id': 'unique_partners'}, inplace=True)
    return temp
