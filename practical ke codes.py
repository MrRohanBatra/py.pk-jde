def one():
    st=[1,2,6,35,4,654,67,5]
    for i in range(len(st),1,-1):
        for j in range(0,i-1):
            if st[j]>st[j+1]:
                st[j],st[j+1]=st[j+1],st[j]
            else:
                pass
    print(st)
def two():
    a,b=0,0
    n=input("enter a string")
    for i in n:
        if i.isupper():
            a=a+1
        elif i.islower():
            b=b+1
    print("total uppercase = ",a)
    print('total lower case =' ,b)
def three():
    s=0
    p=1
    for i in range(1,11):
        s=s+i
        p=p*i
    print("sum is ",s," and product is ",p)
def four(a,b,c):
    if a>b and a>c:
        print("enter greatest no is ",a)
    elif b>a and b>c:
        print("largest number is ",b)
    elif c>a and c>b:
        print("largest number is ",c)
def five(l):
    z=[]
    for i in l:
        z.append(i*i)
    print(z)
def six(p,r,t):
    i=p*r*t/100
    print ("simple interest ",i)
    a=input("if you want to know the compound interest type c\nOr type e to exit ")
    if a=="c":
        n=int(input("enter time period in an year"))
        z=r/n
        w=n*t
        x=(1+z)**w
        b=p*x
        print("Compund interest= ",b-p)
    elif a=='e':
        print("exiting")
def seven(x,y):
    if x>y:
        smaller=y
        greater=x
    elif x<y:
        smaller=x
        greater=y
    for i in range(1,smaller-1):
        if x%i==0 and y%i==0:
            hcf=i
    a=x*y
    lcm=a/hcf
    print("HCF is ",hcf)
    print("LCM is ",lcm)
def eight(l):
    a=[]
    for i in l:
        if i%2==0:
            i.append(a)
    print(a)
def nine():
    n=intput("Enter file location")
    f=open(n,'r')
    y=f.read(10)
    print(y)
    f.close()
def ten():
    n=input("enter file location")
    f=open(n,'r')
    x=f.readlines()
    for i in x:
        if i[0]=='P':
            print(i)
        else:
            print("no line with first element P")
    f.close()
def eleven():
    n=input("Enter a file location")
    f=open(n,'w')
    for i in range(0,10):
        name=input("Enter a name ")
        Add=input("Enter a address")
        contact=input("Enter a contact number")
        email=input("Enter a email")
        x=name+add+contact+email
        f.write(x)
        f.close()
def twelve():
    n=input("Enter a file location")
    contact=input("Enter contact number")
    f=open(n,'r')
    x=f.readline()
    for i in x:
        y=i.split(" ")
        for j in y:
            if j==contact:
                print(y)
def thirteen():
    n=input("Enter location of file to be read ")
    m=input("Enter the location of file to be written")
    f=open(n,'r')
    g=open(m,'a')
    x=f.readlines()
    g.append(x)
    f.close()
    g.close()
def fourteen():
    n=intput("Enter a location of file to be read")
    m=input("Enter the location of file to be written")
    f=open(n,'r')
    g=open(m,'a')
    x=f.readlines()
    for i in x:
        if i[0]=='P' or i[0]=='p':
            g.append(i)
    f.close()
    g.close()
def fifteen():
    n=input("Enter the location of file")
    f=open(n,'r')
    x=f.readline()
    for i in x:
        if i[0]!='s' or i[0]!='S':
            print(i)
    f.close()
def sixteen():
    n=input("Enter the location of file to be read ")
    m=input("Enter the location of file to be written")
    f=open(n,'r')
    g=open(m,'a')
    x=f.readlines()
    a=[]
    for i in x:
        y=x.split(" ")
        for j in y:
            if j!="to" or j!="the":
                a.append(j)
    for z in a:
        g.append(z)
    f.close()
    g.close()
def seventeen():
    import pickle
    n=input("Enter the location of bin file to be written")
    f=open(n,'ab')
    while True:
        id=int(input("Enter an id"))
        name=input("Enter a name")
        quantity=int(input("Enter quantity"))
        price=int(input("Enter price"))
        pickle.dump([id,name,quantity,price],f)
        i=input("Enter e to exit or c to continue")
        if i=='e' or i=='E':
            print("exiting")
            f.close()
def eighteen():
    import csv
    n=input("Enter the location of csv file to be read ")
    with open(n,'r') as f:
        r=csv.reader(f)
        for i in r:
            print(i)
def nineteen(l):
    import csv
    n=input("Enter location of csv file to be read ")
    with open(n,'a') as f:
        w=csv.writer(f)
        w.writerows(l)
def twenty():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="rohan",database="crime")
    mycursor=mydb.cursor()
    llist=[]
    a=int(input("Enter Id number: "))
    llist.append(a)
    b=input("Enter Offender Name: ")
    llist.append(b)
    c=int(input("Enter Age of Offender: "))
    llist.append(c)
    d=input("Enter Crime committed by offender: ")     
    llist.append(d)
    e=input("Enter date of crime committed: ")
    llist.append(e)
    f=input("Enter date of record entry: ")
    llist.append(f)
    g=int (input ("Enter number of witnesses: "))
    llist.append(g)
    print(llist)
    rec=(llist)
    sql="insert into criminals(id,Name,Age,crime,date_of_crime,date_of_entry,no_of_witnesses)values(%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,rec)
    print("Record Added")
    mydb.commit()
def twentyone():
    import mysql.connector
    Mydb = mysql.connector.connect (host="localhost", user="root",passwd="rohan",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender you want to delete")
    a1=input("Enter the ID Number")
    info=(a1,)
    sql=("delete from criminals where id=%s")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Record Deleted")
def twentytwo():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="rohan",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender you want to view")
    b1=input("Enter the ID Number")
    data=(b1,)
    sql=("select * from criminals where id=%s")
    mycursor.execute(sql,data)
    myrecords= mycursor.fetchall()
    for x in myrecords:
        print(x)
def twentythree():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="rohan",database="crime")
    mycursor=mydb.cursor()
    choice4=0
    choice4=input("Select the order for the records to be sorted: \n 1.Ascending\n 2.Descending \n")
    if choice4=="1":
        sql=("select id,Name,Age,crime,date_of_crime,date_of_entry,no_of_witnesses from criminals order by Age ASC")
        mycursor.execute(sql)
        myrecords= mycursor.fetchall()
        for x in myrecords:
            print(x)
        mydb.commit()
    elif choice4=="2":
        sql2=("select id,Name,Age,crime,date_of_crime,date_of_entry,no_of_witnesses from criminals order by Age DESC")
        mycursor.execute(sql2)
        myrecords= mycursor.fetchall()
        for x in myrecords:
            print(x)
        mydb.commit()
    else:
       print("Wrong input")
def twentyfour():
    while True:
        print("Select the column you want to update:")
        print("1.Name")
        print("2.Age")
        print("3.Crime")
        print("4.Date Of Crime")
        print("5.Date of entry")
        print("6.Number of witnesses")
        print("7.Exit")
        choice= int(input("What's your choice?(1-7)\nAnswer: "))
        if choice==1:
            updname()
        elif choice==2:
            updage()
        elif choice==3:
            updcrime
        elif choice==4:
            upddateofc
        elif choice==5:
            updentry
        elif choice==6:
            updwitness()
        elif choice==7:
            print("Exiting")
            break
    def updname():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="rohan",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender whose record is to be updated")
    c1=input("Enter the ID Number:")
    c2=input("Enter New Name:")
    info=(c2,c1)
    sql=("update criminals set Name= %s where id= %s ")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Data Updated Successfully")

    def updage(): 
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="rohan",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender whose record is to be updated")
    c1=input("Enter the ID Number:")
    c2=input("Enter New Age:")
    info=(c2,c1)
    sql=("update criminals set Age= %s  where id= %s ")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Data Updated Successfully")

    def updcrime(): 
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="rohan",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender whose record is to be updated")
    c1=input("Enter the ID Number:")
    c2=input("Enter New Crime:")
    info=(c2,c1)
    sql=("update criminals set crime= %s where id= %s ")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Data Updated Successfully")
        
    def upddateofc(): 
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="rohan",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender whose record is to be updated")
    c1=input("Enter the ID Number:")
    c2=input("Enter New Date of crime:")
    info=(c2,c1)
    sql=("update criminals set date_of_crime='%s' where id='%s'")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Data Updated Successfully")

    def updentry(): 
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="rohan",database="crime")
    mycursor=mydb.cursor()
    print("Enter the ID Number of the offender whose record is to be updated")
    c1=input("Enter the ID Number:")
    c2=input("Enter Date of entry:")
    info=(c2,c1)
    sql=("update criminals set date_of_entry='%s' where id= %s ")
    mycursor.execute(sql,info)
    mydb.commit()
    print("Data Updated Successfully")
    def updwitness():
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="rohan",database="crime")
        mycursor=mydb.cursor()
        print("Enter the ID Number of the offender whose record is to be updated")
        c1=input("Enter the ID Number:")
        c2=input("Enter New Number Of Witnesses:")
        info=(c2,c1)
        sql=("update criminals set no_of_witnesses= %s  where id= %s ")
        mycursor.execute(sql,info)
        mydb.commit()
        print("Data Updated Successfully")
