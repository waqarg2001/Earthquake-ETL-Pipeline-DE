# Databricks notebook source
df=spark.read.option('multiline','true').json('/mnt/dlearthquakeproject/raw/usgs_data/4.5_week.geojson')
df=df.select('features')


# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *

#Flatten array of structs and structs
def flatten(df):
   # compute Complex Fields (Lists and Structs) in Schema   
   complex_fields = dict([(field.name, field.dataType)
                             for field in df.schema.fields
                             if type(field.dataType) == ArrayType or  type(field.dataType) == StructType])
   while len(complex_fields)!=0:
      col_name=list(complex_fields.keys())[0]
      print ("Processing :"+col_name+" Type : "+str(type(complex_fields[col_name])))
    
      # if StructType then convert all sub element to columns.
      # i.e. flatten structs
      if (type(complex_fields[col_name]) == StructType):
         expanded = [col(col_name+'.'+k).alias(col_name+'_'+k) for k in [ n.name for n in  complex_fields[col_name]]]
         df=df.select("*", *expanded).drop(col_name)
    
      # if ArrayType then add the Array Elements as Rows using the explode function
      # i.e. explode Arrays
      elif (type(complex_fields[col_name]) == ArrayType):    
         df=df.withColumn(col_name,explode_outer(col_name))
    
      # recompute remaining Complex Fields in Schema       
      complex_fields = dict([(field.name, field.dataType)
                             for field in df.schema.fields
                             if type(field.dataType) == ArrayType or  type(field.dataType) == StructType])
   return df

# COMMAND ----------

df_new=flatten(df)

# COMMAND ----------

column_names = [field.name for field in df_new.schema.fields]

# Create a list of concat_ws expressions for each column
concat_ws_exprs = [
    concat_ws(", ", array_distinct(collect_list(col))).alias(col)
    for col in column_names
]

# Apply the aggregation with the concat_ws expressions
grouped_df = df_new.groupBy("features_id").agg(*concat_ws_exprs)


# COMMAND ----------

from pyspark.sql.functions import split

# Split the features_geometry_coordinates column into separate columns
grouped_df = grouped_df.withColumn("coordinates_array", split(col("features_geometry_coordinates"), ", "))

# Extract the longitude, latitude, and depth from the coordinates_array column
grouped_df = grouped_df.withColumn("longitude", grouped_df["coordinates_array"][0].cast("double"))
grouped_df = grouped_df.withColumn("latitude", grouped_df["coordinates_array"][1].cast("double"))
grouped_df = grouped_df.withColumn("depth", grouped_df["coordinates_array"][2].cast("double"))

# Drop the temporary coordinates_array column if needed
grouped_df = grouped_df.drop("coordinates_array")



# COMMAND ----------

comma_present = grouped_df["features_properties_place"].contains(",")

# Use when and split functions to extract the words after a comma or the entire column value
grouped_df = grouped_df.withColumn(
    "place_name",
    when(comma_present, split(col("features_properties_place"), ",")[1])
    .otherwise(col("features_properties_place"))
)


# COMMAND ----------

from pyspark.sql.functions import col, from_unixtime

# Assuming you have a DataFrame grouped_df with a column "features_properties_time"
# Convert Unix timestamps (in milliseconds) to datetime and create a new column "time"
grouped_df = grouped_df.withColumn("time", from_unixtime(col("features_properties_time") / 1000))
grouped_df = grouped_df.withColumn("date", date_format(col("time"), "yyyy-MM-dd"))
grouped_df = grouped_df.withColumn("time_of_day", date_format(col("time"), "HH:mm:ss"))



# COMMAND ----------

final_df=grouped_df.select('date','time_of_day','place_name','longitude','latitude','depth',col('features_properties_mag').alias('magnitude'),col('features_properties_title').alias('title'))

# COMMAND ----------

final_df.write.mode('overwrite').parquet('/mnt/dlearthquakeproject/processed/usgs_data/')
