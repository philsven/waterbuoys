import psycopg2
from psycopg2 import Error
from datetime import datetime as dt

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="bcxhrhesvgzbip",
                                  password="10e228b36528b12993464f5125731348790fb165d2faea854d6bdc1d063ca11f",
                                  host="ec2-52-31-219-113.eu-west-1.compute.amazonaws.com",
                                  port="5432",
                                  database="d3jc8l4j82srkb")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    
    sql_SELECT = '''SELECT * FROM sensordata;'''
    date = str(dt.now().strftime("%Y-%m-%d %H:%M:%S"))
    sql_INSERT = '''INSERT INTO sensordata VALUES(
                        nextval('id_sequence'), '{}', 'Temperature', {});'''.format(date, 25.0)
    
    cursor.execute(sql_INSERT)
    connection.commit()
    #data = cursor.fetchall()
    #print(data) 
    
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")