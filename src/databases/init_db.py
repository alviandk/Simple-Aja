from . import db_connections

def inititate():
    conn = db_connections.get_db_connection()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute("DROP TABLE IF EXISTS accounts;")
    cur.execute("DROP TABLE IF EXISTS customers;")
    cur.execute(
        "CREATE TABLE accounts ("
            "id serial PRIMARY KEY,"
            "account_number varchar (150) UNIQUE NOT NULL,"
            "customer_number varchar (150) UNIQUE NOT NULL,"
            "balance integer NOT NULL,"
            "date_added date DEFAULT CURRENT_TIMESTAMP"
        ");"
    )
    cur.execute(
        "CREATE TABLE customers ("
            "id serial PRIMARY KEY,"
            "customer_number varchar (150) UNIQUE NOT NULL,"
            "name varchar (150) NOT NULL,"
            "date_added date DEFAULT CURRENT_TIMESTAMP"
        ");"
    )

    # Insert data into the table

    cur.execute(
        f"INSERT INTO accounts (account_number, customer_number, balance)"
        "VALUES (555001, 1001, 10000)"
    )
    cur.execute(
        f"INSERT INTO accounts (account_number, customer_number, balance)"
        "VALUES (555002, 1002, 15000)"
    )

    cur.execute(
        f"INSERT INTO customers (customer_number, name) "
        f"VALUES (1001, 'Bob Martin')"
    )
    cur.execute(
        f"INSERT INTO customers (customer_number, name) "
        f"VALUES (1002, 'Linus Torvalds')"
    )

    conn.commit()

    cur.close()
    conn.close()
    