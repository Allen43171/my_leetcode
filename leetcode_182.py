# 182. Duplicate Emails
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame
    result = person.loc[person.duplicated(subset=['email']), ['email']]
    result = result.drop_duplicates()
    
    return result