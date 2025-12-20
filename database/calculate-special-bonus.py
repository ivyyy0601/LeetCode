import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    res = employees[(^(employees["name"].str.startswith("M")) &  (employees["employee_id"] % 2 = 1)]
    return res
    