# PySpark Broadcast Join Example (Databricks)

A simple, hands-on Databricks notebook that demonstrates **broadcast joins** in PySpark — a performance optimization technique used when joining a large DataFrame with a much smaller one.

##  What This Notebook Does

1. Creates two sample DataFrames:
   - `orders_df` — a set of order records (`order_id`, `customer_id`, `amount`)
   - `customers_df` — a small lookup table of customers (`customer_id`, `customer_name`)
2. Performs a **regular join** between `orders_df` and `customers_df`.
3. Performs the **same join using `broadcast()`** on the smaller DataFrame.
4. Uses `.explain(True)` to compare the physical execution plans and show how Spark avoids a costly shuffle when broadcasting.

##  What Is a Broadcast Join?

In distributed Spark joins, data usually needs to be **shuffled** across the cluster so matching keys land on the same node — this is expensive for large datasets.

A **broadcast join** avoids this by sending a small DataFrame to every executor node in full, so the join happens locally without shuffling the large DataFrame. It's ideal when:

- One DataFrame is small enough to fit in memory on each executor (commonly < ~10MB, tunable via `spark.sql.autoBroadcastJoinThreshold`)
- You're joining a large fact table with a small dimension/lookup table

##  Tech Stack

- Apache Spark (PySpark)
- Databricks Notebook

##  How to Run

1. Import this notebook into a Databricks workspace (or open it via a linked Databricks Git folder).
2. Attach it to a running cluster.
3. Run all cells sequentially.
4. Check the output of `result.explain(True)` to see the difference between the shuffle join and the broadcast join execution plans (look for `BroadcastHashJoin` vs `SortMergeJoin`).

##  File Structure

```
├── broadcast_join.py   # Databricks source notebook (regular join vs broadcast join)
└── README.md
```

##  Keywords / Tags

`pyspark` `apache-spark` `databricks` `broadcast-join` `spark-optimization` `big-data` `data-engineering` `sql-joins` `spark-sql` `performance-tuning`

##  Short Description (for GitHub "About" section)

> Demonstrates PySpark broadcast joins vs regular joins in Databricks, with execution plan comparison for performance optimization.
