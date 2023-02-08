# Todo:
   1. To be replaced by custom dbx installation document

# Benefits:

1. .py file can't be run directy in databricks[before 2023] so all your codes to be in notebooks. 
This stops us from using folder structure like cookiecutter. In this case, dbx setup will help
you run the code in local as well as in databricks
2. dbx provides utility for spark, mlflow, dbutils so that a spark project can be setup in local
effortlessly

# Limitation of dbx way[in local way] of working:

1. The sample data used in local may not satisfy the conditions in code, 
but it will satisfy in databricks, then the effort to collect sample in
local is time consuming, tidious.
    -Todo: To solve this, intermediate data to be prepared and that has to be used in local
2. Sometimes, if a python library version is difference in local compared
to databricks, this may cause issue.
    -Todo: To solve this, requirement.txt to be used in target environment
