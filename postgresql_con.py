import psycopg2


#establishing the connection
conn = psycopg2.connect(
   database="django", user='postgres', password='suresh', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection



def create_tables():
    """ create tables in the PostgreSQL database"""
    command = 
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """
    cursor.execute(command)
    cursor.close()


if __name__ == '__main__':
    create_tables()
