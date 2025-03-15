import psycopg


conn = psycopg.connect("host=localhost port=5432 dbname=postgres user=postgres password=postgres connect_timeout=10 sslmode=prefer")
conn.commit()

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

def get_persons(person):
    cur = conn.cursor()
    cur.execute("SELECT * FROM persons;")
    cur.fetchall()
    conn.commit()

