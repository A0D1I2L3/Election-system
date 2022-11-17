import mysql.connector as broker

mydb=broker.connect(host='localhost',user='root',passwd='tiger')
mycursor=mydb.cursor()





mycursor.execute("Create database IF NOT EXISTS Electionsys")
mycursor.execute("use Electionsys")   
mycursor.execute("create table IF NOT EXISTS admin(Cndt_Id char(20) primary key,Cndt_Name char(20),Vote_cnt int(3))")



    
candidateNo=int(input("Enter number of candidates:-"))
for i in range(candidateNo):
    candidateID=input("Enter id of candidate:-")
    candidateName=input("Enter Name of candidate:-")

    sql='''Insert into admin(Cndt_Id,Cndt_Name) values(%s,%s)'''
    
    data=(candidateID,candidateName)

    mycursor.execute(sql,data)


mydb.commit()






