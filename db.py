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



def get_one_person():
    cur = conn.cursor()
    cur.execute("SELECT * FROM persons;")
    cur.fetchone()
    conn.commit()


def get_five_hundred_persons():
    cur = conn.cursor()
    cur.execute("SELECT * FROM persons;")
    cur.fetchmany(500)
    conn.commit()


import time

t1 = time.perf_counter(), time.process_time()

for i in range(500):
    get_one_person()

t2 = time.perf_counter(), time.process_time()

print(f"one person real time: {t2[0] - t1[0]:.2f} seconds")
print(f"one person CPU time: {t2[1] - t1[1]:.2f} seconds")


t1 = time.perf_counter(), time.process_time()

get_five_hundred_persons()

t2 = time.perf_counter(), time.process_time()

print(f"500 persons real time: {t2[0] - t1[0]:.2f} seconds")
print(f"500 persons CPU time: {t2[1] - t1[1]:.2f} seconds")