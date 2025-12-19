import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    final = pd.merge(customers,orders, left_on = 'id', right_on = 'customerId', how='left')
    res = final[final['customerId'].isna()][['name']]
    return res.rename(columns={'name':'Customers'})