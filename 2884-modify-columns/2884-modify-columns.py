import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    for i in employees.index:
        employees.loc[i, "salary"] *= 2

    return employees