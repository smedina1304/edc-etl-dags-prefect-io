import prefect
from prefect import task, Flow
from prefect.schedules import IntervalSchedule
from datetime import datetime, timedelta
import pandas as pd

retry_delay = timedelta(minutes=15)

@task
def get_data():
    df = pd.read_csv("https://github.com/BigDataGal/Python-for-Data-Science/blob/master/titanic-train.csv")
    return df



