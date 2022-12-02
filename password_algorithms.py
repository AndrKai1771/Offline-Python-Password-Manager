from random import choice as rc
import mysql.connector as mc
from time import sleep

mydb = mc.connect(host="localhost", username="root", port=3307, password="AndrKai", database="Testcreds")
mycursor = mydb.cursor()


def pass_generator():
    uppercase = []
    lowercase = []
    digits = []
    for i in range(65,91):
        uppercase.append(chr(i))
        lowercase.append(chr(i+32))
        if i - 17 <= 57:
            digits.append(chr(i-17))
            pass
    symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

    pw = ''
    sequence = [1,2,3]
    for i in range(3):
        ch = rc(sequence)
        if ch == 1:
            pw += rc(uppercase) + rc(lowercase) + rc(digits) + rc(symbol)
        elif ch == 2: 
            pw += rc(symbol)+ rc(lowercase) + rc(uppercase) +rc(digits) 
        elif ch == 3:
            pw += rc(digits) + rc(uppercase) + rc(symbol) + rc(lowercase)

    return pw
# a = pass_generator()
# print("-----------------------------------------------------\nA New Strong Password For Your Account => ",a,"\n-----------------------------------------------------",sep="")


def verifier(site:str, uname:str):
    site = site.lower()
    creds = (site, uname)
    mycursor.execute("SELECT site, uname FROM creds WHERE site='{}' AND uname='{}'".format(site, uname))
    result = mycursor.fetchall()

    for i in result:
        if i == creds:
            return True
    else:
        return False 



def adder(site:str, uname:str, pw:str):
    mycursor.execute("INSERT INTO creds(site,uname,password) Values('{0}', '{1}', '{2}')".format(site.lower(), uname, pw))
    mydb.commit()
    return "Password '{0}' For '{1}' As User '{2}' Added To The Database".format(pw, site, uname)


def updater(site:str, uname:str, pw:str):
    mycursor.execute("UPDATE creds SET password='{0}' WHERE (site='{1}' AND uname='{2}')".format(pw, site.lower(), uname))
    mydb.commit()


def pass_retriever(site:str, uname:str):
    mycursor.execute("SELECT password FROM creds WHERE (site='{0}' AND uname='{1}')".format(site.lower(), uname))
    result = mycursor.fetchall()
    for i in result: 
        return i[0]



def deleter(site:str, uname:str):
    mycursor.execute("DELETE FROM creds WHERE (site='{}' AND uname='{}')".format(site.lower(), uname))
    mydb.commit()
    return "User '{}' For '{}' Deleted Successfully"


def data_retriever():
    mycursor.execute("SELECT * FROM creds")
    try:
        while True:
            r = mycursor.fetchone()
            j = 0
            print('-'*30)
            for i in r:
                if j == 0:
                    j += 1
                    continue
                elif j == 1:
                    print('Site: ',i,)
                    j += 1
                elif j == 2:
                    print('Username: ',i) 
                    j += 1
                elif j == 3:
                    print("Password: ", i)   
            sleep(1)
            print('-'*30)
            print()
    except:
        print("All Records Fetched.")
    return 0
    
def admin_command():
    mycursor.execute('DELETE FROM creds')
    mydb.commit()
    return 'All Credentials Deleted'
