# installed library mysql-connector-python
import mysql.connector

#creating connection 

class read:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "vamshi",
                database = "bank"
                )
    
    def specific_info(self,customer_id,table_name):
        cur = self.conn.cursor()
        if table_name=='personaldetails' or table_name=='bankdetails':
            cur.execute(f"SELECT * FROM {table_name} WHERE CUSTOMER_ID={customer_id}")
            print(cur.fetchall())
        
        if table_name=='transistiondetails':
            cur.execute(f'''select * from transistiondetails where transistion_id in
                (select transistion_id from accountdetails where account_no in
                (select account_no from bankdetails where customer_id={customer_id}));''')
            print(cur.fetchall())