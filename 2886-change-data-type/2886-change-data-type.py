import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = round(students["grade"]).astype(int)
    return students