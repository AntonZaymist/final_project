import psycopg2


connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="postgres"
)

cursor = connection.cursor()

add_group = "INSERT INTO auth_group (name) VALUES ('test_group')"
cursor.execute(add_group)
connection.commit()