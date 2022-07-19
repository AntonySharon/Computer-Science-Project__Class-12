import winsound

from datetime import *

import time

import os

print("\n\t\t PROVIDE YOUR MySQL PASSWORD AND USERNAME")

u=input('\n\t\t\t Enter SQL USERNAME :')

pas=input('\n\t\t\t Enter SQL PASSWORD :')
        
os.system("cls")

import mysql.connector as mysql

mcon=mysql.connect(host='localhost',user=u,passwd=pas)

mcur=mcon.cursor()

mcur1=mcon.cursor()

mcur2=mcon.cursor()

mcur.execute("create database if not exists project")

mcur.execute("use project")

print("******************************************************************************")

print("------------------------------- Welcome To -----------------------------------")

print("--------------------------- GRAVITY SMARTPHONES ------------------------------")

#input_details table
try:

    mcur.execute('create table input_details(name1 varchar(20),name2 varchar(20),phone_number varchar(12),place varchar(20),phone_name varchar(20),model_number int)') 

except:

    pass

#order_details table
try:

    mcur.execute('create table order_details(date_of_order varchar(15),name1 varchar(20),name2 varchar(20),phone_number varchar(12),place varchar(20))') 

except:

    pass

#mobile_services table
try:
    
    mcur1.execute('create table mobile_services(s_no int,service_type char(30),cost int,service_charge int,total int)')

    mcur1.execute('insert into mobile_services values(1,"Protection Glass           ",300 ,50 , 350 )')

    mcur1.execute('insert into mobile_services values(2,"Display Replacement        ",1500,100, 1600)')

    mcur1.execute('insert into mobile_services values(3,"Battery Replacement        ",2000,100, 2100)')

    mcur1.execute('insert into mobile_services values(4,"Camera Lens Change         ",6000,200, 6200)')

    mcur1.execute('insert into mobile_services values(5,"ChargingPort Repair        ",1000,100, 1100)')
        
    mcur1.execute('insert into mobile_services values(6,"Speaker Repair             ",1500,100, 1600)')

    mcur1.execute('insert into mobile_services values(7,"Warranty Extension         ",3500,0  , 3500)')

    mcur1.execute('insert into mobile_services values(8,"Complete Mobile Maintenance",5000,0  , 5000)')

    mcon.commit()

except:

    pass

def add_det():
    #add details

    os.system("cls")

    winsound.PlaySound("SystemQuestion",winsound.SND_ASYNC)

    c=input("\n WOULD YOU LIKE TO SEE THE EXISTING SERVICES (y/n)---- :")

    print('')

    if c=='y' or c=='Y':
        
        mcur1.execute('select * from mobile_services')

        print("")

        print('{:<7}'.format('S.No'),'{:<28}'.format('Service Type'),'{:<7}'.format('Cost'),'{:<12}'.format('Service Charge'),'{:>11}'.format("Total"))

        print("")

        while True:

            try:

                b=mcur1.fetchone()
                
                print('{:<7}'.format(b[0]),'{:<28}'.format(b[1]),'{:<7}'.format(b[2]),'{:>11}'.format(b[3]),'{:>14}'.format(b[4]))
                    
                print('')

            except:

                break
        
    e=input("\n PRESS ENTER TO PROCEED TO ADDING DETAILS ")
    
    s_no=int(input("\n ENTER THE SERVICE NUMBER :"))
    
    service_type=input("\n ENTER THE SERVICE TYPE :")

    cost=int(input("\n ENTER THE COST :"))

    service_charge=int(input("\n ENTER THE SERVICE CHARGE :"))

    total=cost+service_charge

    mcur1.execute("insert into mobile_services values(%s,%s,%s,%s,%s)",(s_no,service_type,cost,service_charge,total,))

    mcon.commit()

    winsound.PlaySound("SystemQuestion",winsound.SND_ASYNC)

    c=input("\n WOULD YOU LIKE TO SEE THE SERVICES AFTER EDITING (y/n) :")

    print('')

    os.system("cls")

    if c=='y' or c=='Y':
         
        mcur2.execute('select * from mobile_services')

        print("")
        
        print('{:<7}'.format('S.No'),'{:<28}'.format('Service Type'),'{:<7}'.format('Cost'),'{:<12}'.format('Service Charge'),'{:>11}'.format("Total"))

        print("")

        while True:

            try:

                b=mcur2.fetchone()
                
                print('{:<7}'.format(b[0]),'{:<28}'.format(b[1]),'{:<7}'.format(b[2]),'{:>11}'.format(b[3]),'{:>14}'.format(b[4]))
                    
                print('')

            except:

                break
            
    else:

        print("\n\t\t PRESS ENTER IF YOU LIKE TO PROCEED")

        #opt=input("\n\t\t Do You Want to continue....?(y/n) :")

def del_det():
    #delete details

    winsound.PlaySound("SystemQuestion",winsound.SND_ASYNC)
    
    c=input("\n WOULD YOU LIKE TO SEE THE EXISTING SERVICES (y/n) :")

    if c=='y' or c=='Y':
        
        mcur2.execute('select * from mobile_services')

        print("")

        print('{:<7}'.format('S.No'),'{:<28}'.format('Service Type'),'{:<7}'.format('Cost'),'{:<12}'.format('Service Charge'),'{:>11}'.format("Total"))

        print("")

        while True:

            try:

                b=mcur2.fetchone()
                
                print('{:<7}'.format(b[0]),'{:<28}'.format(b[1]),'{:<7}'.format(b[2]),'{:>11}'.format(b[3]),'{:>14}'.format(b[4]))
                    
                print('')

            except:

                break
        
    d=int(input("\n\t\t ENTER THE SERVICE NUMBER YOU WANT TO DELETE :"))

    mcur2.execute("delete from mobile_services where s_no=%s",(d,))

    mcon.commit()

    c=input("\n WOULD YOU LIKE TO SEE THE SERVICES AFTER DELETING (y/n) :")

    if c=='y' or c=='Y':
        
        mcur2.execute('select * from mobile_services')
        
        print('')

        print('{:<7}'.format('S.No'),'{:<28}'.format('Service Type'),'{:<7}'.format('Cost'),'{:<12}'.format('Service Charge'),'{:>11}'.format("Total"))

        print("")

        while True:

            try:

                b=mcur2.fetchone()
            
                print('{:<7}'.format(b[0]),'{:<28}'.format(b[1]),'{:<7}'.format(b[2]),'{:>11}'.format(b[3]),'{:>14}'.format(b[4]))
                
                print('')

            except:

                break

def ser_details():

    mcur1.execute('select * from mobile_services')

    print('')

    print('{:<7}'.format('S.No'),'{:<28}'.format('Service Type'),'{:<7}'.format('Cost'),'{:<12}'.format('Service Charge'),'{:>11}'.format("Total"))

    print("")

    while True:

        try:

            b=mcur1.fetchone()
            
            print('{:<7}'.format(b[0]),'{:<28}'.format(b[1]),'{:<7}'.format(b[2]),'{:>11}'.format(b[3]),'{:>14}'.format(b[4]))
                
            print('')

        except:

            break
            

def order():

    #details of customer

    print("\n REDIRECTING TO CUSTOMER INPUT PAGE .... ")

    time.sleep(2)

    os.system('cls')

    n1=input("\n\t Enter your first name :")

    n2=input("\n\t Enter your second name :")

    no=input("\n\t Enter your Phone Number :")#mistake

    place=input("\n\t Enter your Place :")

    pname=input("\n\t Enter your Smart Phone Name :")

    model=input("\n\t Enter your Phone Model Number :")

    #placing order

    print("\n\t REDIRECTING TO PLACING ORDER PAGE .... ")

    time.sleep(3)

    os.system('cls')
    
    o=int(input("\n\t ENTER YOUR DESIRED ITEM NUMBER :"))

    q=int(input("\n\t ENTER DESIRED NUMBER OF QUANTITY :"))
    
    print('\n\t ===== DETAILS YOU HAVE ENQUIRED IS AS FOLLOWS ===== \n')

    today=date.today()
    
    #writing into order details

    mcur.execute("insert into input_details values(%s,%s,%s,%s,%s,%s)",(n1,n2,no,place,pname,model,))

    mcur2.execute("insert into order_details values(%s,%s,%s,%s,%s)",(today,n1,n2,no,place,))
    
    mcon.commit()#writing
    
    mcur.execute("select * from mobile_services where s_no=%s",(o,))

    print("")

    print('{:<7}'.format('S.No'),'{:<28}'.format('Service Type'),'{:<7}'.format('Cost'),'{:<12}'.format('Service Charge'),'{:>11}'.format("Total"))

    print("")

    while True:

        try:

            b=mcur.fetchone()
            
            print('{:<7}'.format(b[0]),'{:<28}'.format(b[1]),'{:<7}'.format(b[2]),'{:>11}'.format(b[3]),'{:>14}'.format(b[4]))
                
            print('')

        except:

            break
    
    print("\n\t !!! SUCCESSFULLY PLACED YOUR ORDER !!!")
    
    mcur1.execute("select total from mobile_services where s_no=%s",(o,))

    winsound.PlaySound("SystemQuestion",winsound.SND_ASYNC)
    
    print('{:>9}'.format('\n\t  TOTAL PRICE :'),end='')
    
    e=mcur1.fetchall()
    
    for j in e:
        
        for k in j:
            
            print('{:>9}'.format(k*q),end='')

            print("\n\n\t  Date of Order :",today)

        print('\n')

    
def cust_hist():

    today=date.today()

    ot='y' or 'Y'

    while ot=='y' or ot=='Y':

        print("\n\t\t CHOOSE YOUR OPTION PLEASE .... ")

        print("\n\t\t 1. SEE TODAYS ORDER HISTORY ")

        print("\n\t\t 2. SEE ORDER HISTORY OF ANOTHER DAYS ")

        p=int(input("\n\t\t CHOOSE YOUR CHOICE PLEASE(1/2) :"))

        if p==1:

            mcur2.execute("select * from order_details where date_of_order=%s",(today,))

            print("")

            print('{:<15}'.format("Date"),'{:<15}'.format("First Name"),'{:<15}'.format("Last Name"),'{:<12}'.format("Phone No."),'{:<12}'.format("Place"))

            print("")

            while True:

                try:

                    b=mcur2.fetchone()
            
                    print('{:<15}'.format(b[0]),'{:<15}'.format(b[1]),'{:<15}'.format(b[2]),'{:<12}'.format(b[3]),'{:<12}'.format(b[4]))
                
                    print('')

                except:

                    break

        elif p==2:

            d=input("\n\t Enter the Desired Date (yyyy-mm-dd) :")

            mcur2.execute("select * from order_details where date_of_order=%s",(d,))

            print("")

            print('{:<15}'.format("Date"),'{:<15}'.format("First Name"),'{:<15}'.format("Last Name"),'{:<12}'.format("Phone No."),'{:<12}'.format("Place"))

            print("")

            while True:

                try:

                    b=mcur2.fetchone()
            
                    print('{:<15}'.format(b[0]),'{:<15}'.format(b[1]),'{:<15}'.format(b[2]),'{:<12}'.format(b[3]),'{:<12}'.format(b[4]))
                
                    print('')

                except:

                    break
            

        ot=input("\n Do yo want to stay in customer history page ...?(y/n) :")

        os.system("cls")
               
            



opt='y' or 'Y'
        
while opt=='y' or opt=='Y':

    print("\n\t\t CHOOSE YOUR LOGIN TYPE")

    print("\n\t\t 1. ADMIN LOGIN ")

    print("\n\t\t 2. CUSTOMER LOGIN ")

    p=int(input("\n\t\t CHOOSE YOUR CHOICE PLEASE :"))

    os.system("cls")

    if p==1:

        u=input("\n\t\t ENTER USERNAME :")
    
        pw=input("\n\t\t ENTER PASSWORD :")

        if (u=="admin" or u=="ADMIN") and pw=="1234":

            os.system("cls")

            o='y' or 'Y'
        
            while o=='y' or o=='Y':

                print("\n\t\t 1. ADD DETAILS ")

                print("\n\t\t 2. DELETE DETAILS ")

                print("\n\t\t 3. PURCHASE HISTORY DETAILS ")

                ch=int(input("\n\t\t ENTER YOUR CHOICE PLEASE :"))

                os.system("cls")    

                if ch==1:

                    add_det()

                elif ch==2:

                    del_det()

                elif ch==3:

                    cust_hist()

                o=input("\n Do You Want to stay in Admin Page ....?(y/n) :")

        else:

            winsound.PlaySound("SystemQuestion",winsound.SND_ASYNC)
            
            print("\n\t\t SORRY!!! YOUR USERNAME OR PASSWORD WENT WRONG")

            print("\n\t\t PLEASE TRY AGAIN !!!.....")
            
    elif p==2:
        
        op='y' or 'Y'
        
        while op=='y' or op=='Y':

            print("\n=============================================================================")
            
            print("\n\t\t GRAVIY SMARTPHONE SERVICE LIST ")
            
            print("\n\t\t 1. OUR SERVICES ")
            
            print("\n\t\t 2. PLACE YOUR ORDER ")

            print("\n\t\t 3. ABOUT US ")
            
            c=int(input("\n\t\t ENTER YOUR CHOICE(1/2/3) :"))
            
            if c==1:

                ser_details()
                
            elif c==2:
                
                order()

            elif c==3:

                print("\n Gravity Smartphones is an established company since 1989.\n Our company provides with differebt samrtphone services throughout India and   also have our branches in 10 different countries.\n The motive of our company is to provide best and trusting services to our      customers.\n Our company specialises in most of the smartphone brands and we have our       staffs well trained to do out their job.")

            op=input("\n Do You Want to Stay in Customer Page....?(y/n) :")

            os.system("cls")

            continue

    else:

        continue

    opt=input("\n Do You Want To Continue Our Services....?(y/n) :")

    os.system("cls")

print("\n\t\t ==== THANK YOU FOR USING OUR SERVICES ===== ")
