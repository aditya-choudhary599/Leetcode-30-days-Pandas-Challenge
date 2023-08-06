# Question Link : https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    # Created the new columns
    for i in range(0, subjects.shape[0], 1):
        students[subjects.loc[i, 'subject_name']] = 0
    # print(students)

    melted_students = pd.melt(students, id_vars=['student_id', 'student_name'], value_vars=subjects['subject_name'].unique(
    ), var_name='subject_name', value_name='attended_exams')

    melted_students.sort_values(
        by=['student_id', 'subject_name'], inplace=True)
    # print(melted_students)

    examinations = examinations.groupby(
        ['student_id', 'subject_name'], as_index=False).size()
    # print(examinations)

    ans = melted_students.merge(
        examinations, on=['student_id', 'subject_name'], how='left')
    # print(ans)

    # To replace NA with 0
    ans.fillna(0, inplace=True)
    # print(ans)

    ans.drop(['attended_exams'], axis=1, inplace=True)
    ans.rename(columns={'size': 'attended_exams'}, inplace=True)
    # print(ans)

    ans['attended_exams'] = ans['attended_exams'].astype(int)
    return ans[['student_id', 'student_name', 'subject_name', 'attended_exams']]
