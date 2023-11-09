# installed library mysql-connector-python
import mysql.connector

#creating connection
class insert:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="vamshi",
            database="bank"
            )
    def personaldetails(self,cid,fname,lname,addr,pn,an,pan):
        cur=self.conn.cursor()
        cur.execute(f"insert into personaldetails values({cid},'{fname}','{lname}','{addr}',{pn},'{an}','{pan}')")
        self.conn.commit()
        print("-------------personal information has saved sucessfully---------------")

    def bankdetails(self,acn,cid,ifsc,actype):
        cur=self.conn.cursor()
        cur.execute(f"insert into bankdetails values({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("------------bank details has been sucessfully saved------------------")

    def transistiondetails(self,transid,senderacc,receiveracc,amount,method):
        cur=self.conn.cursor()
        cur.execute(f"insert into transistiondetails values({transid},{senderacc},{receiveracc},{amount},'{method}')")
        self.conn.commit()
        print("------------transistion details has been sucessfully saved------------------")
    def accountdetails(self,acn,transid,amount,clsb,transtype):
        cur=self.conn.cursor()
        cur.execute(f"insert into accountdetails values({acn},{transid},{amount},'{clsb}','{transtype}')")
        self.conn.commit()
        print("------------account details has been sucessfully saved------------------")