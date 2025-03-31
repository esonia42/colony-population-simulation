import psycopg


conn = psycopg.connect("host=localhost port=5432 dbname=postgres user=postgres password=postgres connect_timeout=10 sslmode=prefer")
conn.commit()

def get_conn():
    conn = psycopg.connect("host=localhost port=5432 dbname=postgres user=postgres password=postgres connect_timeout=10 sslmode=prefer")
    conn.commit()
    return conn

def insert_persons(person):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO persons (person_id, sex, age, name, colony) VALUES (%s, %s, %s, %s, %s)",
        (person.id, person.sex, person.age, person.name, person.colony.name))
    conn.commit()

def remove_persons(person):
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM orders WHERE person_id = person_id")
    conn.commit()

def get_persons():
    cur = conn.cursor()
    cur.execute("SELECT * FROM persons;")
    cur.fetchall()
    conn.commit()

def delete():
    cur = conn.cursor()
    cur.execute("DELETE FROM persons;")
    cur.fetchall()
    conn.commit()


def get_one_person(connection):
    cur = connection.cursor()
    cur.execute("SELECT * FROM persons;")
    cur.fetchone()
    conn.commit()


def get_multiple_persons(n):
    cur = conn.cursor()
    cur.execute("SELECT * FROM persons;")
    cur.fetchmany(n)
    conn.commit()


def loop_over_tasks(number_of_tasks: int):
    connection = get_conn()
    for i in range(number_of_tasks):
        get_one_person(connection)
    print(number_of_tasks, " finished")

'''with conn.cursor() as cursor:
    cursor.execute("EXPLAIN ANALYZE SELECT * FROM persons WHERE column = %s", ("person_id",))
    print(cursor.fetchall())  # Check the query plan'''
