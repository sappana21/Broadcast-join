# Databricks notebook source
orders = [
    (1, 101, 500),
    (2, 102, 1000),
    (3, 103, 700),
    (4, 101, 200),
    (5, 102, 150)
]

orders_df = spark.createDataFrame(
    orders,
    ["order_id", "customer_id", "amount"]
)

display(orders_df)

# COMMAND ----------

customers = [
    (101, "Sapana"),
    (102, "Rahul"),
    (103, "John")
]

customers_df = spark.createDataFrame(
    customers,
    ["customer_id", "customer_name"]
)

display(customers_df)

# COMMAND ----------

result = orders_df.join(
    customers_df,
    "customer_id"
)

display(result)

# COMMAND ----------

from pyspark.sql.functions import broadcast

result = orders_df.join(
    broadcast(customers_df),
    "customer_id"
)

display(result)

# COMMAND ----------

result.explain(True)