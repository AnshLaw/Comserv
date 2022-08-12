import pickle
import os
import random
import tabulate
import string
import pyfiglet
import mysql.connector
import smtplib
import datetime

con=mysql.connector.connect(host='localhost',password='BRAIN',user='root', buffered=True)
cur=con.cursor()
try:
        cur.execute('create database comserv')
except:
        pass
cur.execute('use comserv')
def Create():
        try:
                cur.execute('create table server(ID int(4) PRIMARY KEY,Name varchar(20),Email varchar(40),Age int(2),Mobile_No bigint,Verified varchar(3),Roles varchar(20), Date_of_Joining date)')
                print("Table Created")
                
        except:
                print("Table Exist")
                
def Insert():
    query="insert into server values({},'{}','{}',{},{},'{}','{}','{}')".format(id,name,email,age,phone,v,ro,doj)
    cur.execute(query)
    con.commit()

def SortSQL():
    s=int(input("Enter your choice: 1)ID/ 2)Name/ 3)Age/ 4)Verification/ 5)Date_of_Joining:"))
    order=int(input("Enter your choice: 1)Ascending Order/ 2)Descending Order:"))
    if s==1 and order==1:
        q="select*from server order by ID"
        cur.execute(q)
        con.commit()
        data=cur.fetchall()
        table = tabulate.tabulate(data, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
        print(table)
    if s==1 and order==2:
            qu="select*from server order by ID desc"
            cur.execute(qu)
            con.commit()
            data=cur.fetchall()
            table = tabulate.tabulate(data, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
            print(table)
    if s==2 and order==1:
        q1="select*from server order by Name"
        cur.execute(q1)
        con.commit()
        dn=cur.fetchall()
        table = tabulate.tabulate(dn, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
        print(table)
    if s==2 and order==2:
            qu1="select*from server order by Name desc"
            cur.execute(qu1)
            con.commit()
            data=cur.fetchall()
            table = tabulate.tabulate(data, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
            print(table) 
    if s==3 and order==1:
        q2="select*from server order by Age"
        cur.execute(q2)
        con.commit()
        dv=cur.fetchall()
        table = tabulate.tabulate(dv, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
        print(table)
    if s==3 and order==2:
            qu2="select*from server order by Age desc"
            cur.execute(qu2)
            con.commit()
            data=cur.fetchall()
            table = tabulate.tabulate(data, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
            print(table)
    if s==4 and order==1:
        q3="select*from server order by Verified"
        cur.execute(q3)
        con.commit()
        dj=cur.fetchall()
        table = tabulate.tabulate(dj, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
        print(table)
    if s==4 and order==2:
            qu3="select*from server order by Verified desc"
            cur.execute(qu3)
            con.commit()
            data=cur.fetchall()
            table = tabulate.tabulate(data, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
            print(table)
    if s==5 and order==1:
            qu4="select*from server order by Date_of_Joining"
            cur.execute(qu4)
            con.commit()
            data=cur.fetchall()
            table = tabulate.tabulate(data, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
            print(table)
    if s==5 and order==2:
            qu5="select*from server order by Date_of_Joining desc"
            cur.execute(qu5)
            con.commit()
            data=cur.fetchall()
            table = tabulate.tabulate(data, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
            print(table)
            
def ShowSQL():
        global sc
        Q="select*from server"
        cur.execute(Q)
        con.commit()
        ds=cur.fetchall()
        print("*********************************************************************************************************")
        table = tabulate.tabulate(ds, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
        print(table)
        
def ShowmemSQL():
        Q="select*from server where ID={}".format(id,)
        cur.execute(Q)
        con.commit()
        ds=cur.fetchall()
        print("*********************************************************************************************************")
        table = tabulate.tabulate(ds, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
        print(table)
                
def SearchSQL():
    global cho
    cho=int(input("Enter your choice(1.ID/2.Roles/3.Date of joining):"))
    if cho==1:
        global se
        se=int(input("enter the id to be searched:"))
        q4="select*from server where ID={}".format(se,)
        cur.execute(q4)
        con.commit()
        dss=cur.fetchall()
        print("*********************************************************************************************************")
        table = tabulate.tabulate(dss, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
        print(table)
        
    if cho==2:
        global role
        role=input("enter the role to be searched:")
        q5="select*from server where Roles='{}'".format(role,)
        cur.execute(q5)
        con.commit()
        dss=cur.fetchall()
        print("*********************************************************************************************************")
        table = tabulate.tabulate(dss, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
        print(table)
    if cho==3:
        global doj
        doj=input("enter the date of joining to be searched(yyyy-mm-dd):")
        q6="select*from server where Date_of_Joining='{}'".format(doj,)
        cur.execute(q6)
        con.commit()
        dss=cur.fetchall()
        print("*********************************************************************************************************")
        table = tabulate.tabulate(dss, headers=['ID', 'Name', 'Email', 'Age', 'Mobile No.', 'Verified', 'Roles', 'Date of Joining'], tablefmt='psql')
        print(table)
            
def UpdateSQL():
    global u
    u=int(input("enter the server id to be updated:"))
    global name
    global email
    global age
    global phone
    global ro
    c=input("Do you want to update your name?:")
    if c=='y' or c=='Y':
            name=input("Enter new name:")
            q7="update server set Name='{}' where ID={}".format(name,u)
            cur.execute(q7)
            con.commit()
    else:
            pass
    c=input("Do you want to update your email?:")
    if c=='y' or c=='Y':
            email=input("Enter new email:")
            q8="update server set Email='{}' where ID={}".format(email,u)
            cur.execute(q8)
            con.commit()
    else:
            pass
    c=input("Do you want to update your age?:")
    if c=='y' or c=='Y':
            age=int(input("Enter new age:"))
            q9="update server set Age={} where ID={}".format(age,u)
            cur.execute(q9)
            con.commit()
    else:
            pass
    c=input("Do you want to update your phone no.?:")
    if c=='y' or c=='Y':
            phone=int(input("Enter new phone no:"))
            q10="update server set Mobile_No={} where ID={}".format(phone,u)
            cur.execute(q10)
            con.commit()
    else:
            pass
    c=input("Do you want to update your role?:")
    if c=='y' or c=='Y':
            ro=input("Enter role of person:")
            q11="update server set Roles='{}' where ID={}".format(ro,u)
            cur.execute(q11)
            con.commit()
    else:
            pass
    print("Table Records updated...")

def DeleteSQL():
    q12="delete from server where ID={}".format(d,)
    cur.execute(q12)
    con.commit()
    print("Table Record deleted...")

def CredSQL():
        try:
                cur.execute('create table cred(Email_ID varchar(40) PRIMARY KEY, Password varchar(30), ID int(4), Designation varchar(6))')
                print("Table Created")
        except:
                print("Table Exist")
def InsSQL():
        Q2="insert into cred values('{}','{}',{},'{}')".format(user,password,id,desig)
        cur.execute(Q2)
        con.commit()

def delete():
    f = open("idfile","rb")
    l=pickle.load(f)
    f.close()
    global d
    d = int(input("Enter the id of member to be deleted:"))
    f = open("Temp","wb")
    k=[]
    for i in l:
        if i[0]==d:
            continue
        k.append(i)
    pickle.dump(k,f)
    f.close()
    os.remove("idfile")
    os.rename("Temp","idfile")
    DeleteSQL()
            
def code(l):
    global v
    global result
    key = string.ascii_letters + string.digits
    result=''.join((random.choice(key) for i in range(l)))


def chk1():
    global id
    print("ID already in use...try a different one")
    id=int(input("Enter a different id:"))
    f=open("cred","rb")
    try:
        while True:
            A=pickle.load(f)
            for i in A:
                if i[2]==id:
                        chk1()
                else:
                    continue
    except EOFError:
        pass
    except pickle.UnpicklingError:
        pass
    f.close()

        
def chk():
    global id
    print("ID already in use...try a different one")
    id=int(input("Enter a different id:"))
    f=open("idfile","rb")
    try:
        while True:
            A=pickle.load(f)
            for i in A:
                if i[0]==id:
                        chk()
                else:
                    continue
    except EOFError:
        pass
    except pickle.UnpicklingError:
        pass
    f.close()



def addmem():
        ch='y'
        Rec=[]
        f1=open("idfile","ab")
        while True:
                global id
                id=int(input("Enter your Server ID(XXXX):"))
                if len(str(id))!=4:
                        id=int(input("Enter a 4-digit Server ID(XXXX):"))
                try:
                        f=open("idfile","rb")
                        while True:
                            A=pickle.load(f)
                            for i in A:
                                if i[0]==id:
                                        chk()
                                else:
                                    continue
                        f.close()
                except EOFError:
                    pass
                except pickle.UnpicklingError:
                    pass
                        
                global name
                name=input("Enter your name:")
                global email
                email=input("Enter your email address:")
                if '@' not in email or '.' not in email:
                    print("Invalid email address")
                    email=input("Enter correct email address(use @ or .):")
                else:
                    pass
                global age
                age=int(input("Enter your age:"))
                global phone
                phone=input("Enter your mobile no.:")
                if len(phone)!=10 or phone.isdigit()==False:
                    print("Please enter valid Mobile No")
                    p=int(input("Enter valid phone no.:"))
                else:
                    pass
                global v
                v="no"
                global ro
                ro=input("Enter role of person:")
                global doj
                x=datetime.date.today()
                doj=x.strftime("%Y-%m-%d")
                R=[id,name,email,age,phone,v,ro,doj]
                Rec.append(R)
                Insert()
                ch=input("Enter more?(Y/N)")
                if ch=='n' or ch=='N':
                        pickle.dump(Rec,f1)
                        print("Member(s) added succesfully...:)")
                        break
                else:
                        continue
        f1.close()

def addmem1():
        Rec=[]
        f1=open("idfile","ab")
        global id
        id=int(input("Enter your Server ID(XXXX):"))
        if len(str(id))!=4:
                id=int(input("Enter a 4-digit Server ID(XXXX):"))
        try: 
                f=open("idfile","rb")
                while True:
                        A=pickle.load(f)
                        for i in A:
                                if i[0]==id:
                                        chk()
                                else:
                                    continue
                f.close()
        except EOFError:
                pass
        except pickle.UnpicklingError:
                pass
                        
        global name
        name=input("Enter your name:")
        global email
        email=input("Enter your email address:")
        if '@' not in email or '.' not in email:
                print("Invalid email address")
                email=input("Enter correct email address(use @ or .):")
        else:
                pass
        global age
        age=int(input("Enter your age:"))
        global phone
        phone=input("Enter your mobile no.:")
        if len(phone)!=10 or phone.isdigit()==False:
                print("Please enter valid Mobile No")
                p=int(input("Enter valid phone no.:"))
        else:
                pass
        global v
        v="no"
        global ro
        ro=input("Enter role of person:")
        global doj
        x=datetime.date.today()
        doj=x.strftime("%Y-%m-%d")
        R=[id,name,email,age,phone,v,ro,doj]
        Rec.append(R)
        Insert()
        pickle.dump(Rec,f1)
        print("Member added succesfully...:)")
        f1.close()

def Feed():
     
     f=pyfiglet.figlet_format("Thank You for using Comserv", font="standard")
     print(f)
     print("Your Feedback is valuable and confidential.")
     star=input("How many stars would you give to Comserv?(*->*****):")
     if star=="*" or star=="**":
         print("We will surely try to get better pls provide us with your suggestions...:)")
         feed=input("Suggestions:")
         f2=open("Feedback.txt","a")
         f2.write("Suggestions:")
         f2.write('\n')
         f2.write('>')
         f2.write(feed)
         f2.write('\n')
         f2.close()
     elif star=="***" or star=="****":
         print("We truly appreciate your rating....:)")
         ask=input("Would you like to provide any suggestions?(Y/N):")
         if ask=="n" or ask=="N":
             pass
         else:
             feed=input("Suggestions:")
             print("Thank you for your time...:)")
             f2=open("Feedback.txt","a")
             f2.write("Suggestions:")
             f2.write('\n')
             f2.write('>')
             f2.write(feed)
             f2.write('\n')
             f2.close()
     elif star=="*****":
         print("We feel highly obliged in serving you...thank you!")
     else:
         print("Thank You")

     print("For any assistance contact:- comserv.team@gmail.com")

def Email():
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    uid=input("Enter your email address:")
    pas=input("Enter your password:")
    s.login(uid,pas)
    to=input("Enter receiver's email address:")
    msg=input("Enter your message:")
    s.sendmail(uid,to,msg)
    s.quit
    print("Email sent successfully...")


def helper():
        u=pyfiglet.figlet_format("Help & Support", font="speed")
        print(u)
        print("1: Register:-")
        print("Use this option to register yourself in the Comserv community system. You will be asked to enter your email id and password and automatically a verification will run for you to register.")
        print("2: Login:-")
        print("Use this option to login into the server using your registered email id and password only.")
        print("3: Feedback:-")
        print("Use this option to provide us feedback about our community server management system 'Comserv'\n\n")
        print("For furthur information and support contact:- comserv.team@gmail.com")
        print("Once again thank you for using Comserv...:)")
        
def H():
        u=pyfiglet.figlet_format("Help & Support", font="speed")
        print(u)
        print("1: Add Info:-")
        print("Use this option to add your information in the server. Various fields are available to enter records. For server id make sure it is 4-digit and unique.\n If id is not unique you would be prompted with the same message.")
        print("2: My records:-")
        print("Use this option to get the list of your records in the server. You can always access tables in MySQL using 'comserv' database and 'server' table.")
        print("3: Update my records:-")
        print("Use this option to update your details and accordingly results will be shown.")
        print("4: Verification:-")
        print("Use this option to get verified as a real person and prove that you are not a robot.")
        print("5: Messaging and Email:-")
        print("Use this option to send emails to members using their email ids through this option. If error occurs please see to it that your google account has given access to less secure apps. Also if you have enabled 2 factor verification, go to google account settings and use the app related password generated rather than your account password.")
        print("For furthur information and support contact:- comserv.team@gmail.com")
        print("Once again thank you for using Comserv...:)")
        
def Help():
        u=pyfiglet.figlet_format("Help & Support", font="speed")
        print(u)
        print("1: Add members:-")
        print("Use this option to add members in your server. Various fields are available to enter records. For server id make sure it is 4-digit and unique.\n If id is not unique you would be prompted with the same message.")
        print("2: Show members:-")
        print("Use this option to get the list of all members in the server. You can always access tables in MySQL using 'comserv' database and 'server' table.")
        print("3: Sort:-")
        print("Use this option to sort members according to ID, name and verification. Accordingly results will be shown by using Show members option.")
        print("4: Search Members:-")
        print("Use this option to search members using their server IDs or roles.")
        print("5: Update Member Records:-")
        print("Use this option to update details of members and accordingly results will be shown.")
        print("6: Remove Members:-")
        print("Use this option to remove existing members from the server.")
        print("7: Verification:-")
        print("Use this option to get verified as a real person and prove that you are not a robot.")
        print("8: Messaging and Email:-")
        print("Use this option to send emails to members using their email ids through this option. If error occurs please see to it that your google account has given access to less secure apps. Also if you have enabled 2 factor verification, go to google account settings and use the app related password generated rather than your account password.")
        print("9: Feedback:-")
        print("Use this option to provide us feedback about our community server management system 'Comserv'\n\n")
        print("For furthur information and support contact:- comserv.team@gmail.com")
        print("Once again thank you for using Comserv...:)")  

def About():
        u=pyfiglet.figlet_format("Comserv", font="speed")
        print(u)
        print("Comserv is a community management server system developed by Ansh Raj Suryavanshi, supporting a database for various community platforms like MS Teams, Zoom, Discord and Telegram etc. Comserv helps you to keep track of your members and handle their info. with ease. Comserv uses mailing services for communication among server clients and provides supreme authority to administrators.")
        print("For furthur information and support contact:- comserv.team@gmail.com")
        print("Once again thank you for using Comserv...:)")  


def Cpass():
    global password
    global cpass
    password=input('Create Your Password:')
    cpass=input('Confirm Your Password:')
    if password==cpass:
        pass
    else:
        print("Password didn't match.....")
        Cpass()
def checker():
    print("Username already in use...try a different one")
    user=input("Enter a different email address:")
    f3=open("cred","rb")
    try:
        while True:
            A=pickle.load(f3)
            for i in A:
                if i[0]==user:
                    checker()
                else:
                    continue
        
    except EOFError:
        pass
    except pickle.UnpicklingError:
        pass
    f3.close()

def checkAdmin():
    print("Invalid email address or password or you are not registered as an Admin..:(")
    uid=input("Enter your valid email address:")
    password=input("Enter your valid password:")
    f=open("cred","rb")
    try:
        while True:
            A=pickle.load(f)
            for i in A:
                    if i[0]==uid and i[1]==password and i[3]=="Admin":
                            print("Logged in successfully.....:)")
                            AdminMenu()
                            
                    else:    
                            checkAdmin()
        
    except EOFError:
        pass
    except pickle.UnpicklingError:
        pass
    f.close()

def checkMem():
    print("Invalid email address or password or you are not registered as an Member..:(")
    uid=input("Enter your valid email address:")
    password=input("Enter your valid password:")
    f=open("cred","rb")
    try:
        while True:
            A=pickle.load(f)
            for i in A:
                    if i[0]==uid and i[1]==password and i[3]=="Member":
                            print("Logged in successfully.....:)")
                            MemMenu()
                            
                    else:    
                            checkMem()
    except EOFError:
        pass
    except pickle.UnpicklingError:
        pass
    f.close()

def Register():
    Rec=[]
    f2=open("cred","ab")
    global user
    user=input("Enter your email address:")
    if '@' not in user or '.' not in user:
                print("Invalid email address")
                user=input("Enter correct email address(use @ or .):")
    try:
    
        f3=open("cred","rb")
        while True:
            A=pickle.load(f3)
            for i in A:
                if i[0]==user:
                    checker()                              
                else:
                    continue
        f3.close()
    except EOFError:
        pass
    except pickle.UnpicklingError:
        pass
                        
    global password
    global cpass
    password=input("Create your password:")
    cpass=input("Confirm your password:")
    if password==cpass:
        pass
    else:
        print("Password didn't match....")
        Cpass()
    global id
    id=int(input('Enter your server ID(XXXX):'))
    try:
            f=open("cred","rb")
            while True:
                    A=pickle.load(f)
                    for i in A:
                            if i[2]==id:
                                    chk1()
                            else:
                                    continue
            f.close()
    except EOFError:
            pass
    except pickle.UnpicklingError:
            pass
    global desig
    desig=input("Registering as(Admin/Member):")
    R=[user,password,id,desig]
    print("Verifying email address....")
    print("A verification code has been sent to your inbox, enter it below")
    Verifmail()
    while (cod!=result):
            print("Verification failed....try again")
            print("A verification code has been sent to your inbox, enter it below")
            Verifmail()
    if cod==result:
            print("Verification complete...email verified!")
            Rec.append(R)
            pickle.dump(Rec,f2)
            CredSQL()
            InsSQL()
    f2.close()
                    
def LoginAdmin():
    global uid
    uid=input('Enter your email address:')
    global password
    password=input("Enter your password:")
    found=0
    f=open("cred","rb")
    try:
        while True:
            A=pickle.load(f)
            for i in A:
                if i[0]==uid and i[1]==password and i[3]=="Admin":
                        print("Logged in succesfully.....:)")
                        AdminMenu()
                        found+=1
    except EOFError:
        pass
    except pickle.UnpicklingError:
        pass
    if found==0:
            checkAdmin()
    f.close()

def LoginMem():
    global uid
    uid=input('Enter your email address:')
    global password
    password=input("Enter your password:")
    found=0
    f=open("cred","rb")
    try:
        while True:
            A=pickle.load(f)
            for i in A:
                if i[0]==uid and i[1]==password and i[3]=="Member":
                    print("Logged in successfully.....:)")
                    MemMenu()
                    found+=1
    except EOFError:
        pass
    except pickle.UnpicklingError:
        pass
    if found==0:
            checkMem()
    f.close()
    


def Verifmail():
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    usrid="comserv.team@gmail.com"
    pas="yvmxlgjljltdakai"
    s.login(usrid,pas)
    to=user
    code(6)
    x="Your Comserv verification code is "
    msg=x+result
    s.sendmail(usrid,to,msg)
    s.quit
    print("Email sent successfully...")
    global cod
    cod=input("Enter verification code(sent to your inbox):")

def AdminMenu():
        while True:
                print("*************************************************************************************************************************************************************")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>Welcome To Community Server Management System<<<<<<<<<<<<<<<<<<< <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                a=pyfiglet.figlet_format("Comserv", font="speed")
                b=pyfiglet.figlet_format("Admin Menu", font="speed")
                print(a)
                print("#####################################################################################################################")
                print(b)
                                                   
                print("1: Add Members")
                print("2: Show Members")
                print("3: Sort(Basis of- ID/Name/Age/Verification/Date of joining)")
                print("4: Search Members(Basis of ID/Roles/Date of joining)")
                print("5: Update Member Records")
                print("6: Remove Members")
                print("7: Verification")
                print("8: Messaging and Email")
                print("9: Help & Support")
                print("10: Logout")
                print("\t\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Thank You for Using Comserv<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                ch=input("Enter your Choice:")
                if ch=='1':
                        Create()
                        addmem()
                elif ch=='2':
                        Create()
                        ShowSQL()
                elif ch=='3':
                        SortSQL()
                elif ch=='4':
                        SearchSQL()
                elif ch=='5':
                        UpdateSQL()
                elif ch=='6':
                        delete()
                elif ch=='7':
                        cap=pyfiglet.figlet_format("CAPTCHA", font="speed")
                        print(cap)
                        while True:
                                global e
                                e=int(input("Enter the server ID to verify:"))
                                code(6)
                                print("Code:",result)
                                c=input("Enter the code displayed above:")
                                if c==result:                                                                               
                                        print("You are not a robot....Verification Complete....Member License Activated!!!")
                                        q12="update server set Verified='yes' where ID={}".format(e,)
                                        cur.execute(q12)
                                        con.commit()
                                        break
                                else:                                                                                       
                                        print("Verification Failed...Try again :(")
                elif ch=='8':
                        Email()
                elif ch=='9':
                        Help()
                elif ch=='10':
                        print("You have logged out successfully....:)")
                        break
                        
                else:
                        print("Invalid option......:(")





def MemMenu():
        while True:
                
                print("*************************************************************************************************************************************************************")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>Welcome To Community Server Management System<<<<<<<<<<<<<<<<<<< <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                a=pyfiglet.figlet_format("Comserv", font="speed")
                b=pyfiglet.figlet_format("Member Menu", font="speed")
                print(a)
                print("#####################################################################################################################")
                print(b)
                print("1: Add Info(if not registered yet)")                                   
                print("2: My records")
                print("3: Update my records")
                print("4: Verification")
                print("5: Messaging and Email")
                print("6: Help & Support")
                print("7: Logout")
                print("\t\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Thank You for Using Comserv<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                ch=input("Enter your Choice:")
                if ch=='1':
                      Create()
                      addmem1()
                elif ch=='2':
                        global id
                        id=int(input("Enter your server ID(XXXX):"))
                        ShowmemSQL()
                elif ch=='3':
                        UpdateSQL()
                elif ch=='4':
                        cap=pyfiglet.figlet_format("CAPTCHA", font="speed")
                        print(cap)
                        while True:
                                global e
                                e=int(input("Enter the server ID to verify:"))
                                code(6)
                                print("Code:",result)
                                c=input("Enter the code displayed above:")
                                if c==result:                                                                               
                                        print("You are not a robot....Verification Complete....Member License Activated!!!")
                                        q12="update server set Verified='yes' where ID={}".format(e,)
                                        cur.execute(q12)
                                        con.commit()
                                        break
                                else:                                                                                       
                                        print("Verification Failed...Try again :(")
                elif ch=='5':
                        Email()
                elif ch=='6':
                        H()
                elif ch=='7':
                        print("You have logged out successfully....:)")
                        break
                        
                else:
                        print("Invalid option......:(")


while True:
    
    print("*************************************************************************************************************************************************************")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>Welcome To Community Server Management System<<<<<<<<<<<<<<<<<<< <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    z=pyfiglet.figlet_format("Welcome To Comserv", font="speed")
    y=pyfiglet.figlet_format("Main Menu", font="speed")
    print(z)
    print("#####################################################################################################################")
    print(y)
    print("1: Register")
    print("2: Login")
    print("3: Feedback")
    print("4: Help & Support")
    print("5: About Comserv")
    print("6: Exit")
    print("\t\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Thank You for Using Comserv<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    choice=input("Enter your Choice:")
    if choice=='1':
            Register()
    elif choice=='2':
            c=input("Login as 1. Admin/ 2. Member :")
            if c=='1':
                    LoginAdmin()
            if c=='2':
                    LoginMem()
    elif choice=='3':
            Feed()
    elif choice=='4':
            helper()
    elif choice=='5':
            About()
    elif choice=='6':
            break
    else:
            print('Invalid Option.......:(')
