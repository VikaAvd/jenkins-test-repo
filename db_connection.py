import pymssql

def get_db_connection():
    """
    Connect to the SQL Server database using pymssql.
    Adjust the server, user, password, and database values to match your environment.
    
    Note: pymssql does not require an ODBC driver specification.
    """
    conn = pymssql.connect(
        server='host.docker.internal\\SQLEXPRESS01',
        user='robot',
        password='Vika_password123',
        database='TRN'
    )
    return conn


