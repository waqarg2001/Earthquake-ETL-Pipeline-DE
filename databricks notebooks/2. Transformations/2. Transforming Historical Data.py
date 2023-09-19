# Databricks notebook source
df=spark.read.option('header',True).csv('/mnt/dlearthquakeproject/raw/historical_data/Significant Earthquake Dataset 1900-2023.csv')
display(df)

# COMMAND ----------

from pyspark.sql.functions import date_format,col,split,when
df = df.withColumn("date", date_format(col("Time"), "yyyy-MM-dd"))
df = df.withColumn("time_on_day", date_format(col("Time"), "HH:mm:ss"))
display(df)

# COMMAND ----------


comma_present = df["Place"].contains(",")

# Use when and split functions to extract the words after a comma or the entire column value
df = df.withColumn(
    "place_name",
    when(comma_present, split(col("Place"), ",")[1])
    .otherwise(col("Place"))
)

# COMMAND ----------

display(df)

# COMMAND ----------

df_without_null=df.na.drop(subset='Place')
display(df_without_null)

# COMMAND ----------

df_final=df_without_null.select(col('Place').alias('Title'),'Latitude','Longitude','Depth',col('Mag').alias('Magnitude'),'date','time_on_day','place_name')

# COMMAND ----------

display(df_without_null)

# COMMAND ----------

df_final=(df_without_null.dropDuplicates())

# COMMAND ----------

display(df_final)

# COMMAND ----------

df_final.write.mode('overwrite').parquet("/mnt/dlearthquakeproject/processed/historical_data/")

# COMMAND ----------


