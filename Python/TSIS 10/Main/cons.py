import psycopg2

# * https://www.postgresqltutorial.com/postgresql-python/
## ! CREATE DATABASE sample;
conn = psycopg2.connect(
    host="localhost",
    database="sample",
    user="postgres",
    password="YOUR DATABASE PASSWORD HERE")


# create a cursor
cur = conn.cursor()



###### Create table
cur.execute("""
CREATE TABLE posts (
    name VARCHAR(255),
    post_text TEXT,
    created_date DATE
);
""")



###### Create
sql = """
INSERT INTO posts(name) VALUES (%s) RETURNING name, post_text
"""
post_name = 'post 1'
cur.execute(sql, (post_name,))

inserted_name = cur.fetchone()
print(inserted_name)



###### Update
sql = """
UPDATE posts SET post_text=%s WHERE name=%s
"""
post_text = 'hello from python'
post_name = 'post 1'
cur.execute(sql, (post_text, post_name))

print(cur.rowcount)



###### Read
sql = """
SELECT * FROM posts
"""
cur.execute(sql)

row = cur.fetchone()

while row is not None:
    print(row)
    row = cur.fetchone()



###### Delete
sql = """
DELETE FROM posts WHERE name=%s
"""
post_name = 'post 1'
cur.execute(sql, (post_name,))

print(cur.rowcount)



# close the communication with the PostgreSQL
cur.close()
conn.commit()