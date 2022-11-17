import mysql.connector as broker

mydb=broker.connect(host='localhost',user='root',passwd='tiger')
mycursor=mydb.cursor()

mycursor.execute("Use electionsys")
mycursor.execute("Select Cndt_name,position,vote_cnt from candidates group by position order by vote_cnt;")
data=mycursor.fetchall()

for i in data:
    print(i)



