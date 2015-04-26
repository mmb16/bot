import mysql.connector
from mysql.connector import errorcode
#connect to server
conn = mysql.connector.connect(user='mmb16', password='MOHbdoudy1',
                              host='cteddb.c3jkcjrdyabp.us-west-2.rds.amazonaws.com',
                              database='morf')
c= conn.cursor()

DB_NAME = 'morf'

'''
def create_database(cursor):
    try:
        cursor.execute(
                       "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
'''
'''
#Build login table
c.execute("""DROP TABLE IF EXISTS LOGIN""")
conn.commit()
c.execute(
           "CREATE TABLE `LOGIN` ("
               "`phone_no` int(10) NOT NULL,"
               "`email` varchar(40) NOT NULL,"
               "`username` varchar(8) NOT NULL,"
               "`password` varchar(15) NOT NULL,"
               "PRIMARY KEY (`username`)"
               ") ENGINE=InnoDB")

c.execute("""DROP TABLE IF EXISTS T1""")
conn.commit()
c.execute(
          "CREATE TABLE `T1` ("
    "`id` int(12) NOT NULL,"
    "`T_id` int(12) NOT NULL,"
    "`d_pending` decimal(10,2) NOT NULL,"
    "`friends` varchar(15) NOT NULL,"
    "`phone_no` int(10) NOT NULL,"
    "`Name` varchar(20) NOT NULL,"
    "`email` varchar(40) NOT NULL,"
    "`username` varchar(8) NOT NULL,"
    "`acct_balance` decimal(10,2) NOT NULL,"
    "`in_balance` decimal(10,2) NOT NULL,"
    "`out_balance` decimal(10,2) NOT NULL,"
    "PRIMARY KEY (`id`),"
    "CONSTRAINT `T1_fk1` FOREIGN KEY (`phone_no`)"
    " REFERENCES `LOGIN` (`phone_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")


#tfs = time for settling
c.execute("""DROP TABLE IF EXISTS T2""")
conn.commit()
c.execute("CREATE TABLE `T2` ("
    "`T_id` int(12) NOT NULL,"
    "`id_1` int(12) NOT NULL,"
    "`d_pending` decimal(10,2) NOT NULL,"
    "`date_r` date NOT NULL,"
    "`amount` decimal(10,2) NOT NULL,"
    "`id_2` int(12) NOT NULL,"
    "`date_s` date NOT NULL,"
    "`tfs` interval NOT NULL,"
    "`T_num` int(8) NOT NULL,"
    "PRIMARY KEY (`T_id`),"
    "CONSTRAINT `T2_fk1` FOREIGN KEY (`id_1`)"
    " REFERENCES `T1` (`id`) ON DELETE CASCADE"
    "CONSTRAINT `T2_fk2` FOREIGN KEY (`id_2`)"
    " REFERENCES `T1` (`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

add_user = ("INSERT INTO LOGIN "
                "(phone_no, email, username, password) "
                "VALUES (%s, %s, %s, %s)")

data_user = ('8167877031', 'mmb123', 'rob', 'jeff123')
c.execute(add_user, data_user)
conn.commit()

query = ("SELECT * FROM LOGIN ")

c.execute(query)

for row in c:
    print (row)
print 'print works'
conn.close()
'''

from datetime import date, datetime, timedelta
import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(user='mmb16', password='MOHbdoudy1',
                               host='cteddb.c3jkcjrdyabp.us-west-2.rds.amazonaws.com',
                               database='morf')
c = conn.cursor()


DB_NAME = 'morf'
c.execute("""DROP TABLE IF EXISTS employees""")
conn.commit()
c.execute(
                       "CREATE TABLE `employees` ("
                       "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
                       "  `birth_date` date NOT NULL,"
                       "  `first_name` varchar(14) NOT NULL,"
                       "  `last_name` varchar(16) NOT NULL,"
                       "  `gender` enum('M','F') NOT NULL,"
                       "  `hire_date` date NOT NULL,"
                       "  PRIMARY KEY (`emp_no`)"
                       ") ENGINE=InnoDB")

c.execute("""DROP TABLE IF EXISTS departments""")
conn.commit()
c.execute(
 "CREATE TABLE `departments` ("
 "  `dept_no` char(4) NOT NULL,"
 "  `dept_name` varchar(40) NOT NULL,"
 "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
 ") ENGINE=InnoDB")

c.execute("""DROP TABLE IF EXISTS salaries""")
conn.commit()
c.execute(
 "CREATE TABLE `salaries` ("
 "  `emp_no` int(11) NOT NULL,"
 "  `salary` int(11) NOT NULL,"
 "  `from_date` date NOT NULL,"
 "  `to_date` date NOT NULL,"
 "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
 "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
 "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
 ") ENGINE=InnoDB")


tomorrow = datetime.now().date() + timedelta(days=1)
add_employee = ("INSERT INTO employees "
                "(first_name, last_name, hire_date, gender, birth_date) "
                "VALUES (%s, %s, %s, %s, %s)")

data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
c.execute(add_employee, data_employee)
conn.commit()

query = ("SELECT * FROM employees ")

c.execute(query)

for row in c:
    print (row)
print 'print works'
conn.close()

