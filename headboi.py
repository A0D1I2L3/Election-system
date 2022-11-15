import mysql.connector as broker

mydb=broker.connect(host='localhost',user='root',passwd='tiger')
mycursor=mydb.cursor()



while(1):
    try:
        mycursor.execute("Create database Electionsys")
    except broker.errors.DatabaseError:
        
        break

while(1):
    try:
        mycursor.execute("USE Electionsys")       
        mycursor.execute("create table admin(Cndt_Id char(20) primary key,Cndt_Name char(20),Vote_cnt int(3))")

    except broker.errors.ProgrammingError :
        
        break


mycursor.execute("USE Electionsys")       

candidateNo=int(input("Enter number of candidates:-"))
for i in range(candidateNo):
    candidateID=input("Enter id of candidate:-")
    candidateName=input("Enter Name of candidate:-")

    sql='''Insert into admin(Cndt_Id,Cndt_Name) values(%s,%s)'''
    
    data=(candidateID,candidateName)

    mycursor.execute(sql,data)


mydb.commit()






