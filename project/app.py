from flask import Flask, request, jsonify, render_template
from flask_cors import CORS,cross_origin
import pymongo
import json, time
import datetime
import mysql.connector

app=Flask(__name__)

# MySQL connector
sql_db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="case_study_1"
)

# Mongo connector
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
nosql_db = mongo_client["assignment2"]
col = nosql_db["data_sample"]



@app.route('/')
def hello_world():
    print (request)
    return 'hello_world'


@app.route('/check', methods=['POST', 'GET'])
# @cross_origin(origin='localhost')
def returnsSomething():

    query = {'':''}
    all_cols = col.find({},{"\"GEO\"":1})
    geo_dict = {}
    timetaken = ''

    for x in all_cols:
        if x.get("\"GEO\""):
            if not x.get("\"GEO\"").replace('"', '').replace(' ', '_') in geo_dict.keys():

                geo_dict[x.get("\"GEO\"").replace('"', '').replace(' ', '_')] = x.get("\"GEO\"").replace('"', '')

    if request.method == 'POST':
        print (request.form)
        result_sql =[]
        result_nosql =[]
        try:
            qs = request.form.get('qs').replace('_', ' ')
            db = request.form.get('db')
        except:
            qs = None
            db = None

        if qs and db == 'sql':
            before = time.time()

            cursor = sql_db.cursor()
            query = 'SELECT * FROM data_sample where GEO="' + qs + '"'
            cursor.execute(query)
            result_sql = cursor.fetchall()

            after = time.time()
            timetaken = (str(before-after) + ' seconds').replace('-', '')

            return render_template('index.html', geos=geo_dict, result_sql=result_sql, timetaken=timetaken)


        if qs and db == 'nosql':
            before = time.time()
            print (before)
            
            query = '"'+ qs + '"'
            result_nosql = col.find({"\"GEO\"": query})
            after = time.time()
            print (after)

            timetaken = (str(before-after) + ' seconds').replace('-', '')
            # for x in result_nosql[:10]:
            #     print (x)
            return render_template('index.html', geos=geo_dict, result_nosql=result_nosql, timetaken=timetaken)
    return render_template('index.html', geos=geo_dict) 

