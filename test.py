import mysql.connector
from mysql.connector import errorcode
#connect to server
conn = mysql.connector.connect(user='mmb16', password='MOHbdoudy1',
                               host='cteddb.c3jkcjrdyabp.us-west-2.rds.amazonaws.com',
                               database='morf')
c = conn.cursor()

#create a table
c.execute("""DROP TABLE IF EXISTS LOGIN""")
conn.commit()
c.execute("""CREATE TABLE LOGIN (
          phone_no int(10) primary key NOT NULL,
          email text,
          username text,
          password text)""")

c.execute("""DROP TABLE IF EXISTS T1""")
conn.commit()
c.execute("""CREATE TABLE T1 (
          id int(12) primary key NOT NULL,
          phone_no int(10),
          Tid int(12), #foreign key,
          dpending int,
          friends text,
          name text,
          email text,
          username text,
          acct_balance int(10),
          in_balance int(10),
          out_balance int(10))""")

c.execute("""DROP TABLE IF EXISTS T2""")
conn.commit()
c.execute("""CREATE TABLE T2 (
          Tid int(12) primary key NOT NULL,
          id1 int(12), #foreign key,
          dpending int,
          date_r date,
          amount int(10),
          id2 int(12), #foreign key,
          date_s date,
          tfs int,
          Tnum int(8))""")


#insert data
#there is a problem when it reaches 10 digits
c.execute("""INSERT INTO LOGIN VALUES ('816787703', 'mmb583@nyu.edu', 'mmb16', 'mohbdoudy')""")
conn.commit()

#read data
c.execute("""SELECT * FROM LOGIN""")
for row in c:
    print (row)

conn.close()