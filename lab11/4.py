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

# Define the function to query data with pagination
def get_paginated_data(limit_val, offset_val):
    cur.callproc('get_paginated_data', [limit_val, offset_val])
    records = cur.fetchall()
    return records

# Example usage
limit = 10  # Number of records per page
offset = 0  # Offset (starting from 0 for the first page)
result = get_paginated_data(limit, offset)
print(result)

# Close cursor and connection
cur.close()
conn.close()
