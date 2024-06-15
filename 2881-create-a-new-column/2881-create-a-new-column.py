import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    bonus = []
    for salary in employees["salary"]:
        bonus.append(salary * 2)
    
    employees["bonus"] = bonus
    return employees