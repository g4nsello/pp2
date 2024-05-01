import psycopg2

# Establish connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123"
)

# Create a cursor object
cur = conn.cursor()

# Define the function to retrieve records by pattern
def get_records_by_pattern(pattern_text):
    cur.callproc('get_records_by_pattern', [pattern_text])
    records = cur.fetchall()
    return records

# Example usage
pattern = input("Name: ")
result = get_records_by_pattern(pattern)
print(result)

# Close cursor and connection
cur.close()
conn.close()
