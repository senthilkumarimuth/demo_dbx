# What is dbx?
Databricks CLI eXtensions - aka dbx is a CLI tool for IDE based development and advanced Databricks workflows management.

# Pros
dbx simplifies Databricks workflows development, deployment and launch across multiple environments. i.e

Develop a new Python project on Databricks solely in IDE without using Notebooks

Develop a new Python project on Databricks with Databricks Notebooks and partially in the IDE[mixed mode]

It also helps to package your project and deliver it to your Databricks environment in a versioned fashion. Designed in a CLI-first manner, it is built to be actively used both inside CI/CD pipelines and as a part of local tooling for rapid prototyping[1]

Unlike databricks connect, dbx doesn’t insist python version to be same in local and databricks[This was one of cons of databricks connect]

# Cons

dbx currently doesn't provide interactive debugging capabilities. If you want to use interactive debugging, you can use Databricks Connect, and then use dbx for deployment operations.

# Benefits:

1. .py file can't be run directy in databricks[before 2023] so all your codes to be in notebooks. 
This stops us from using folder structure like cookiecutter, doesn't allow us
do pytest, pylint etc and also doesn't allow to enjoy the IDE features. In this case, 
this custom modified repo of  dbx rep of databricks labs will help
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
