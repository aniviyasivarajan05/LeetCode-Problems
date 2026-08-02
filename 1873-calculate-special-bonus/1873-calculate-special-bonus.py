import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = 0

    mask = (
        (employees["employee_id"] % 2 == 1)
        & (~employees["name"].str.startswith("M"))
    )

    employees.loc[mask, "bonus"] = employees.loc[mask, "salary"]

    return employees[["employee_id", "bonus"]].sort_values(by="employee_id")