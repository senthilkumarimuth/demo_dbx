import pandas as pd
import sys, os
from pathlib import Path, PurePath
from common import Task

# enable below line if you get 'PYTHON NOT FOUND' error or python3 not found error
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

#get root path
root_path = PurePath(Path(__file__).parents[2]).as_posix()

#provide input file path, db, table name
input_file_path = os.path.join(root_path, "data", "raw", "sample.csv")
db = 'testdatabase'
table = 'test'

class csv_to_table(Task):
    def csv_reader(self):
        # read csv file from local
        _data = pd.read_csv(input_file_path)
        return _data
    def converter(self):
        df = self.spark.createDataFrame(self.csv_reader())
        self.spark.sql(f"CREATE DATABASE IF NOT EXISTS {db}")
        df.write.format('delta').mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"{db}.{table}")
    def launch(self):
        self.converter()
        pass

obj = csv_to_table()
obj.launch()