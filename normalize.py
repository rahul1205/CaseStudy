import mysql.connector


# MySQL connector
sql_db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="case_study_1"
)

def make_geo_table():
    cursor = sql_db.cursor()
    query = 'SELECT GEO FROM data_sample'
    cursor.execute(query)
    result_sql = set(cursor.fetchall())

    for r in result_sql:
        query = 'insert into geo(geo) values (\"' + r[0] + '\")'
        print (query)
        cursor.execute(query)
        sql_db.commit()

def populate_foreign_keys():
    cursor = sql_db.cursor()
    query = 'SELECT geo, id FROM geo'
    cursor.execute(query)
    geo_dict = dict(cursor.fetchall())

    query1 = 'SELECT id, GEO from data_sample'
    cursor.execute(query1)
    data = cursor.fetchall()
    # print (data)
    faulty_id = []
    for d in data:
        if d[1] in geo_dict.keys():
            geo_id = geo_dict.get(d[1])
            query3 = 'update data_sample set geo_id=' + str(geo_id) + ' where id=' + str(d[0])
            print (query3)
            cursor.execute(query3)
            sql_db.commit()
        else:
            faulty_id.append(d[0])
    print (faulty_id)


# populate_foreign_keys()
