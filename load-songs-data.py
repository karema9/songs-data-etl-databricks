# Databricks notebook source
# MAGIC %md
# MAGIC ## Preprocessing songs data

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TABLE songs_data_table (
# MAGIC   artists_id STRING,
# MAGIC   artist_name STRING, 
# MAGIC   duration DOUBLE, 
# MAGIC   release STRING,
# MAGIC   tempo DOUBLE, 
# MAGIC   time_signature DOUBLE, 
# MAGIC   title STRING,  
# MAGIC   year DOUBLE,
# MAGIC   processed_time TIMESTAMP
# MAGIC )
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO songs_data_table
# MAGIC SELECT
# MAGIC   artist_id,
# MAGIC   artist_name,
# MAGIC   duration,
# MAGIC   release,
# MAGIC   tempo,
# MAGIC   time_signature,
# MAGIC   title,
# MAGIC   year,
# MAGIC   current_timestamp()
# MAGIC FROM
# MAGIC   songs_data
