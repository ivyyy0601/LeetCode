import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    temp= employee["salary"].drop_duplicates().sort_values(ascending = False)
    res= pd.DataFrame([temp.iloc[1] if len(temp)>=2 else None ] )
    return res.rename(columns={0:"SecondHighestSalary"})