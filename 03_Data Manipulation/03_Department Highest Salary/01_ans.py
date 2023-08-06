# Question Link : https://leetcode.com/problems/department-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    dep_ids = employee['departmentId'].unique()
    helper = {'Department': [], 'Employee': [], 'Salary': []}

    for id in dep_ids:
        temp = employee.query("`departmentId` == @id")
        maxi = temp['salary'].max()
        curr_ans = temp.query("`salary` == @maxi")

        # Loop through employees with the highest salary in the current department
        for idx, row in curr_ans.iterrows():
            department_name = department.query("`id` == @id")['name'].values[0]
            helper['Department'].append(department_name)
            helper['Employee'].append(row['name'])
            helper['Salary'].append(maxi)

    return pd.DataFrame(helper)
