from create import insert
from read import read
from update import update
from delete import delete

obj=insert()
objread=read()
objupdate=update()
objdelete=delete()
print("------------- Bank Management System ---------------")
print("For Inserting the data press 1 : ")
print("For Reading the data press 2 : ")
print("For Updating the data press 3 : ")
print("For Deleting the data press 4 : ")

opr = int(input("Please enter your operation: "))

def myopr():
    print("---- For Personal information press 1 ----")
    print("---- For Bank details press 2 ------------")
    print("---- For transistion details press 3 -----")
    print("---- For Account details press 4 ---------")
    vr = int(input("Please Select your table : "))
    if vr == 1:
        return 'personaldetails'
    elif vr ==2:
        return 'bankdetails'
    elif vr ==3:
        return 'transistiondetails'
    elif vr ==4:
        return 'accountdetails'
if opr==1:
    h=myopr()
    if h =="personaldetails":
        

        cid = int(input("please enter customer id:"))
        fname = input("please enter customer first name:")
        lname = input("please enter customer last name:")
        addr = input("please eneter customer address:")
        pn = int(input("please enter customer phone number:"))
        an = input("please enter customer aadhar number:")
        pan = input("please enter customer pan number:")

        obj.personaldetails(cid,fname,lname,addr,pn,an,pan)
    elif h=='bankdetails':
        acn = int(input("please enter account number:"))
        cid = int(input("please enter customerid:"))
        ifsc = input("please enter ifsc code:")
        actype = input("please enter account type:")
        obj.bankdetails(acn,cid,ifsc,actype)  
    elif h=='transistiondetails':
        transid=int(input("please enter transistion id:"))
        senderacc=int(input("please enter sender account no:"))
        receiveracc=int(input("please enter receiver account no:"))
        amount=int(input("please enter amount:"))
        method=input("please enter method:")
        obj.transistiondetails(transid,senderacc,receiveracc,amount,method)
    elif h=="accountdetails":
        acn=int(input("please enter account number:"))
        transid=int(input("please enter transistion id:"))
        amount=int(input("please enter amount:"))
        clsb=int(input("please enter closingbalance:"))
        transtype=input("please enter transistion type:")
        obj.accountdetails(acn,transid,amount,clsb,transtype)

if opr==2: # user wanted to read the data
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    print(objread.specific_info(cusid,j))

if opr==3:
    j=myopr()
    cusid=int(input("please enter customer id for fetching data"))
    colname=input("please enter column name:")
    newval=input("please enter new values:")
    objupdate.myupdate(j,colname,newval,cusid)

if opr==4:
    k=myopr()
    cusid=int(input("please enter customer id to delete the data:"))
    objdelete.specific_del(k,cusid)