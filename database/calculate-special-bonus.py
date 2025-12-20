import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    no = employees[(employees["name"].str.startswith("M")) | (employees["employee_id"] % 2 == 0)]
    yes = employees[(~employees["name"].str.startswith("M")) & (employees["employee_id"] % 2 == 1)]
    no["salary"] = 0
    res = pd.concat([yes,no], ignore_index=True)[["employee_id","salary"]].sort_values("employee_id")
    return res.rename(columns={"salary":"bonus"})
    