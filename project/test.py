import pymongo
import mysql.connector


# mydb = myclient["assignment2"]
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="case_study_1"
)

mycursor = mydb.cursor()

query = "SELECT * FROM data_sample where GEO=" + '"Canada"'
mycursor.execute(query)
all_cols = mycursor.fetchall()

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mycol = mydb["data_sample"]

# all_cols = mycol.find({},{"\"GEO\"":1})

# # geo_list = []
# for x in all_cols:
# 	if not x.get("\"GEO\"") in geo_list:
# 		geo_list.append(x.get("\"GEO\""))

print (all_cols)
		