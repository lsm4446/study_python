# import modules
from pyspark.sql import SQLContext
from pyspark.sql.functions import *

# read the csv with library
df = sqlContext.read.format('com.databricks.spark.csv')\
                    .options(header='true', inferSchema='true')\
                    .load('C:\test.csv')

# convert the df to tmp table (as if it's in database)
df.registerTempTable("df_tmp")

# extract data from table with sql
df1 = sqlContext.sql("select ismydoc, actiontype, sessionid, datetime from df_tmp where ismydoc = true")

## Lazy Execution
df2 = sqlContext.sql("select * from df_tmp")

df2_pdf = df2.select("sessionid", "ext").filter(" ext == 'PDF' or ext = 'DOC'").dropDuplicates().cache()
df2.distinct().count()

df2_min_date = df2.groupby("sessionid").agg(min("datetime").alias("min_date"))
df2_min_date.show()

df2_join = df2_pdf.join(df2_min_date, "sessionid", "left")
df2_join.show()

df2_join1 = df2_join.groupby("min_date", "ext").agg(count("sessionid").alias("cnt"))

df2_join1.describe().show()

# Pandas
df2_pd = df2.toPandas()
df2_pd.head()
df2_pd.describe()
