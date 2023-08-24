import psycopg2
import os


# Read SQL script from the file
with open("script.sql", "r") as file:
    sql_script = file.read()


try:
    # Replace with your database connection details
    connection = psycopg2.connect(
        database=os.getenv("RDS_DATABASE"),
        user=os.getenv("RDS_USERNAME"),
        password=os.getenv("RDS_PASSWORD"),
        host=os.getenv("RDS_HOST"),
        port=os.getenv("RDS_PORT")
    )
    
    # Create a cursor
    cursor = connection.cursor()

    # Execute the SQL script
    cursor.execute(sql_script)
    
    # Commit the changes
    connection.commit()
    print("SQL script executed successfully!")

except Exception as e:
    # Rollback in case of an error
    connection.rollback()
    print("Error:", e)

finally:
    # Close the connection and cursor
    cursor.close()
    connection.close()