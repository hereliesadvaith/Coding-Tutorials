import psycopg2

conn = psycopg2.connect(
    host="localhost", dbname="mydb", user="advaith", password="pswd", port=5432
)
cur = conn.cursor()

advaith = "name"
customer = cur.execute(
    f"""
    INSERT INTO product_type({advaith})
    VALUES(
        'shoes'
    );
"""
)
conn.commit()

cur.execute(
    """
    SELECT * FROM public.product_type;
"""
)
print(
    cur.fetchall()
)  # gives a list of tuples of row. curson stores the value for only one execution

cur.close()
conn.close()
