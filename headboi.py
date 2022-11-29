import mysql.connector as broker

mydb=broker.connect(host='localhost',user='root',passwd='tiger')
mycursor=mydb.cursor()





mycursor.execute("Create database IF NOT EXISTS Electionsys")
mycursor.execute("use Electionsys")   

mycursor.execute("create table IF NOT EXISTS candidates(Cndt_Id char(20) primary key,Cndt_Name char(20),Position char(20),Vote_cnt int(3) default 0)")



    
candidateNo=int(input("Enter number of candidates:-"))
for i in range(candidateNo):
    candidateID="CD"+f"{i}"
    PositionName=input("Enter position of candidate:-")
    candidateName=input("Enter Name of candidate:-")

    sql='''Insert into candidates(Cndt_Id,Cndt_Name,Position) values(%s,%s,%s)'''
    
    data=(candidateID,candidateName,PositionName)

    mycursor.execute(sql,data)


mydb.commit()






