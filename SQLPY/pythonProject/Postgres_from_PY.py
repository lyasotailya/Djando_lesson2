import psycopg2

con = psycopg2.connect(database='pytest', user='postgres', password='28081974')


def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
                DROP TABLE IF EXISTS Clients_phone;
                DROP TABLE IF EXISTS Clients;
                """)
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Clients (
                Clients_id SERIAL PRIMARY KEY,
                First_name VARCHAR(40) NOT NULL,
                Last_name VARCHAR(40) NOT NULL,
                email VARCHAR(40) NOT NULL,
                phone INTEGER
                );
                """)
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Clients_phone (
                id SERIAL PRIMARY KEY,
                Clients_id INTEGER NOT NULL REFERENCES Clients(Clients_id),
                phone INTEGER
                );
                """)
        conn.commit()
    conn.close()


def add_client(conn, first_name, last_name, email, phone=None):
    with conn.cursor() as cur:
        cur.execute(f"""
                INSERT INTO Clients(First_name, Last_name, email, phone)
                VALUES ({first_name}, {last_name}, {email}, {phone});
                """)
        conn.commit()
    conn.close()


def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute(f"""
                INSERT INTO Clients_phone(Clients_id, phone)
                VALUES ({client_id}, {phone});
                """)
        conn.commit()
    conn.close()


def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    with conn.cursor() as cur:
        cur.execute(f"""
                UPDATE Clients
                SET First_name = {first_name}, Last_name = {last_name}, email = {email}, phone = {phones}
                WHERE Clients_id = {client_id}
                """)
        conn.commit()
    conn.close()


def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute(f"""
                DELETE FROM Clients_phone
                WHERE Client_id = {client_id} AND phone = {phone};
                """)
        conn.commit()
    conn.close()


def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute(f"""
                DELETE FROM Clients_phone
                WHERE Client_id = {client_id};
                """)
        cur.execute(f"""
                DELETE FROM Clients
                WHERE Client_id = {client_id};
                """)
        conn.commit()
    conn.close()


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        cur.execute(f"""
                SELECT *
                FROM Clients, Clients_phone
                WHERE Clients.Clients_id = Clients_phone.Clients_id 
                AND Clients.First_name = {first_name} 
                AND Clients.Last_name = {last_name}
                AND Clients.email = {email}
                AND Clients.phone = {phone}
                """)
        conn.commit()
    conn.close()
